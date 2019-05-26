package tests;

import component.TestBase;
import org.testng.annotations.Test;
import pages.HomePage;
import pages.VehiclePage;

public class VehiclePageMainSection2Test extends TestBase {
    @Test(dataProvider = "devices")
    public void testVehiclePageMainSection2(TestDevice device){

        log.info( "Launching the application..." );
        start();

        String specFile = specPath + "vehiclePageMainSection2.spec";

        log.info( "Navigating to vehicle page" );
        click( HomePage.skipNowLink );

        log.info( "CLicking on business button. ");
        click( VehiclePage.businessButton );

        log.info( "Verifying the main section of vehicle page" );
        checkPageLayout( specFile,device.getTags() );

    }

}
