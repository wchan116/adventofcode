const directions: Record<
  "n" | "ne" | "nw" | "e" | "w" | "s" | "se" | "sw",
  (x: number, y: number) => [number, number]
> = {
  n: (x, y) => [x + 1, y],
  ne: (x, y) => [x + 1, y + 1],
  nw: (x, y) => [x + 1, y - 1],
  e: (x, y) => [x, y + 1],
  w: (x, y) => [x, y - 1],
  s: (x, y) => [x - 1, y],
  se: (x, y) => [x - 1, y + 1],
  sw: (x, y) => [x - 1, y - 1],
};

let how = 0;

const dfs = (
  grid: string[][],
  x: number,
  y: number,
  dir: keyof typeof directions,
  s?: string,
) => {
  if (x < 0 || x >= grid.length) return;
  if (y < 0 || y >= grid[0].length) return;

  const word = s === undefined ? grid[x][y] : s + grid[x][y];
  if (!"XMAS".startsWith(word)) return;
  if (word === "XMAS") {
    // console.log("S", word, x, y);
    ++how;
  }

  const [new_x, new_y] = directions[dir](x, y);
  dfs(grid, new_x, new_y, dir, word);
};

export const p1 = (inp: string[]) => {
  const grid = inp.map((i) => i.split(""));
  for (let i = 0; i < grid.length; ++i) {
    for (let j = 0; j < grid[i].length; ++j) {
      if (grid[i][j] === "X") {
        Object.keys(directions).forEach((d) => {
          dfs(grid, i, j, d as keyof typeof directions);
        });
      }
    }
  }

  return how;
};

export const p2 = (inp: string[]) => {
  const grid = inp.map((i) => i.split(""));
  let i = 1;
  let j = 1;

  let xmas = 0;
  while (i < grid.length) {
    if (
      grid[i][j] === "A" &&
      grid[i + 1][j + 1] === "S" &&
      grid[i - 1][j - 1] === "M" &&
      grid[i + 1][j - 1] === "S" &&
      grid[i - 1][j + 1] === "M"
    ) {
      xmas++;
    }
    if (i + 2 >= grid.length) {
      i = 0;
      j++;
    } else {
      i++;
    }
  }
};
