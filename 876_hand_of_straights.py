class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        

        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for key in sorted(count.keys()):

            if count[key] == 0:
                continue
            
            need = count[key]


            for i in range(0, groupSize):

                if key+i not in count:
                    return False
                
                if count[key + i] < need:
                    return False
                
                count[key + i] = count[key+i] - need
        
        return True