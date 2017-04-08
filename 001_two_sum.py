"""
Note:
    Time: O(n) / O(nlogn) as map causes time complexity as well
    Space: O(n)
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        res, lookup = [], {}
        for index, value in enumerate(nums):
            if target-value in lookup:
                res.append(lookup[target-value])
                res.append(index)
            else:
                lookup[value] = index
        return res

if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
