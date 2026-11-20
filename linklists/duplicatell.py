class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Treat each INDEX as a node.
        # nums[index] tells us which index to visit next.
        #
        # Example: nums = [1, 3, 4, 2, 2]
        # Following indices: 0 → 1 → 3 → 2 → 4 → 2 → ...
        #                                  ↑_____|
        #
        # Every value is a valid index, so we never reach None.
        # Eventually, we revisit an index and enter a cycle.
        # The cycle's entrance is the duplicate number.

        # PHASE 1: Find a meeting point inside the cycle.
        slow = 0
        fast = 0

        # Move before checking equality.
        # Both start at 0, but that initial equality isn't a cycle meeting.
        slow = nums[slow]          # Follow one connection.
        fast = nums[nums[fast]]    # Follow two connections.

        while True:
            # Compare their positions after a complete round.
            if slow == fast:
                slow1 = slow      # Save the meeting index itself.
                break             # Exit phase 1, not the function.

            slow = nums[slow]
            fast = nums[nums[fast]]

        # PHASE 2: Find the cycle's entrance.
        # The first meeting point is not necessarily the entrance.
        #
        # Keep slow1 at the meeting point.
        # Start slow2 at the SAME starting index used in phase 1.
        slow2 = 0

        # Now BOTH pointers move ONE step each round.
        # Floyd's algorithm guarantees they meet at the cycle entrance:
        # the distance from 0 to the entrance matches the distance
        # from the meeting point to the entrance, allowing full cycle laps.
        while slow1 != slow2:
            slow1 = nums[slow1]
            slow2 = nums[slow2]

        # Equality makes the loop stop, so return AFTER the loop.
        # The entrance has incoming connections from two different indices:
        # one from the path into the cycle and one from inside the cycle.
        # Both positions store this entrance index as their value.
        # Therefore, this index is the duplicated VALUE.
        return slow1

        # Time: O(n)
        # Extra space: O(1)
        # The input array is never modified.