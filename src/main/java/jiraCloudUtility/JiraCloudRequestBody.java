package jiraCloudUtility;


import java.text.SimpleDateFormat;
import java.util.Date;

public class JiraCloudRequestBody {
    private static String data;

    private JiraCloudRequestBody() {

    }

    public static String getDataForTestStatus(int statusId,String issueId) {
        data = "{\n" +
                "   \"status\": {\n" +
                "      \"id\": \""+statusId+"\"\n" +
                "   },\n" +
                "   \"projectId\": \""+JiraConfiguration.getJiraProjectId()+"\",\n" +
                "   \"issueId\": \""+issueId+"\"\n" +
                "}";
        return data;
    }

    public static String getDataToCloneCycle(String cycleName) {
        data = "{\n" +
                "  \"name\": \"" + cycleName + "\",\n" +
                "  \"description\": \"Cycle created from automation \",\n" +
                "  \"startDate\": \"" + getDate() + "\",\n" +
                "  \"endDate\": \"" + getDate() + "\",\n" +
                "  \"projectId\": \"" + JiraConfiguration.getJiraProjectId() + "\",\n" +
                "  \"versionId\": \""+JiraConfiguration.getJiraProjectVersionId()+"\"\n" +
                "}";
        return data;
    }

    private static String getDate() {
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyy-MM-dd");
        return simpleDateFormat.format(new Date());
    }


}



