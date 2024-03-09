import pygame


def fail(self, start_1):
    if start_1 == 0:
        self.imeg_kart = [pygame.image.load("iz/nach_karta_ur.png"), pygame.image.load("iz/nach_karta_z.png"),
                          pygame.image.load("iz/karta_tir_1_ur.png"), pygame.image.load("iz/karta_tir_1_z.png"),
                          pygame.image.load("iz/karta_tir_2_ur.png"), pygame.image.load("iz/karta_tir_2_z.png")]
        self.imeg_kart_t = [pygame.image.load("iz/kaloda_1.png"), pygame.image.load("iz/kaloda_2.png"),
                            pygame.image.load("iz/kaloda_3.png"), pygame.image.load("iz/kaloda_4.png"),
                            pygame.image.load("iz/kaloda_5.png"), pygame.image.load("iz/kaloda_6.png")]
    elif start_1 == 1:
        self.imeg_kaster = [pygame.image.load('iz/kaster_t.0.1.png'), pygame.image.load('iz/kaster_t.0.2.png'),
                            pygame.image.load('iz/kaster_t.0.3.png'), pygame.image.load('iz/kaster_t.0.4.png'),
                            pygame.image.load('iz/kaster_t.0.5.png')]
        self.patarn_mobs = [pygame.image.load("iz/mod_patarn_fon.png"), pygame.image.load("iz/mod_patarn_chit.png"),
                            pygame.image.load("iz/mod_patarn_mech.png"), pygame.image.load("iz/mod_patarn_hp.png")]
        self.magazin_schot_t = self.kaloda_kart = self.andom_magazin = [0, 0, 0, 0, 0, 0]
    elif start_1 == 2:
        self.anim_I_0 = [pygame.image.load('iz/ur_modam_0.0.png'), pygame.image.load('iz/ur_modam_0.1.png'),
                         pygame.image.load('iz/ur_modam_0.2.png'), pygame.image.load('iz/ur_modam_0.3.png'),
                         pygame.image.load('iz/ur_modam_0.4.png'), pygame.image.load('iz/ur_modam_0.5.png'),
                         pygame.image.load('iz/ur_modam_0.6.png')]
        self.anim_MOB_0 = [pygame.image.load('iz/ur_modam_1.0.png'), pygame.image.load('iz/ur_modam_1.1.png'),
                           pygame.image.load('iz/ur_modam_1.2.png'), pygame.image.load('iz/ur_modam_1.3.png'),
                           pygame.image.load('iz/ur_modam_1.4.png'), pygame.image.load('iz/ur_modam_1.5.png'),
                           pygame.image.load('iz/ur_modam_1.6.png')]
