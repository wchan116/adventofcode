const is_list_predicate = (
  nums: number[],
  pred: (a: number, b: number) => boolean,
) => {
  let prev = nums[0];
  for (let i = 1; i < nums.length; ++i) {
    if (pred(prev, nums[i])) {
      return false;
    }
    prev = nums[i];
  }
  return true;
};

const is_increasing = (nums: number[]): boolean => {
  return is_list_predicate(nums, (a, b) => a > b);
};

const is_decreasing = (nums: number[]): boolean => {
  return is_list_predicate(nums, (a, b) => a < b);
};

const is_stable = (nums: number[]): boolean => {
  return is_list_predicate(
    nums,
    (a, b) => Math.abs(a - b) === 0 || Math.abs(a - b) > 3,
  );
};

const is_safe = (nums: number[]) =>
  !((!is_increasing(nums) && !is_decreasing(nums)) || !is_stable(nums));

export const p1 = (inp: string[]) => {
  let safe = 0;

  inp.forEach((line) => {
    const nums = line.split(" ").map(Number);

    if (is_safe(nums)) {
      ++safe;
    }
  });

  return safe;
};

export const p2 = (inp: string[]) => {
  let safe = 0;

  inp.forEach((line) => {
    const nums = line.split(" ").map(Number);

    if (is_safe(nums)) {
      ++safe;
    } else {
      let safe_with_removed = false;
      for (let i = 0; i < nums.length; ++i) {
        if (is_safe(nums.slice(0, i).concat(nums.slice(i + 1)))) {
          safe_with_removed = true;
        }
      }
      if (safe_with_removed) {
        ++safe;
      }
    }
  });

  return safe;
};
