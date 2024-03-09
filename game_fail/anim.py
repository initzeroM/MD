import pygame

from game_fail import mob, ur, interfeis


def anim_I_y(self):
    self.schot_t += 1
    self.fon.blit(self.anim_I_0[7 - self.anim_I], (200, 250))
    if self.schot_t == 4:
        self.schot_t = 0
        self.anim_I -= 1
    if self.anim_I == 0:
        if self.hp_schot_mob > 0:
            image_fon = pygame.image.load("iz/fon_game.png")
            self.fon.blit(image_fon, (0, 0))
            self.fon.blit(self.patarn_mobs[int(self.patarn)], (438, 162))
            mob.mob(self)
    ur.ur_fon(self)
    if self.hp_schot != 't':
        interfeis.HP(self)
    self.teknologi()


def anim_MOB_y(self):
    self.schot_t += 1
    self.fon.blit(self.anim_MOB_0[7 - self.anim_MOB], (180, 0))
    if self.schot_t == 4:
        self.schot_t = 0
        self.anim_MOB -= 1
    if self.anim_MOB == 0:
        if self.hp_schot_mob > 0:
            image_fon = pygame.image.load("iz/fon_game.png")
            self.fon.blit(image_fon, (0, 0))
            self.fon.blit(self.patarn_mobs[int(self.patarn)], (438, 162))
            mob.mob(self)
            if self.kaloda_d:
                image = pygame.image.load("iz/sp_kart.png")
                self.fon.blit(image, (153, 504))
            if self.kaloda_s:
                self.fon.blit(self.imeg_kart[int(self.y)], (354, 504))
            mob.mob_hp(self)
    ur.ur_fon(self)
    if self.hp_schot != 't':
        interfeis.HP(self)
    self.teknologi()