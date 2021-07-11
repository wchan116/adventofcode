import java.awt.image.AreaAveragingScaleFilter;
import java.util.*;
import java.util.regex.*;

public class Day16 {

    static List<Set<String>> pot_opcodes = new ArrayList<>();
    static int end = 0;
    public static int p1(List<String> inp) {
        Pattern b = Pattern.compile("Before:\\s*\\[(\\d+), (\\d+), (\\d+), (\\d+)\\]");
        Pattern c = Pattern.compile("(\\d+) (\\d+) (\\d+) (\\d+)");
        Pattern a = Pattern.compile("After:\\s*\\[(\\d+), (\\d+), (\\d+), (\\d+)\\]");
        List<Integer> before = new ArrayList<>();
        List<Integer> command = new ArrayList<>();
        List<Integer> after = new ArrayList<>();
        for (int i = 0; i < 16; ++i) {
            pot_opcodes.add(new HashSet<>());
        }
        int samples = 0;

        for (int line = 0; line < inp.size(); ++line) {
            Matcher bm = b.matcher(inp.get(line));
            Matcher cm = c.matcher(inp.get(line));
            Matcher am = a.matcher(inp.get(line));
            if (bm.matches()) {
                for (int i = 0; i < bm.groupCount(); ++i) {
                    before.add(Integer.parseInt(bm.group(i+1)));
                }
            }
            else if (cm.matches()) {
                for (int i = 0; i < cm.groupCount(); ++i) {
                    command.add(Integer.parseInt(cm.group(i+1)));
                }
            }
            else if (am.matches()) {
                for (int i = 0; i < am.groupCount(); ++i) {
                    after.add(Integer.parseInt(am.group(i+1)));
                }
            }
            else if (inp.get(line).equals("")) {
                if (before.isEmpty() || after.isEmpty() || command.isEmpty() ) {
                    end = line;
                    break;
                }

                int potential_opcodes = 0;
                int opcode = command.get(0);
                int inputA = command.get(1);
                int inputB = command.get(2);
                int output = command.get(3);
                int changes = 0;
                for (int i = 0; i < 4; ++i) {
                    if (!before.get(i).equals(after.get(i))) {
                        changes++;
                    }
                }
                if (changes > 1) continue;

                // addr
                if ((before.get(inputA) + before.get(inputB)) == after.get(output)) {
//                    System.out.println("addr");
                    pot_opcodes.get(opcode).add("addr");
                    potential_opcodes++;
                }
                // addi
                if ((before.get(inputA) + inputB) == after.get(output)) {
//                    System.out.println("addi");
                    pot_opcodes.get(opcode).add("addi");
                    potential_opcodes++;
                }
                // mulr
                if ((before.get(inputA) * before.get(inputB)) == after.get(output)) {
//                    System.out.println("mulr");
                    pot_opcodes.get(opcode).add("mulr");
                    potential_opcodes++;
                }
                // muli
                if ((before.get(inputA) * inputB) == after.get(output)) {
//                    System.out.println("muli");
                    pot_opcodes.get(opcode).add("muli");
                    potential_opcodes++;
                }
                // banr
                if ((before.get(inputA) & before.get(inputB)) == after.get(output)) {
//                    System.out.println("banr");
                    pot_opcodes.get(opcode).add("banr");
                    potential_opcodes++;
                }
                // bani
                if ((before.get(inputA) & inputB) == after.get(output)) {
//                    System.out.println("bani");
                    pot_opcodes.get(opcode).add("bani");
                    potential_opcodes++;
                }
                // borr
                if ((before.get(inputA) | before.get(inputB)) == after.get(output)) {
//                    System.out.println("borr");
                    pot_opcodes.get(opcode).add("borr");
                    potential_opcodes++;
                }
                // bori
                if ((before.get(inputA) | inputB) == after.get(output)) {
//                    System.out.println("bori");
                    pot_opcodes.get(opcode).add("bori");
                    potential_opcodes++;
                }
                // setr
                if (before.get(inputA).equals(after.get(output))) {
//                    System.out.println("setr");
                    pot_opcodes.get(opcode).add("setr");
                    potential_opcodes++;
                }
                // seti
                if (inputA == after.get(output)) {
//                    System.out.println("seti");
                    pot_opcodes.get(opcode).add("seti");
                    potential_opcodes++;
                }
                // gtir
                if ((inputA > before.get(inputB)) && (after.get(output) == 1)) {
//                    System.out.println("gtir");
                    pot_opcodes.get(opcode).add("gtir");
                    potential_opcodes++;
                }
                if ((inputA <= before.get(inputB)) && (after.get(output) == 0)) {
//                    System.out.println("gtir");
                    pot_opcodes.get(opcode).add("gtir");
                    potential_opcodes++;
                }
                // gtri
                if ((before.get(inputA) > inputB) && (after.get(output) == 1)) {
//                    System.out.println("gtri");
                    pot_opcodes.get(opcode).add("gtri");
                    potential_opcodes++;
                }
                if ((before.get(inputA) <= inputB) && (after.get(output) == 0)) {
//                    System.out.println("gtri");
                    pot_opcodes.get(opcode).add("gtri");
                    potential_opcodes++;
                }
                // gtrr
                if ((before.get(inputA) > before.get(inputB)) && (after.get(output) == 1)) {
//                    System.out.println("gtrr");
                    pot_opcodes.get(opcode).add("gtrr");
                    potential_opcodes++;
                }
                if ((before.get(inputA) <= before.get(inputB)) && (after.get(output) == 0)) {
//                    System.out.println("gtrr");
                    pot_opcodes.get(opcode).add("gtrr");
                    potential_opcodes++;
                }
                // eqir
                if ((inputA == before.get(inputB)) && (after.get(output) == 1)) {
//                    System.out.println("egir");
                    pot_opcodes.get(opcode).add("eqir");
                    potential_opcodes++;
                }
                if ((inputA != before.get(inputB)) && (after.get(output) == 0)) {
//                    System.out.println("egir");
                    pot_opcodes.get(opcode).add("eqir");
                    potential_opcodes++;
                }
                // eqri
                if ((before.get(inputA) == inputB) && (after.get(output) == 1)) {
//                    System.out.println("egri");
                    pot_opcodes.get(opcode).add("eqri");
                    potential_opcodes++;
                }
                if ((before.get(inputA) != inputB) && (after.get(output) == 0)) {
//                    System.out.println("egri");
                    pot_opcodes.get(opcode).add("eqri");
                    potential_opcodes++;
                }
                // eqrr
                if (before.get(inputA).equals(before.get(inputB)) && (after.get(output) == 1)) {
//                    System.out.println("egrr");
                    pot_opcodes.get(opcode).add("eqrr");
                    potential_opcodes++;
                }
                if ((!before.get(inputA).equals(before.get(inputB))) && (after.get(output) == 0)) {
//                    System.out.println("egrr");
                    pot_opcodes.get(opcode).add("eqrr");
                    potential_opcodes++;
                }
//                System.out.println(potential_opcodes);
                if (potential_opcodes >= 3) {
                    ++samples;
                }

                before = new ArrayList<>();
                command = new ArrayList<>();
                after = new ArrayList<>();
            }
        }
//        System.out.println(pot_opcodes);
/*
        for (int i = 0; i < opcodes.length; ++i) {
            System.out.print(i);
            System.out.print("    ");
        }
        System.out.println();
        for (int i = 0; i < opcodes.length; ++i) {
            System.out.print(opcodes[i]);
            System.out.print("    ");
        }
*/
//        System.out.println(nsamples);
        return samples;
    }

    static boolean allEmpty() {
        for (int i = 0; i < pot_opcodes.size(); ++i) {
            if (!pot_opcodes.get(i).isEmpty()) {
                return false;
            }
        }
        return true;

    }
    public static int p2(List<String> inp) {
        String[] opcodes = new String[16];
        while (!allEmpty()) {
            for (int i = 0; i < pot_opcodes.size(); ++i) {
//                System.out.println(pot_opcodes);
                if (pot_opcodes.get(i).size() == 1) {
                    for (var opc : pot_opcodes.get(i)) {
                        opcodes[i] = opc;
//                        System.out.println("asda " + opc);
                    }
//                    System.out.println("aaa " + opcodes[i]);
                    for (var popc : pot_opcodes) {
                        popc.remove(opcodes[i]);
                    }
                }
            }

        }
        int[] registers = new int[4];
        Pattern p = Pattern.compile("(\\d+) (\\d+) (\\d+) (\\d+)");
        for (int i = end; i < inp.size(); ++i) {
            Matcher m = p.matcher(inp.get(i));

            if (!m.matches()) continue;
            int opcode = Integer.parseInt(m.group(1));
            int inputA = Integer.parseInt(m.group(2));
            int inputB = Integer.parseInt(m.group(3));
            int output = Integer.parseInt(m.group(4));

            switch (opcodes[opcode]) {
                case "addr":
                    registers[output] = registers[inputA] + registers[inputB];
                    break;
                case "addi":
                    registers[output] = registers[inputA] + inputB;
                    break;
                case "mulr":
                    registers[output] = registers[inputA] * registers[inputB];
                    break;
                case "muli":
                    registers[output] = registers[inputA] * inputB;
                    break;
                case "banr":
                    registers[output] = registers[inputA] & registers[inputB];
                    break;
                case "bani":
                    registers[output] = registers[inputA] & inputB;
                    break;
                case "borr":
                    registers[output] = registers[inputA] | registers[inputB];
                    break;
                case "bori":
                    registers[output] = registers[inputA] | inputB;
                    break;
                case "setr":
                    registers[output] = registers[inputA];
                    break;
                case "seti":
                    registers[output] = inputA;
                    break;
                case "gtir":
                    registers[output] = (inputA > registers[inputB]) ? 1 : 0;
                    break;
                case "gtri":
                    registers[output] = (registers[inputA] > inputB) ? 1 : 0;
                    break;
                case "gtrr":
                    registers[output] = (registers[inputA] > registers[inputB]) ? 1 : 0;
                    break;
                case "eqir":
                    registers[output] = (inputA == registers[inputB]) ? 1 : 0;
                    break;
                case "eqri":
                    registers[output] = (registers[inputA] == inputB) ? 1 : 0;
                    break;
                case "eqrr":
                    registers[output] = (registers[inputA] == registers[inputB]) ? 1 : 0;
                    break;
            }
        }
/*
        for (int i = 0; i < opcodes.length; ++i) {
            System.out.println(opcodes[i]);
        }
*/

        return registers[0];
    }

    public static void main(String[] args) {
        List<String> inp = Utils.readFromFile(args[0]);
        System.out.println(p1(inp));
        System.out.println(p2(inp));
    }
}