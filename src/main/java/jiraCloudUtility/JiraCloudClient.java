package jiraCloudUtility;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;

import org.json.simple.JSONObject;
import org.json.simple.JSONValue;

import com.thed.zephyr.cloud.rest.ZFJCloudRestClient;
import com.thed.zephyr.cloud.rest.client.JwtGenerator;

import component.JiraAPIException;

public class JiraCloudClient {
    private String baseUrl;
    private String j_user;
    private String j_password;

    public JiraCloudClient(String url) {
//        if (!url.endsWith("/")) {
//            url = url + "/";
//        }
        this.baseUrl = url;
    }

    public String getJiraUser() {
        return this.j_user;
    }

    public String getJiraPassword() {
        return this.j_password;
    }


    public void setJiraUser(String user) {
        this.j_user = user;
    }

    public void setJiraPassword(String password) {
        this.j_password = password;
    }

    public Object doGet(String uri) throws IOException, JiraAPIException {
        return this.sendRequest("GET", uri, null);
    }

    public Object doPost(String uri, Object data) throws IOException, JiraAPIException {
        return this.sendRequest("POST", uri, data);
    }

    public Object doPut(String uri, Object data) throws IOException, JiraAPIException {
        return this.sendRequest("PUT", uri, data);
    }

    private Object sendRequest(String requestMethod, String uri, Object data)
            throws IOException, JiraAPIException {
        URL url = new URL(this.baseUrl + uri);
        HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
        httpURLConnection.addRequestProperty("Content-Type", "application/json");
        httpURLConnection.addRequestProperty("Authorization", getAuthorization(uri, requestMethod));
        httpURLConnection.addRequestProperty("zapiAccesskey", JiraConfiguration.getZephyrAccessKey());
        if (requestMethod.equals("POST") || requestMethod.equals("PUT")) {
            if (data != null) {
                httpURLConnection.setDoOutput(true);
                httpURLConnection.setRequestMethod(requestMethod);
                OutputStreamWriter ostream = new OutputStreamWriter(httpURLConnection.getOutputStream());
                ostream.write(data.toString());
                ostream.close();
            }
        }
        int status = httpURLConnection.getResponseCode();
        InputStream istream;
        if (status != 200 && status != 201) {
            istream = httpURLConnection.getErrorStream();
            if (istream == null) {
                throw new JiraAPIException("JIRA API return HTTP " + status + " (No additional error message received)");
            }
        } else {
            istream = httpURLConnection.getInputStream();
        }

        String text = "";
        if (istream != null) {
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(
                            istream,
                            "UTF-8"
                    )
            );

            String line;
            while ((line = reader.readLine()) != null) {
                text += line;
                text += System.getProperty("line.separator");
            }
            reader.close();
        }

        Object result;
        if (text != "") {
            result = JSONValue.parse(text);
        } else {
            result = new JSONObject();
        }
        if (status != 200 && status != 201) {
            String error = "No additional error message received";
            if (result != null && result instanceof JSONObject) {
                JSONObject obj = (JSONObject) result;
                if (obj.containsKey("error")) {
                    error = '"' + (String) obj.get("error") + '"';
                }
            }
            throw new JiraAPIException("JIRA API returned HTTP " + status + "(" + error + ")"
            );
        }

        return result;
    }

    public String getAuthorization(String uri, String requestMethod) {
        ZFJCloudRestClient client = ZFJCloudRestClient.restBuilder(this.baseUrl, JiraConfiguration.getZephyrAccessKey(), JiraConfiguration.getZephyrSecretKey(), JiraConfiguration.getZephyrUserName()).build();
        JwtGenerator jwtGenerator = client.getJwtGenerator();
        URI zephyrUri = null;
        try {
            zephyrUri = new URI(this.baseUrl+uri);
        } catch (Exception e) {
            e.getMessage();
        }
        return jwtGenerator.generateJWT(requestMethod, zephyrUri, JiraConfiguration.getJwtTokenExpirationTime());
    }
}

