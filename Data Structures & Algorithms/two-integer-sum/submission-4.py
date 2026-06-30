class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ar = nums
        for i in range(len(ar)):
            for j in range( i+1, len(ar)):
                if ar[i]+ar[j] == target:
                    return [i, j]

