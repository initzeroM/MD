import pygame

from game_fail import interfeis


def ur_8(self):
    image_fon = pygame.image.load("iz/exit_fon.png")
    g = self.fon.blit(image_fon, (0, 0))
    if self.check_click(g, (0, 0), pygame.image.load("iz/exit_fon.png"),
                        pygame.image.load("iz/exit_fon.png")):
        self.ur_kart += 1
        image_fon = pygame.image.load("iz/fon_pb.png")
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
            image_text = pygame.image.load("iz/schot_0.0.png")
            self.fon.blit(image_text, (195, 480))
            self.fon.blit(image_text, (219, 480))
        else:
            image_text = pygame.image.load(f"iz/schot_0.{w[0]}.png")
            self.fon.blit(image_text, (171, 480))
            image_text = pygame.image.load(f"iz/schot_0.{w[1]}.png")
            self.fon.blit(image_text, (195, 480))
            image_text = pygame.image.load("iz/schot_0.0.png")
            self.fon.blit(image_text, (219, 480))
            self.fon.blit(image_text, (243, 480))


def ur_9(self):
    image_fon = pygame.image.load("iz/fon_pb.png")
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
        image_text = pygame.image.load("iz/schot_0.0.png")
        self.fon.blit(image_text, (195, 480))
        self.fon.blit(image_text, (219, 480))
    else:
        image_text = pygame.image.load(f"iz/schot_0.{w[0]}.png")
        self.fon.blit(image_text, (171, 480))
        image_text = pygame.image.load(f"iz/schot_0.{w[1]}.png")
        self.fon.blit(image_text, (195, 480))
        image_text = pygame.image.load("iz/schot_0.0.png")
        self.fon.blit(image_text, (219, 480))
        self.fon.blit(image_text, (243, 480))

    image_text = pygame.image.load("iz/text_exit_sl1_0.1.png")
    exit_sl1 = self.fon.blit(image_text, (138, 594))

    image_text = pygame.image.load("iz/text_exit_0.1.png")
    exit_w = self.fon.blit(image_text, (138, 642))
    if self.check_click(exit_sl1, (138, 594), pygame.image.load("iz/text_exit_sl1_0.1.png"),
                        pygame.image.load("iz/text_exit_sl1_1.1.png")):
        interfeis.seve_shot_s(w)
        self.sl = 't'
        self.n = 0
        self.ur_kart = 0
        self.schit_f = 0
        self.hp_schot = 't'
        interfeis.t_start(self)
        interfeis.kaster(self)
    elif self.check_click(exit_w, (138, 642), pygame.image.load("iz/text_exit_0.1.png"),
                          pygame.image.load("iz/text_exit_1.1.png")):
        interfeis.seve_shot_s(w)
        return False
    return True
