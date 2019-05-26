package tests;

import com.galenframework.config.GalenConfig;
import com.galenframework.config.GalenProperty;
import component.TestBase;
import component.Util;
import org.openqa.selenium.By;
import org.testng.annotations.Test;

public class OperationPageTest extends TestBase {
    @Test(dataProvider = "devices")
    public void testOperationPage(TestDevice device) {
        start();
        String specFile = specPath + "operation.spec";
        javaScriptScroll();
        log.info( "login to application." );
        login();
        log.info( "Navigating to operation page." );
        click( By.xpath("//*[@id=\"btn_continue\"]"));
        javaScriptScroll();
        click( By.xpath("//button[@id='btn_continue']"));
        javaScriptScroll();
      // click( By.xpath("//*[@id=\"_operationsInfo\"]/div[4]/div[1]/div[2]/span/i"));

        log.info("Verifying the operation page layout.");
        Util.waitForSec(3);
        checkPageLayout(specFile,device.getTags());
        Util.waitForSec(3);
    }


}
