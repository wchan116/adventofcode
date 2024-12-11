const get_lists = (inp: string[]): [number[], number[]] => {
  const stack1: number[] = [];
  const stack2: number[] = [];

  inp.forEach((line) => {
    const matches = line.match(/(\d+)\s+(\d+)/);
    if (matches) {
      stack1.push(Number(matches[1]));
      stack2.push(Number(matches[2]));
    }
  });
  stack1.sort();
  stack2.sort();

  return [stack1, stack2];
};

export const p1 = (inp: string[]) => {
  const [stack1, stack2] = get_lists(inp);

  let distance = 0;

  for (let i = 0; i < stack1.length; ++i) {
    const a = stack1[i] ?? 0;
    const b = stack2[i] ?? 0;
    distance += Math.abs(a - b);
  }

  return distance;
};

export const p2 = (inp: string[]) => {
  const [stack1, stack2] = get_lists(inp);

  let sim = 0;
  stack1.forEach((num) => {
    sim += num * stack2.filter((n2) => n2 === num).length;
  });

  return sim;
};
