import pygame

from game_fail import interfeis, ur


def mob(self):
    if self.n0 == 1:
        image_game = pygame.image.load("iz/slizen_0.1.png")
        self.fon.blit(image_game, (98, 201))
        return 1
    elif self.n0 == 2:
        image_game = pygame.image.load("iz/slizen_0.0.png")
        self.fon.blit(image_game, (98, 201))
        return 1
    elif self.n0 == 3:
        image_game = pygame.image.load("iz/kamen_t.0.png")
        self.fon.blit(image_game, (98, 201))
        return 1
    elif self.n0 == 4:
        image_game = pygame.image.load("iz/kamen_0.0.png")
        self.fon.blit(image_game, (98, 201))
        return 2


def mob_hp(self):
    if self.hp_schot_mob == 8:
        image_text = pygame.image.load("iz/hp_100%.png")
        self.fon.blit(image_text, (99, 174))
    elif self.hp_schot_mob == 7:
        image_text = pygame.image.load("iz/hp_85%.png")
        self.fon.blit(image_text, (99, 174))
    elif self.hp_schot_mob == 6:
        image_text = pygame.image.load("iz/hp_70%.png")
        self.fon.blit(image_text, (99, 174))
    elif self.hp_schot_mob == 5:
        image_text = pygame.image.load("iz/hp_55%.png")
        self.fon.blit(image_text, (99, 174))
    elif self.hp_schot_mob == 4:
        image_text = pygame.image.load("iz/hp_40%.png")
        self.fon.blit(image_text, (99, 174))
    elif self.hp_schot_mob == 3:
        image_text = pygame.image.load("iz/hp_30%.png")
        self.fon.blit(image_text, (99, 174))
    elif self.hp_schot_mob == 2:
        image_text = pygame.image.load("iz/hp_20%.png")
        self.fon.blit(image_text, (99, 174))
    elif self.hp_schot_mob == 1:
        image_text = pygame.image.load("iz/hp_10%.png")
        self.fon.blit(image_text, (99, 174))


def sm_pr(self):
    if self.hp_schot_mob <= 0 and self.anim_I == 0 and self.anim_MOB == 0:
        self.pob_m = 1
        image_fon = pygame.image.load("iz/fon_pb_boi.png")
        self.fon.blit(image_fon, (0, 0))
        image_r = pygame.image.load("iz/pb_boi_t.0.png")
        image_r0 = pygame.image.load("iz/pb_boi_0.0.png")
        r = self.fon.blit(image_r, (162, 523))
        if self.check_click(r, (162, 523), image_r, image_r0):
            self.schit_f = 0
            self.ur_kart += 1
            self.hp_schot_mob = 8
            self.game_start()
            ur.ur(self)
        if self.hp_schot != 't':
            interfeis.HP(self)
        self.teknologi()