### Problem 54 - Poker Hands
###---------------------------------------------------------------------------------------------------------------------------------------------------------------
### The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): 
### the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), 
### each player's hand is in no specific order, and in each hand there is a clear winner.

### Solution

from typing import Dict, List, Set, Tuple
import numpy as np

poker_hands = np.genfromtxt('../p054_poker.txt', delimiter=' ', dtype='str')

card_values = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

# Function to determine if royal flush
def isRoyalFlush(hand: List[int], suit: Set[str]) -> Tuple[bool, int]:
	if np.array_equal(hand[8:], np.array([1, 1, 1, 1, 1])):
		if len(suit) == 1:
			return True, card_values['A']
	return False, None

# Function to determine if straight flush
def isStraightFlush(hand: List[int], suit: Set[str]) -> Tuple[bool, int]:
	straight, highCard = isStraight(hand)
	if straight:
		if len(suit) == 1:
			return True, highCard
	return False, None

# Function to determine if four of a kind
def isFourOfAKind(hand: List[int]) -> Tuple[bool, int]:
	for i in range(len(hand)):
		if hand[i] == 4:
			return True, i
	return False, None

# Function to determine in full house
def isFullHouse(hand: List[int]) -> Tuple[bool, int]:
	triple = False
	double = False
	threeCard = None
	for i in range(len(hand)):
		if hand[i] == 3:
			triple = True
			threeCard = i
		if hand[i] == 2:
			double = True
	if triple and double:
		return True, threeCard
	else:
		return False, None

# Function to determine if flush
def isFlush(suit: Set[str], highCard: int) -> Tuple[bool, int]:
	if len(suit) == 1:
		return True, highCard
	return False, None

# Function to determine if straight
def isStraight(hand: List[int]) -> Tuple[bool, int]:
	consecutive = 0
	for i in range(len(hand)):
		if hand[i] > 0:
			consecutive += 1
		else:
			consecutive = 0
		if consecutive == 5:
			highCard = i
			return True, highCard
	return False, None

# Function to determine if three of a kind
def isThreeOfAKind(hand: List[int]) -> Tuple[bool, int]:
	for i in range(len(hand)):
		if hand[i] == 3:
			return True, i
	return False, None

# Function to determine if one or two pairs
def isPairs(hand: List[int]) -> Tuple[bool, int, int]:
	num_pairs = 0
	high_pair = -1
	for i in range(len(hand)):
		if hand[i] == 2:
			num_pairs += 1
			if i > high_pair:
				high_pair = i
	if num_pairs > 0:
		return True, high_pair, num_pairs
	else:
		return False, None, None

# Function to evaluate hand and assign heuristic
def evaluateHand(hand: List[int], suit: Set[int], high_card: int) -> Tuple[int, int]:

	# Royal Flush
	rf_bool, rf_hc = isRoyalFlush(hand, suit)
	if rf_bool:
		return 9, rf_hc

	# Straight Flush
	sf_bool, sf_hc = isStraightFlush(hand, suit)
	if sf_bool:
		return 8, sf_hc

	# Four of a Kind
	fk_bool, fk_hc = isFourOfAKind(hand)
	if fk_bool:
		return 7, fk_hc

	# Full House
	fh_bool, fh_hc = isFullHouse(hand)
	if fh_bool:
		return 6, fh_hc

	# Flush
	fl_bool, fl_hc = isFlush(suit, high_card)
	if fl_bool:
		return 5, fl_hc

	# Straight
	st_bool, st_hc = isStraight(hand)
	if st_bool:
		return 4, st_hc

	# Three of a Kind
	tk_bool, tk_hc = isThreeOfAKind(hand)
	if tk_bool:
		return 3, tk_hc

	# Two Pairs or One Pair
	pa_bool, pa_hc, num_pairs = isPairs(hand)
	if pa_bool:
		if num_pairs == 2:
			return 2, pa_hc
		else:
			return 1, pa_hc

	# Return 0 if only high card
	return 0, high_card


p1_wins = 0
for hand in poker_hands:
	
	player1_cards = np.zeros(13)
	player1_suit = set()
	player1_highcard = 0

	player2_cards = np.zeros(13)
	player2_suit = set()
	player2_highcard = 0

	for card in range(0, 5):
		
		player1_cards[card_values[hand[card][0]]] += 1
		player1_suit.add(hand[card][1])

		if card_values[hand[card][0]] > player1_highcard:
			player1_highcard = card_values[hand[card][0]]

	for card in range(5, 10):

		player2_cards[card_values[hand[card][0]]] += 1
		player2_suit.add(hand[card][1])

		if card_values[hand[card][0]] > player2_highcard:
			player2_highcard = card_values[hand[card][0]]

	p1_score, p1_high = evaluateHand(player1_cards, player1_suit, player1_highcard)
	p2_score, p2_high = evaluateHand(player2_cards, player2_suit, player2_highcard)

	if p1_score > p2_score:
		p1_wins += 1
	elif p1_score == p2_score:
		if p1_high > p2_high:
			p1_wins += 1
		elif p1_high == p2_high:
			if player1_highcard > player2_highcard:
				p1_wins += 1

print('The number of hands won by Player 1 is: ' + str(p1_wins))