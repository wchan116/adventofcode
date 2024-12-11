export const p1 = (inp: string[]) => {
  let sum = 0;
  inp.forEach((line) => {
    const matches = line.match(/(mul\(\d{1,3},\d{1,3}\))/g);
    matches?.forEach((m) => {
      console.log(m);
      const nums = m
        .match(/(\d{1,3}),(\d{1,3})/)
        ?.slice(1, 3)
        .map(Number);
      sum += nums[0] * nums[1];
    });
  });
  return sum;
};

export const p2 = (inp: string[]) => {
  let sum = 0;
  let on = true;
  inp.forEach((line) => {
    const matches = line.match(/(mul\(\d{1,3},\d{1,3}\))|do\(\)|don't\(\)/g);
    matches?.forEach((m) => {
      if (m === "do()") {
        on = true;
      } else if (m === "don't()") {
        on = false;
      } else {
        if (on) {
          const nums = m
            .match(/(\d{1,3}),(\d{1,3})/)
            ?.slice(1, 3)
            .map(Number);
          sum += nums[0] * nums[1];
        }
      }
    });
  });
  return sum;
};
