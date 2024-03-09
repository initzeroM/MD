import pygame

from game_fail import interfeis, game


def ur(self):
    self.pob_m = 0
    if self.ur_kart == 0:
        image_text = pygame.image.load("iz/karta_ur_t.0.png")
        image_text0 = pygame.image.load("iz/karta_ur_0.0.png")
        t = self.fon.blit(image_text, (216, 600))
        self.teknologi()
        return [t, (216, 600), image_text, image_text0]
    elif self.ur_kart == 1:
        image_text_0 = pygame.image.load("iz/kn_ur_0.1.png")
        self.fon.blit(image_text_0, (190, 600))
        image_text = pygame.image.load("iz/karta_ur_t.1.png")
        image_text0 = pygame.image.load("iz/karta_ur_0.1.png")
        t = self.fon.blit(image_text, (252, 408))
        self.hp_schot = 8
        interfeis.HP(self)
        self.kaloda_kart = [2, 2, 0, 0, 0, 0]
        return [t, (252, 408), image_text, image_text0]
    elif self.ur_kart == 2:
        image_text_0 = pygame.image.load("iz/kn_ur_0.1.png")
        self.fon.blit(image_text_0, (190, 600))
        self.fon.blit(image_text_0, (220, 408))
        image_text = pygame.image.load("iz/karta_ur_t.2.png")
        image_text0 = pygame.image.load("iz/karta_ur_0.2.png")
        t = self.fon.blit(image_text, (216, 216))
        return [t, (216, 216), image_text, image_text0]
    elif self.ur_kart == 3:
        image_text_0 = pygame.image.load("iz/kn_ur_0.1.png")
        self.fon.blit(image_text_0, (190, 600))
        self.fon.blit(image_text_0, (220, 408))
        self.fon.blit(image_text_0, (180, 216))
        image_text = pygame.image.load("iz/karta_ur_t.3.png")
        image_text0 = pygame.image.load("iz/karta_ur_0.3.png")
        t = self.fon.blit(image_text, (252, 24))
        return [t, (252, 24), image_text, image_text0]
    elif self.ur_kart == 4:
        image_text = pygame.image.load("iz/karta_ur_t.4.png")
        image_text0 = pygame.image.load("iz/karta_ur_0.4.png")
        t = self.fon.blit(image_text, (216, 624))
        return [t, (216, 624), image_text, image_text0]
    elif self.ur_kart == 5:
        self.hp_schot = 8
        image_text_0 = pygame.image.load("iz/kn_ur_0.1.png")
        self.fon.blit(image_text_0, (190, 624))
        image_text = pygame.image.load("iz/karta_ur_t.5.png")
        image_text0 = pygame.image.load("iz/karta_ur_0.5.png")
        t = self.fon.blit(image_text, (255, 432))
        return [t, (255, 432), image_text, image_text0]
    elif self.ur_kart == 6:
        image_text_0 = pygame.image.load("iz/kn_ur_0.1.png")
        self.fon.blit(image_text_0, (190, 624))
        self.fon.blit(image_text_0, (220, 432))
        image_text = pygame.image.load("iz/karta_ur_t.6.png")
        image_text0 = pygame.image.load("iz/karta_ur_0.6.png")
        t = self.fon.blit(image_text, (219, 240))
        return [t, (219, 240), image_text, image_text0]
    elif self.ur_kart == 7:
        image_text_0 = pygame.image.load("iz/kn_ur_0.1.png")
        self.fon.blit(image_text_0, (190, 624))
        self.fon.blit(image_text_0, (220, 432))
        self.fon.blit(image_text_0, (199, 240))
        image_text = pygame.image.load("iz/karta_ur_t.7.png")
        image_text0 = pygame.image.load("iz/karta_ur_0.7.png")
        t = self.fon.blit(image_text, (252, 48))
        return [t, (252, 48), image_text, image_text0]


def ur_fon(self):
    self.game_start()
    if self.ur_kart == 0:
        image_fon = pygame.image.load("iz/fon_kaster_0.1.png")
        self.fon.blit(image_fon, (0, 0))

        image_0 = pygame.image.load("iz/kaster_0.1.png")
        image_1 = pygame.image.load("iz/kaster_1.1.png")
        h = self.fon.blit(image_0, (245, 350))
        return [[h, (245, 350), image_0, image_1], 1]
    elif self.ur_kart == 1:
        image_fon = pygame.image.load("iz/fon_game.png")
        self.fon.blit(image_fon, (0, 0))
        image_0 = pygame.image.load("iz/kolid_kart.png")
        er = self.fon.blit(image_0, (153, 504))
        er1 = self.fon.blit(image_0, (354, 504))
        self.n0 = 1
        game.game(self, er, er1)
        if not self.kaloda_s:
            image_1 = pygame.image.load("iz/sp_kart.png")
            self.fon.blit(image_1, (153, 504))
        return [er, er1, 1, 2]
    elif self.ur_kart == 2:
        self.hp_schot_mob = 8
        sr = interfeis.magazin(self)
        image_2 = pygame.image.load("iz/magazin_exit_t.0.png")
        image_3 = pygame.image.load("iz/magazin_exit_0.0.png")
        z = self.fon.blit(image_2, (90, 614))
        image_4 = pygame.image.load("iz/chench_hp_0.0.png")
        image_5 = pygame.image.load("iz/chench_hp_t.0.png")
        return [[z, (90, 614), image_2, image_3],
                [sr[0], (389, 433), image_4, image_5],
                [sr[1], (87, 204), sr[6], sr[7]],
                [sr[2], (240, 204), sr[6], sr[7]],
                [sr[3], (393, 204), sr[6], sr[7]],
                [sr[4], (87, 414), sr[6], sr[7]],
                [sr[5], (240, 414), sr[6], sr[7]],
                7]
    elif self.ur_kart == 3:
        image_fon = pygame.image.load("iz/fon_game.png")
        self.fon.blit(image_fon, (0, 0))
        image_0 = pygame.image.load("iz/kolid_kart.png")
        er = self.fon.blit(image_0, (153, 504))
        er1 = self.fon.blit(image_0, (354, 504))
        self.n0 = 2
        game.game(self, er, er1)
        if not self.kaloda_s:
            image = pygame.image.load("iz/sp_kart.png")
            self.fon.blit(image, (153, 504))
        self.magazin_schot_t = [0, 0, 0, 0, 0, 0]
        self.magazin_schot = 2
        self.random_magazin = [0, 0, 0, 0, 0, 0]
        return [er, er1, 2, 2]
    elif self.ur_kart == 4:
        self.hp_schot_mob = 8
        image_fon = pygame.image.load("iz/fon_kaster_0.2.png")
        self.fon.blit(image_fon, (0, 0))
        image_0 = pygame.image.load("iz/kaster_0.1.png")
        image_1 = pygame.image.load("iz/kaster_1.1.png")
        h = self.fon.blit(image_0, (245, 350))
        return [[h, (245, 350), image_0, image_1], 1]
    elif self.ur_kart == 5:
        image_fon = pygame.image.load("iz/fon_game.png")
        self.fon.blit(image_fon, (0, 0))
        image_0 = pygame.image.load("iz/kolid_kart.png")
        er = self.fon.blit(image_0, (153, 504))
        er1 = self.fon.blit(image_0, (354, 504))
        self.n0 = 3
        game.game(self, er, er1)
        if not self.kaloda_s:
            image = pygame.image.load("iz/sp_kart.png")
            self.fon.blit(image, (153, 504))
        return [er, er1, 3, 2]
    elif self.ur_kart == 6:
        self.hp_schot_mob = 8
        sr = interfeis.magazin(self)
        image_2 = pygame.image.load("iz/magazin_exit_t.0.png")
        image_3 = pygame.image.load("iz/magazin_exit_0.0.png")
        z = self.fon.blit(image_2, (90, 614))
        image_4 = pygame.image.load("iz/chench_hp_0.0.png")
        image_5 = pygame.image.load("iz/chench_hp_t.0.png")
        return [[z, (90, 614), image_2, image_3],
                [sr[0], (389, 433), image_4, image_5],
                [sr[1], (87, 204), sr[6], sr[7]],
                [sr[2], (240, 204), sr[6], sr[7]],
                [sr[3], (393, 204), sr[6], sr[7]],
                [sr[4], (87, 414), sr[6], sr[7]],
                [sr[5], (240, 414), sr[6], sr[7]],
                7]
    elif self.ur_kart == 7:
        image_fon = pygame.image.load("iz/fon_game.png")
        self.fon.blit(image_fon, (0, 0))
        image_0 = pygame.image.load("iz/kolid_kart.png")
        er = self.fon.blit(image_0, (153, 504))
        er1 = self.fon.blit(image_0, (354, 504))
        self.n0 = 4
        game.game(self, er, er1)
        if not self.kaloda_s:
            image = pygame.image.load("iz/sp_kart.png")
            self.fon.blit(image, (153, 504))
        return [er, er1, 4, 2]
