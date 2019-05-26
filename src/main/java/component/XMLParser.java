package component;

import com.google.common.base.Strings;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathFactory;
import java.io.File;
import java.util.HashMap;
import java.util.Map;


public class XMLParser {

    public static Map<String, String> getExecutedTestsIdsAndStatus() {
        HashMap<String, String> results = new HashMap<String, String>();
        try {
            Util.waitForSec( 5 );
            File file = new File( System.getProperty( "user.dir" ) + "/test-output/testng-results.xml" );
            if (file.exists()) {
                DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
                DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();

                Document doc = dBuilder.parse( file );
                doc.getDocumentElement().normalize();

                XPath xPath = XPathFactory.newInstance().newXPath();
                NodeList nodeList = (NodeList) xPath.compile( "//test-method" ).evaluate( doc, XPathConstants.NODESET );
                for (int i = 0; i < nodeList.getLength(); i++) {
                    Element node = (Element) nodeList.item( i );
                    if (!Strings.isNullOrEmpty( node.getAttribute( "description" ) )) {
                        results.put( node.getAttribute( "description" ), node.getAttribute( "status" ) );
                    }
                }
            } else {
                throw new RuntimeException( "Testng results xml file not found." );
            }
        } catch (Exception e) {
            e.getMessage();

        }

        return results;


    }

}
