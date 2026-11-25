class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find mid 
        leftid = 0
        rightid = len(nums)-1

        while (leftid <= rightid):
            mid = leftid+(rightid - leftid)//2

            if(target == nums[mid]):
                return mid
            
            if(target < nums[mid]):
                rightid = mid-1
            else:
                leftid = mid+1
            


            

        
        return -1




        