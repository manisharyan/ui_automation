package tests;

import component.TestBase;
import org.testng.annotations.Test;
import pages.HomePage;

public class VehiclePageMainSection1Test extends TestBase {
    @Test(dataProvider = "devices")
    public void testVehiclePageMainSection1(TestDevice device){

        log.info( "Launching the application..." );
        start();

        String specFile = specPath + "vehiclePageMainSection1.spec";

        log.info( "Navigating to vehicle page" );
        click( HomePage.skipNowLink );

        log.info( "Verifying the vehicle page main section" );
        checkPageLayout( specFile,device.getTags() );

    }

}
