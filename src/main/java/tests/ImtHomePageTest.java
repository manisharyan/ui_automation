package tests;

import component.TestBase;
import component.Util;
import org.testng.annotations.Test;

import java.util.List;

public class ImtHomePageTest extends TestBase {
    public List<String> op;

    @Test(dataProvider = "devices")
    public void testImtHomePage(TestDevice device) {
        start();

        String specFile = specPath + "imtHomePage.spec";
        System.out.println("Printing Tags:" + device.getTags());
        checkPageLayout(specFile, device.getTags());
        Util.waitForSec(3);
        op = device.getTags();
    }
}