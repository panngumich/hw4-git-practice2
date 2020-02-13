
#########################################
##### Name: Neng Pan  ###################
##### Uniqname: panng ###################
#########################################

import unittest
import hw4_cards as cards
import random

# SI 507 Winter 2020
# Homework 4 - Code

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        """
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        """
        card = cards.Card(0, 12)
        self.assertEqual(card.rank_name, "Queen")

    def test_2_club(self):
        """
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        """
        card = cards.Card(1, 2)
        self.assertEqual(card.suit_name, "Clubs")

    def test_3_king_of_spades(self):
        """
        Test that if you invoke the __str__ method of a card instance that is created with: 
        suit=3, rank=13, it returns the string "King of Spades"
        """
        card = cards.Card(3, 13)
        self.assertEqual(card.__str__(), "King of Spades")
    
    def test_4_deck_card_number(self):
        """
        Test that if you create a deck instance, it will have 52 cards in its cards instance variable
        """
        deck = cards.Deck()
        self.assertLessEqual(len(deck.cards), 52)
    
    def test_5_deal_card_return(self):
        """
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        """
        deck = cards.Deck()
        card = cards.Card(3, 13).__str__()
        dealt = deck.deal_card(i=-1).__str__()
        self.assertEqual(dealt, card)

    def test_6_deal_card_fewer(self):
        """
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        """
        deck = cards.Deck()
        original_card = len(deck.cards)
        deck.deal_card()
        dealt_card = len(deck.cards)
        self.assertGreater(original_card, dealt_card)
    
    def test_7_replace_card_more(self):
        """
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. 
        (Use deal_card function first to remove a card from the deck and then add the same card back in)
        """
        deck = cards.Deck()
        removed = deck.deal_card()
        removed_list = len(deck.cards)
        deck.replace_card(removed)
        replaced_list = len(deck.cards)
        self.assertGreater(replaced_list, removed_list)
    
    def test_8_replace_card_size_not_affected(self):
        """
        Test that if you invoke the replace_card method with a card that is already in the deck, 
        the deck size is not affected.
        (The function must silently ignore it if you try to add a card that’s already in the deck)
        """
        deck = cards.Deck()
        current_number = len(deck.cards)
        exist_card = random.choice(deck.cards)
        deck.replace_card(exist_card)
        replaced_number = len(deck.cards)
        self.assertEqual(current_number, replaced_number)





############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
