class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = mx
            if temp > mx:
                mx = temp
        arr[-1] = -1
        return arr

        
            
            