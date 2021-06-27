import java.io.BufferedReader;
import java.io.FileReader;
import java.util.List;
import java.util.ArrayList;

public class Utils {
    public static List<String> readFromFile(String file) {
        List<String> inp = new ArrayList<String>();
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = br.readLine()) != null) {
                inp.add(line);
            } 
        }
        catch (Exception e) {
            System.out.println("File Not Found!");
        }
        return inp;
    }
}