import pygame

from game_fail import interfeis


def smert(self):
    image_fon = pygame.image.load("iz/fon_sm.png")
    self.fon.blit(image_fon, (6, 6))
    w = 0
    fr = 1
    for i in self.kaloda_kart:
        w += i * fr
        if i % 2 == 0:
            fr += 1
    w += self.ur_kart
    w = str(w)
    if len(w) == 1:
        image_text = pygame.image.load(f"iz/schot_0.{w}.png")
        self.fon.blit(image_text, (171, 480))
        image_text0 = pygame.image.load("iz/schot_0.0.png")
        self.fon.blit(image_text0, (195, 480))
        self.fon.blit(image_text0, (219, 480))
    else:
        image_text = pygame.image.load(f"iz/schot_0.{w[0]}.png")
        self.fon.blit(image_text, (171, 480))
        image_text = pygame.image.load(f"iz/schot_0.{w[1]}.png")
        self.fon.blit(image_text, (195, 480))
        image_text0 = pygame.image.load("iz/schot_0.0.png")
        self.fon.blit(image_text0, (219, 480))
        self.fon.blit(image_text0, (243, 480))

    image_text1 = pygame.image.load("iz/text_exit_sl1_0.1.png")
    image_text1_0 = pygame.image.load("iz/text_exit_sl1_1.1.png")
    exit_sl1 = self.fon.blit(image_text1, (138, 594))

    image_text2 = pygame.image.load("iz/text_exit_0.1.png")
    image_text2_0 = pygame.image.load("iz/text_exit_1.1.png")
    exit_w = self.fon.blit(image_text2, (138, 642))
    if self.check_click(exit_sl1, (138, 594), image_text1, image_text1_0):
        interfeis.seve_shot_sm(w)
        self.sl = 't'
        self.n = 0
        self.ur_kart = 0
        self.schit_f = 0
        self.hp_schot = 't'
        interfeis.t_start(self)
        interfeis.kaster(self)
    elif self.check_click(exit_w, (138, 642), image_text2, image_text2_0):
        interfeis.seve_shot_sm(w)
        return False
    return True
