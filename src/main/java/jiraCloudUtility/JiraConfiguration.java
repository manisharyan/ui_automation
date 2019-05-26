package jiraCloudUtility;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.util.Properties;

public class JiraConfiguration {

    static Properties properties;

    private JiraConfiguration() {

    }

    public static void loadJiraConfig() {
        properties = new Properties();
        try {
            InputStream in = new FileInputStream(new File("src/main/java/jiraCloudUtility/jiraConfig.properties").getAbsolutePath());
            properties.load(in);
        } catch (Exception e) {
            e.getMessage();

        }
    }


    public static String getJiraSupport() {
        return properties.getProperty("jiraSupport");
    }

    public static String getJiraBaseUrl() {
        return properties.getProperty("jiraBaseUrl");
    }

    public static String getJiraUserName() {
        return properties.getProperty("jiraUserName");
    }

    public static String getJiraPassword() {
        return properties.getProperty("jiraPassword");
    }

    public static String getJiraProjectId() {
        return properties.getProperty("jiraProjectId");
    }

    public static String getZephyrBaseUrl() {
        return properties.getProperty("zephyrBaseUrl");
    }

    public static String getZephyrAccessKey() {
        return properties.getProperty("zephyrAccessKey");
    }

    public static String getZephyrSecretKey() {
        return properties.getProperty("zephyrSecretKey");
    }

    public static int getJwtTokenExpirationTime() {
        return Integer.parseInt(properties.getProperty("jwtTokenExpirationTimeInSec"));
    }

    public static String getJiraCycleIdToClone() {
        return properties.getProperty("jiraCycleIdToClone");
    }

    public static String getZephyrUserName() {
        return properties.getProperty("zephyrUserName");
    }

    public static String getJiraProjectVersionId() {
        return properties.getProperty("jiraProjectVersionId");
    }
}
