from utils.io_util import read_file


# input_path = 'inputs/day9_test.txt'
input_path = 'inputs/day9.txt'
nums = [int(n) for n in read_file(input_path)]

def process_nums(nums, preamble_len):
    # The rest
    head = 0

    for n in nums[preamble_len:]:
        valid_sums = []
        for i in range(head, head+preamble_len-1):
            for j in range(head+1, head+preamble_len):
                valid_sums.append(nums[i] + nums[j])

        if n not in valid_sums:
            print(f'Invalid number found: {n}')
            return n
            
        head += 1


def find_cont_nums(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if sum(nums[i:j]) > target:
                break
            if sum(nums[i:j]) == target:
                print('Found the set:', nums[i:j])
                return nums[i:j]


n = process_nums(nums, 25)
target = find_cont_nums(nums, n)
print(min(target) + max(target))