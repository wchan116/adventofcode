import java.util.*;
import java.util.regex.*;

public class Day09 {

    public static void rotate(Deque<Integer> board, int n) {
        if (board.isEmpty()) return;
        if (n > 0) {
            for (int i = 0; i < n; ++i) {
                int tmp = board.pollFirst();
                board.offerLast(tmp);
            }
        }
        else {
            for (int i = 0; i < Math.abs(n); ++i) {
                int tmp = board.pollLast();
                board.offerFirst(tmp);
            }

        }

    }
    public static long p1(List<String> inp, int multiplier) {
        Pattern p = Pattern.compile("(\\d+) players; last marble is worth (\\d+) points");
        Matcher m = p.matcher(inp.get(0));
        if (!m.matches()) return -1;
        int nplayers = Integer.parseInt(m.group(1));
        int nmarbles = Integer.parseInt(m.group(2)) * multiplier;
        long[] players = new long[nplayers];
        Deque<Integer> board = new LinkedList<Integer>();
        board.offer(0);
        for (int i = 1; i <= nmarbles; ++i) {
            if (i % 23 == 0) {
                players[i % nplayers] += i;
                rotate(board, -7);
                players[i % nplayers] += board.pollLast();
                rotate(board, 1);
            }
            else {
                rotate(board, 1);
                board.offer(i);
            }
            // System.out.println(board);
        }

        long max = -99;
        for (int i = 0; i < nplayers; ++i) {
            max = Math.max(max, players[i]);
        }

        return max;
    }

    public static void main(String[] args) {
        List<String> inp = Utils.readFromFile(args[0]);
        System.out.println(p1(inp, 1));
        System.out.println(p1(inp, 100));
    }
}