from collections import defaultdict as dd
from itertools import combinations, permutations, product

# From Q1, Q2, Q3 and Q4

# index values
PLAY_TYPE = 0
PLAY = 1
CARD = 1
PHASE_ID = 0
PHASE = 1
PLAYS = 1
PLAY_1 = 0
GROUPS = 1
PLAYER = 0
END = -1

# totalled accumulations
ACCUMULATIONS = [34, 55, 68, 76, 81, 84, 86, 87]

# dictionary matching card values to their respective scores
SCORES = {'A': 25, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}

# dictionary matching scores to their respective card values
VALUE_SCORES = {25: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                8: '8', 9: '9', 10: '0', 11: 'J', 12: 'Q', 13: 'K'}


# index values
CARD_1 = 0
VALUE = 0
VALUE_ = 1
SUIT = 1
FIRST = 0
SET_1 = 0
SET_2 = 1

VALUES_ORDERED = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'J',
                  'Q', 'K', '2', '3', '4', '5', '6', '7', '8', '9',
                  '0', 'J', 'Q', 'K', '2', '3', '4', '5', '6', '7', 
                  '8', '9', '0', 'J', 'Q', 'K', '2', '3', '4', '5',
                  '6', '7', '8', '9', '0', 'J', 'Q', 'K']


# dictionary matching card values to their respective integer values
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13} 



def card_1_value_count(cards):
    """Accepts `cards` - a list of cards with tuples of value and suit as 
    input and returns the number of times the value of card 1 appears in 
    `cards`.
    """
    
    # finds the value of card 1
    card_1_value = cards[CARD_1][VALUE]
    
    # tallies the number of times the value of card 1 is the same as the value 
    # of each card in `cards`
    first_value_count = 0 
    for value, suit in cards:
        if value == card_1_value:
            first_value_count += 1
            
    return first_value_count


def card_1_suit_count(cards):
    """Accepts `cards` - a list of cards with tuples of value and suit as 
    input and returns the number of times the suit of card 1 appears in 
    `cards`.
    """
    
    # finds the suit of card 1
    card_1_suit = cards[CARD_1][SUIT]
    
    # tallies the number of times the suit of card 1 is the same as the suit 
    # of each card in `cards`    
    first_suit_count = 0 
    for value, suit in cards:
        if suit == card_1_suit:
            first_suit_count += 1
            
    return first_suit_count


def is_run(cards, num):
    """Accepts `cards` - a list of cards with tuples of value and suit as 
    input and `num` - an integer number with a maximum of 8. True is returned 
    if `cards` is a run of `num` cards with at least two `natural` cards and
    False is return if it is not.
    """
    
    # value of first card in group
    card_1_value = cards[CARD_1][VALUE]
    
    if len(cards) == num:
        
        # finds the values of each card in the group
        values = [value for value, suit in cards]
        
        # removes the wild card from a different copy of cards
        cards_copy1 = cards.copy()
        for card in cards:
            if card[VALUE] == 'A':
                cards_copy1.remove(card)
                
        # checks if there is at least two natural cards
        if len(cards_copy1) >= 2:    
                
            # checks that the first card is not a wild card
            if card_1_value != 'A':
                
                # finds the `num` values needed to check for that it is a run
                ordered_index = VALUES_ORDERED.index(card_1_value)
                values_needed = VALUES_ORDERED[ordered_index:ordered_index 
                                               + num]
                
                # checks to see that all `num` card values (as required) match
                # with the `num` values of the needed run (can be wild)
                count = 0
                for value, value_needed in zip(values, values_needed):
                    if value == value_needed or value == 'A':
                        count += 1
                if count == num:
                    return True
            
            # if the first card is a wild card
            else:
                for value in values:
                    if value != 'A':
                        index_non_a = values.index(value)
                        break

                # finds the `num` values needed to check for that it is a run
                ordered_index = VALUES_ORDERED.index(value)
                index_needed = ordered_index + 12 - index_non_a
                values_needed = VALUES_ORDERED[index_needed:index_needed + num]

                # checks to see that all `num` card values (as required) match
                # with the `num` values of the needed run (can be wild)              
                count = 0
                for value, value_needed in zip(values, values_needed):
                    if value == value_needed or value == 'A':
                        count += 1
                if count == num:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False
    
    
def is_same_colour(cards):
    """Accepts `cards` - a list of cards with tuples of value and suit as 
    input and returns True if all cards have the same colour or False if they
    do not all have the same colour.
    """    
    
    # keeps a count of how many times each colour occurs and checks if all
    # cards in the input `cards` have the same colour
    count_black = 0
    count_red = 0
    for value, suit in cards:
        if suit in 'SC':
            count_black += 1
            if count_black == len(cards):
                return True
        else:
            count_red += 1
            if count_red == len(cards):
                return True
                
    return False
    
    
def is_34_accumulation(cards):
    """Accepts `cards` - a list of cards with tuples of value and suit as 
    input and returns True if the values sum to 34 or False if they do not
    """
  
    # looks into the dictionary and accumulates the values
    accumulation = 0
    for value, suit in cards:
        accumulation += VALUES[value]
        
    return accumulation == 34


def phazed_group_type(group):
    """Accepts `group` - a list of cards where each element is composed as a
    2-character string with the value (drawn from '234567890JQKA') followed by 
    the suit (drawn from 'SHDC'). A sorted list of integers representing each 
    combination type for which the group is valid for is returned.
    """
    
    if not group:
        return None
    
    
    combination_types= []
    cards = []
    
    # splits each card in `group` as a list of cards with tuples of value and 
    # suit
    for card in group:
        value, suit = list(card)
        cards.append((value, suit))
    
    # finds the value of the first card
    card_1_value = cards[CARD_1][VALUE]

    # Combination 1
    if len(cards) == 3:
        
        # checks if the values of three non wild cards are the same
        if card_1_value != 'A' and card_1_value_count(cards) == 3:
            combination_types.append(1)
            
        # checks if the conditions are met for when there is a wild card
        elif any('A' in card for card in cards):
                
            # removes the wild card from a different copy of cards
            cards_copy1 = cards.copy()
            for card in cards:
                if card[VALUE] == 'A':
                    cards_copy1.remove(card)
                    
            # checks if there is at least two natural cards
            if len(cards_copy1) >= 2:
                
                # checks if the value of the remaining 2 natural cards 
                # are the same
                if card_1_value_count(cards_copy1) == 2:
                    combination_types.append(1)
                        
    # Combination 2
    if len(cards) == 7:
        
        # checks if the suit of all non wild cards are the same
        if card_1_value != 'A' and card_1_suit_count(cards) == 7:
            combination_types.append(2)
            
        # checks if the conditions are met for when there is a wild card
        elif any('A' in card for card in cards):
                
            # removes the wild card from a different copy of cards
            cards_copy1 = cards.copy()
            for card in cards:
                if card[VALUE] == 'A':
                    cards_copy1.remove(card)
                    
            # checks if there is at least two natural cards
            if len(cards_copy1) >= 2:
                
                # checks if the suit of the remaining natural cards 
                # are the same
                if card_1_suit_count(cards_copy1) == len(cards_copy1):
                    combination_types.append(2)
                    
    # Combination 3
    if len(cards) == 4:
        
        # checks if the values of four non wild cards are the same
        if card_1_value != 'A' and card_1_value_count(cards) == 4:
            combination_types.append(3)
            
        # checks if the conditions are met for when there is a wild card
        elif any('A' in card for card in cards):
                
            # removes the wild card from a copy of the group of cards
            cards_copy1 = cards.copy()
            for card in cards:
                if card[VALUE] == 'A':
                    cards_copy1.remove(card)
                    
            # checks if there is at least two natural cards
            if len(cards_copy1) >= 2:
                
                # checks if the value of the remaining natural cards 
                # are the same
                if card_1_value_count(cards_copy1) == len(cards_copy1):
                    combination_types.append(3)
    
    # Combination 4
    # checks that the group of cards is a run of eight cards
    if is_run(cards, 8):
        combination_types.append(4)

    # Combination 5
    # checks if the group of cards is a run of four cards
    if is_run(cards, 4):
        
        # removes the wild card from a copy of the group of cards
        cards_copy1 = cards.copy()
        for card in cards:
            if card[VALUE] == 'A':
                cards_copy1.remove(card)
                
        # checks if all non wild cards have the same colour
        if is_same_colour(cards_copy1):
            combination_types.append(5)
    
    # Combination 6
    # checks if the group of cards accumulate to 34
    if is_34_accumulation(cards):
        combination_types.append(6)
    
    # Combination 7
    # checks if the group of cards accumulate to 34 and have the same colour
    if is_34_accumulation(cards) and is_same_colour(cards):
        combination_types.append(7)
        
    return combination_types

    

def phazed_phase_type(phase):
    """Accepts `phase` - a combination of card groups in the form of a list of
    where each element is composed as a 2-character string with the value 
    (drawn from '234567890JQKA') followed by the suit (drawn from 'SHDC'). A 
    sorted list of integers representing each Phase for which `phase` is valid 
    for is returned.
    """
    
    # Checks that phase is not empty
    if all(not group for group in phase):
        return None

    phases = []
    
    # Applies to phases 2 and 5
    if len(phase) == 1:
        
        # Phase 2
        # Checks if the set satisfies card combination type 2
        if 2 in phazed_group_type(phase[SET_1]):
            phases.append(2)
            
        # Phase 5
        # Checks if the set satisfies card combination type 4
        if 4 in phazed_group_type(phase[SET_1]):
            phases.append(5)
    
    # Applies to phases 1, 3, 4, 6, 7
    elif len(phase) == 2:
        
        # Phase 1
        # Checks if both groups satisfy card combination type 1 
        if (1 in phazed_group_type(phase[SET_1]) 
            and 1 in phazed_group_type(phase[SET_2])):
            phases.append(1)
        
        # Phase 3
        # Checks if both groups satisfy card combination type 6
        if (6 in phazed_group_type(phase[SET_1]) 
            and 6 in phazed_group_type(phase[SET_2])):
            phases.append(3)
                
        # Phase 4
        # Checks if both groups satisfy card combination type 3
        if (3 in phazed_group_type(phase[SET_1]) 
            and 3 in phazed_group_type(phase[SET_2])):
            phases.append(4)
            
        # Phase 6
        # Checks if both groups satisfy card combination type 7
        if (7 in phazed_group_type(phase[SET_1]) 
            and 7 in phazed_group_type(phase[SET_2])):
            phases.append(6)

        # Phase 7
        # Checks if the two groups in the phase satifies both card combination 
        # types 5 and 3 in that order
        if (5 in phazed_group_type(phase[SET_1]) 
            and 3 in phazed_group_type(phase[SET_2])):
            phases.append(7)
    
    return sorted(phases)


def phazed_is_valid_play(play, player_id, table, turn_history, phase_status, 
                         hand, discard):
    """Accepts as input, `play` - which descrbes the play being made and 
    `player_id`, `table`, `turn_history`, `phase_status`, `hand`, `discard` - 
    describing the current hand state. True is returned if `play` is valid
    relative to the current hand state and False otherwise.
    """
    
    # Finds history of turns in current lap
    if len(turn_history) < 4:
        current_turns = turn_history
    elif len(turn_history) % 4 == 0:
        current_turns = turn_history[- 4:]
        if current_turns[END][PLAYER] != player_id:
            current_turns = []
    else:
        current_turns = turn_history[- (len(turn_history) % 4):]
    
    # Play Type 1
    # Checks if a card was picked up from the top of the deck
    if play[PLAY_TYPE] == 1:

        # Checks if the player making the pickup play has not yet made a play
        count = 0
        for player, plays in current_turns:
            if player_id == player:
                count += 1
        if count != 0:
            return False
        
        return True
        
        
    # Play Type 2  
    # Checks if a card was picked up from the discard pile    
    elif play[PLAY_TYPE] == 2:
        
        # Checks if the player making the pickup play has not yet made a play
        count = 0
        for player, plays in current_turns:
            if player_id == player:
                count += 1
        if count != 0:
            return False
            
        # Checks if the card attempted to be picked up is the same as the
        # card on the discard pile
        if not play[CARD] == discard:
            return False

        return True
        
        
    # Play Type 3
    elif play[PLAY_TYPE] == 3:
        
        # Checks if the phase play matches the declared phase type
        if not play[PHASE][PHASE_ID] in phazed_phase_type(play[PHASE][PLAY]):
            return False
        
        # Checks if it is the required phase
        if not play[PHASE][PHASE_ID] == phase_status[player_id] + 1:
            return False
        
        # Checks if the player has already made a play
        count = 0
        for player, plays in current_turns:
            if player_id == player:
                count += 1
        if count == 0:
            return False
        
        # Checks if the player has not yet played a phase in the current hand
        if not table[player_id][PHASE_ID] is None:
            return False
        
        # finds the number of times each card in hand occurs
        hand_cards_count = dd(int)
        for card in hand:
            hand_cards_count[card] += 1

        # Checks if all cards in the attempted phase play are in the players 
        # `hand` and counts how many times each card occurs in the attempted
        # phase play
        play_cards_count = dd(int)
        for group in play[PHASE][PLAY]:
            for card in group:
                if card not in hand:
                    return False
                play_cards_count[card] += 1
        
        # Checks if the player is trying to play the same card more what they
        # have in their hand
        for card, play_card_count in play_cards_count.items():
            if play_card_count > hand_cards_count[card]:
                return False
        
        return True
    
    # Play Type 4
    elif play[PLAY_TYPE] == 4:
        
        # Checks if the player has already made a play
        count = 0
        for player, plays in current_turns:
            if player_id == player:
                count += 1
        if count == 0:
            return False
        
        # Checks if the player has already played a phase in the current hand
        if table[player_id][PHASE_ID] is None:
            return False
        
        # Finds the card about to play
        play_card = play[PLAY][CARD - 1]
        
        # Checks if the player has the card about to play in their hand
        if play_card not in hand:
            return False
        
        # Finds the player ID of the phase the card is to be placed on
        play_player = play[1][1][0]
        
        # Checks if the phase play the player is about to play on exists
        if table[play_player][PHASE_ID] is None:
            return False
        
        # Finds the index of the group within the phase the card is to 
        # be placed on
        group_index = play[1][1][1]
        
        # Finds the group within the phase the card is to be placed on
        play_group = table[play_player][GROUPS][group_index]
        
        # Finds the index of the position within the group the card is 
        # to be played to
        position_index = play[1][1][2]

        
        # Checks if the play is to be made on phase 1 or 4
        # (Place a card of the same value on to a set of cards of 
        # the same value)
        if table[play_player][PHASE_ID] in [1, 4]:
            
            # Checks if the card is placed at a valid index for the group
            if not position_index <= len(play_group):
                return False
            
            # Returns True if the card about to play is a wild card
            if play_card[VALUE] == 'A':
                return True
            
            # Finds the value of the cards in the groups to be played on
            values = [value for value, suit in play_group]

            # Checks if the card has the same value as the cards in the group
            if not play_card[VALUE] in values:
                return False
            
            return True
            
            
        # Checks if the play is to be made on phase 2
        # (Place a card of the same suit on to a set of cards of 
        # the same suit)
        if table[play_player][PHASE_ID] == 2:
            
            # Checks if the card is placed at a valid index for the group
            if not position_index <= len(play_group):
                return False
            
            # Returns True if the card about to play is a wild card
            if play_card[VALUE] == 'A':
                return True            
            
            # Finds the value of the cards in the groups to be played on
            suits = [suit for value, suit in play_group]

            # Checks if the card has the same value as the cards in the group
            if not play_card[SUIT] in suits:
                return False
            
            return True
            
            
        # Checks if the play is to be made on phase 3
        # (Place a card to build on an accumulation)
        if table[play_player][PHASE_ID] == 3:
            
            # Checks if the card is placed at a valid index for the group
            if not position_index <= len(play_group):
                return False            
            
            # looks into the dictionary and accumulates the values
            accumulation = 0
            for value, suit in play_group:
                accumulation += VALUES[value]
            
            # finds the index value in `ACCUMULATIONS` of which
            # totalled accumulation they are up to
            index = 0
            for accumulation_fixed in ACCUMULATIONS:
                if accumulation >= accumulation_fixed:
                    index = ACCUMULATIONS.index(accumulation_fixed)
                else:
                    break
            
            # finds the accumulation total which being built towards
            next_accumulation = ACCUMULATIONS[index + 1] 

            # Checks whether the player only has one card left in the hand
            if len(hand) == 1:

                # Checks if it is completing the accumulation
                if (accumulation + VALUES[play_card[VALUE]] 
                    == next_accumulation):
                    return True
                else:
                    return False
                
            # finds the maximum allowed value
            max_allowed = (ACCUMULATIONS[index + 1] - ACCUMULATIONS[index])

            # Checks if the addition to the current accumulation will not go 
            # over the total limit of the accumulation in which the player is 
            # building towards
            if not VALUES[play_card[VALUE]] <= max_allowed:
                return False
            
            return True
                

        # Checks if the play is to be made on phase 5
        # (Place a card which continues the sequence on a run)
        if table[play_player][PHASE_ID] == 5:  
            
            # Checks if the card is placed at a valid index for the group
            if position_index not in [0, len(play_group)]:
                return False
            
            # Checks if there is already 12 cards in the run
            if len(play_group) == 12:
                return False
            
            # Checks whether it is a valid run
            # If the card is added to the start of the run
            if position_index == 0:
                
                # splits each card in the new group as a list of cards with 
                # tuples of value and suit                
                new_run_together = [play_card] + play_group
                new_run = [(value, suit) for value, suit in new_run_together]
                
                if is_run(new_run, len(play_group) + 1):
                    return True
                
            # If the card is added to the end of the run
            if position_index == len(play_group):
                
                # splits each card in the new group as a list of cards with 
                # tuples of value and suit                  
                new_run_together = play_group + [play_card]
                new_run = [(value, suit) for value, suit in new_run_together]
                
                if is_run(new_run, len(play_group) + 1):
                    return True
                
            return False
        
        # Checks if the play is to be made on phase 6
        # (Place a card to build on an accumulation of the same colour)
        if table[play_player][PHASE_ID] == 6:
            
            # splits each card in the new group as a list of cards with 
            # tuples of value and suit                
            new_run_together = [play_card] + play_group
            new_run = [(value, suit) for value, suit in new_run_together]
            
            # Checks if all cards in the new accumulation has the same colour
            if not is_same_colour(new_run):
                return False
            
            # Checks if the card is placed at a valid index for the group
            if not position_index <= len(play_group):
                return False            
            
            # looks into the dictionary and accumulates the values
            accumulation = 0
            for value, suit in play_group:
                accumulation += VALUES[value]

            # finds the index value in `ACCUMULATIONS` of which
            # totalled accumulation they are up to
            index = 0
            for accumulation_fixed in ACCUMULATIONS:
                if accumulation >= accumulation_fixed:
                    index = ACCUMULATIONS.index(accumulation_fixed)
                else:
                    break
                    
            # finds the accumulation total which being built towards
            next_accumulation = ACCUMULATIONS[index + 1] 

            # Checks whether the player only has one card left in the hand
            if len(hand) == 1:

                # Checks if it is completing the accumulation
                if (accumulation + VALUES[play_card[VALUE]] 
                    == next_accumulation):
                    return True
                else:
                    return False
                
            # finds the maximum allowed value
            max_allowed = (ACCUMULATIONS[index + 1] - ACCUMULATIONS[index])

            # Checks if the addition to the current accumulation will not go 
            # over the total limit of the accumulation in which the player is 
            # building towards
            if not VALUES[play_card[VALUE]] <= max_allowed:
                return False
            
            return True         
            
        # Checks if the play is to be made on phase 7
        if table[play_player][PHASE_ID] == 7:            
            
            # If placing a card which continues the sequence on a run of the 
            # same colour
            if group_index == 0:
            
                # splits each card in the new group as a list of cards with 
                # tuples of value and suit                
                new_run_together = [play_card] + play_group
                new_run = [(value, suit) for value, suit in new_run_together]
                
                # Checks if all cards in the new run has the same 
                # colour
                if not is_same_colour(new_run):
                    return False
                
                # Checks if the card is placed at a valid index for the group
                if position_index not in [0, len(play_group)]:
                    return False
                
                # Checks if there is already 12 cards in the run
                if len(play_group) == 12:
                    return False
                
                # Checks whether it is a valid run
                # If the card is added to the start of the run
                if position_index == 0:
                    
                    # splits each card in the new group as a list of cards with 
                    # tuples of value and suit                
                    new_run_together = [play_card] + play_group
                    new_run = [(value, suit) for value, suit 
                               in new_run_together]
                    
                    if is_run(new_run, len(play_group) + 1):
                        return True
                    
                # If the card is added to the end of the run
                if position_index == len(play_group):
                    
                    # splits each card in the new group as a list of cards with 
                    # tuples of value and suit                  
                    new_run_together = play_group + [play_card]
                    new_run = [(value, suit) for value, suit 
                               in new_run_together]
                    
                    if is_run(new_run, len(play_group) + 1):
                        return True
                    
                return False                            
                
            # If placing a card of the same value on to a set of cards of 
            # the same value
            if group_index == 1:            
    
                # Checks if the card is placed at a valid index for the group
                if not position_index <= len(play_group):
                    return False
                
                # Returns True if the card about to play is a wild card
                if play_card[VALUE] == 'A':
                    return True
                
                # Finds the value of the cards in the groups to be played on
                values = [value for value, suit in play_group]
    
                # Checks if the card has the same value as the cards in the 
                # group
                if not play_card[VALUE] in values:
                    return False
                
                return True
            
            
    # Play Type 5   
    elif play[PLAY_TYPE] == 5:
        
        # Checks if the player has already made a play
        count = 0
        for player, plays in current_turns:
            if player_id == player:
                count += 1
        if count == 0:
            return False

        # Checks if the attempted discard card is a card which the player holds
        if not play[CARD] in hand:
            return False 
        
        # Finds the plays the player has made so far in the turn
        for player, plays in current_turns:
            if player_id == player:
                break

        # Checks if the player has already discarded a card
        if plays[len(plays) - 1][PLAY_TYPE] == 5:
            return False

        for item in plays:
            
                # Checks if the player has played on a card in the turn
                if item[PLAY_TYPE] == 4:
                
                    # Finds the player ID of the phase the card was placed on
                    play_player = item[1][1][0]
                    
                    # Checks if the player has made a play on an accumulation
                    if table[play_player][PHASE_ID] in [3, 6]:
                        
                        # Checks if accumulation of all cards sum to a 
                        # valid accumulation for each group
                        for group in table[play_player][GROUPS]:
                            
                            # looks into the dictionary and accumulates the 
                            # values
                            accumulation = 0
                            for value, suit in group:
                                accumulation += VALUES[value]
                                
                            if accumulation not in ACCUMULATIONS:
                                return False

        return True
    
    
    return False


def phazed_score(hand):
    """Accepts `hand` - a list of cards where each element is composed as a
    2-character string with the value (drawn from '234567890JQKA') followed by 
    the suit (drawn from 'SHDC'). The score for the `hand` is returned as a
    non-negative integer.
    """
    
    # finds the score values for each card in `hand` by looking into the
    # dictionary `SCORES`
    scores = [SCORES[value] for value, suit in hand]
    
    return sum(scores)



# Q5 Starts here

def phazed_play(player_id, table, turn_history, phase_status, hand, discard):
    """Accepts as input `player_id`, `table`, `turn_history`, `phase_status`,
    `hand` and `discard` - describing the current hand state. For each phase 
    state the player is on, `phazed_play` returns a 2-tuple describing the 
    optimum play to make. By default, `phazed_play` returns a play which picks
    up from the discard pile if the score of the card on the discard pile is
    less than 4. If not, picks up the card from the deck. Depending on the
    play state, `phazed_play` returns a discard play which discards the
    highest scoring card in `hand` by default.
    """
    
    # determines whether a phase has been played in the turn
    played_phase_in_turn = False
    for player, plays in turn_history:
        if player == player_id:
            for play_type, play in plays:
                if play_type == 3:
                    played_phase_in_turn = True
                    break

                    
    # if on phase 1
    if phase_status[player_id] == 0:

        # finds a list of wild cards in hand and
        # finds the number of times each value occurs that isn't a wild card
        values_count = dd(int)
        for value, suit in hand:
            if value != 'A':
                values_count[value] += 1
        
        # values are arranged in order of greatest count
        values_count_greatest = sorted([(count, value) for value, count
                              in values_count.items()], reverse=True)
        
        
        # values are arranged in order of least count
        values_count_least = sorted([(count, value) for value, count
                              in values_count.items()])
        
        
        # best pickup scenario
        # picks up from discard pile if there is a card and not a wild
        # card and value occurs most in hand but less than 3
        if discard is not None and values_count_greatest:
            value, suit = discard
            if (values_count_greatest[FIRST][VALUE_] == value 
                and values_count[value] < 3 and value != 'A'):
                if phazed_is_valid_play((2, discard), player_id, table,
                                        turn_history, phase_status,
                                        hand, discard):
                    return (2, discard)           


        # checks if `group` a card combination of 3 cards with same value
        # is a valid group type 1
        allowed_combinations = []
        for group in combinations(hand, 3):
            if 1 in phazed_group_type(list(group)):
                allowed_combinations.append(list(group))
        
        # sorts order based on the sets of cards with greatest score
        if allowed_combinations:
            allowed_combinations = sorted(allowed_combinations, key=lambda 
                                          group: SCORES[group[FIRST][VALUE]], 
                                          reverse=True)
        
        # plays phase 1 if a combination of 2 sets in 'allowed_combinations'
        # is valid
        for phase in combinations(allowed_combinations, 2):
            play = (3, (1, list(phase)))
            if phazed_is_valid_play(play, player_id, table, turn_history,
                            phase_status, hand, discard):
                return play

        
        # best discard card to build towards phase:
        # discards card with value of least count
        if values_count_least:
            for value, suit in hand:
                if value == values_count_least[FIRST][VALUE_]:
                    discard_card = ''.join([value, suit])
                    if phazed_is_valid_play((5, discard_card), player_id,
                                            table, turn_history,
                                            phase_status, hand, discard):
                        return (5, discard_card)
        

    # if on phase 2
    if phase_status[player_id] == 1 and not played_phase_in_turn:
        
        # finds the number of times each suit occurs that isn't a wild card
        suits_count = dd(int)
        for value, suit in hand:
            if value != 'A':
                suits_count[suit] += 1
        
        # suits are arranged in order of greatest count
        suits_count_greatest = sorted([(count, suit) for suit, count
                              in suits_count.items()], reverse=True)
        
        
        # suits are arranged in order of least count
        suits_count_least = sorted([(count, suit) for suit, count
                              in suits_count.items()])
        
        
        # best pickup scenario
        # picks up from discard pile if there is a card and it's not a wild
        # card and suit occurs most in hand
        if discard is not None and suits_count_greatest:
            value, suit = discard
            if suits_count_greatest[FIRST][SUIT] == suit and value != 'A':
                if phazed_is_valid_play((2, discard), player_id, table,
                                        turn_history, phase_status,
                                        hand, discard):
                    return (2, discard)              
        
        
        # checks if `group` a card combination of 7 cards with same suit 
        # is a valid group type 2
        allowed_combinations = []
        for group in combinations(hand, 7):
            if 2 in phazed_group_type(list(group)):
                allowed_combinations.append(list(group))
                
        # sorts order based on the sets of cards with greatest score
        allowed_combinations = sorted(allowed_combinations,
                                      key=phazed_score, reverse=True)  
        
        # plays phase 2 if a possible phase in `allowed_combinations` is valid
        for phase in allowed_combinations:
            play = (3, (2, [phase]))
            if phazed_is_valid_play(play, player_id, table, turn_history,
                            phase_status, hand, discard):
                return play

        
        # best discard card to build towards phase:
        # discards card with suit of least count
        if suits_count_least:
            for value, suit in hand:
                if suit == suits_count_least[FIRST][SUIT]:
                    discard_card = ''.join([value, suit])
                    if phazed_is_valid_play((5, discard_card), player_id,
                                            table, turn_history,
                                            phase_status, hand, discard):
                        return (5, discard_card)
         
            
    # if on phase 3
    if phase_status[player_id] == 2 and not played_phase_in_turn:    

        # checks if `group` is a valid group type with 34 accumulation
        allowed_combinations = []
        for i in range(3, len(hand) + 1):
            for group in combinations(hand, i):
                if is_34_accumulation([(value, suit) for value,
                                       suit in group]):
                    allowed_combinations.append(list(group))
                    
        # sorts order based on the sets of cards with greatest number of cards
        # and makes a phase play if a combination of two 34 accumulation
        # is valid        
        for phase in combinations(sorted(allowed_combinations, key=len,
                                         reverse=True), 2):
            play = (3, (3, list(phase)))
            if phazed_is_valid_play(play, player_id, table, turn_history,
                            phase_status, hand, discard):
                return play        

        
    # if on phase 4
    if phase_status[player_id] == 3 and not played_phase_in_turn:    

        # finds the number of times each value occurs that isn't a wild card
        values_count = dd(int)
        for value, suit in hand:
            if value != 'A':
                values_count[value] += 1
        
        # values are arranged in order of greatest count
        values_count_greatest = sorted([(count, value) for value, count
                              in values_count.items()], reverse=True)
        
        
        # values are arranged in order of least count
        values_count_least = sorted([(count, value) for value, count
                              in values_count.items()])
        
        
        # best pickup scenario
        # picks up from discard pile if there is a card and not a wild
        # card and value occurs most in hand but less than 4
        if discard is not None and values_count_greatest:
            value, suit = discard
            if (values_count_greatest[FIRST][VALUE_] == value 
                and values_count[value] < 4 and value != 'A'):
                if phazed_is_valid_play((2, discard), player_id, table,
                                        turn_history, phase_status,
                                        hand, discard):
                    return (2, discard)  
        

        # checks if `group` a card combination of 4 cards with same value
        # is a valid group type 3
        allowed_combinations = []
        for group in combinations(hand, 4):
            if 3 in phazed_group_type(list(group)):
                allowed_combinations.append(list(group))
        
        # sorts order based on the sets of cards with greatest score
        if allowed_combinations:
            allowed_combinations = sorted(allowed_combinations, key=lambda 
                                          group: SCORES[group[FIRST][VALUE]], 
                                          reverse=True)
            
        # plays phase 4 if a combination of 2 sets in 'allowed_combinations'
        # is valid
        for phase in combinations(allowed_combinations, 2):
            play = (3, (4, list(phase)))
            if phazed_is_valid_play(play, player_id, table, turn_history,
                            phase_status, hand, discard):
                return play

            
        # best discard card to build towards phase:
        # discards card with value of least count
        if values_count_least:
            for value, suit in hand:
                if value == values_count_least[FIRST][VALUE_]:
                    discard_card = ''.join([value, suit])
                    if phazed_is_valid_play((5, discard_card), player_id,
                                            table, turn_history,
                                            phase_status, hand, discard):
                        return (5, discard_card)
        
                
    # if on phase 5
    if phase_status[player_id] == 4 and not played_phase_in_turn: 
        
        # finds `hands_values_items', a list of sorted individual non wild
        # cards for each card value in hand and `wilds`, a list of wild cards
        # in hand
        hand_copy = hand.copy()
        wilds = []
        for value, suit in hand:
            if value == 'A':
                wild = ''.join([value, suit])
                hand_copy.remove(wild)
                wilds.append(wild)
        hand_values_dict = dd(list)
        for value, suit in hand_copy:
            hand_values_dict[VALUES[value]].append(''.join([value, suit]))
        hand_values_sorted = sorted(hand_values_dict.items())
        hand_values_items = [cards[FIRST] for value, cards
                             in hand_values_sorted]
        
        # best pickup scenario
        # picks up from discard pile if there is a non wild card and
        # value of `discard` is not in hand
        hand_values = [value for value, cards in hand_values_sorted]
        if discard is not None and hand_values:
            if (discard[VALUE] != 'A' 
                and VALUES[discard[VALUE]] not in hand_values):
                if phazed_is_valid_play((2, discard), player_id, table,
                                        turn_history, phase_status,
                                        hand, discard):
                    return (2, discard)             
        
        # loops all possible number of wild cards through each position in
        # `hand_values_items` and finds all possible `allowed_runs` 
        # made of 8 cards
        allowed_runs = []
        if wilds:
            for i in range(1, len(wilds) + 1):
                wild = wilds[0:i]
                for j in range(len(hand_values_items)):
                    pre_run = hand_values_items.copy()
                    pre_run.insert(j, wild)
                    pre_run2 = []
                    for card in pre_run:
                        if type(card) is list:
                            pre_run2 += card
                        else:
                            pre_run2.append(card)
                    if len(pre_run2) == 8:
                            if 4 in phazed_group_type(pre_run2):
                                allowed_runs.append(pre_run2)
                            
                    if len(pre_run2) > 8:        
                        for k in range(len(pre_run2) - 7):
                            run = pre_run2[k:8 + k]
                            if 4 in phazed_group_type(run):
                                allowed_runs.append(run)
        
        # if there were no wild cards in `hand` determines if
        # `hand_values_items` can produce a run of 8 cards
        else:
            for i in range(len(hand_values_items) - 7):
                run = hand_values_items[i:8 + i]
                if 4 in phazed_group_type(run):
                    allowed_runs.append(run)
        
        # sorts order based on the run of cards with greatest score
        allowed_runs = sorted(allowed_runs, key=phazed_score, reverse=True)  
        
        # plays phase 5 if a possible run of 8 cards in `allowed_runs` is valid
        for phase in allowed_runs:
            play = (3, (5, [phase]))
            if phazed_is_valid_play(play, player_id, table, turn_history,
                            phase_status, hand, discard):
                return play     

            
        # best discard card to build to phase
        # discards card with most non wild value count
        hand_values_most = sorted(hand_values_dict.items(), reverse=True)
        for value, cards in hand_values_most:
            if len(cards) > 1:
                discard_card = cards[FIRST]
                if phazed_is_valid_play((5, discard_card), player_id,
                                        table, turn_history,
                                        phase_status, hand, discard):
                    return (5, discard_card)
                
        
    # if on phase 6
    if phase_status[player_id] == 5 and not played_phase_in_turn:

        # checks if `group` is a valid group type with 34 accumulation of same
        # colour
        allowed_combinations = []
        for i in range(3, len(hand) + 1):
            for group in combinations(hand, i):
                if 7 in phazed_group_type(list(group)):
                    allowed_combinations.append(list(group))
                    
        # sorts order based on the sets of cards with greatest number of cards
        # and makes a phase play if a combination of two 34 accumulation of
        # same colour is valid
        for phase in combinations(sorted(allowed_combinations, key=len,
                                         reverse=True), 2):
            play = (3, (6, list(phase)))
            if phazed_is_valid_play(play, player_id, table, turn_history,
                            phase_status, hand, discard):
                return play        


    # if on phase 7
    if phase_status[player_id] == 6 and not played_phase_in_turn:
        
        # finds `hands_values_items', a list of sorted individual non wild
        # cards for each card value in hand and `wilds`, a list of wild cards
        # in hand
        hand_copy = hand.copy()
        wilds = []
        for value, suit in hand:
            if value == 'A':
                wild = ''.join([value, suit])
                hand_copy.remove(wild)
                wilds.append(wild)
        hand_values_dict = dd(list)
        for value, suit in hand_copy:
                hand_values_dict[VALUES[value]].append(''.join([value, suit]))
        hand_values_sorted = sorted(hand_values_dict.items())
        hand_values_items = [cards[FIRST] for value, cards 
                             in hand_values_sorted]
        
        # loops all possible number of wild cards through each position in
        # `hand_values_items` and finds all possible `allowed_runs` 
        # made of 4 cards of same colour
        allowed_runs = [] 
        if wilds:
            for i in range(1, len(wilds) + 1):
                wild = wilds[0:i]
                for j in range(len(hand_values_items)):
                    pre_run = hand_values_items.copy()
                    pre_run.insert(j, wild)
                    pre_run2 = []
                    for card in pre_run:
                        if type(card) is list:
                            pre_run2 += card
                        else:
                            pre_run2.append(card)
                    if len(pre_run2) == 4:
                        if 5 in phazed_group_type(pre_run2):
                            allowed_runs.append(pre_run2)
                                        
                    if len(pre_run2) > 4:        
                        for k in range(len(pre_run2) - 3):
                            run = pre_run2[k:4 + k]
                            if 5 in phazed_group_type(run):
                                allowed_runs.append(run)
                                
        # if there were no wild cards in `hand`, determines if
        # `hand_values_items` can produce a run of 4 cards of same colour
        else:
            for i in range(len(hand_values_items) - 3):
                run = hand_values_items[i:4 + i]
                if 5 in phazed_group_type(run):
                    allowed_runs.append(run)
                    
        # sorts order based on the run of cards with greatest score
        allowed_runs = sorted(allowed_runs, key=phazed_score, reverse=True)
        
        # checks if `group` a card combination of 4 cards with same value
        # is a valid group type 3
        allowed_combinations = []
        for group in combinations(hand, 4):
            if 3 in phazed_group_type(list(group)):
                allowed_combinations.append(list(group))
                
        # sorts order based on the sets of cards with greatest score
        if allowed_combinations:
            allowed_combinations = sorted(allowed_combinations, key=lambda x: 
                                          SCORES[x[FIRST][VALUE]], 
                                          reverse=True)
        
        # combines each of `allowed_runs` and `allowed_combinations` to create
        # possible combinations of phase 7
        allowed_phases = []
        for phase in product(allowed_runs, allowed_combinations):
            allowed_phases.append(list(phase))
        
        # plays phase 7 if possible phase 7s in 'allowed_phases' is valid
        for phase in allowed_phases:
            play = (3, (7, list(phase)))
            if phazed_is_valid_play(play, player_id, table, turn_history,
                            phase_status, hand, discard):
                return play  

        
        # sorts order of hand based on card with greatest score
        hand = sorted(hand, key=lambda card: SCORES[card[VALUE]], reverse=True)       
        
        # finds `group` a card combination of 4 cards with same value that
        # is a valid group type 3
        best_set = []
        for group in combinations(hand, 4):
            if 3 in phazed_group_type(list(group)):
                best_set.append(list(group))
                break
        
        # build towards set of four cards of same value
        if not best_set:
            
            # finds the number of times each value occurs that isn't 
            # a wild card
            values_count = dd(int)
            for value, suit in hand:
                if value != 'A':
                    values_count[value] += 1
            
            # values are arranged in order of greatest count
            values_count_greatest = sorted([(count, value) for value, count
                                  in values_count.items()], reverse=True)
            
            
            # values are arranged in order of least count
            values_count_least = sorted([(count, value) for value, count
                                  in values_count.items()])
            
            
            # best pickup scenario
            # picks up from discard pile if there is a card and not a wild
            # card and value occurs most in hand but less than 4
            if discard is not None and values_count_greatest:
                value, suit = discard
                if (values_count_greatest[FIRST][VALUE_] == value 
                    and values_count[value] < 4 and value != 'A'):
                    if phazed_is_valid_play((2, discard), player_id, table,
                                            turn_history, phase_status,
                                            hand, discard):
                        return (2, discard)
                    
            # best discard card to build towards phase:
            # discards card with value of least count
            if values_count_least:
                for value, suit in hand:
                    if value == values_count_least[FIRST][VALUE_]:
                        discard_card = ''.join([value, suit])
                        if phazed_is_valid_play((5, discard_card), player_id,
                                                table, turn_history,
                                                phase_status, hand, discard):
                            return (5, discard_card)
         
        # builds towards run
        if best_set:
            
            for card in best_set[FIRST]:
                hand.remove(card)
            
            # finds `hands_values_items', a list of sorted individual non wild
            # cards for each card value in hand and `wilds`, a list of wild 
            # cards in hand
            hand_copy = hand.copy()
            wilds = []
            for value, suit in hand:
                if value == 'A':
                    wild = ''.join([value, suit])
                    hand_copy.remove(wild)
                    wilds.append(wild)
            hand_values_dict = dd(list)
            for value, suit in hand_copy:
                hand_values_dict[VALUES[value]].append(''.join([value, suit]))
            hand_values_sorted = sorted(hand_values_dict.items())
            hand_values_items = [cards[FIRST] for value, cards
                                 in hand_values_sorted]
            
            # best pickup scenario
            # picks up from discard pile if there is a non wild card and
            # value of `discard` is not in hand
            hand_values = [value for value, cards in hand_values_sorted]
            if discard is not None and hand_values:
                if (discard[VALUE] != 'A' 
                    and VALUES[discard[VALUE]] not in hand_values):
                    if phazed_is_valid_play((2, discard), player_id, table,
                                            turn_history, phase_status,
                                            hand, discard):
                        return (2, discard)
                    
            # best discard card to build to phase
            # discards card with most non wild value count
            hand_values_most = sorted(hand_values_dict.items(), reverse=True)
            for value, cards in hand_values_most:
                if len(cards) > 1:
                    discard_card = cards[FIRST]
                    if phazed_is_valid_play((5, discard_card), player_id,
                                            table, turn_history,
                                            phase_status, hand, discard):
                        return (5, discard_card)

    
    
    # pickup play and discard play by default:

    # picks up from discard pile if there is a card
    # and the score of it is less than 4
    if discard is not None:
        if SCORES[discard[VALUE]] < 4:
            if phazed_is_valid_play((2, discard), player_id, table,
                                    turn_history, phase_status,
                                    hand, discard):
                return (2, discard)
            
    # otherwise picks up from the deck
    if phazed_is_valid_play((1, None), player_id, table, turn_history,
                            phase_status, hand, discard):
        return (1, None)
    
    
    # discard play
    # finds card with maximum score in `hand' to discard
    max_score = max([SCORES[value] for value, suit in hand])
    card_value = VALUE_SCORES[max_score]
    discard_card = [card for card in hand if card_value in card][FIRST]
    
    # discards the card with the maximum score if valid
    if phazed_is_valid_play((5, discard_card), player_id, table, turn_history,
                            phase_status, hand, discard):
        return (5, discard_card)




  
if __name__ == '__main__':
    
    """
    phazed_is_valid_play(play, player_id, table, turn_history, phase_status, 
                      hand, discard)
    """
    """
    print(
        
   phazed_play(0, [[None, []], [None, []], [None, []], [None, []]],
   [[3, [[1, 'XX'], [5, '2D']]], [0, [[1, '0H']]]],
   [4, 4, 6, 5],
   ['2C', '3C', '3D', '3S', '4C', '5H', '7S', '9S', 'QC', 'QD', '0H'], '2D')     
        
        
    )
    """
    """
    print(phazed_play(1, [(None, []), (4, [['2C', '3H', '4D', 'AD', '6S', '7C',
      '8S', '9H', '0S', 'JS']]), (None, []), (None, [])], [(0, [(2, 'JS'),
      (5, 'JS')]), (1, [(2, 'JS'), (3, (4, [['2C', '3H', '4D', 'AD', '6S',
      '7C', '8S', '9H']])), (4, ('0S', (1, 0, 8))), (4, ('JS',
      (1, 0, 9)))])], [0, 4, 0, 0], ['5D', 'AD', '5S', '9S', '5S', 'JS'],
                      '7H'))
      
    """