def straight(ranks,cards):
    a = []
    b = []
    for i in ranks:
        i=i.split()
        a.append(cards[i[0]])
        b.append(i[2])
    a.sort()
    if(len(set(a))==5 and a[4]==13 and a[3]==12 and a[2]==11 and a[1]==10 and a[0]==1 and len(set(b))==1):
        return "Royal Flush"
    elif(len(set(a))==5 and a[4]-a[0]==4  and len(set(b))==1):
        return 'Straight Flush'
    else:
        return False
def four(ranks,cards):
    a = []
    b = []
    for i in ranks:
        i=i.split()
        a.append(cards[i[0]])
        b.append(i[2])
    a.sort()
    if((a.count(max(a))==4 or a.count(min(a))==4) and len(set(b))==4):
        return 'Four of a kind'
    else:
        return False
def full_house(ranks,cards):
    a = []
    for i in ranks:
        i=i.split()
        a.append(cards[i[0]])
    a.sort()
    
    if((a.count(max(a))==2 and a.count(min(a))==3)or(a.count(min(a))==2 and a.count(max(a))==3)):
        return 'Full House'
    else:
        return False
def flush(ranks,cards):
    a = []
    for i in ranks:
        i=i.split()
        a.append(i[2])
    if(len(set(a))==1):
        return 'Flush'
    return False
def sequence(ranks,cards):
    a = []
    for i in ranks:
        i=i.split()
        a.append(cards[i[0]])
    a.sort()
    if(len(set(a))==5 and a[4]-a[0]==4):
        return 'Sequence'
    else:
        return False
def three_kind(ranks,cards):
    a = []
    for i in ranks:
        i=i.split()
        a.append(cards[i[0]])
#     print(a)
    if(len(set(a))==3):
        return 'Three of a Kind'
    return False
def two_pair(ranks,cards):
    a = []
    for i in ranks:
        i=i.split()
        a.append(cards[i[0]])
    a.sort()
    if((a.count(min(a))==2 and a.count(max(a))==2) or (a.count(min(a))==2 and a.count(a[2])==2) or (a.count(a[2])==2 and a.count(max(a))==2)):
        return 'Two Pair'
    return False
def pair(ranks,cards):
    a = []
    for i in ranks:
        i=i.split()
        a.append(cards[i[0]])
    if(len(set(a))==4):
        return 'A Pair'
    return False
def max_card(ranks,cards):
    a = []
    for i in ranks:
        i=i.split()
        a.append(cards[i[0]])
    b = max(a)
    for i in ranks:
        c = i
        i=i.split()
        if(b==cards[i[0]]):
            return c
def max_card1(ranks,cards):
    return 'Max Card'
def build_best_hand(hands_2, hands_5):
    hands = []
    hands.append(hands_5)
    for i in hands_2:
        hand = []
        hand.append(i)
        for j in hands_5:
            for k in hands_5:
                if j != k:
                    hand.append(k)
            hands.append(hand.copy())
            hand = []
            hand.append(i)
    hand = [hands_2[0],hands_2[1],0,0,0]
    l = len(hands_5)
    for i in range(l):
        hand[2] = hands_5[i]
        for j in range(i+1,l):
            if i==j or j == l:
                continue
            hand[3] = hands_5[j]
            for k in range(j+1, l):
                if k==j or k==l:
                    continue
                hand[4] = hands_5[k]
                hands.append(hand.copy())
    for i in hands:
        i.sort()
    return poker(hands)
def poker(hands):
    return max(hands, key=hand_rank)
def hand_rank(a):
    cards = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
    if(not straight(a,cards)):
        if(not four(a,cards)):
            if(not full_house(a,cards)):
                if(not flush(a,cards)):
                    if(not sequence(a,cards)):
                        if(not three_kind(a,cards)):
                            if(not two_pair(a,cards)):
                                if(not pair(a,cards)):
                                    return max_card(a,cards)
                                else:
                                    return pair(a,cards)
                            else:
                                return two_pair(a,cards)
                        else:
                            return three_kind(a,cards)
                    else:
                        return sequence(a,cards)
                else:
                    return flush(a,cards)
            else:
                return full_house(a,cards)
        else:
            return four(a,cards)
    else:
        return straight(a,cards)


def winner(a,b,e):
    wi = {"Royal Flush":10,"Straight Flush":9,"Four of a kind":8,"Full House":7,"Flush":6,"Sequence":5,"Three of a Kind":4,"Two Pair":3,"A Pair":2,"Max Card":1}
    cards = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
    a1 = a
    b1 = b
    a = build_best_hand(a,e)
    b = build_best_hand(b,e)
#     print(a)
# #     print(b)
    s = [str(i) for i in hand_rank(a)]  
    res = ("".join(s))
#     print(res)
    s1 = [str(i) for i in hand_rank(b)]  
    res1 = ("".join(s1))
#     print(res1)
    if res in a and res1 in b:
#         print("HEllo")
        res = max_card(a1,cards)
        res1 = max_card(b1,cards)
        res=res.split()
        res1=res1.split()
#         print(cards[str(res[0])])
        p1=cards[str(res[0])]
        p2=cards[str(res1[0])]
        #print(p1)
        #print(p2)
        if p1>p2:
            return "user"
        elif p1<p2:
            return "computer"
        else:
            return "draw"
    elif res in a and res1 not in b:
        return "computer"
    elif res not in a and res1 in b:
        return "user"
    else:
#         print("HEllo")
        p1 = wi[str(res)]
        p2 = wi[str(res1)]
#         print(a)
#         print(b)
        if(p1>p2):
            return "user"
        elif p2 > p1:
            return "computer"
        else:
            res=max_card(a1,cards)
            res1=max_card(b1,cards)
            res=res.split()
            res1=res1.split()
            #print(cards[str(res[0])])
            p1=cards[str(res[0])]
            p2=cards[str(res1[0])]
#             print(p1)
#             print(p2)
            if p1>p2:
                return "user"
            elif p1<p2:
                return "computer"
            else:
                return "draw"
    
    
# if __name__ =='__main__':
#     wi = {"Royal Flush":10,"Straight Flush":9,"Four of a kind":8,"Full House":7,"Flush":6,"Sequence":5,"Three of a Kind":4,"Two Pair":3,"A Pair":2}
#     a = ['Six of Clubs','Ace of Clubs']
#     e = ['Eight of Clubs','Three of Clubs','Five of Clubs','Ace of Diamonds','Jack of Clubs']
#     a = build_best_hand(a,e)
#     print(wi[hand_rank(a)])