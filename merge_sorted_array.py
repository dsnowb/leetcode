class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(len(nums1)):
            while len(nums2) and nums2[0] < nums1[i]:
                for j in range(len(nums1) - 1, i, -1):
                    nums1[j] = nums1[j - 1]
                nums1[i] = nums2.pop(0)
                i += 1
            if not len(nums2):
                break
        
        if len(nums2):
            for i in range(len(nums2)):
                nums1[-1 - i] = nums2[-1 - i]
