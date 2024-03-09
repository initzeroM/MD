import pygame
from game_fail import interfeis


def schot_0(self, rows):
    r_text_schot = self.schot_r()
    if self.kj == 1:
        rows, self.me, self.kj = interfeis.shot_al_sm()
    if rows:
        if self.me[0][0].split()[1] == '0':
            image_fon = pygame.image.load("iz/death_p.png")
        else:
            image_fon = pygame.image.load("iz/win_p.png")
        if len(self.me[0][0].split()[0]) == 1:
            image_text = pygame.image.load(f"iz/schot_0.{self.me[0][0].split()[0]}.png")
            self.fon.blit(image_text, (209, 362))
            image_text0 = pygame.image.load("iz/schot_0.0.png")
            self.fon.blit(image_text0, (233, 362))
            self.fon.blit(image_text0, (257, 362))
        else:
            image_text = pygame.image.load(f"iz/schot_0.{self.me[0][0].split()[0][0]}.png")
            self.fon.blit(image_text, (209, 362))
            image_text_0 = pygame.image.load(f"iz/schot_0.{self.me[0][0].split()[0][1]}.png")
            self.fon.blit(image_text_0, (233, 362))
            image_text0 = pygame.image.load("iz/schot_0.0.png")
            self.fon.blit(image_text0, (257, 362))
            self.fon.blit(image_text0, (281, 362))
        self.fon.blit(image_fon, (139, 339))
        if len(self.me) > 1:
            if self.me[1][0].split()[1] == '0':
                image_fon = pygame.image.load("iz/death_p.png")
            else:
                image_fon = pygame.image.load("iz/win_p.png")
            if len(self.me[1][0].split()[0]) == 1:
                image_text = pygame.image.load(f"iz/schot_0.{self.me[1][0].split()[0]}.png")
                self.fon.blit(image_text, (209, 434))
                image_text0 = pygame.image.load("iz/schot_0.0.png")
                self.fon.blit(image_text0, (233, 434))
                self.fon.blit(image_text0, (257, 434))
            else:
                image_text = pygame.image.load(f"iz/schot_0.{self.me[1][0].split()[0][0]}.png")
                self.fon.blit(image_text, (209, 434))
                image_text_0 = pygame.image.load(f"iz/schot_0.{self.me[1][0].split()[0][1]}.png")
                self.fon.blit(image_text_0, (233, 434))
                image_text0 = pygame.image.load("iz/schot_0.0.png")
                self.fon.blit(image_text0, (257, 434))
                self.fon.blit(image_text0, (281, 434))
            self.fon.blit(image_fon, (139, 411))
        if len(self.me) > 2:
            if self.me[2][0].split()[1] == '0':
                image_fon = pygame.image.load("iz/death_p.png")
            else:
                image_fon = pygame.image.load("iz/win_p.png")
            if len(self.me[2][0].split()[0]) == 1:
                image_text = pygame.image.load(f"iz/schot_0.{self.me[2][0].split()[0]}.png")
                self.fon.blit(image_text, (209, 506))
                image_text0 = pygame.image.load("iz/schot_0.0.png")
                self.fon.blit(image_text0, (233, 506))
                self.fon.blit(image_text0, (257, 506))
            else:
                image_text = pygame.image.load(f"iz/schot_0.{self.me[2][0].split()[0][0]}.png")
                self.fon.blit(image_text, (209, 506))
                image_text_0 = pygame.image.load(f"iz/schot_0.{self.me[2][0].split()[0][1]}.png")
                self.fon.blit(image_text_0, (233, 506))
                image_text0 = pygame.image.load("iz/schot_0.0.png")
                self.fon.blit(image_text0, (257, 506))
                self.fon.blit(image_text0, (281, 506))
            self.fon.blit(image_fon, (139, 483))
    if self.check_click(r_text_schot, (450, 549), pygame.image.load("iz/nazad_sl_schot_0.1.png"),
                        pygame.image.load("iz/nazad_sl_schot_1.1.png")):
        self.sl = 't'
        interfeis.t_start(self)
        interfeis.kaster(self)
        self.namber_kaster = 0
    return rows
