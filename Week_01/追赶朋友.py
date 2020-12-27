class Solution:
    def findMinMinutes(self, n: int, k: int) -> int:
        if n > k:
            return n - k
        else:
            i = 0
            k0 = k - k % 2
            while k0 / 2 > 2 * n:
                i += 1
                k0 = k0 / 2
            OneStep = int(min(abs(k0 - n), abs(n - k0 / 2)))
            return i + OneStep + k % 2







