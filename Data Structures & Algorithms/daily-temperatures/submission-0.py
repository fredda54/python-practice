class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        results=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                print(stk[-1])
                stkT, stkInd = stk.pop()
                results[stkInd] = i - stkInd
            stk.append((t,i))
        return results





