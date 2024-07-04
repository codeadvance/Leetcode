class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={} #empty dictionary- reason we haven't started anything yet
        for i in range(len(nums)):
            if nums[i] not in dic: #not found then unique value store in there
                dic[nums[i]]=i
            else:
                if abs(i-dic[nums[i]]) <=k:
                    return True
                else:
                    dic[nums[i]]=i
        return False
