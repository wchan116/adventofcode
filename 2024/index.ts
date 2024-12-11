import fs from "fs";
import childProcess from "child_process";

function die(msg: string) {
  console.log(msg);
  process.exit(1);
}

async function main() {
  if (process.argv.length < 3) {
    die("Usage: pnpm test <day-number>");
  }

  let day = process.argv[2]?.padStart(2, "0");

  try {
    const day_code = `./days/${day}.ts`;
    let day_input_file = `input/${day}.in`;

    if (process.argv.length === 4 && process.argv[3] === "temp") {
      day_input_file = "./temp";
    }

    let day_input = fs
      .readFileSync(day_input_file, "utf-8")
      .split(/\r?\n/)
      .filter((line) => line !== "")
      .map((line) => line.trim());

    const { p1, p2 } = await import(day_code);
    console.log("Part 1 -", p1(day_input));
    console.log("Part 2 -", p2(day_input));
  } catch (e) {
    console.log(e);
    die(`ERROR: Day ${day} files do not exist`);
  }
}

main();
