class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Rotated sorted array with DISTINCT values.
        # At least one half of the current range is sorted.
        l = 0
        r = len(nums) - 1

        # Both endpoints are included; l == r leaves one node to check.
        while l <= r:
            mid = l + (r - l) // 2

            # Found the target: return its INDEX.
            if nums[mid] == target:
                return mid

            # LEFT half is sorted.
            # <= also handles l == mid (a one-element half).
            if nums[l] <= nums[mid]:

                # Is the target inside this sorted half's value range?
                # BOTH boundaries must hold.
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    # Target cannot be in the sorted left half.
                    l = mid + 1

            # Otherwise, RIGHT half is sorted.
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    # Target cannot be in the sorted right half.
                    r = mid - 1

            # We always exclude mid because it was already checked.

        # l > r: no candidates remain.
        return -1



    # search is rotated array II
    class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        # Search range includes BOTH l and r.
        l = 0
        r = len(nums) - 1

        while l <= r:
            # Recalculate mid whenever the search range changes.
            mid = l + (r - l) // 2

            # Check the middle BEFORE discarding any positions.
            if nums[mid] == target:
                return True

            # DUPLICATES: equal endpoints and middle hide which half is sorted.
            # We already know the middle isn't the target, so these equal
            # endpoints aren't the target either. Safely skip both.
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue  # Restart the loop and calculate a new mid.

            # LEFT half is sorted.
            if nums[l] <= nums[mid]:

                # Target must satisfy BOTH boundaries to belong here.
                # Exclude mid because we already checked it.
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # Otherwise, RIGHT half is sorted.
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        # l > r means no candidates remain.
        return False


    # worst tc can be O(n) because may be entire array is fully duplicate 