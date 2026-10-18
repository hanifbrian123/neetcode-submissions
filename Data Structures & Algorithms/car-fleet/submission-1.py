class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        
        pos_speed = [(p, s) for p, s in zip(position, speed)]
        pos_speed.sort(key = lambda x: x[0])
        stack = [(target - pos_speed[-1][0]) / pos_speed[-1][1]]

        for i in range(n-2, -1, -1):
            timeNeeded = (target - pos_speed[i][0]) / pos_speed[i][1]
            if timeNeeded > stack[-1]:
                stack.append(timeNeeded)
        
        return len(stack)