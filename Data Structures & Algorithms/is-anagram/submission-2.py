class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr_s = list(s)
        arr_t = list(t)
        arr_s.sort()
        arr_t.sort()
        if len(arr_s) != len(arr_t):
            return False

        if arr_s == arr_t:
            return True
        else:
            return False