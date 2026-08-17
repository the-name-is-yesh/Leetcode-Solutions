class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.presum = list(itertools.accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        # return sum(self.nums[left:right+1])
        if left == 0:
            return self.presum[right]
        else:
            return self.presum[right] - self.presum[left-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)