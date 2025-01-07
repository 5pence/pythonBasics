import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class Deck:
    """ This class geerates a standard French deck of playing cards """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# let's play snap
def play_snap(deck1, deck2):
    print("press Enter for next turn (Control+C to quit): ")
    while True:
        input()  # wait for the enter key...

        # draw random card from each deck
        card1 = random.choice(deck1)
        card2 = random.choice(deck2)

        # Show what was drawn
        print(f"Player 1 drew: {card1.rank} of {card1.suit}")
        print(f"Player 2 drew: {card2.rank} of {card2.suit}")

        # Check if they match
        if card1.rank == card2.rank:
            print("SNAP! It's a match\n")
        else:
            print("No match this time...\n")


if __name__ == "__main__":
    # Create two decks of cards
    deck1 = Deck()
    deck2 = Deck()

    try:
        play_snap(deck1, deck2)
    except KeyboardInterrupt:
        print("\nGame Stopped - Thanks for playing")
