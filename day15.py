from collections import defaultdict
from utils.io_util import Timer

def memory_game(nums, nturns=2020):
    memory = defaultdict(list)
    last_num = 0
    
    for i in range(nturns):
        if i < len(nums):
            last_num = nums[i]
            memory[last_num].append(i)
        else:
            if len(memory[last_num]) == 1:  # last number is new
                last_num = 0
                memory[last_num].append(i)
            else:
                last_num = memory[last_num][-1] - memory[last_num][-2]
                memory[last_num].append(i)

            if len(memory[last_num]) == 3:
                memory[last_num].pop(0)

    return last_num

# nums = [0,3,6]
nums = [0,3,1,6,7,5]

timer = Timer()
timer.start()
print(memory_game(nums, 30000000))
timer.stop()