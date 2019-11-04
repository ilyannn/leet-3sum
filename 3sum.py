class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        results = []

        # To handle repeating numbers we will count values.
        counts = {}
        for a in nums:
            counts[a] = counts.get(a, 0) + 1

        # All solutions where 3 numbers are the same.
        if counts.get(0, 0) >= 3:
            results.append([0, 0, 0])

        # All solutions where 2 numbers are the same.
        for a, ac in counts.items():
            if a != 0 and ac >= 2:
                b = -2 * a
                if b in counts:
                    results.append([a, a, b])

        # All solutions with different numbers.
        nums = sorted(counts.keys())
        n = len(nums)

        for ai, a in enumerate(nums):
            for bi, b in enumerate(nums[ai + 1:]):
                c = -a - b
                if c <= b:
                    break
                if c in counts:
                    results.append([a, b, c])

        return results
