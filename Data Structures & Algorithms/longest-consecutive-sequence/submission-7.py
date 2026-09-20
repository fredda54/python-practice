class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        sort = sorted(nums)
        lst = []
        print(sort)
        for n in range(0,len(sort)):
            if not lst:
                lst.append(sort[n])
            elif sort[n] == lst[-1]:
                pass
            elif sort[n] == lst[-1] + 1:
                lst.append(sort[n])
            else:
                lst = []
                lst.append(sort[n])
            hashmap[len(lst)]=lst
    
        for i in range(len(sort),-1,-1):
            if hashmap[i]: return i
        return 0


            