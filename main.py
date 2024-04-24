"""
Author:         Tori Slagle
Date:           4/23/24
Assignment:     Project 02
Course:         CPSC1051
Lab Section:    001

CODE DESCRIPTION:

This program simulates a text-based game of Candyland. Players will
roll dice to navigate along the candy-themed map, facing special spaces triggering
events like drawing cards and other random effects.
"""
# Candy Land Adventure

import random
import pickle

class CandyCard:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Deck of Cards that the user will draw from if prompted.
class CandyDeck:
    def __init__(self):
        self.cards = [
            CandyCard("Sweet Treat", "You found a delicious candy! Move forward 2 spaces."),
            CandyCard("Sticky Situation", "Oops! You got stuck in caramel. Skip your next turn."),
            CandyCard("Shortcut", "You found a shortcut! Move forward 3 spaces."),
            CandyCard("Licorice Trap", "Watch out for the licorice trap! Move back 1 space."),
            CandyCard("Gummy Bear Slide", "Slide down the gummy bear slide! Move forward 4 spaces."),
            CandyCard("Chocolate Fountain", "Enjoy the chocolate fountain! Move forward 2 spaces."),
            CandyCard("Sour Candy", "Ew, sour candy! Move back 2 spaces."),
            CandyCard("Rainbow Bridge", "Cross the rainbow bridge! Move forward 3 spaces."),
            CandyCard("Cotton Candy Clouds", "Bounce on the cotton candy clouds! Move forward 2 spaces."),
            CandyCard("Marshmallow Puddle", "Oops, you stepped into a marshmallow puddle! Skip your next turn.")
        ]

    def draw_card(self):
        return random.choice(self.cards)

class Player:
    def __init__(self, character):
        self.character = character
        self.position = 0

# Main
class CandyAdventure:
    def __init__(self, num_players):
        #Creates a board of all the possible spaces players could land on
        self.board = [
            ("Candy Castle", "Welcome to the magnificent Candy Castle, the sweetest place in all the land!"),
            ("Caramel Canyon", "Watch your step as you navigate the sticky Caramel Canyon. You may draw a card."),
            ("Lollipop Woods", "You enter the enchanting Lollipop Woods, where candy trees sway in the breeze. You may draw a card."),
            ("Gumdrop Mountains", "You climb the colorful Gumdrop Mountains, enjoying the vibrant scenery. You may draw a card."),
            ("Peppermint Forest", "Take a deep breath and enjoy the refreshing Peppermint Forest."),
            ("Licorice Lagoon", "Beware! You got caught in the sticky Licorice Lagoon."),
            ("Candy Cane Lane", "Stroll along the delightful Candy Cane Lane, where every step is sweet."),
            ("Chocolate Swamp", "You enjoy a boost from the delicious Chocolate Swamp."),
            ("Gingerbread Glade", "The air is filled with the warm aroma of gingerbread in Gingerbread Glade. You may draw a card."),
            ("Peanut Butter Palace", "Explore the grand Peanut Butter Palace, a haven for peanut butter lovers. You may draw a card."),
            ("Marshmallow Marsh", "Oops! You sunk into the fluffy Marshmallow Marsh."),
            ("Rocky Road", "Watch your step! The Rocky Road is treacherous."),
            ("Butterscotch Bridge", "Cross the Butterscotch Bridge and admire the caramel-colored river below. You may draw a card."),
            ("Jellybean Junction", "Welcome to Jellybean Junction, where the streets are paved with candy. You may draw a card."),
            ("Cotton Candy Clouds", "You get swept away by the magically delicious Cotton Candy Clouds! Sweet!"),
            ("Taffy Tundra", "Uh oh! You got stuck in Taffy Tundra."),
            ("Sugarplum Peak", "Ascend the sweet Sugarplum Peak and take in the breathtaking views. You may draw a card."),
            ("Frosting Falls", "Admire the shimmering Frosting Falls as they cascade into sugary pools below. You may draw a card."),
            ("Cinnamon City", "You're allergic to cinnamon! Run!"),
            ("Jujube Jungle", "Venture into the colorful Jujube Jungle, where every tree bears fruity delights. You may draw a card.")
        ]
        self.deck = CandyDeck()
        self.players = []
        # Asks each player to enter a name for their character
        for i in range(num_players):
            print(f"Player {i+1}, enter your name: ")
            character_name = input().upper()
            self.players.append(Player(character_name))
        
        # Assigns each space with 1 of 3 gameplay options: drawing a card, automatic reward, or automatic consequence.
        self.special_spaces = {
            "Caramel Canyon": "draw_card",
            "Lollipop Woods": "draw_card",
            "Gumdrop Mountains": "draw_card",
            "Peppermint Forest": "automatic_reward",
            "Licorice Lagoon": "automatic_consequence",
            "Candy Cane Lane": "automatic_reward",
            "Chocolate Swamp": "automatic_reward",
            "Gingerbread Glade": "draw_card",
            "Peanut Butter Palace": "draw_card",
            "Marshmallow Marsh": "automatic_consequence",
            "Rocky Road": "automatic_consequence",
            "Butterscotch Bridge": "draw_card",
            "Jellybean Junction": "draw_card",
            "Cotton Candy Clouds": "automatic_reward",
            "Taffy Tundra": "automatic_consequence",
            "Sugarplum Peak": "draw_card",
            "Frosting Falls": "draw_card",
            "Cinnamon City":"automatic_consequence",
            "Jujube Jungle": "draw_card"
        }
    # Rolls a random number between 1 and 6
    def roll_die(self):
        return random.randint(1, 6)
    # Moves player based on the number rolled from the dice
    def move_player(self, player, spaces):
        player.position += spaces

    # Handles each special space appropriately
    def handle_special_space(self, player, space_name):
        print(self.get_space_message(space_name))  # Display the message for the current space
        if space_name in self.special_spaces:
            special_action = self.special_spaces[space_name]
            if special_action == "draw_card":
                draw_choice = input(f"{player.character}, do you want to draw a card? (yes/no): ").lower()
                if draw_choice == "yes":
                    card = self.deck.draw_card()
                    print(f"{player.character} drew a card:")
                    print(card.name)
                    print(card.description)
                    self.resolve_card_effect(player, card)
                else:
                    print(f"{player.character} chose not to draw a card. Ending turn.")
            elif special_action == "automatic_reward":
                print(f"{player.character} gets an automatic reward for landing on {space_name}.")
                random_spaces = random.randint(1, 4)  # Choose a random number of spaces to move ahead
                print(f"{player.character} moves ahead {random_spaces} spaces.")
                self.move_player(player, random_spaces)
            elif special_action == "automatic_consequence":
                print(f"{player.character} gets an automatic consequence for landing on {space_name}.")
                random_spaces = random.randint(1, 4)  # Choose a random number of spaces to move back
                print(f"{player.character} moves back {random_spaces} spaces.")
                self.move_player(player, -random_spaces)
                   

    def play(self):
        print("Welcome to Candy Land Adventure!")
        print("Get ready to embark on a delicious journey through the enchanting world of candy! In this sweet adventure, you'll roll the dice, navigate through candy-filled landscapes, and encounter thrilling surprises along the way. Keep an eye out for special spaces that trigger exciting events, and don't forget to draw cards for extra fun. The first player to reach the Candy Castle and meet the Candy King wins! Let the sugary adventure begin!")

        while True:
            for player in self.players:
                print(f"{player.character}, press Enter to roll the die...")
                input()
                roll = self.roll_die()
                print(f"{player.character} rolled a {roll}.")
                self.move_player(player, roll)

                if player.position >= len(self.board):
                    print(f"Congratulations, {player.character}! You've reached the Candy Castle and met the Candy King!")
                    return

                current_space = self.board[player.position][0]  # Extracting the space name from the tuple
                self.handle_special_space(player, current_space)
                print()

    def get_space_message(self, space_name):
        for space in self.board:
            if space[0] == space_name:
                return space[1]
        return f"Welcome to {space_name}!"
    
    def save_game(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_game(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

if __name__ == "__main__":
    print("Enter the number of players:")
    num_players = int(input())
    candy_adventure = CandyAdventure(num_players)
    candy_adventure.play()

    save_choice = input("Do you want to save the game? (yes/no): ").lower()
    if save_choice == "yes":
        filename = input("Enter the filename to save the game: ")
        candy_adventure.save_game(filename)

    load_choice = input("Do you want to load a saved game? (yes/no): ").lower()
    if load_choice == "yes":
        filename = input("Enter the filename to load the game: ")
        loaded_game = CandyAdventure.load_game(filename)
        loaded_game.play()
   
