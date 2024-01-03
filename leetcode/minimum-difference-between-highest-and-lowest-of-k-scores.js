/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumDifference = function(nums, k) {
    if (k == 1) {
        return 0
    };

    nums.sort((a, b) => a - b)
    minDifference = Infinity

    console.log(nums)
    for (let i = 0; i < nums.length - k + 1;i++) {
            console.log(i, nums[i])
            minDifference = Math.min(minDifference, nums[i + k - 1] - nums[i])

    }
    return minDifference
};