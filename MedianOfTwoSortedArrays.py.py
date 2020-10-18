class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedArr = sorted(nums1 + nums2)
        mid = int(len(sortedArr) / 2) 
        if len(sortedArr) % 2 == 0:
            return (sortedArr[mid - 1 ] + sortedArr[mid])/2
        else:
            return sortedArr[mid]
