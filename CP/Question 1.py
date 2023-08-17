def check_10(rank_counts):
    if "10" in rank_counts.keys():
        rank_counts["X"] = rank_counts["10"]
        del rank_counts["10"]
    return rank_counts

def rank_Counts(hand):
    rank_counts = {}

    for card in hand:
        if card[:-1] in rank_counts:
            rank_counts[card[:-1]] +=1
        else:
            rank_counts[card[:-1]] = 1

    check_rank_counts = check_10(rank_counts)

    return check_rank_counts

def is_flush(hand):
    suits = {card[-1] for card in hand} # hashset => (s,d,c,h)
    return len(suits) == 1 # if all same {s} or ... 

def is_straight(sorted_ranks):
    testset = "123456789XJQKA"
    temp_sorted_ranks = sorted_ranks[:] 

    if "A" in sorted_ranks and "2" in sorted_ranks:
        temp_sorted_ranks.pop()
        temp_sorted_ranks = ["1"] + temp_sorted_ranks

    return True if ("".join(temp_sorted_ranks) in testset) else False

def PokerHandRanking(hand):
    if len(hand) != len(set(hand)):
        return "Invalid Hand"
    
    rank_counts = rank_Counts(hand)
    
    rank_order = "23456789XJQKA"
    
    sorted_ranks = sorted(rank_counts.keys(), key=lambda x: rank_order.index(x))

    if is_flush(hand):
        if is_straight(sorted_ranks):
            if "A" in sorted_ranks and "K" in sorted_ranks:
                return "Royal Flush"
            else:
                return "Straight Flush" 
        else:
            return "Flush"  
    
    elif 4 in rank_counts.values():
        return "Four of a Kind"
    
    elif 3 in rank_counts.values():
        if 2 in rank_counts.values():
            return 'Full House'
        else:
            return 'Three of a Kind'
   
    elif is_straight(sorted_ranks):
        return "Straight"
        
    elif list(rank_counts.values()).count(2) == 2:
        return "Two Pair"
    
    elif 2 in rank_counts.values():
        return "Pair"
        
    else:
        return 'High Card'

#testcase
hand = ["10h", "Js", "Qh", "Ks", "Ah"]
print(PokerHandRanking(hand))



    
    