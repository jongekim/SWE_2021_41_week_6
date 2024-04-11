from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    answer = [0, 0]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                if i<j :
                    answer = [i, j]
                    break
                else :
                    answer = [j, i] 
                    break
    print(answer) 
    return answer