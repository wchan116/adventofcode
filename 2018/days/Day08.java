import java.util.*;
import java.util.regex.*;

public class Day08 {
    static int checksum;
    static List<Integer> node_loc = new ArrayList<Integer>();
    static Map<Integer, List<Integer>> nodes = new HashMap<Integer, List<Integer>>();
    public static int p1(List<String> inp) {
        String input = inp.get(0);
        int[] in = Arrays.stream(input.split(" ")).mapToInt(Integer::parseInt).toArray();
        checksum = 0;
        getChildren(in, in.length);
        return checksum;
    }

    public static Pair<Integer, Integer> getChildren(int[] input, int max_len) {
        int children = input[0];
        int last_pos = 0;
        node_loc.add(max_len - input.length);
        for (int i = 0; i < children; ++i) {
            last_pos += getChildren(Arrays.copyOfRange(input, last_pos + 2, input.length), max_len).getX();
        }
        // add checksum 
        int mnum = input[1];
        int cs = 0;
        for (int i = 0; i < mnum; ++i) {
            if (nodes.get(max_len - input.length) == null) {
                nodes.put(max_len - input.length, new ArrayList<>());
            }
            nodes.get(max_len - input.length).add(input[i + last_pos + 2]);
            cs += input[i + last_pos + 2];
        }
        checksum += cs;
        // System.out.println(checksum);

        return Pair.createPair(2 + mnum + last_pos, cs);
    }

    public static Pair<Integer, Integer> getValue(int[] input, int max_len) {
        int children = input[0];
        int last_pos = 0;
        node_loc.add(max_len - input.length);
        int[] c = new int[children];
        for (int i = 0; i < children; ++i) {
            var p = getValue(Arrays.copyOfRange(input, last_pos + 2, input.length), max_len);
            last_pos += p.getX();
            c[i] = p.getY();
        }
        // add checksum 
        int mnum = input[1];
        int cs = 0;
        if (children == 0) {
            for (int i = 0; i < mnum; ++i) {
                cs += input[i + last_pos + 2];
            }
            return Pair.createPair(2 + mnum + last_pos, cs);

        }
        else {
            for (int i = 0; i < mnum; ++i) {
        // System.out.printf("============ %d ============\n", max_len - input.length);
        //     System.out.println(input[i + last_pos + 2] - 1);
                if (input[i + last_pos + 2] > children) {
                    cs += 0;
                }
                else {

                cs += c[input[i + last_pos + 2] - 1];
                }
            }
            return Pair.createPair(2 + mnum + last_pos, cs);
        }

        // System.out.printf("============ %d ============\n", max_len - input.length);
        // for (int i = 0; i < children; ++i) {
        //     System.out.println(c[i]);
        // }
        // System.out.printf("============ %d ============\n", max_len - input.length);
        // checksum += cs;
        // System.out.println(checksum);

    }

    public static int p2(List<String> inp) {
        String input = inp.get(0);
        int[] in = Arrays.stream(input.split(" ")).mapToInt(Integer::parseInt).toArray();
        var v = getValue(in, in.length);
        return v.getY();
    }

    public static void main(String[] args) {
        List<String> inp = Utils.readFromFile(args[0]);
        System.out.println(p1(inp));
        System.out.println(p2(inp));
    }
}