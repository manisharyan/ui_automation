package component;

public class Util {

    public static void waitForSec(int i) {
        try {
            Thread.sleep(i * 1000);
        } catch (Exception e) {

        }
    }

}
