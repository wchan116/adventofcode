import java.util.*;
import java.util.regex.*;

public class Day06 {

    public static int distance(Pair<Integer, Integer> v, Pair<Integer, Integer> w) {
        return Math.abs(v.getX() - w.getX()) + Math.abs(v.getY() - w.getY());
    }

    static List<Pair<Integer, Integer>> points = new ArrayList<Pair<Integer, Integer>>();
    static int max_x = 0;
    static int max_y = 0;

    public static int p1(List<String> inp) {
        for (String line : inp) {
            Pattern p = Pattern.compile("(\\d+), (\\d+)");
            Matcher m = p.matcher(line);
            if (!m.matches()) continue;
            int x = Integer.parseInt(m.group(1));
            int y = Integer.parseInt(m.group(2));

            points.add(Pair.createPair(x, y));
            max_x = Math.max(max_x, x);
            max_y = Math.max(max_y, y);
        }
        ++max_x;
        ++max_y;
        System.out.println(max_x + " " +  max_y);

        int[][] grid = new int[max_x][max_y];

        List<Integer> f_points = new ArrayList<Integer>();
        int[] areas = new int[points.size()];


        for (int i = 0; i < max_x; ++i) {
            for (int j = 0; j < max_y; ++j) {
                //int closest = -1;
                // int best_dist = Integer.MAX_VALUE;
                boolean tie = false;
                List<Integer> ds = new ArrayList<Integer>();
                for (int p = 0; p < points.size(); ++p) {
                    ds.add(distance(Pair.createPair(i, j), points.get(p)));
                }
                int closest = Collections.min(ds);
                if (ds.indexOf(closest) != ds.lastIndexOf(closest)) tie = true;
                if (tie) {
                    grid[i][j] = -1;
                }
                else {
                    grid[i][j] = ds.indexOf(closest);
                    areas[ds.indexOf(closest)]++;
                }

                // grid[i][j] = tie ? -1 : ds.indexOf(closest);
            }
        }
        for (int p = 0; p < points.size(); ++p) {
            var point = points.get(p);
            boolean finite = false;
            for (int y = point.getY(); y >= 0; --y) {
                if (grid[point.getX()][y] != grid[point.getX()][point.getY()]) finite = true;
            }
            if (!finite) continue;
            finite = false;
            for (int y = point.getY(); y < max_y; ++y) {
                if (grid[point.getX()][y] != grid[point.getX()][point.getY()]) finite = true;
            }
            if (!finite) continue;
            finite = false;
            for (int x = point.getX(); x >= 0; --x) {
                if (grid[x][point.getY()] != grid[point.getX()][point.getY()]) finite = true;
            }
            if (!finite) continue;
            finite = false;
            for (int x = point.getX(); x < max_x; ++x) {
                if (grid[x][point.getY()] != grid[point.getX()][point.getY()]) finite = true;
            }
            if (finite) {
                f_points.add(p);
            }
        }
        // System.out.println(f_points);
        // for (int i = 0; i < max_x; ++i) {
        //     for (int j = 0; j < max_y; ++j) {
        //         System.out.print(grid[i][j] + " ");
        //     }
        //         System.out.println();
        // }
        int largest = -1;
        for (var fp : f_points) {
            largest = Math.max(largest, areas[fp]);
        }
        return largest;
    }

    public static int p2(List<String> inp, int threshold) {
        int[][] grid = new int[max_x][max_y];

        for (int i = 0; i < max_x; ++i) {
            for (int j = 0; j < max_y; ++j) {
                int sum = 0;
                for (int p = 0; p < points.size(); ++p) {
                    sum += distance(Pair.createPair(i, j), points.get(p));
                }
                if (sum < threshold) {
                    grid[i][j] = 1;
                }
                else {
                    grid[i][j] = 0;
                }

            }
        }
        int area = 0;

        for (int i = 0; i < max_x; ++i) {
            for (int j = 0; j < max_y; ++j) {
                area += grid[i][j];
            }
        }
        return area;
    }

    public static void main(String[] args) {
        List<String> inp = Utils.readFromFile(args[0]);
        System.out.println(p1(inp));
        System.out.println(p2(inp, 10000));
    }
}