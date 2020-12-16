from collections import Counter, defaultdict
from utils.io_util import read_file


input_path = 'inputs/day10_test1.txt'
input_path = 'inputs/day10_test2.txt'
input_path = 'inputs/day10.txt'


nums = sorted([int(n) for n in read_file(input_path)] + [0])

def count_diff(nums):
    diffs = [nums[i]-nums[i-1] for i in range(1, len(nums))]
    count = Counter(diffs)
    count[3] += 1
    return count 

def dp(nums):
    dp_count = defaultdict(int)
    dp_count[0] = 1

    for n in nums[1:]:
        dp_count[n] = dp_count[n-1] + dp_count[n-2] + dp_count[n-3]

    return dp_count


print(dp(nums))