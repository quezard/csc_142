#  Game class

import pygame
import pygwidgets
from Constants import WHITE
from Deck import Deck, BLACKJACK_DICT

def calculate_score(hand):
    total = 0
    aces = 0

    for card in hand:
        rank = card.getRank()
        value = card.getValue()

        if rank == "Ace":
            aces += 1
        else:
            total += value

    for _ in range(aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1

    return total


class Game():
    CARD_OFFSET = 90
    PLAYER_Y = 350
    DEALER_Y = 150

    def __init__(self, window):
        self.window = window
        self.oDeck = Deck(window, rankValueDict=BLACKJACK_DICT)

        self.messageText = pygwidgets.DisplayText(
            window, (50, 500), '', width=900,
            justified='center', fontSize=36, textColor=WHITE
        )

        self.hitButton = pygwidgets.TextButton(window, (50, 540), 'Hit')
        self.stayButton = pygwidgets.TextButton(window, (200, 540), 'Stay')
        self.newGameButton = pygwidgets.TextButton(window, (350, 540), 'New Game')

        self.start_new_round()

    # ⭐ NEW: Centering helper method
    def get_center_start_x(self, hand):
        total_width = len(hand) * self.CARD_OFFSET
        return (1000 - total_width) // 2   # window width = 1000

    def start_new_round(self):
        self.oDeck.shuffle()
        self.player_hand = []
        self.dealer_hand = []
        self.game_over = False
        self.messageText.setValue("")

        self.dealer_draw(conceal=True)
        self.player_draw()
        self.player_draw()

        self.layout_cards()

    # ⭐ UPDATED: Cards now centered on screen
    def layout_cards(self):
        # Center player cards
        start_x_player = self.get_center_start_x(self.player_hand)
        for i, card in enumerate(self.player_hand):
            card.setLoc((start_x_player + i * self.CARD_OFFSET, self.PLAYER_Y))

        # Center dealer cards
        start_x_dealer = self.get_center_start_x(self.dealer_hand)
        for i, card in enumerate(self.dealer_hand):
            card.setLoc((start_x_dealer + i * self.CARD_OFFSET, self.DEALER_Y))

    def player_draw(self):
        card = self.oDeck.getCard()
        card.reveal()
        self.player_hand.append(card)

    def dealer_draw(self, conceal=False):
        card = self.oDeck.getCard()
        if conceal:
            card.conceal()
        else:
            card.reveal()
        self.dealer_hand.append(card)

    def reveal_dealer_cards(self):
        for card in self.dealer_hand:
            card.reveal()

    def handle_hit(self):
        if self.game_over:
            return

        self.player_draw()
        self.layout_cards()

        if calculate_score(self.player_hand) > 21:
            self.messageText.setValue("You bust! Dealer wins.")
            self.finish_round()

    def handle_stay(self):
        if self.game_over:
            return

        self.reveal_dealer_cards()
        self.layout_cards()

        while calculate_score(self.dealer_hand) < 17:
            self.dealer_draw()
            self.layout_cards()

        self.resolve_winner()

    def resolve_winner(self):
        p = calculate_score(self.player_hand)
        d = calculate_score(self.dealer_hand)

        if d > 21:
            self.messageText.setValue("Dealer busts! You win.")
        elif p > d:
            self.messageText.setValue("You win!")
        elif d > p:
            self.messageText.setValue("Dealer wins.")
        else:
            self.messageText.setValue("It's a tie!")

        self.finish_round()

    def finish_round(self):
        self.game_over = True
        self.reveal_dealer_cards()
        self.layout_cards()

    def handle_event(self, event):
        if self.hitButton.handleEvent(event):
            self.handle_hit()

        if self.stayButton.handleEvent(event):
            self.handle_stay()

        if self.newGameButton.handleEvent(event):
            self.start_new_round()

    def draw(self):
        for card in self.player_hand:
            card.draw()
        for card in self.dealer_hand:
            card.draw()

        self.messageText.draw()
        self.hitButton.draw()
        self.stayButton.draw()
        self.newGameButton.draw()