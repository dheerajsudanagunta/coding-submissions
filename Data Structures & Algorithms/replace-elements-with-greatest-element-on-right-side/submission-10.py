class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightmax = -1
        ans = [0]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            ans[i] = rightmax
            rightmax = max(arr[i],rightmax)
        return ans
            



        
            
     

