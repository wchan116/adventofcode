import java.util.*;
import java.util.regex.*;

public class Day08 {
    static int checksum;
    public static int p1(List<String> inp) {
        String input = inp.get(0);
        int[] in = Arrays.stream(input.split(" ")).mapToInt(Integer::parseInt).toArray();
        checksum = 0;
        getChildren(in);
        return checksum;
    }

    public static int getChildren(int[] input) {
        int children = input[0];
        int last_pos = 0;
        for (int i = 0; i < children; ++i) {
            last_pos += getChildren(Arrays.copyOfRange(input, last_pos + 2, input.length));
        }
        // add checksum 
        int mnum = input[1];
        for (int i = 0; i < mnum; ++i) {
            checksum += input[i + last_pos + 2];
        }
        // System.out.println(checksum);

        return 2 + mnum + last_pos;
    }

    public static int p2(List<String> inp) {
        return -1;
    }

    public static void main(String[] args) {
        List<String> inp = Utils.readFromFile(args[0]);
        System.out.println(p1(inp));
        System.out.println(p2(inp));
    }
}