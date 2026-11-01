class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = {}
        for num in hand:
            freq[num] = 1 + freq.get(num, 0)
        
        hand.sort()
        stack = []
        for i in range(len(hand)-1, 0, -1):
            if hand[i] - hand[i-1] >= 2:
                stack.append(hand[i])
        stack.append(hand[0])
        
        
        numGroup = len(hand) // groupSize
        curVal = stack.pop()
        
        for i in range(numGroup):
            nextVal = None
            if curVal is None:
                return False
            for j in range(groupSize):
                if freq.get(curVal, 0) != 0:
                    freq[curVal] -= 1
                    if nextVal is None and freq[curVal] >= 1:
                        nextVal = curVal
                    curVal += 1
                else:
                    return False
            if nextVal is not None:
                curVal = nextVal
            elif freq.get(curVal, 0) == 0:
                if stack:
                    curVal = stack.pop()
                else:
                    curVal = None

        return True
"""
stack = 
curval = 8
1 2 3 4 5 6 8 9 9 10 10 11



0
1
2
1 1 1 2 2 2 3 3 3
1 2 2 3 4



1 2 4 2 3 5 3 4
1 2 2 3 3 4 4 5





8


min = 9
1 2 3
8 9 10
9 10 11
"""