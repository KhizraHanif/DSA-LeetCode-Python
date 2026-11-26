#Find the sorted half → save its smallest value → search the other half.
class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        l = 0
        r = len(nums)-1
      
        mini = nums[0]
        while l <= r:
            mid = l + (r-l)//2
            if nums[l] <= nums[mid]:
            # Left half is sorted: save its smallest value.
                mini = min(mini, nums[l])
                l = mid + 1       # Explore the right half.
            else:
            # Right half is sorted: save its smallest value.
                mini = min(mini, nums[mid])
                r = mid - 1       # Explore the left half.
        return mini

        return -1



                    






