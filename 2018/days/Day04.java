import java.util.*;
import java.util.regex.*;

public class Day04 {
    static Map<Integer, Map<Integer, Integer>> timeline = new HashMap<Integer, Map<Integer, Integer>>();

    public static void buildTimeline(List<String> inp) {
        Pattern guard = Pattern.compile("\\[\\d+\\-\\d+\\-\\d+ (\\d+):(\\d+)\\] Guard #(\\d+) begins shift");
        Pattern asleep = Pattern.compile("\\[\\d+\\-\\d+\\-\\d+ (\\d+):(\\d+)\\] falls asleep");
        Pattern awake = Pattern.compile("\\[\\d+\\-\\d+\\-\\d+ (\\d+):(\\d+)\\] wakes up");

        int curr_guard = -1;
        int last_sleep = 0;
        for (String line : inp) {
            Matcher g = guard.matcher(line);
            Matcher s = asleep.matcher(line);
            Matcher w = awake.matcher(line);

            if (g.matches()) {
                curr_guard = Integer.parseInt(g.group(3));
                if (timeline.get(curr_guard) == null) {
                    timeline.put(curr_guard, new HashMap<Integer, Integer>());
                    for (int i = 0; i < 60; ++i) {
                        timeline.get(curr_guard).put(i, 0);
                    }
                }
            }
            else if (s.matches()) {
                last_sleep = Integer.parseInt(s.group(2));
            }
            else if (w.matches()) {
                int wake_time = Integer.parseInt(w.group(2));
                for (int i = last_sleep; i < wake_time; ++i) {
                    timeline.get(curr_guard).put(i, timeline.get(curr_guard).getOrDefault(i, 0) + 1);
                }
            }
        }

    }

    public static int p1(List<String> inp) {
        int sleepiest_guard = -1;
        int sleepiest_time = -1;
        int sleepiest_min = -1;
        int sleepiest_min_amt = -1;

        for (var guard : timeline.keySet()) {
            int time = 0;
            for (var t : timeline.get(guard).keySet()) {
                time += timeline.get(guard).get(t);
            }
            if (time > sleepiest_time) {
                sleepiest_time = time;
                sleepiest_guard = guard;
            }
        }

        for (var t : timeline.get(sleepiest_guard).keySet()) {
            if (timeline.get(sleepiest_guard).get(t) > sleepiest_min_amt) {
                sleepiest_min_amt = timeline.get(sleepiest_guard).get(t);
                sleepiest_min = t;
            }
        }
        return sleepiest_guard * sleepiest_min;
    }

    public static int p2(List<String> inp) {
        int sleepiest_guard = -1;
        int sleepiest_time = -1;
        int sleepiest_min = -1;

        for (var guard : timeline.keySet()) {
            for (var t : timeline.get(guard).keySet()) {
                if (timeline.get(guard).get(t) > sleepiest_time) {
                    sleepiest_guard = guard;
                    sleepiest_time = timeline.get(guard).get(t);
                    sleepiest_min = t;
                }
            }
        }
        return sleepiest_guard * sleepiest_min;
    }

    public static void main(String[] args) {
        List<String> inp = Utils.readFromFile(args[0]);
        Collections.sort(inp);
        buildTimeline(inp);
        System.out.println(p1(inp));
        System.out.println(p2(inp));
    }
}