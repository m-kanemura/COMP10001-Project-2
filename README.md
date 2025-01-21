# COMP10001-Project-2

This is my solution to the COMP10001 Project "Phazed".

Outline
Project 2 is based around a card game called "Phazed".

In terms of Project 2 marking, you should now see the Assessment tab for each question, with a mark breakdown: as with Project 1, for Q1-Q5, we will manually mark your code for Approach and Commenting, but for Q6 (the bonus question), marking will be done exclusively based on the bonus tournament (i.e. fully automatically); note that there are no "hidden" test cases set up, meaning you will get the green diamond if you pass the examples BUT that marking of Correctness will still take place, based on the "assess" (= hidden hidden) test cases ... another reason to make use of the tournament to expose errors in your code (and do your own testing, rather than just relying on us!).

Glossary
A glossary, to hopefully help clarify the different "moving parts" of Phazed:

Game: a series of up to 20 Hands, with a cumulative score (based on the sum of the points left in each player's hand at the end of each Hand), which ends either at the end of a Hand in which one or more players have played their last Phase (in which case the player completing their Phases wins, and in the case of a tie, the player with the lowest points wins) OR after 20 Hands (in which case the player with the lowest points wins).
Hand: a series of up to 50 rounds (= 50 Turns per player), based on a fresh deal of the combined decks of cards, which ends when one of the following occurs: (1) a player plays their last card; (2) the Deck has been exhausted; or (3) 50 rounds have been completed.
Turn: a series of Plays by a given player, starting with a single Pick-up Play (from either the Deck or Discard Pile), optionally followed by a Phase Play and zero or more Build Plays to the table, and ended either by the player exhausting their hand (i.e. having played all their cards), or discarding a single card to the Discard Pile.
Play: one of the following actions: (1) a Pick-up Play from the Deck or Discard Pile; (2) a Phase Play of a complete Phase to the table; (3) a Build Play of a single card from the hand (i.e. the cards held by the player) to an existing Group on the table, consistent with the composition of that Group (e.g. for a Set of cards of the same value, a Build Play must be of a card of the same value as the existing cards or a Wild); or (4) a Discard Play of a single card from the hand to the Discard Pile.
Phase: 1-2 Groups of cards, in one of the following combinations:
Phase 1: two Sets of three cards of the same value
Phase 2: one Set of seven cards of the same suit
Phase 3: two Accumulations of cards, each of value 34
Phase 4: two Sets of four cards of the same value
Phase 5: one Run of eight cards
Phase 6: two Accumulations of cards of the same colour, each of value 34
Phase 7: one Run of four cards of one colour + one Set of four cards of the same value
Group: one of the following combinations of cards:
a “Set” of N cards of the same value: N cards of the same value, of any suit
a “Set” of N cards of the same suit: N cards of the same suit, of any values
a “Run” of N cards: a consecutive sequence of N cards (of any combination of suits/colours), based on value; note that, for the purpose of runs, Jacks, Queens and Kings take on the values 11, 12 and 13, resp., and runs can wrap around from 13 to 2
a “Run” of N cards of the same colour: a run of N cards where all cards are of the same colour, as defined by the suit (Spades and Clubs are black, and Hearts and Diamonds are red); once again, runs of the same colour can loop around from 13 to 2
an “N-accumulation” of cards: cards of any suit/colour which add up to N in terms of their combined value; for the purpose of accumulations, Jacks, Queens and Kings take on the values 11, 12 and 13, resp., and Aces take on the value 1
an “N-accumulation” of cards of the same colour: cards of a given colour (all red or all black) which add up to N in terms of their combined value
Accumulation "completion": when building on an accumulation, a player must "complete" it to the next value in the series defined by the (decreasing) Fibonacci sequence 21, 13, 8, 5, 3, 2, 1, 1. That is, when building on a 34-accumulation, the player must perform a series of Build Plays so that it totals 34 + 21 = 55 (noting that they can then continue to build on it to reach the next value of 34 + 21 + 13 = 68, but most complete to 55 along the way).
Tournament
The tournaments for Q5 and Q6 are now up and running, and available once you have submitted your player and passed the one test; a couple of things to note with the tournament:
the moment you submit a player to the tournament, it will be randomly sampled to participate in games against other randomly-selected players, and you will be able to see the full play history of each such game (by clicking on the player ID, then clicking through to an individual game)
you may only have four players active in the tournament at one time (to avoid it getting clogged up with lots of players from one student), with the default policy being that the four most recently-submitted players are selected to be active, and older submissions inactive
if your player is disqualified (by means of making an invalid play, or taking too much time), it will end the game; once a given player has been disqualified from a total of 10 games, it is automatically disqualified from the tournament and will not be sampled to participate in any more games
the actual marking based on the tournament will be based on a freshly-run tournament after submissions close, using the last player that you each submit, so make sure your last submission to the tournament is the player you want to have used for tournament marking, noting that we will not be able to rerun the tournament/recalculate the tournament mark if you submit the wrong player
as a general comment, the tournament is where a lot of debugging of your code will happen, as it will expose your player to a more diverse set of inputs than the static tests, so you should try to submit as early as possible to benefit from this; note that the volume of games in the random (= unofficial) tournament is fixed, meaning that players submitted now will play lots of games (because there are so few players), but players submitted right before the submission deadline will play much fewer games (simply because there will be more players to randomly sample from)
FAQ
Can we assume that all card inputs will be valid?
Yes.

Why aren't there more test cases for phasedout_play valid?
Because there are very few game states where only one play is possible, which is what is required for a unit test.

How do I capture game state in my player, to use as part of my strategy?
If you are wanting to store game state in some way, or data about your player strategy (many of you won't, but for those doing more involved things, this will be relevant, to avoid redundancy of computation), you are permitted to create a SINGLE (that's right, just one ... five is right out) global variable to store this information (noting that this could be a dictionary or an instance of a class, and embed arbitrarily complex objects).

How will tournament marks be calculated?
The tournament is based on running players off against each other randomly (noting that "custom games" don't get counted in the tournament statistics). If your player makes an invalid play at any point, it will be disqualified from the whole game. If your player is disqualified enough times, it will be disqualified from the entire tournament (which is a good reason to submit your player sooner rather than later, to confirm that it is robust over different game states). The marking of the game will be based on your final submission to the tournament, which you can do from Q5 once you pass the test case (noting that we don't do this automatically — it is up to you to enter your player yourself, as we don't know what what players you want entered or not entered — and also that there's a 10 minute exclusion to entering players after each submission ... another reason not to be last minute with the project, did I hear?). Marking will be based on: (1) confirming that your player is not disqualified from the tournament (you will receive 0 marks for the tournament if you are disqualified); and (2) the ranking of the version of the player you submit last to the tournament (so make sure your final submission is the one you want marked!).

For the bonus question, how is marking going to work?
The bonus question will be marked exclusively based on the bonus tournament (separate to the standard tournament, linked off the bonus question on Grok), following the same criteria as for the standard tournament (i.e. your final player mustn't be disqualified in order to get marks).

So how do I access the tournaments?
The tournament for Q5 is now linked from the question on Grok, and the bonus tournament for Q6 will be added in the next day or so.

What are the time limits for my code in the tournament?
There are three time limits that your code must work within:
TIME_LIMIT_INIT = 2.0 # Seconds allowed to initiate player code
TIME_LIMIT_PLAY = 4.0 # Seconds allowed to execute a play
TOTAL_TIME_LIMIT = 60.0 # Cumulative seconds allowed to execute all plays in match
