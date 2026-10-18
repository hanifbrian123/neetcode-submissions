class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = [n-1]
        
        pos_speed = [(position[i], speed[i]) for i in range(n)]
        pos_speed.sort(key = lambda x: x[0])

        for i in range(n-2, -1, -1):
            timeNeededA = (target - pos_speed[i][0]) / pos_speed[i][1]
            
            topSt = stack[-1]
            timeNeededB = (target - pos_speed[topSt][0]) / pos_speed[topSt][1]

            if timeNeededA > timeNeededB:
                stack.append(i)
        
        return len(stack)