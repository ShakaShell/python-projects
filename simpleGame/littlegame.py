# Michael Roberts
# Section 11
# On my honor, I have neither received nor given any unauthorized assistance on this assignment.

import random

class Game:
    def __init__(self):
        self.player_name = ""
        self.inventory = []
        self.health = 100
        self.current_room = 'forest'
        self.rooms = {
            'forest': {
                'description': 'You are in a dark, dense forest. There are paths to the north and east.',
                'north': 'mountain',
                'east': 'cave'
            },
            'mountain': {
                'description': 'You are at the foot of a towering mountain. A path leads back south.',
                'south': 'forest'
            },
            'cave': {
                'description': 'You are in a damp cave. There is a treasure chest here!',
                'south': 'forest'
            }
        }

    def start_game(self):
        print("Welcome to the Adventure Game!")
        self.player_name = input("What is your name, adventurer? ")
        print(f"Hello, {self.player_name}! Your adventure begins now.")
        self.game_loop()

    def game_loop(self):
        while self.health > 0:
            self.show_room()
            action = input("What would you like to do? (move, check inventory, quit): ").lower()
            if action == 'move':
                self.move()
            elif action == 'check inventory':
                self.check_inventory()
            elif action == 'quit':
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Invalid action. Please try again.")
        else:
            print("You have perished in your adventure. Game over.")

    def show_room(self):
        room = self.rooms[self.current_room]
        print(room['description'])

    def move(self):
        room = self.rooms[self.current_room]
        directions = list(room.keys())
        directions.remove('description')
        print("You can move to: " + ', '.join(directions))
        direction = input("Which direction would you like to go? ").lower()
        if direction in directions:
            self.current_room = room[direction]
            self.handle_event()
        else:
            print("You can't go that way.")

    def handle_event(self):
        if self.current_room == 'cave':
            self.find_treasure()

    def find_treasure(self):
        print("You found a treasure chest!")
        choice = input("Do you want to open it? (yes/no): ").lower()
        if choice == 'yes':
            treasure = random.choice(['gold', 'silver', 'gem'])
            print(f"You found a {treasure}!")
            self.inventory.append(treasure)
        else:
            print("You decided to leave the treasure chest closed.")

    def check_inventory(self):
        if self.inventory:
            print("You have the following items in your inventory:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")

if __name__ == "__main__":
    game = Game()
    game.start_game()
