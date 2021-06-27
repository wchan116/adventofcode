import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

public class Day01 {

    public static int p1(List<String> inp) {
        int freq = 0;

        for (String line : inp) {
            freq += Integer.parseInt(line);
        }

        return freq;
    }

    public static int p2(List<String> inp) {
        int freq = 0;
        Set<Integer> visited = new HashSet<Integer>() {{
            add(0);
        }};

        int i = 0;
        while (true) {
            if (i == inp.size()) {
                i = 0;
            }
            freq += Integer.parseInt(inp.get(i++));
            if (visited.contains(freq)) {
                return freq;
            }

            visited.add(freq);
        }
    }

    public static void main(String[] args) {
        List<String> inp = Utils.readFromFile(args[0]);
        System.out.println(p1(inp));
        System.out.println(p2(inp));
    }
}