
import random

class Card( object ):
    """ Model a playing card. """

    # Rank is an integer (1-13), where aces are 1 and kings are 13.
    # Suit is an integer (1-4), where clubs are 1 and spades are 4.
    # Value is an integer (1-10), where aces are 1 and face cards are 10.

    # List to map integer rank to printable character (index 0 used for no rank)
    rank_list = ['x','A','2','3','4','5','6','7','8','9','10','J','Q','K']

    # List to map integer suit to printable character (index 0 used for no suit)
    suit_list = ['x','c','d','h','s']
    
    def __init__( self, rank=0, suit=0 ):
        """ Initialize card to specified rank (1-13) and suit (1-4). """
        self.__rank = 0
        self.__suit = 0
        # Verify that rank and suit are integers and that they are within
        # range (1-13 and 1-4), then update instance variables if valid.
        if type(rank) == int and type(suit) == int:
            if rank in range(1,14) and suit in range(1,5):
                self.__rank = rank
                self.__suit = suit
        
    def rank( self ):
        """ Return card's rank (1-13). """
        return self.__rank

    def value( self ):
        """ Return card's value (1 for aces, 2-9, 10 for face cards). """
        # Use ternary expression to determine value.
        return self.__rank if self.__rank < 10 else 10

    def suit( self ):
        """ Return card's suit (1-4). """
        return self.__suit

    def __eq__( self, other ):
        """ Return True if cards of equal ranks and suits. """
        if isinstance(other, Card):
            return self.__rank == other.__rank and self.__suit == other.__suit
        else:
            return False

    def __le__( self, other ):
        """ Return True if rank of self <= rank of other. """
        return self.rank() <= other.rank()

    def __lt__( self, other ):
        """ Return True if rank of self < rank of other. """
        return self.rank() < other.rank()

    def __ge__( self, other ):
        """ Return True if rank of self >= rank of other. """
        return self.rank() >= other.rank()

    def __gt__( self, other ):
        """ Return True if rank of self > rank of other. """
        return self.rank() > other.rank()

    def __str__( self ):
        """ Convert card into a string (usually for printing). """
        # Use rank to index into rank_list; use suit to index into suit_list.
        return "{}{}".format( (self.rank_list)[self.__rank], (self.suit_list)[self.__suit] )

    def __repr__( self ):
        """ Convert card into a string for use in the shell. """
        return self.__str__()
        
class Deck( object ):
    """ Model a deck of 52 playing cards. """

    # Implement the deck as a list of cards.  The last card in the list is
    # defined to be at the top of the deck.

    def __init__( self ):
        """ Initialize deck (Ace of clubs on bottom, King of spades on top). """
        self.__deck = [Card(r,s) for s in range(1,5) for r in range(1,14)]

    def shuffle( self ):
        """ Shuffle deck using shuffle method in random module. """
        random.shuffle(self.__deck)

    def deal( self ):
        """ Return top card from deck (return None if deck empty). """
        # Use ternary expression to guard against empty deck.
        return self.__deck.pop() if len(self.__deck) else None

    def is_empty( self ):
        """ Return true if deck is empty. """
        return len(self.__deck) == 0

    def __len__( self ):
        """ Return number of cards remaining in deck. """
        return len(self.__deck)
    
    def __str__( self ):
        """ Return string representing deck (usually for printing). """
        return ", ".join([str(card) for card in self.__deck])
            
    def __repr__( self ):
        """ Return string representing deck (for use in shell). """
        return self.__str__()

    def display( self, cols=13 ):
        """ Column-oriented display of deck. """
        for index, card in enumerate(self.__deck):
            if index%cols == 0:
                print()
            print("{:3s} ".format(str(card)), end="" )
        print()
        print()

