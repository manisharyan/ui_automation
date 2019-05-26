package component;

import com.google.common.base.Strings;
import config.Configuration;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Map;
import java.util.concurrent.atomic.AtomicReference;

public class ResultsMarker {
    static int statusId = 0;
    private JiraClient jiraClient;
    private String endPoint;
    private String automationCycleName;
    private String cycleId;

    public ResultsMarker() {
        Configuration.loadConfig();
        jiraClient = new JiraClient( Configuration.getJiraBaseUrl() );
        jiraClient.setJiraUser( Configuration.getJiraUsername() );
        jiraClient.setJiraPassword( Configuration.getJiraPassword() );

    }

    public static void main(String args[]) {
        ResultsMarker marker = new ResultsMarker();
        marker.markResultsToJira();
    }

    public void markResultsToJira() {
        Map<String, String> testStatus = XMLParser.getExecutedTestsIdsAndStatus();
        String cycleCreation = createCycle();
        if (cycleCreation.contains( "jobProgressToken" )) {
            cycleId = getCycleId( Configuration.getJiraProjectId() );
            System.out.println( "Automation cycle created successfully in JIRA and now marking automation results to created cycle ==> " + automationCycleName );
            jiraUpdation( testStatus );
        } else {
            System.out.println( "Automation cycle is not created." );
        }
    }

    private void jiraUpdation(Map<String, String> testStatus) {
        for (Map.Entry<String, String> entry : testStatus.entrySet()) {
            System.out.println( entry.getKey() + " = " + entry.getValue() );
            if (entry.getValue().equals( ResultConvertor.PASS.toString() )) {
                statusId = ResultConvertor.PASS.getStatus();
            } else if (entry.getValue().equals( ResultConvertor.FAIL.toString() )) {
                statusId = ResultConvertor.FAIL.getStatus();
            }
            String executionId = getExecutionId( entry.getKey() );
            if (!Strings.isNullOrEmpty( executionId )) {
                updateTestCaseResult( executionId );
            } else {
                System.out.println( "There is no execution id for TestCase ==> " + entry.getKey() );
            }
        }
    }

    private void updateTestCaseResult(String executionId) {
        try {
            endPoint = Resources.testStepStatusEndPoint + executionId + "/execute";
            String testUpdateResult = jiraClient.doPut( endPoint, RequestBody.getDataForTestStatus( statusId ) ).toString();
            JSONObject response = new JSONObject( testUpdateResult );
            if (String.valueOf( response.get( "id" ) ).equals( executionId )) {
                System.out.println( "Automation Result for TestCase " + response.get( "issueId" ) + " ==> " + response.get( "issueKey" ) +
                        " marked in cycle " + response.get( "cycleName" ) );
            }

        } catch (Exception e) {
            System.out.println( e );
        }
    }

    private String getExecutionId(String key) {
        String executionId = null;
        endPoint = Resources.executionIdEndPoint + "?issueId=" + key + "&cycleId=" + cycleId;
        try {
            JSONObject myResponse = new JSONObject( jiraClient.doGet( endPoint ).toString() );
            JSONArray values = myResponse.getJSONArray( "executions" );
            for (int i = 0; i < values.length(); i++) {
                JSONObject jsonObject = values.getJSONObject( i );
                if (jsonObject.has( "id" ))
                    executionId = jsonObject.get( "id" ).toString();
                //System.out.println( "Execution id from response : " + executionId );
            }
        } catch (Exception e) {
            System.out.println( e );
        }
        return executionId;
    }

    public String createCycle() {
        endPoint = Resources.cloneCycleEndPoint;
        try {
            automationCycleName = "Automation_Cycle_" + getUniquify();
            return jiraClient.doPost( endPoint, RequestBody.getDataToCloneCycle( automationCycleName ) ).toString();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (JiraAPIException e) {
            e.printStackTrace();
        }
        return null;
    }

    public String getCycleId(String projectId) {
        String currentCycleId = null;
        endPoint = Resources.getAllCycleInfoEndPoint + projectId;
        try {
            String response = jiraClient.doGet( endPoint ).toString();
            JSONObject jsonObject = new JSONObject( response );
            for (String key : jsonObject.keySet()) {
                JSONArray jsonArray = jsonObject.getJSONArray( key );
                //System.out.println( "Outer Length of Json ============" + jsonArray.length() );
                for (int i = 0; i < jsonArray.length(); i++) {
                    //System.out.println( "Inner Length of Json " + jsonArray.getJSONObject( i ).length() );
                    for (String cycleId : jsonArray.getJSONObject( i ).keySet()) {
                        if (!cycleId.equals( "recordsCount" )) {
                            JSONObject cycle = jsonArray.getJSONObject( i ).getJSONObject( cycleId );
                            if ((cycle.get( "name" ).toString()).equals( automationCycleName )) {
                                currentCycleId = cycleId;
                                break;
                            }
                        }

                    }

                }

            }


        } catch (IOException e) {
            e.printStackTrace();
        } catch (JiraAPIException e) {
            e.printStackTrace();
        }
        return currentCycleId;
    }

    public String getUniquify() {
        String uniqueString = LocalDateTime.now().format( DateTimeFormatter.ofPattern( "yyyy-MM-dd_HH:mm:ss.SSS" ) );
        return uniqueString;
    }

    public void createIssue(){

    }

}