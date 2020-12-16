import numpy as np


nums = np.loadtxt('inputs/day1.txt')
nums.sort()

def part1():
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == 2020:
                print(nums[i] * nums[j])
                return

def part2():
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(i, len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020:
                    print(nums[i] * nums[j] * nums[k])
                    return

part2()