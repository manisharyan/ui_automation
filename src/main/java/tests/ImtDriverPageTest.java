package tests;

import component.TestBase;
import component.Util;
import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.util.List;

public class ImtDriverPageTest extends TestBase {
    public List<String> op;

    @Test(dataProvider = "devices")
    public void testImtDriverPage(TestDevice device) {
        start();
        Util.waitForSec(3);

        click( By.xpath("//a[contains(text(),'skip')]") );

        Util.waitForSec(3);
        enterValue(By.xpath("//*[@id=\"Mfgmonth\"]"),"Jan" );
        enterValue(By.xpath("//*[@id=\"Mfyear\"]"),"2018" );
        enterValue(By.xpath("//*[@id=\"CatlogValueincltesla\"]"),"78" );
        enterValue(By.xpath("//*[@id=\"kmdrive\"]"),"2018" );
        Util.waitForSec(3);

        click(By.xpath("//button[@type='button']"));
        Util.waitForSec(6);

        String specFile = specPath + "imtDriverPage.spec";
        checkPageLayout(specFile, device.getTags());
        Util.waitForSec(3);

    }
}