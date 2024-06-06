class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        lookup = Counter(hand)
        hand.sort()

        if len(hand) % groupSize:
            return False

        while hand:
            card_num = hand.pop()
            while hand and card_num not in lookup:
                card_num = hand.pop()

            lookup[card_num] -= 1
            if not lookup[card_num]:
                del lookup[card_num]

            if not hand:
                return True

            for i in range(groupSize - 1):
                if card_num - 1 in lookup:
                    lookup[card_num - 1] -= 1
                    if not lookup[card_num - 1]:
                        del lookup[card_num - 1]
                else:
                    # print(hand, card_num, lookup)
                    return False
                card_num -= 1


        