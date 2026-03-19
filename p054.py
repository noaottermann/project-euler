from euler import run
from utils import *

# Euler Problem 54

def solve():
    poker = [line.strip() for line in open('p054_poker.txt')]
    player1_wins = 0
    for hand in poker:
        cards = hand.split()
        player1 = cards[:5]
        player2 = cards[5:]
        if compare_hands(player1, player2) > 0:
            player1_wins += 1
    return player1_wins
    
def compare_hands(hand1, hand2):
    score1 = hand_rank(hand1)
    score2 = hand_rank(hand2)
    if score1 > score2:
        return 1
    if score1 < score2:
        return -1
    return 0
    
def hand_rank(hand):
    values = sorted([card_value(card) for card in hand], reverse=True)
    suits = [card[1] for card in hand]
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    groups = sorted(((count, value) for value, count in counts.items()), reverse=True)

    is_flush = len(set(suits)) == 1

    unique_values = sorted(set(values), reverse=True)
    is_straight = False
    straight_high = None
    if len(unique_values) == 5:
        if unique_values[0] - unique_values[-1] == 4:
            is_straight = True
            straight_high = unique_values[0]
        elif unique_values == [14, 5, 4, 3, 2]:
            is_straight = True
            straight_high = 5

    if is_straight and is_flush and straight_high == 14:
        return (10, [14])  # Royal Flush
    if is_straight and is_flush:
        return (9, [straight_high])  # Straight Flush
    if groups[0][0] == 4:
        four_value = groups[0][1]
        kicker = groups[1][1]
        return (8, [four_value, kicker])  # Four of a Kind
    if groups[0][0] == 3 and groups[1][0] == 2:
        return (7, [groups[0][1], groups[1][1]])  # Full House
    if is_flush:
        return (6, values)  # Flush
    if is_straight:
        return (5, [straight_high])  # Straight
    if groups[0][0] == 3:
        trip_value = groups[0][1]
        kickers = sorted([v for v in values if v != trip_value], reverse=True)
        return (4, [trip_value] + kickers)  # Three of a Kind
    if groups[0][0] == 2 and groups[1][0] == 2:
        pair_values = sorted([groups[0][1], groups[1][1]], reverse=True)
        kicker = groups[2][1]
        return (3, pair_values + [kicker])  # Two Pairs
    if groups[0][0] == 2:
        pair_value = groups[0][1]
        kickers = sorted([v for v in values if v != pair_value], reverse=True)
        return (2, [pair_value] + kickers)  # One Pair
    return (1, values)  # High Card
    
def card_value(card):
    value_str = card[0]
    if value_str.isdigit():
        return int(value_str)
    elif value_str == 'T':
        return 10
    elif value_str == 'J':
        return 11
    elif value_str == 'Q':
        return 12
    elif value_str == 'K':
        return 13
    elif value_str == 'A':
        return 14
    
if __name__ == '__main__':
    run(solve, problem_id=54)