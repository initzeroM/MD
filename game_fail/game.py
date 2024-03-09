from game_fail import interfeis, mob
import pygame
import random


def game(self, p, d):
    ty = pygame.image.load("iz/fon_kart_magazin_0.0.png")
    ty1 = pygame.image.load("iz/fon_kart_magazin_t.0.png")
    self.pob_m = 0
    mob.sm_pr(self)
    if self.hp_schot_mob > 0 or self.anim_I != 0 or self.anim_MOB != 0 and self.pob_m == 0:
        image_fon = pygame.image.load("iz/fon_game.png")
        self.fon.blit(image_fon, (0, 0))
        self.fon.blit(self.patarn_mobs[self.patarn], (438, 162))
        fr = mob.mob(self)
        if self.anim_I > 0:
            self.schot_t += 1
            self.fon.blit(self.anim_I_0[7 - self.anim_I], (200, 250))
            if self.schot_t == 4:
                self.schot_t = 0
                self.anim_I -= 1
            if self.anim_I == 0:
                if self.hp_schot_mob > 0:
                    image_fon = pygame.image.load("iz/fon_game.png")
                    self.fon.blit(image_fon, (0, 0))
                    self.fon.blit(self.patarn_mobs[self.patarn], (438, 162))
                    mob.mob(self)
        if self.kaloda_d:
            image_0 = pygame.image.load("iz/sp_kart.png")
            self.fon.blit(image_0, (153, 504))
        if self.anim_I == 0 and self.anim_MOB == 0 and self.kaloda_d and self.check_click(p, (150, 501), ty,
                                                                                          ty1):
            self.y = self.kaloda_d[0]
            self.kaloda_d = self.kaloda_d[1:]
            self.kaloda_s.append(self.y)
            if not self.kaloda_d:
                image_fon = pygame.image.load("iz/fon_game.png")
                self.fon.blit(image_fon, (0, 0))
                mob.mob(self)
            interfeis.patrn_proverka(self, fr)
            if self.ur_kart < 3:
                yu = [0, 0, 0, 1, 1, 2, 2]
                random.shuffle(yu)
                self.patarn = yu[0]
            else:
                yu = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3]
                random.shuffle(yu)
                self.patarn = yu[0]
            image_game = pygame.image.load("iz/mod_patarn_fon.png")
            self.fon.blit(image_game, (438, 162))
            self.fon.blit(self.patarn_mobs[self.patarn], (438, 162))
            mob.mob(self)
            if self.kaloda_d:
                image = pygame.image.load("iz/sp_kart.png")
                self.fon.blit(image, (153, 504))
            mob.mob_hp(self)
        if self.kaloda_s:
            self.fon.blit(self.imeg_kart[self.y], (354, 504))
        if self.anim_I == 0 and self.anim_MOB == 0 and self.kaloda_s and self.check_click(d, (351, 501), ty,
                                                                                          ty1):
            self.kaloda_d = self.kaloda_d + self.kaloda_s
            self.kaloda_s = []
            random.shuffle(self.kaloda_d)
            image_fon = pygame.image.load("iz/fon_game.png")
            self.fon.blit(image_fon, (0, 0))
            image = pygame.image.load("iz/sp_kart.png")
            self.fon.blit(image, (153, 504))
            image_game = pygame.image.load("iz/mod_patarn_fon.png")
            self.fon.blit(image_game, (438, 162))
            self.fon.blit(self.patarn_mobs[self.patarn], (438, 162))
            mob.mob(self)
            if self.kaloda_d:
                image = pygame.image.load("iz/sp_kart.png")
                self.fon.blit(image, (153, 504))
        mob.mob_hp(self)
        mob.sm_pr(self)
    if self.anim_MOB > 0 and self.anim_I == 0 and self.pob_m == 0:
        self.schot_t += 1
        self.fon.blit(self.anim_MOB_0[7 - self.anim_MOB], (180, 0))
        if self.schot_t == 4:
            self.schot_t = 0
            self.anim_MOB -= 1
        if self.anim_MOB == 0:
            if self.hp_schot_mob > 0:
                image_fon = pygame.image.load("iz/fon_game.png")
                self.fon.blit(image_fon, (0, 0))
                self.fon.blit(self.patarn_mobs[self.patarn], (438, 162))
                mob.mob(self)
                if self.kaloda_d:
                    image = pygame.image.load("iz/sp_kart.png")
                    self.fon.blit(image, (153, 504))
                if self.kaloda_s:
                    self.fon.blit(self.imeg_kart[self.y], (354, 504))
                mob.mob_hp(self)
            mob.sm_pr(self)
