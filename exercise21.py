# Given a sequence numbers print the median of the sequence. Note: your solution should work if the sequence is a list or tuple.
numbers=[1,2,3,4,5,6,7]
nums = sorted(numbers)
n = len(nums)

if n % 2 == 1:
    print(nums[n//2])
else:
    print((nums[n//2 - 1] + nums[n//2]) / 2)