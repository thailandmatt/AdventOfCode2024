f = open('Day7.txt' , "r")
lines = f.readlines()
f.close()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

total = 0

def canBe(nums, answer):
    if len(nums) == 1:
        return nums[0] == answer
    
    if (nums[0] * nums[1] <= answer):
        newNums = [nums[0] * nums[1]] + nums[2:]
        ok = canBe(newNums, answer)
        if (ok): return True

    if (nums[0] + nums[1] <= answer):
        newNums = [nums[0] + nums[1]] + nums[2:]
        ok = canBe(newNums, answer)
        if (ok): return True

    return False

def canBe2(nums, answer):
    if len(nums) == 1:
        return nums[0] == answer
    
    if (nums[0] * nums[1] <= answer):
        newNums = [nums[0] * nums[1]] + nums[2:]
        ok = canBe2(newNums, answer)
        if (ok): return True

    if (nums[0] + nums[1] <= answer):
        newNums = [nums[0] + nums[1]] + nums[2:]
        ok = canBe2(newNums, answer)
        if (ok): return True

    if (int(str(nums[0]) + str(nums[1])) <= answer):
        newNums = [int(str(nums[0]) + str(nums[1]))] + nums[2:]
        ok = canBe2(newNums, answer)
        if (ok): return True

    return False
    
for line in lines:
    split1 = line.split(':')
    nums = [int(x) for x in split1[1].strip().split(' ')]
    answer = int(split1[0])
    ok = canBe(nums, answer)
    if (ok): total += answer

print(total)

total2 = 0
for line in lines:
    split1 = line.split(':')
    nums = [int(x) for x in split1[1].strip().split(' ')]
    answer = int(split1[0])
    ok = canBe2(nums, answer)
    if (ok): total2 += answer

print(total2)