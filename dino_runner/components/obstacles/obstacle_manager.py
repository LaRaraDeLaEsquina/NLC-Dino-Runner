import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            small_cactus = Cactus(SMALL_CACTUS)
            large_cactus = Cactus(LARGE_CACTUS)
            cactus_avai_sizes = [small_cactus, large_cactus]
            size_cactus = random.choice(cactus_avai_sizes)
            self.obstacles.append(size_cactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                #elif game.player.shield == True:
                else:
                    self.obstacles.remove(obstacle)

            #elif game.player.hammer_rect.colliderect(obstacle.rect):
             #   if game.player.hammer:
              #      self.obstacles.remove(obstacle)

            break
            

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
