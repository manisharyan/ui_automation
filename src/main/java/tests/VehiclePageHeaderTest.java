package tests;

import component.TestBase;
import org.testng.annotations.Test;
import pages.HomePage;

public class VehiclePageHeaderTest extends TestBase {
    @Test(dataProvider = "devices")
    public void testVehiclePageHeader(TestDevice device){

        log.info( "Launching the application..." );
        start();

        String specFile = specPath + "vehiclePageHeader.spec";

        log.info( "Navigating to vehicle page" );
        click( HomePage.skipNowLink );

        log.info( "Verifying the vehicle page header" );
        checkPageLayout( specFile,device.getTags() );

    }

}
