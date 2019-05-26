package tests;

import component.TestBase;
import org.testng.annotations.Test;
import pages.HomePage;
import pages.VehiclePage;

public class VehiclePageFooterTest extends TestBase {
    @Test(dataProvider = "devices")
    public void testVehiclePageFooter(TestDevice device){

        log.info( "Launching the application..." );
        start();

        String specFile = specPath + "vehiclePageFooter.spec";

        log.info( "Navigating to vehicle page" );
        click( HomePage.skipNowLink );

        log.info( "Verifying the footer section on vehicle page" );
        checkPageLayout( specFile,device.getTags() );

    }

}
