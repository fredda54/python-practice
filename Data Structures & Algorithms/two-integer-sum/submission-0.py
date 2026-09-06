class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {};
        for i in range(len(nums)+1):
            j = i+1;
            diff = target - nums[j];
            hashmap[nums[i]] = i;
            if diff in hashmap:
                return [hashmap[diff],j]
