import pygame
import random

from game_fail import game, interfeis, ur


def sl_game_0(self):
    if self.f == 'none':
        self.schit_f = 0
        self.ur_kart += 1
        self.game_start()
        self.ur()
    elif self.f[-1] == 2:
        game.game(self, self.f[0], self.f[1])
    elif self.f[-1] == 1:
        if self.check_click(self.f[0][0], self.f[0][1], self.f[0][2], self.f[0][3]):
            self.schit_f = 0
            self.ur_kart += 1
            self.game_start()
            ur.ur(self)
    elif self.f[-1] == 7:
        ur.ur_fon(self)
        if self.magazin_schot != 0:
            if self.magazin_schot_t[5] != 1 and self.check_click(self.f[1][0], self.f[1][1],
                                                                 self.f[1][2], self.f[1][3]):
                self.magazin_schot -= 1
                self.hp_schot = 8
                self.fon.blit(pygame.image.load("iz/chench_hp_1.0.png"), (389, 433))
                self.magazin_schot_t[5] = 1
            if self.magazin_schot_t[0] != 1 and self.check_click(self.f[2][0], self.f[2][1],
                                                                 self.f[2][2], self.f[2][3]):
                self.magazin_schot_t[0] = 1
                self.magazin_schot -= 1
                self.fon.blit(pygame.image.load("iz/fon_kart_magazin_1.0.png"), self.f[2][1])
                self.kaloda_kart[self.random_magazin[0]] += 1
            if self.magazin_schot_t[1] != 1 and self.check_click(self.f[3][0], self.f[3][1],
                                                                 self.f[3][2], self.f[3][3]):
                self.magazin_schot_t[1] = 1
                self.magazin_schot -= 1
                self.fon.blit(pygame.image.load("iz/fon_kart_magazin_1.0.png"), self.f[3][1])
                self.kaloda_kart[self.random_magazin[1]] += 1
            if self.magazin_schot_t[2] != 1 and self.check_click(self.f[4][0], self.f[4][1],
                                                                 self.f[4][2], self.f[4][3]):
                self.magazin_schot_t[2] = 1
                self.magazin_schot -= 1
                self.fon.blit(pygame.image.load("iz/fon_kart_magazin_1.0.png"), self.f[4][1])
                self.kaloda_kart[self.random_magazin[2]] += 1
            if self.magazin_schot_t[3] != 1 and self.check_click(self.f[5][0], self.f[5][1],
                                                                 self.f[5][2], self.f[5][3]):
                self.magazin_schot_t[3] = 1
                self.magazin_schot -= 1
                self.fon.blit(pygame.image.load("iz/fon_kart_magazin_1.0.png"), self.f[5][1])
                self.kaloda_kart[self.random_magazin[3]] += 1
            if self.magazin_schot_t[4] != 1 and self.check_click(self.f[6][0], self.f[6][1],
                                                                 self.f[6][2], self.f[6][3]):
                self.magazin_schot_t[4] = 1
                self.magazin_schot -= 1
                self.fon.blit(pygame.image.load("iz/fon_kart_magazin_1.0.png"), self.f[6][1])
                self.kaloda_kart[self.random_magazin[4]] += 1
        if self.check_click(self.f[0][0], self.f[0][1], self.f[0][2], self.f[0][3]):
            self.schit_f = 0
            self.ur_kart += 1
            self.game_start()
            ur.ur(self)


def sl_game_1(self):
    self.game_start()
    s = ur.ur(self)
    if self.ur_kart == 4 and self.ur_2 == 0:
        self.n = 1
        self.ur_2 = 1
    if self.check_click(s[0], s[1], s[2], s[3]):
        yu = [0, 0, 1, 2]
        random.shuffle(yu)
        self.patarn = yu[0]
        self.schit_f = 1
        self.f = ur.ur_fon(self)
        image_fon = pygame.image.load("iz/fon_sistem_blok.png")
        self.fon.blit(image_fon, (474, 711))
        self.y = 'none'
        self.hp_schot_mob = 8
        self.sistem_text()
        interfeis.kaloda_d_patarn(self)


def sl_game_sistem(self):
    if self.hp_schot != 't':
        interfeis.HP(self)
    self.teknologi()
