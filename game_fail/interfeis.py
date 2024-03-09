import pygame
import random
import sqlite3


def HP(self):
    image_text0 = pygame.image.load("iz/hp_fon.png")
    self.fon.blit(image_text0, (6, 6))
    if self.hp_schot >= 8:
        image_text = pygame.image.load("iz/hp_100%.png")
        self.fon.blit(image_text, (6, 6))
    elif self.hp_schot == 7:
        image_text = pygame.image.load("iz/hp_85%.png")
        self.fon.blit(image_text, (6, 6))
    elif self.hp_schot == 6:
        image_text = pygame.image.load("iz/hp_70%.png")
        self.fon.blit(image_text, (6, 6))
    elif self.hp_schot == 5:
        image_text = pygame.image.load("iz/hp_55%.png")
        self.fon.blit(image_text, (6, 6))
    elif self.hp_schot == 4:
        image_text = pygame.image.load("iz/hp_40%.png")
        self.fon.blit(image_text, (6, 6))
    elif self.hp_schot == 3:
        image_text = pygame.image.load("iz/hp_30%.png")
        self.fon.blit(image_text, (6, 6))
    elif self.hp_schot == 2:
        image_text = pygame.image.load("iz/hp_20%.png")
        self.fon.blit(image_text, (6, 6))
    elif self.hp_schot == 1:
        image_text = pygame.image.load("iz/hp_10%.png")
        self.fon.blit(image_text, (6, 6))


def seve_shot_s(w):
    c = sqlite3.connect('iz/schot.db')
    cu = c.cursor()
    cu.execute("INSERT INTO schot(name) VALUES(?)", [f'{w} {1}'])
    c.commit()
    cu.close()
    c.close()


def seve_shot_sm(w):
    if int(w) >= 7:
        c = sqlite3.connect('iz/schot.db')
        cu = c.cursor()
        cu.execute("INSERT INTO schot(name) VALUES(?)", [f'{w} {0}'])
        c.commit()
        cu.close()
        c.close()


def shot_al_sm():
    c = sqlite3.connect('iz/schot.db')
    cu = c.cursor()
    cu.execute("SELECT * FROM schot")
    rows = cu.fetchall()
    cu.close()
    c.close()
    kj = 0
    me = sorted(rows, reverse=True, key=lambda x: int(x[0].split()[0]))
    return rows, me, kj


def start():
    pygame.init()
    pygame.display.set_caption('MD')
    pygame.display.set_icon(pygame.image.load('iz/iconka.png'))
    fon = pygame.display.set_mode([624, 792])
    clock = pygame.time.Clock()
    return clock, fon


def kaster(self):
    kq = self.namber_kaster % 24
    if 0 <= kq <= 4:
        self.fon.blit(self.imeg_kaster[0], (380, 242))
    elif 5 <= kq <= 9:
        self.fon.blit(self.imeg_kaster[1], (380, 242))
    elif 10 <= kq <= 14:
        self.fon.blit(self.imeg_kaster[2], (380, 242))
    elif 15 <= kq <= 19:
        self.fon.blit(self.imeg_kaster[3], (380, 242))
    else:
        self.fon.blit(self.imeg_kaster[4], (380, 242))
    self.namber_kaster += 1


def kaloda(self):
    fon_1 = pygame.image.load("iz/fon_kaloda.png")
    self.fon.blit(fon_1, (6, 6))
    fon_1 = pygame.image.load("iz/fon_kaloda_exit_0.1.png")
    r = self.fon.blit(fon_1, (576, 9))
    p = 0
    j = 0
    qo = [(36, 121), (36, 306), (36, 492), (309, 121), (309, 306), (309, 492)]
    for i in self.kaloda_kart:
        if i > 0:
            self.fon.blit(self.imeg_kart[j], qo[p])
            self.fon.blit(self.imeg_kart_t[i - 1], (qo[p][0] + 158, qo[p][1] + 50))
            p += 1
        j += 1
    return r


def magazin(self):
    image_fon = pygame.image.load("iz/fon_magazin.png")
    self.fon.blit(image_fon, (0, 0))
    t0, t1, t2, t3, t4 = 0, 0, 0, 0, 0
    if self.random_magazin[5] == 0:
        k1_1 = [2, 2, 3, 3, 3]
        k1_2 = [2, 2, 2, 3, 3]
        k2_1 = [2, 2, 2, 3, 3, 3, 4, 5]
        k3_2 = [4, 5]
        self.random_magazin = [random.choice(k1_1), random.choice(k1_2), random.choice(k2_1),
                               random.choice(k2_1), random.choice(k3_2), 1]
    ty = pygame.image.load("iz/fon_kart_magazin_0.0.png")
    ty1 = pygame.image.load("iz/fon_kart_magazin_t.0.png")
    if self.magazin_schot_t[5] == 0:
        image_0 = pygame.image.load("iz/chench_hp_0.0.png")
        z1 = self.fon.blit(image_0, (389, 433))
    else:
        image_1 = pygame.image.load("iz/chench_hp_1.0.png")
        z1 = self.fon.blit(image_1, (389, 433))
    if self.magazin_schot_t[0] == 0:
        self.fon.blit(self.imeg_kart[self.random_magazin[0]], (90, 207))
        t0 = self.fon.blit(ty, (87, 204))
    if self.magazin_schot_t[1] == 0:
        self.fon.blit(self.imeg_kart[self.random_magazin[1]], (243, 207))
        t1 = self.fon.blit(ty, (240, 204))
    if self.magazin_schot_t[2] == 0:
        self.fon.blit(self.imeg_kart[self.random_magazin[2]], (396, 207))
        t2 = self.fon.blit(ty, (393, 204))
    if self.magazin_schot_t[3] == 0:
        self.fon.blit(self.imeg_kart[self.random_magazin[3]], (90, 417))
        t3 = self.fon.blit(ty, (87, 414))
    if self.magazin_schot_t[4] == 0:
        self.fon.blit(self.imeg_kart[self.random_magazin[4]], (243, 417))
        t4 = self.fon.blit(ty, (240, 414))
    return z1, t0, t1, t2, t3, t4, ty, ty1


def kaloda_d_patarn(self):
    u = -1
    self.kaloda_d = []
    self.kaloda_s = []
    for i in self.kaloda_kart:
        u += 1
        for j in range(i):
            self.kaloda_d.append(u)
    random.shuffle(self.kaloda_d)


def ur_2_start(self):
    image_fon = pygame.image.load("iz/fon_karta.png")
    self.fon.blit(image_fon, (0, -792 + self.time_ur))
    image_text = pygame.image.load("iz/kn_ur_0.1.png")
    self.fon.blit(image_text, (190, 600 + self.time_ur))
    self.fon.blit(image_text, (220, 408 + self.time_ur))
    self.fon.blit(image_text, (180, 216 + self.time_ur))
    self.fon.blit(image_text, (230, 24 + self.time_ur))
    if self.time_ur == 792:
        self.ur_2 = 2
        self.time_ur = 0
        self.game_start()
        image_fon = pygame.image.load("iz/fon_sistem_blok.png")
        self.fon.blit(image_fon, (474, 711))
        self.sistem_text()
        HP(self)
    self.time_ur += 4


def patrn_proverka(self, fr):
    if self.y in [0, 2]:
        if self.patarn == 1:
            print('net')
            self.anim_I = 7
        elif self.patarn == 2:
            self.hp_schot -= fr
            self.hp_schot_mob -= 1
            self.anim_I = 7
            self.anim_MOB = 7
        else:
            self.hp_schot_mob -= 1
            self.anim_I = 7
    elif self.y == 4:
        if self.patarn == 1:
            print('net')
            self.anim_I = 7
        elif self.patarn == 2:
            self.hp_schot -= fr
            self.hp_schot_mob -= 2
            self.anim_I = 7
            self.anim_MOB = 7
        else:
            self.hp_schot_mob -= 2
            self.anim_I = 7
    elif self.y == 5:
        if self.patarn == 2:
            self.hp_schot_mob -= 1
            self.anim_MOB = 7
    elif self.y in [1, 3]:
        if self.patarn == 2:
            self.anim_MOB = 7
    if self.patarn == 3:
        if self.hp_schot_mob < 8:
            self.hp_schot_mob += 1


def t_start(self):
    image_fon = pygame.image.load("iz/fon_start.png")
    self.fon.blit(image_fon, (0, 0))
    image_text1 = pygame.image.load("iz/text.0.1.png")
    r_text1 = self.fon.blit(image_text1, (156, 393))

    image_text2 = pygame.image.load("iz/text.0.2.png")
    r_text2 = self.fon.blit(image_text2, (156, 441))

    image_text3 = pygame.image.load("iz/text.0.3.png")
    r_text3 = self.fon.blit(image_text3, (156, 489))
    return [r_text1, r_text2, r_text3]