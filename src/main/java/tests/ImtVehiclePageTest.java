package tests;

import component.TestBase;
import component.Util;
import org.testng.annotations.Test;
import pages.HomePage;

public class ImtVehiclePageTest extends TestBase {

    @Test(dataProvider = "devices")
    public void testImtVehiclePage(TestDevice device){

        log.info( "Launching the application" );
        start();
        String specFile = specPath + "imtVehiclePage.spec";

        log.info( "Navigate to vehicle page." );
        click(HomePage.skipNowLink );
        Util.waitForSec( 2 );

        log.info( "Verifying the vehicle page." );
        checkPageLayout( specFile,device.getTags() );


    }
}
