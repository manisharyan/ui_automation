package jiraCloudUtility;

public class JiraCloudResources {

    private JiraCloudResources(){

    }

    public static final String testExecutionIdEndPoint = "/public/rest/api/1.0/executions?issueId=";

    public static final String testStepStatusEndPoint = "/public/rest/api/1.0/execution/";

    public static final String cloneCycleEndPoint = "/public/rest/api/1.0/cycle?clonedCycleId=";
}
