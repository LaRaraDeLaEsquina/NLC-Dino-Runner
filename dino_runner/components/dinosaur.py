import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, SHIELD_TYPE, RUNNING_HAMMER, JUMPING_HAMMER, DUCKING_HAMMER, HAMMER_TYPE
from pygame.sprite import Sprite

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}


class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5
    Y_POS_DUCK = Y_POS + 40

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jum = False
        self.dino_duck = False
        self.jump_vel = self.JUMP_VEL
        self.dino_ducking_pos = self.Y_POS_DUCK
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False

        self.show_text = False
        self.shield_time_up = 0


    def events(self):
        if self.dino_run:
            self.run()
        elif self.dino_jum:
            self.jump()
        elif self.dino_duck:
            self.duck()

    def update(self, user_imput):
        self.events()
        if user_imput[pygame.K_UP] and not self.dino_jum:
            self.dino_jum = True
            self.dino_run = False
            self.dino_duck = False
        elif user_imput[pygame.K_DOWN] and not self.dino_jum:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jum = False
        elif not self.dino_jum:
            self.dino_jum = False
            self.dino_run = True
            self.dino_duck = False

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1
    
    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jum:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
            

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jum = False
            self.jump_vel = self.JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.dino_ducking_pos
        self.step_index += 1


    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def check_invincibility(self):
        pass

    