def mean(nums):
    return sum(nums) / len(nums)


def median(nums):
    nums = list(nums)
    nums.sort()
    n = len(nums)
    # 根据题设要求返回的中位数，除以 2 下取整
    return nums[n >> 1]


def max_val_sub(nums):
    n = len(nums)
    max_val = float("-inf")

    for mask in range(1, 1 << n):
        subseq = [nums[i] for i in range(n) if mask & (1 << i)]
        seq_mean = mean(subseq)
        seq_median = median(subseq)
        max_val = max(max_val, seq_mean - seq_median)

    return max_val


if __name__ == "__main__":
    a = [1, 3, 5, 9]
    print(max_val_sub(a))
