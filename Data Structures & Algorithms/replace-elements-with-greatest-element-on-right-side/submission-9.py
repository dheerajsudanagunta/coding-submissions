class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            rightmax = -1
            for j in range(i+1,len(arr)):
                rightmax = max(arr[j],rightmax)
            arr[i] = rightmax
        return arr



        
            
     

