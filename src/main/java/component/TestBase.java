package component;

import com.galenframework.config.GalenConfig;
import com.galenframework.config.GalenProperty;
import com.galenframework.testng.GalenTestNgTestBase;
import config.Configuration;
import org.apache.log4j.Logger;
import org.apache.log4j.PropertyConfigurator;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.ITestContext;
import org.testng.annotations.*;

import java.io.File;
import java.lang.reflect.Method;
import java.util.List;


import static java.util.Arrays.asList;


public abstract class TestBase extends GalenTestNgTestBase {

    public static final Logger log = Logger.getLogger( TestBase.class.getName() );

    protected String specPath = System.getProperty( "user.dir" ) + "/src/test/java/resources/specFiles/";

    static {
        log.info( "Loding the configuration..." );
        Configuration.loadConfig();
        PropertyConfigurator.configure( new File( "src/main/java/config/log4j.properties" ).getAbsolutePath() );
        GalenConfig.getConfig().setProperty( GalenProperty.SCREENSHOT_FULLPAGE, "true" );

    }

    public void start() {

        load( Configuration.getUrl() );
        Util.waitForSec( 3 );
        //click(By.cssSelector("#lnklogin"));
        Util.waitForSec( 5 );
    }


    public void login() {
        enterValue( By.xpath( "//input[@placeholder='Email']" ), Configuration.getUser() );
        enterValue( By.xpath( "//input[@placeholder='Password']" ), Configuration.getPassword() );
        click( By.xpath( "//*[@id=\"theSubmit\"]" ) );
        Util.waitForSec( 2 );


    }

    public void click(By by) {
        waitForElement( by );
        getDriver().findElement( by ).click();
        Util.waitForSec( 1 );
    }

    public void enterValue(By by, String value) {
        waitForElement( by );
        // getDriver().findElement( by ).clear();
        getDriver().findElement( by ).sendKeys( value );
    }

    public void waitForElement(By element) {
        try {
            WebDriverWait wait = new WebDriverWait( getDriver(), 60 );
            wait.until( ExpectedConditions.visibilityOf( getDriver().findElement( element ) ) );
        } catch (Exception e) {
            log.info( e.getMessage() );
        }
    }


    @Override
    public WebDriver createDriver(Object[] args) {
        WebDriver driver = null;
        String driverPath = System.getProperty( "user.dir" ) + "/src/main/java/config/";
        switch (Configuration.getBrowser()) {
            case "chrome":
                System.setProperty( Configuration.chromeKey, driverPath + "chromedriver.exe" );
                ChromeOptions options = new ChromeOptions();
                options.addArguments( "disable-infobars" );
                if (Configuration.getHeadless())
                    options.addArguments( "headless" );
                driver = new ChromeDriver( options );
                break;
            case "firefox":
                System.setProperty( Configuration.fireFoxKey, driverPath + "geckodriver.exe" );
                FirefoxOptions firefoxOptions = new FirefoxOptions();
                if (Configuration.getHeadless())
                    firefoxOptions.addArguments( "-headless" );
                driver = new FirefoxDriver( firefoxOptions );
                break;
            case "ie":
                System.setProperty( Configuration.ieKey, driverPath + "IEDriverServer.exe" );
                DesiredCapabilities capabilities = DesiredCapabilities.internetExplorer();
                capabilities.setCapability( CapabilityType.ACCEPT_SSL_CERTS, true );
                capabilities.setCapability( InternetExplorerDriver.INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS, true );
                driver = new InternetExplorerDriver( capabilities );
                break;
            case "Edge":
                System.setProperty( Configuration.edgeKey, driverPath + "MicrosoftWebDriver.exe" );
                driver = new EdgeDriver();
                break;

            default:
                Assert.assertTrue( false, "Browser is not mentioned correctly : " + Configuration.getBrowser() );

        }
        if (args.length > 0) {
            if (args[0] != null && args[0] instanceof TestDevice) {
                TestDevice device = (TestDevice) args[0];
                if (device.getScreenSize() != null) {
                    driver.manage().window().setSize( device.getScreenSize() );

                }
            }
        }
        return driver;
    }

    public void load(String url) {
        getDriver().get( url );
    }

    public void checkPageLayout(String specFile, List<String> tags) {
        try {
            checkLayout( specFile, tags );

        } catch (Exception e) {

            throw new RuntimeException( e );
        }

    }


    @DataProvider(name = "devices")
    public Object[][] devices() {
        return new Object[][]{
                // {new TestDevice("mobile", new Dimension(450, 800), asList("mobile"))},
                {new TestDevice( "desktop", new Dimension( 1366, 768 ), asList( "desktop" ) )},
                //{new TestDevice( "tablet", new Dimension( 768, 1024 ), asList( "tablet" ) )}

        };
    }


    public static class TestDevice {

        private final String name;
        private final Dimension screenSize;
        private final List<String> tags;

        public TestDevice(String name, Dimension screenSize, List<String> tags) {
            this.name = name;
            this.screenSize = screenSize;
            this.tags = tags;
        }

        public String getName() {
            return name;
        }

        public Dimension getScreenSize() {
            return screenSize;
        }

        public List<String> getTags() {
            return tags;
        }

        @Override
        public String toString() {
            return String.format( "%s %dx%d", name, screenSize.width, screenSize.height );
        }
    }

    public void javaScriptScroll() {
        JavascriptExecutor jse = (JavascriptExecutor) getDriver();
        jse.executeScript( "window.scrollBy(0,document.body.scrollHeight)", "" );
        Util.waitForSec( 2 );
    }

   /* @AfterSuite
    public void jiraIntegration() {
        if (Configuration.getJiraFlag()) {
            ResultsMarker.integrationWithJira();

        }
    }*/

    @BeforeMethod
    public void updateMethodName(Method method, Object[] testData, ITestContext ctx){
        ThreadLocal<String> testName = new ThreadLocal<>();
        if (testData.length > 0) {
            testName.set(method.getName() + "_" + testData[0]);
            ctx.setAttribute("testName", testName.get());
        } else
            ctx.setAttribute("testName", method.getName());
    }

}
