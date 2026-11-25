#lower bound  >>> We adjust the binary search so that even if we find the target, we keep looking to the left to see if there is an earlier occurrence.

class Solution:
    def countFreq(self, arr, target):
        n = len(arr)

        # Lower bound: first index with value >= target
        l, r = 0, n - 1
        lb = n

        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid] >= target:
                lb = mid
                r = mid - 1
            else:
                
                l = mid + 1

        # Upper bound: first index with value > target
        l, r = 0, n - 1
        ub = n

        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid] > target:
                ub = mid
                r = mid - 1
            else:
                
                l = mid + 1


        return ub - lb