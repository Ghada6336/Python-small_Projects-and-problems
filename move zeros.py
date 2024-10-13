def moveZeroes(nums):
    zeroes = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            nums[zeroes], nums[i] = nums[i], nums[zeroes]
            zeroes = zeroes + 1
    return nums


nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))

nums2 = [0, 2, 3, 0, 0, 100]
print(moveZeroes(nums2))
