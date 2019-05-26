package component;


public class RequestBody {
    private static String data;

    private RequestBody() {

    }

    public static String getDataForTestStatus(int statusId) {
        data = "{\"status\" : " + statusId + "}";
        return data;
    }

    public static String getDataToCloneCycle(String cycleName) {
        data = "{\n" +
                "  \"clonedCycleId\": \"12\",\n" +
                "  \"name\": \"" + cycleName + "\",\n" +
                "  \"build\": \"\",\n" +
                "  \"environment\": \"\",\n" +
                "  \"description\": \"Released Cycle1\",\n" +
                "  \"startDate\": \"17/Sep/18\",\n" +
                "  \"endDate\": \"30/Sep/18\",\n" +
                "  \"projectId\": \"10003\",\n" +
                "  \"versionId\": \"-1\"\n" +
                "}";
        return data;
    }

    public static String getDataToCreateIssue(String description) {
        data = "{\n" +
                "    \"fields\": {\n" +
                "        \"project\": {\n" +
                "            \"key\": \"MAYUR\"\n" +
                "        },\n" +
                "        \"summary\": \"Creating Demo issue of Type Bug with Galen Report\",\n" +
                "        \"description\": \"" + description + "\",\n" +
                "        \"issuetype\": {\n" +
                "            \"name\": \"Bug\"\n" +
                "        }\n" +
                "    }\n" +
                "}";
        return data;
    }
}



