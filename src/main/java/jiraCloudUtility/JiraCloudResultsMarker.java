package jiraCloudUtility;

import com.google.common.base.Strings;
import component.*;
import config.Configuration;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Map;

public class JiraCloudResultsMarker {
    static int statusId = 0;
    private JiraCloudClient jiraCloudClient;
    private String endPoint;
    private String automationCycleName;
    private String cycleId;

    public JiraCloudResultsMarker() {
        JiraConfiguration.loadJiraConfig();
        jiraCloudClient = new JiraCloudClient(JiraConfiguration.getZephyrBaseUrl());
//        jiraClient.setJiraUser( Configuration.getJiraUsername() );
//        jiraClient.setJiraPassword( Configuration.getJiraPassword() );

    }

    public static void main(String args[]) {
        JiraCloudResultsMarker marker = new JiraCloudResultsMarker();
        marker.markResultsToJira();
    }

    public void markResultsToJira() {
        Map<String, String> testStatus = XMLParser.getExecutedTestsIdsAndStatus();
        String cycleCreation = createCycle();
        JSONObject cycle = new JSONObject(cycleCreation);
        if (cycle.get("name").equals(automationCycleName)) {
            System.out.println("Automation cycle created successfully in JIRA Cloud and now marking automation results to created cycle ==> " + automationCycleName);
            jiraUpdation(testStatus);
        } else {
            throw new RuntimeException("Automation cycle is not created.");
        }
    }

    private void jiraUpdation(Map<String, String> testStatus) {
        for (Map.Entry<String, String> entry : testStatus.entrySet()) {
            System.out.println(entry.getKey() + " = " + entry.getValue());
            if (entry.getValue().equals(ResultConvertor.PASS.toString())) {
                statusId = ResultConvertor.PASS.getStatus();
            } else if (entry.getValue().equals(ResultConvertor.FAIL.toString())) {
                statusId = ResultConvertor.FAIL.getStatus();
            }
            String testExecutionId = getTestExecutionId(entry.getKey());
            if (!Strings.isNullOrEmpty(testExecutionId)) {
                updateTestCaseResult(testExecutionId, entry.getKey());
            } else {
                System.out.println("There is no Test execution id for TestCase ==> " + entry.getKey());
            }
        }
    }

    private void updateTestCaseResult(String testExecutionId, String issueId) {
        String executionIdFromResponse, testCaseIdFromResponse;
        try {
            endPoint = JiraCloudResources.testStepStatusEndPoint + testExecutionId;
            String testUpdateResult = jiraCloudClient.doPut(endPoint, JiraCloudRequestBody.getDataForTestStatus(statusId, issueId)).toString();
            JSONObject response = new JSONObject(testUpdateResult);
            JSONObject executionDetails = response.getJSONObject("execution");
            executionIdFromResponse = executionDetails.get("id").toString();
            testCaseIdFromResponse = executionDetails.get("issueId").toString();
            if (executionIdFromResponse.equals(testExecutionId)) {
                System.out.println("Automation Result for TestCase " + testCaseIdFromResponse + " ==> " + executionDetails.getJSONObject("status").get("name") +
                        " marked in cycle " + executionDetails.get("cycleName"));
            }

        } catch (Exception e) {
            System.out.println(e);
        }
    }

    private String getTestExecutionId(String key) {
        String testExecutionId = null;
        Util.waitForSec(4);
        endPoint = JiraCloudResources.testExecutionIdEndPoint + key + "&projectId=" + JiraConfiguration.getJiraProjectId();
        try {
            JSONObject myResponse = new JSONObject(jiraCloudClient.doGet(endPoint).toString());
            JSONArray values = myResponse.getJSONArray("executions");

            for (int i = 0; i < values.length(); i++) {
                JSONObject jsonObject = values.getJSONObject(i);
                if (jsonObject.has("execution")) {
                    String executionCycle = jsonObject.getJSONObject("execution").get("cycleName").toString();
                    if (executionCycle.equals(automationCycleName)) {
                        testExecutionId = jsonObject.getJSONObject("execution").get("id").toString();

                        break;

                    }
                }

            }

            return testExecutionId;
           // System.out.println("Execution id from response : " + testExecutionId);

        } catch (Exception e) {
            e.getMessage();
        }
        return testExecutionId;
    }

    public String createCycle() {
        endPoint = JiraCloudResources.cloneCycleEndPoint + JiraConfiguration.getJiraCycleIdToClone();
        try {
            automationCycleName = "Automation_Cycle_" + getUniquify();
            return jiraCloudClient.doPost(endPoint, JiraCloudRequestBody.getDataToCloneCycle(automationCycleName)).toString();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (JiraAPIException e) {
            e.printStackTrace();
        }
        return null;
    }


    public String getUniquify() {
        String uniqueString = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd_HH:mm:ss.SSS"));
        return uniqueString;
    }

    public void createIssue() {

    }

}