class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_nums = []
        for num in nums:
            if val == num:
                continue
            new_nums.append(num)
        for i in range(len(new_nums)):
            nums[i]=new_nums[i]
        return len(new_nums)
        