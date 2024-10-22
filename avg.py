def average(nums):
    total = 0
    for num in range(0, len(nums)):
        total = total + nums[num]
    avg = total/len(nums)
    return float(avg)

nums = [10, 15, 20]
Average = average(nums)
print(Average)