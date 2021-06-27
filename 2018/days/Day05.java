import java.util.*;
import java.util.regex.*;

public class Day05 {

    public static String reduce(String inp) {
        Stack<Character> units = new Stack<Character>();

        char[] str = inp.toCharArray();
        for (char c : str) {
            if (units.empty()) {
                units.push(c);
                continue;
            }

            char last = units.peek();
            if (c == last - 32 || c == last + 32) {
                units.pop();
            }
            else {
                units.push(c);
            }
        }
        return stackToString(units); 
    }

    public static String stackToString(Stack<Character> s) {
        String res = "";
        for (char c : s) {
            if (c == ' ') continue;
            res += c;
        }
        return res;
    }

    public static int p1(List<String> inp) {
        return reduce(inp.get(0)).length();
    }

    public static int p2(List<String> inp) {
        String str = inp.get(0);
        int smallest = 9999;
        for (char c = 'a'; c <= 'z'; ++c) {
            String tmp = str.replace(Character.toString(c), "").replace(Character.toString(c - 32), "");
            smallest = Math.min(smallest, reduce(tmp).length());
        }
        return smallest;
    }

    public static void main(String[] args) {
        List<String> inp = Utils.readFromFile(args[0]);
        System.out.println(p1(inp));
        System.out.println(p2(inp));
    }
}