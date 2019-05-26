package config;

import org.jasypt.util.text.BasicTextEncryptor;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.util.Properties;


public class Configuration {
    public static final String chromeKey = "webdriver.chrome.driver";
    public static final String fireFoxKey = "webdriver.gecko.driver";
    public static final String ieKey = "webdriver.ie.driver";
    public static final String edgeKey = "webdriver.edge.driver";
    static Properties properties;

    private Configuration() {

    }

    public static void loadConfig() {
        properties = new Properties();
        try {
            InputStream in = new FileInputStream( new File( "src/main/java/config/input.properties" ).getAbsolutePath() );
            properties.load( in );
        } catch (Exception e) {
            e.getMessage();

        }
    }

    public static String getBrowser() {
        return properties.getProperty( "browser" );
    }

    public static String getUrl() {
        return properties.getProperty( "url" );
    }

    public static String getUser() {
        return properties.getProperty( "username" );
    }

    public static String getPassword() {
        return decrypt( properties.getProperty( "password" ) );
    }

    public static boolean getHeadless() {
        return Boolean.parseBoolean( properties.getProperty( "headless" ) );
    }

    private static String decrypt(String password) {
        BasicTextEncryptor textEncryptor = new BasicTextEncryptor();
        textEncryptor.setPassword( "jasypt" );
        return textEncryptor.decrypt( password );
    }

    public static String getJiraBaseUrl() {
        return properties.getProperty( "jiraBaseURL" );
    }

    public static String getJiraUsername() {
        return properties.getProperty( "jiraUserName" );
    }

    public static String getJiraPassword() {
        return properties.getProperty( "jiraPassword" );
    }

    public static String getJiraProjectId() {
        return properties.getProperty( "jiraProjectId" );
    }

    public static boolean getJiraFlag() {
        return Boolean.parseBoolean( properties.getProperty( "jiraSupport" ) );
    }
}
