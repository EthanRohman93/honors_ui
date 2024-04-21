import random


def generate_goofy_name():
    adjectives = ['Sleepy', 'Blue', 'Happy', 'Crazy', 'Silly', 'Brave', 'Calm']
    nouns = ['Starfish', 'Strawberry', 'Banana', 'Unicorn', 'Penguin', 'Rabbit', 'Dragon']
    return random.choice(adjectives) + random.choice(nouns)
