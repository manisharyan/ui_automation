package component;
 
import com.relevantcodes.extentreports.ExtentReports;

import java.io.File;

public class ExtentManager {
 
    private static ExtentReports extent;
 
    public synchronized static ExtentReports getReporter(){
        if(extent == null){
            String workingDir = System.getProperty("user.dir");
            extent = new ExtentReports(workingDir+"/target/galen-html-reports/ExtentReportResults.html", true);
            extent.loadConfig(new File(System.getProperty("user.dir")+"/src/test/resources/extent-config.xml"));
        }
        return extent;
    }
}