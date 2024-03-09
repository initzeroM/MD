import pygame
from game_fail import interfeis, fail_start

kaster_start = [pygame.image.load('iz/kaster_start_0.0.png'), pygame.image.load('iz/kaster_start_0.1.png'),
                pygame.image.load('iz/kaster_start_0.2.png'), pygame.image.load('iz/kaster_start_0.3.png'),
                pygame.image.load('iz/kaster_start_0.4.png'), pygame.image.load('iz/kaster_start_0.5.png')]
kaster_start_0 = [pygame.image.load('iz/kaster_start_1.0.png'),
                  pygame.image.load('iz/kaster_start_1.1.png'),
                  pygame.image.load('iz/kaster_start_1.2.png'),
                  pygame.image.load('iz/kaster_start_1.3.png'),
                  pygame.image.load('iz/kaster_start_1.4.png')]


def start_anim(self, v):
    start_0 = 0
    start_1 = 0
    while self.sl != 't':
        image_fon = pygame.image.load("iz/fon_start_0.0.png")
        self.fon.blit(image_fon, (0, 0))
        start_0 += 1
        if start_1 <= 5:
            self.fon.blit(kaster_start[start_1], (275, 344))
        elif start_1 <= 20:
            self.fon.blit(kaster_start_0[start_1 % 5], (275, 344))
        else:
            image_fon = pygame.image.load("iz/fon_start.png")
            self.fon.blit(image_fon, (0, 0))
            image_text1 = pygame.image.load("iz/text.0.1.png")
            a1 = self.fon.blit(image_text1, (156, 393))
            image_text2 = pygame.image.load("iz/text.0.2.png")
            a2 = self.fon.blit(image_text2, (156, 441))
            image_text3 = pygame.image.load("iz/text.0.3.png")
            a3 = self.fon.blit(image_text3, (156, 489))
            self.check_click(a1, (156, 393), pygame.image.load("iz/text.0.1.png"),
                             pygame.image.load("iz/text.1.1.png"))
            self.check_click(a2, (156, 441), pygame.image.load("iz/text.0.2.png"),
                             pygame.image.load("iz/text.2.2.png"))
            self.check_click(a3, (156, 489), pygame.image.load("iz/text.0.3.png"),
                             pygame.image.load("iz/text.3.3.png"))
            self.sl = 't'
            interfeis.kaster(self)
        if start_0 == 1:
            fail_start.fail(self, start_1)
        if start_0 == 5:
            start_0 = 0
            start_1 += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 't', False

        v.tick(60)
        pygame.display.flip()
    del start_0
    del start_1
    return 't', True
