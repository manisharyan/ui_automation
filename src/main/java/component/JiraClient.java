package component;

import org.json.simple.JSONObject;
import org.json.simple.JSONValue;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;

public class JiraClient {
    private String baseUrl;
    private String j_user;
    private String j_password;

    public JiraClient(String url) {
        if (!url.endsWith( "/" )) {
            url = url + "/";
        }
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
        return this.sendRequest( "GET", uri, null );
    }

    public Object doPost(String uri, Object data) throws IOException, JiraAPIException {
        return this.sendRequest( "POST", uri, data );
    }

    public Object doPut(String uri, Object data) throws IOException, JiraAPIException {
        return this.sendRequest( "PUT", uri, data );
    }

    private Object sendRequest(String method, String uri, Object data)
            throws IOException, JiraAPIException {
        URL url = new URL( this.baseUrl + uri );
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.addRequestProperty( "Content-Type", "application/json" );
        conn.addRequestProperty( "Authorization", getAuthorization( getJiraUser(), getJiraPassword() ) );
        if (method.equals( "POST" ) || method.equals( "PUT" )) {
            if (data != null) {
                conn.setDoOutput( true );
                conn.setRequestMethod( method );
                OutputStreamWriter ostream = new OutputStreamWriter( conn.getOutputStream() );
                // System.out.println(data);
                ostream.write( data.toString() );
                ostream.close();
            }
        }
        int status = conn.getResponseCode();
        InputStream istream;
        if (status != 200 && status != 201) {
            istream = conn.getErrorStream();
            if (istream == null) {
                throw new JiraAPIException( "JIRA API return HTTP " + status + " (No additional error message received)" );
            }
        } else {
            istream = conn.getInputStream();
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
                text += System.getProperty( "line.separator" );
            }
            reader.close();
        }

        Object result;
        if (text != "") {
            result = JSONValue.parse( text );
        } else {
            result = new JSONObject();
        }
        if (status != 200 && status != 201) {
            String error = "No additional error message received";
            if (result != null && result instanceof JSONObject) {
                JSONObject obj = (JSONObject) result;
                if (obj.containsKey( "error" )) {
                    error = '"' + (String) obj.get( "error" ) + '"';
                }
            }
            throw new JiraAPIException( "JIRA API returned HTTP " + status + "(" + error + ")"
            );
        }

        return result;
    }

    public static String getAuthorization(String user, String password) {
        String userpass = user + ":" + password;
        String basicAuth = null;
        try {
            basicAuth = "Basic " + " " + javax.xml.bind.DatatypeConverter.printBase64Binary( userpass.getBytes( "UTF-8" ) );
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        return basicAuth;
    }
}
