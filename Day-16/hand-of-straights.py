class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cards = {}
        for c in hand:
            cards[c] = cards.get(c,0)+1
    
        while cards:
            s = min(cards.keys())

            for i in range(groupSize):
                if s not in cards:
                    return False
                cards[s] -= 1
                if cards[s] == 0:
                    del cards[s]
                s += 1
        
        return True
            
            







        