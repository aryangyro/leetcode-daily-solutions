# 3420. Count Non-Decreasing Subarrays After K Operations (Hard, Daily Challenge Nov 13, 2026)
# Idea: sliding window over the right end. Keep the window's elements grouped into
# non-decreasing blocks; the cost to make the window non-decreasing is the sum of
# lifts needed to raise each element to its block maximum. A two-stack queue trick
# (in-stack / out-stack) tracks that cost while the left end moves, so each element
# is processed in amortised O(log n). Count valid windows ending at each position.
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        from bisect import bisect_right
        in_vals = []
        in_blocks = []
        in_block_vals = []
        in_pref_cnt = []
        in_pref_cv = []
        in_cost = 0
        out_stack = []

        def total_cost():
            if out_stack:
                ocost, omax = out_stack[-1]
            else:
                ocost, omax = 0, None
            if not in_vals:
                return ocost
            if omax is None:
                return ocost + in_cost
            idx = bisect_right(in_block_vals, omax)
            if idx:
                lift = omax * in_pref_cnt[idx - 1] - in_pref_cv[idx - 1]
            else:
                lift = 0
            return ocost + in_cost + lift

        ans = 0
        left = 0
        for r, x in enumerate(nums):
            in_vals.append(x)
            if not in_blocks:
                in_blocks.append([x, 1, x])
                in_block_vals.append(x)
                in_pref_cnt.append(1)
                in_pref_cv.append(x)
            elif x >= in_blocks[-1][0]:
                in_blocks.append([x, 1, x])
                in_block_vals.append(x)
                in_pref_cnt.append(in_pref_cnt[-1] + 1)
                in_pref_cv.append(in_pref_cv[-1] + x)
            else:
                last = in_blocks[-1]
                last[1] += 1
                last[2] += x
                in_cost += last[0] - x
                in_pref_cnt[-1] += 1
                in_pref_cv[-1] += last[0]
            cost = total_cost()
            while cost > k:
                if not out_stack:
                    oblocks = []
                    ocost = 0
                    while in_vals:
                        y = in_vals.pop()
                        new_cnt = 1
                        new_sum = y
                        inc = 0
                        while oblocks and oblocks[-1][0] <= y:
                            v, c, s = oblocks.pop()
                            inc += c * (y - v)
                            new_cnt += c
                            new_sum += s
                        ocost += inc
                        oblocks.append([y, new_cnt, new_sum])
                        out_stack.append((ocost, oblocks[0][0]))
                    in_blocks.clear()
                    in_block_vals.clear()
                    in_pref_cnt.clear()
                    in_pref_cv.clear()
                    in_cost = 0
                out_stack.pop()
                left += 1
                cost = total_cost()
            ans += r - left + 1
        return ans
