import java.util.*;

public class Day14 {

    public static int p1(List<String> inp) {
        List<Integer> board = new ArrayList<>(Arrays.asList(3, 7));
        int input = 170641;
//        int input = 2018;
        int elf1 = 0;
        int elf2 = 1;

        int i = 0;
        while (i != 2 * input) {
            int score = board.get(elf1) + board.get(elf2);
            Stack<Integer> digits = new Stack<>();
            if (score == 0) {
                digits.push(0);
            }
            while (score != 0) {
                digits.push(score % 10);
                score /= 10;
            }
            while (!digits.isEmpty()) {
                int item = digits.pop();
                board.add(item);
            }

            elf1 = (elf1 + board.get(elf1) + 1) % board.size();
            elf2 = (elf2 + board.get(elf2) + 1) % board.size();

            ++i;
        }
        StringBuilder recipes = new StringBuilder();
        for (int x = input; x < input + 10 && x < board.size(); ++x) {
            recipes.append(board.get(x));
        }

        return Integer.parseInt(recipes.toString());
    }

    public static int p2(List<String> inp) {
        List<Integer> board = new ArrayList<>(Arrays.asList(3, 7));
        String input = "170641";
//        String input = "92510";
//        String input = "51589";
//        String input = "01245";
//        String input = "59414";
        int n = input.length();
        int elf1 = 0;
        int elf2 = 1;

        int i = 0;
        boolean done = false;
        Deque<Integer> d = new ArrayDeque<>(n);
        while (true) {
            int score = board.get(elf1) + board.get(elf2);
            Stack<Integer> digits = new Stack<>();
            if (score == 0) {
                digits.push(0);
            }
            while (score != 0) {
                digits.push(score % 10);
                score /= 10;
            }
            while (!digits.isEmpty()) {
                int item = digits.pop();
                board.add(item);
                if (d.size() == n) {
                    d.pollFirst();
                }
                d.offerLast(item);
                Deque<Integer> tmp_d = new ArrayDeque<>(d);
//            System.out.println(d.toString());
                StringBuilder sb = new StringBuilder();
                while (!d.isEmpty()) {
                    int tmp = d.pollFirst();
                    sb.append(tmp);
                }
                if (sb.toString().equals(input)) {
                    return board.size()- n;
                }
                d = new ArrayDeque<>(tmp_d);
            }

            elf1 = (elf1 + board.get(elf1) + 1) % board.size();
            elf2 = (elf2 + board.get(elf2) + 1) % board.size();

//            System.out.println(board);

/*
            for (int j = 0; j < board.size(); ++j) {
                if (d.size() == n) {
                    d.pollFirst();
                }
                d.offerLast(board.get(j));
                Deque<Integer> tmp_d = new ArrayDeque<>(d);
                StringBuilder sb = new StringBuilder();
                while (!d.isEmpty()) {
                    int tmp = d.pollFirst();
                    sb.append(tmp);
                }
                if (sb.toString().equals(input)) {
                    return j - n + 1;
                }
                d = new ArrayDeque<>(tmp_d);

            }
*/
            ++i;
        }
    }

    public static void main(String[] args) {
        List<String> inp = Utils.readFromFile(args[0]);
        System.out.println(p1(inp));
        System.out.println(p2(inp));
    }
}