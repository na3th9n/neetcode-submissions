class Solution:
    # notes
        # return maximum amount of money you can rob
        # decisions: rob house or don't rob house
        # state: index of the house we are on
        # base cases:
            # if the previous house robbed, return 0
            # return the value of the house if we are robbing it

    # sample
        # nums[], output = 0
        # nums[x], output = x
        # nums[x,y] output = x
        # nums [x,y,z] output = x + z or y

        # [x, y, 3, 3]
        # 
        # i = 0, curr_sum = 1
        # i = 1, 
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]


        curr = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = prev
            prev = max(nums[i] + curr, prev)
            curr = temp

        return prev 