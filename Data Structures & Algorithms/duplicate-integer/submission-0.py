class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b = set()
        for num in nums:
            if num in b:
                return True
            else:
                b.add(num)
        return False
