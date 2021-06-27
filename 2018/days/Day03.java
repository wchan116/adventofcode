import java.util.*;
import java.util.regex.*;

public class Day03 {
    private static Map<Pair<Integer, Integer>, String> overlappers = new HashMap<Pair<Integer, Integer>, String>();

    public static int p1(List<String> inp) {
        Pattern p = Pattern.compile("#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)");
        Set<Pair<Integer, Integer>> visited = new HashSet<Pair<Integer, Integer>>();
        Set<Pair<Integer, Integer>> overlap = new HashSet<Pair<Integer, Integer>>();
        for (String line : inp) {
            Matcher m = p.matcher(line);
            if (!m.matches()) continue;
            String id = m.group(1);
            Pair<Integer, Integer> start = new Pair<Integer, Integer>(
                Integer.parseInt(m.group(2)),
                Integer.parseInt(m.group(3))
            );
            int width = Integer.parseInt(m.group(4));
            int height = Integer.parseInt(m.group(5));

            for (int i = start.getX(); i < start.getX() + width; ++i) {
                for (int j = start.getY(); j < start.getY() + height; ++j) {
                    Pair<Integer, Integer> newPair = Pair.createPair(i, j);
                    if (overlappers.containsKey(newPair)) {
                        overlappers.put(newPair, "X");
                    }
                    else {
                        overlappers.put(newPair, id);
                    }
                    if (visited.contains(newPair)) {
                        overlap.add(newPair);
                    }
                    visited.add(newPair);
                }
            }
        }
        return overlap.size();
    }

    public static int p2(List<String> inp) {
        Pattern p = Pattern.compile("#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)");
        Set<Pair<Integer, Integer>> visited = new HashSet<Pair<Integer, Integer>>();
        for (String line : inp) {
            Matcher m = p.matcher(line);
            if (!m.matches()) continue;
            String id = m.group(1);
            Pair<Integer, Integer> start = new Pair<Integer, Integer>(
                Integer.parseInt(m.group(2)),
                Integer.parseInt(m.group(3))
            );
            int width = Integer.parseInt(m.group(4));
            int height = Integer.parseInt(m.group(5));

            boolean overlap = false;
            for (int i = start.getX(); i < start.getX() + width; ++i) {
                for (int j = start.getY(); j < start.getY() + height; ++j) {
                    Pair<Integer, Integer> newPair = Pair.createPair(i, j);
                    if (overlappers.get(newPair).equals("X")) {
                        overlap = true;
                    }
                }
            }
            if (!overlap) return Integer.parseInt(id);
        }
        return -1;
    }

    public static void main(String[] args) {
        List<String> inp = Utils.readFromFile(args[0]);
        System.out.println(p1(inp));
        System.out.println(p2(inp));
    }
}