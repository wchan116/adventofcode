import java.util.*;
import java.util.regex.*;

public class Day11 {
    static int[][] grid = new int[300][300];
    public static int p1(List<String> inp) {
        int serial = Integer.parseInt(inp.get(0));
//        serial = 18;

        for (int i = 0; i < 300; ++i) {
            for (int j = 0; j < 300; ++j) {
                int rack = (i + 1) + 10;
                int power = ((rack * (j + 1)) + serial) * rack;
                int hundreds = (power % 1000) / 100;
                power = hundreds - 5;
                grid[i][j] = power;
            }
        }
        int max_power = -99999;
        int best_x = 0;
        int best_y = 0;
        for (int i = 0; i < 297; ++i) {
            for (int j = 0; j < 297; ++j) {
                int power = grid[i][j] + grid[i][j+1] + grid[i][j+2] +
                            grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] +
                            grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2];
                if (power > max_power) {
                    max_power = power;
                    best_x = i + 1;
                    best_y = j + 1;
                }
            }
        }
        System.out.println(max_power);
        System.out.println(best_x + "," + best_y);
//        System.out.println(grid[100][152]);
        return -1;
    }

    public static int p2(List<String> inp) {
        int max_power = -999999;
        int best_x = 0;
        int best_y = 0;
        int best_s = 0;
        for (int i = 0; i < 300; ++i) {
            for (int j = 0; j < 300; ++j) {
                for (int size = 1; size <= 300; ++size) {
                    int power = 0;
                    for (int x = i; x < Math.min(i + size, 300); ++x) {
                        for (int y = j; y < Math.min(j + size, 300); ++y) {
                            power += grid[x][y];
                        }
                    }
                    if (power > max_power) {
                        max_power = power;
                        best_x = i + 1;
                        best_y = j + 1;
                        best_s = size;
                    }
                }
            }
        }
        System.out.println(best_x +","+ best_y +","+ best_s);
        return max_power;
    }

    public static void main(String[] args) {
        List<String> inp = Utils.readFromFile(args[0]);
        System.out.println(p1(inp));
        System.out.println(p2(inp));
    }
}