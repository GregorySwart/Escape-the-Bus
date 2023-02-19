## Escape the bus

Python simulation of the drinking game Escape the Bus, specifically the ending, where the player “rides the bus”. Here 
the player needs to correctly guess certain characteristics for four cards in succession. If the player makes a wrong 
guess they must start again from the first question (cards that have been revealed up to this point are discarded). If 
all the cards in the deck are used up the game ends. If the player correctly guesses all four questions in succession 
the player wins or “escapes the bus”. The questions, in order, are the following:

1. Is the first card’s colour red or black?
2. Is the second card’s number higher or lower than the first? (Automatic lose if the numbers are the same)
3. Is the third card’s number between or outside the range of the first two cards? (Automatic lose if the third card’s number matches either the first or the second card)
4. What is the fourth card’s suit?
 
The simulation has three methods: **Random**, **Sensible** and **Optimised**.
* Random: The player makes all guesses on a completely random basis.
* Sensible: The player makes guesses based on the characteristics of the cards that have been revealed (e.g. more likely to guess “higher” on the second card if the first card is an Ace)
* Optimal: The player makes guesses taking into consideration the characteristics of the already revealed cards and keeps count of which cards have been discarded already.

The goal is to determine how much the effectiveness of each of these methods differs from each other: 
- What is the probability of a player escaping the bus when they employ each of the three meetings.
- When a game ends, on average, what is the number of cards left in the deck, if any?

### Plan and progress:
- [x] Implement data classes needed to simulate the game (e.g. cards, a deck that can be shuffled and drawn from etc.)
- [x] Create a game class which allows us to create a method that simulates each of the three modes
- [x] Implement random mode
- [x] Implement sensible mode
- [ ] Implement optimised mode
