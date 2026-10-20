
from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        # Prefix maximums
        pref_max = [0] * (n + 1)
        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        # Suffix minimums
        suff_min = [float("inf")] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        # Count adjacent descents
        pref_drop = [0] * n
        for i in range(1, n):
            pref_drop[i] = (
                pref_drop[i - 1] + (nums[i - 1] > nums[i])
            )

        def check(k: int) -> bool:
            for start in range(0, n, k):
                end = start + k - 1

                # Count descents inside the block
                drops = pref_drop[end] - pref_drop[start]

                # Include the circular last-to-first comparison
                if nums[end] > nums[start]:
                    drops += 1

                if drops > 1:
                    return False

                # Verify ordering across the block boundary
                if pref_max[start] > suff_min[start]:
                    return False

            return True

        answer = 0

        # Enumerate divisors in pairs
        k = 1
        while k * k <= n:
            if n % k == 0:
                if check(k):
                    answer += k

                other = n // k
                if other != k and check(other):
                    answer += other

            k += 1

        return answer
