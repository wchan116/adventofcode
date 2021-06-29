import java.util.*;
import java.util.regex.*;


public class Day07 {

    static List<Character> heads = new ArrayList<Character>();
    public static String p1(List<String> inp) {
        Pattern p = Pattern.compile("Step (\\w).*step (\\w).*");
        Map<Character, List<Character>> prereqs = new HashMap<Character, List<Character>>();
        Map<Character, List<Character>> graph = new HashMap<Character, List<Character>>();

        for (String line : inp) {
            Matcher m = p.matcher(line);
            if (!m.matches()) continue;
            char first = m.group(1).charAt(0);
            char second = m.group(2).charAt(0);

            if (!prereqs.containsKey(second)) {
                prereqs.put(second, new ArrayList<>());
            }

            if (!graph.containsKey(first)) {
                graph.put(first, new ArrayList<>());
                
            }
            prereqs.get(second).add(first);
            graph.get(first).add(second);
        }
        
        // get difference between two sets
        Set<Character> ps = new HashSet<Character>(prereqs.keySet());
        Set<Character> gs = new HashSet<Character>(graph.keySet());
        gs.removeAll(ps);

        Queue<Character> q = new PriorityQueue<Character>();
        StringBuilder order = new StringBuilder();
        for (var head : gs) {
            heads.add(head);
            q.offer(head);
        }

        while (!q.isEmpty()) {
            var curr = q.poll();

            order.append(curr);
            for (var prereq : prereqs.keySet()) {
                prereqs.get(prereq).remove(curr);
            }

            if (graph.get(curr) == null) continue;
            for (var nb : graph.get(curr)) {
                if (prereqs.get(nb).isEmpty()) {
                    q.offer(nb);
                }
            }
        }

        return order.toString();
    }

    public static int p2(List<String> inp, int offset, int nworkers) {
        Pattern p = Pattern.compile("Step (\\w).*step (\\w).*");
        Map<Character, List<Character>> prereqs = new HashMap<Character, List<Character>>();

        for (String line : inp) {
            Matcher m = p.matcher(line);
            if (!m.matches()) continue;
            char first = m.group(1).charAt(0);
            char second = m.group(2).charAt(0);

            if (!prereqs.containsKey(second)) {
                prereqs.put(second, new ArrayList<>());
            }

            prereqs.get(second).add(first);
        }
        char[] order = p1(inp).toCharArray();
        Set<Character> chars = new HashSet<Character>();
        for (var o : order) {
            chars.add(o);
        }

        Job[] workers = new Job[nworkers];
        for (int i = 0; i < nworkers; ++i) {
            workers[i] = new Job();
        }
        for (var head: heads) {
            prereqs.put(head, new ArrayList<>());
        }

        int tick = 0;
        Queue<Character> available = new LinkedList<Character>();
        boolean done = false;
        while (!done) {
            for (var c : chars) {
                if (prereqs.get(c).isEmpty() && !available.contains(c)) {
                    available.offer(c);
                }

            }
            //   System.out.println(available);

            // System.out.println("TICK: " + tick);

            for (int i = 0; i < nworkers; ++i) {
                if (!workers[i].getBusy()) {
                    if (available.peek() != null) {
                        char j = available.poll();
                        workers[i].setJob(j);
                        workers[i].setTime(offset + j - 'A' + 1);
                        workers[i].setBusy(true);
                        chars.remove(j);
                        // System.out.println(i + " Adding " + workers[i].getJob() + " " + workers[i].getTime());
                    }
                }
                if (workers[i].getBusy()) {
                    workers[i].decTime();
                    // System.out.println(i + " " + workers[i].getJob() + " " + workers[i].getTime());
                    if (workers[i].getTime() <= 0) {
                        workers[i].setBusy(false);
                        // System.out.println(workers[i].getJob());
                        // System.out.println(workers[i].getJob());
                        for (var prereq : prereqs.keySet()) {
                            // System.out.println(prereq);
                            // System.out.println(prereqs.get(prereq));
                            prereqs.get(prereq).remove(workers[i].getJob());
                        }
                        if (chars.isEmpty()) {
                            done = true;
                        }
                    }

                }
            }

            ++tick;
            // System.out.println(tick);
        }
        return tick;
    }

    
    public static void main(String[] args) {
        List<String> inp = Utils.readFromFile(args[0]);
        System.out.println(p1(inp));
        System.out.println(p2(inp, 60, 5));
    }
}

class Job {
    private Character job;
    private int time;
    private boolean busy = false;

    public Job() {
        this.busy = false;
    }

    public Character getJob() {
        return job;
    }

    public int getTime() {
        return time;
    }

    public void setJob(Character job) {
        this.job = job;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public boolean getBusy() {
        return busy;
    }

    public void setBusy(boolean busy) {
        this.busy = busy;
    }

    public void decTime() {
        --time;
    }
} 