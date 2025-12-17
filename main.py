"""
Entry point for the platform fighter game.
Creates a Game object and starts the game loop.
"""
import pygame

from game import Game

if __name__ == "__main__":
    game = Game()
    game.run()

