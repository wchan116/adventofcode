import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;
import java.util.stream.Collectors;

public class Day02 {

    public static Map<Character, Integer> getCharCount(String word) {
        Map<Character, Integer> char_cnt = new HashMap<Character, Integer>();
        for (char c : word.toCharArray()) {
            char_cnt.put(c, char_cnt.getOrDefault(c, 0) + 1);
        }
        return char_cnt;
    }

    public static int p1(List<String> inp) {
        int twos = 0;
        int threes = 0;
        for (String line: inp) {
            Map<Character, Integer> char_cnt = getCharCount(line);
            boolean two = false;
            boolean three = false;
            for (int val : char_cnt.values()) {
                if (val == 2) {
                    two = true;
                }
                if (val == 3) {
                    three = true;
                }
            }
            twos = (two) ? (twos + 1) : twos;
            threes = (three) ? (threes + 1) : threes;
        }
        return twos * threes;
    }

    public static String p2(List<String> inp) {
        int strlen = inp.get(0).length();
        for (String i : inp) {
            for (String j : inp) {
                if (i.equals(j)) {
                    continue;
                }
                int wrong = 0;
                int bad_idx = 0;
                char[] i_chars = i.toCharArray();
                char[] j_chars = j.toCharArray();
                for (int x = 0; x < i_chars.length; ++x) {
                    if (i_chars[x] != j_chars[x]) {
                        ++wrong;
                        bad_idx = x;
                    }
                }
                if (wrong == 1) {
                    return i.substring(0, bad_idx) + i.substring(bad_idx + 1);
                }
            }
        }
        return "";
    }

    public static void main(String[] args) {
        List<String> inp = Utils.readFromFile(args[0]);
        System.out.println(p1(inp));
        System.out.println(p2(inp));
    }
}