class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)
        asort = sorted(a)
        bsort = sorted(b)
        if len(asort) != len(bsort):
            return False

        for i in range(len(asort)):
            if asort[i] == bsort[i]:
                continue
            else:
                return False
        return True
        