from game_fail import interfeis, start_0, pr, shot_pr, ur, anim, ur_pb, smert
import pygame


class MD:
    def __init__(self):
        self.f = self.random_magazin = None
        self.fon = self.preset = self.imeg_kart = self.imeg_kart_t =\
            self.imeg_kaster = self.patarn_mobs = self.anim_I_0\
            = self.anim_MOB_0 = False
        self.event = self.y = self.me = self.patarn = 'none'
        self.sl = 'start'
        self.pob_m = self.start_0 = self.start_1 = self.n0 = \
            self.n = self.kj = self.anim_I = self.anim_MOB = self.ur_kart = \
            self.schit_f = self.schot_t = self.ur_2 = self.time_ur = self.namber_kaster = 0
        self.hp_schot, self.hp_schot_mob = 8, 8
        self.magazin_schot = 2
        self.kaloda_d, self.kaloda_s = [], []
        self.magazin_schot_t = self.kaloda_kart = self.andom_magazin = [0, 0, 0, 0, 0, 0]

    def check_click(self, text, b, st, kn):
        mouses_pos = pygame.mouse.get_pos()
        if text.collidepoint(mouses_pos):
            self.fon.blit(kn, b)
            if pygame.mouse.get_pressed()[0]:
                self.preset = True
            elif self.preset:
                self.preset = False
                return True
        else:
            self.fon.blit(st, b)

    def game_start(self):
        image_fon = pygame.image.load("iz/fon_karta.png")
        if self.n == 0:
            self.fon.blit(image_fon, (0, -792))
        else:
            self.fon.blit(image_fon, (0, 0))

    def sistem_text(self):
        image_text = pygame.image.load("iz/option_0.1.png")
        text_option = self.fon.blit(image_text, (546, 714))

        image_text = pygame.image.load("iz/karti_0.1.png")
        text_karti = self.fon.blit(image_text, (486, 714))

        return [text_option, text_karti]

    def schot_r(self):
        image_fon = pygame.image.load("iz/schot_fon.png")
        self.fon.blit(image_fon, (0, 0))

        image_text = pygame.image.load("iz/nazad_sl_schot_0.1.png")
        r_text_schot = self.fon.blit(image_text, (450, 549))
        return r_text_schot

    def teknologi_r_2_0(self):
        image_fon = pygame.image.load("iz/fon_texnologi_2.0.png")
        self.fon.blit(image_fon, (72, 297))

        image_text = pygame.image.load("iz/otmena_0.1.png")
        otmena = self.fon.blit(image_text, (507, 300))

        image_text0 = pygame.image.load("iz/text_exit_sl1_2.1.png")
        exit_sl1 = self.fon.blit(image_text0, (138, 376))

        return [otmena, exit_sl1]

    def teknologi(self):
        image_fon = pygame.image.load("iz/fon_sistem_blok.png")
        self.fon.blit(image_fon, (474, 711))
        kn = self.sistem_text()
        if self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE\
                or self.check_click(kn[0], (546, 714),
                                    pygame.image.load("iz/option_0.1.png"), pygame.image.load("iz/option_1.1.png")):
            self.sl = 'teknologi'
            self.teknologi_r_2_0()
        elif self.check_click(kn[1], (486, 714), pygame.image.load("iz/karti_0.1.png"),
                              pygame.image.load("iz/karti_1.1.png")):
            self.sl = 'kaloda'
            interfeis.kaloda(self)

    def while_game(self):
        v, self.fon = interfeis.start()
        rows = 0
        self.sl, exit_while = start_0.start_anim(self, v)

        while exit_while:
            if self.ur_2 == 1:
                interfeis.ur_2_start(self)

            for self.event in pygame.event.get():
                if self.sl == 'game' and self.schit_f == 1 and self.ur_2 != 1 and not (self.hp_schot in [0, -1]):
                    pr.sl_game_0(self)

                if self.sl == 'game' and self.schit_f == 0 and self.ur_2 != 1 and \
                        self.ur_kart < 8 and not (self.hp_schot in [0, -1]):
                    pr.sl_game_1(self)

                if self.sl == 'game' and self.ur_2 != 1 and self.ur_kart < 8 and \
                        not (self.hp_schot in [0, -1]) and self.hp_schot_mob > 0:
                    pr.sl_game_sistem(self)

                if self.hp_schot in [0, -1]:
                    exit_while = smert.smert(self)

                if self.ur_kart == 8 and not (self.hp_schot in [0, -1]):
                    ur_pb.ur_8(self)

                elif self.ur_kart == 9 and not (self.hp_schot in [0, -1]):
                    exit_while = ur_pb.ur_9(self)

                if self.sl == 'teknologi':
                    kn = self.teknologi_r_2_0()
                    self.sistem_text()
                    if self.check_click(kn[0], (507, 300), pygame.image.load("iz/otmena_0.1.png"),
                                        pygame.image.load("iz/otmena_1.1.png")):
                        self.sl = 'game'
                        if self.schit_f == 0:
                            self.game_start()
                            ur.ur(self)
                        else:
                            ur.ur_fon(self)
                        image_fon = pygame.image.load("iz/fon_sistem_blok.png")
                        self.fon.blit(image_fon, (474, 711))
                        self.sistem_text()
                        if self.hp_schot != 't':
                            interfeis.HP(self)
                    elif self.check_click(kn[1], (138, 376), pygame.image.load("iz/text_exit_sl1_2.1.png"),
                                          pygame.image.load("iz/text_exit_sl1_2.2.png")):
                        self.hp_schot = 0
                        self.sl = 'none'
                        exit_while = smert.smert(self)

                if self.sl == 'kaloda':
                    t = interfeis.kaloda(self)
                    if self.check_click(t, (576, 9), pygame.image.load("iz/fon_kaloda_exit_0.1.png"),
                                        pygame.image.load("iz/fon_kaloda_exit_1.1.png")):
                        self.sl = 'game'
                        if self.schit_f == 0:
                            self.game_start()
                            ur.ur(self)
                        else:
                            ur.ur_fon(self)
                        image_fon = pygame.image.load("iz/fon_sistem_blok.png")
                        self.fon.blit(image_fon, (474, 711))
                        self.sistem_text()
                        if self.hp_schot != 't':
                            interfeis.HP(self)

                if self.sl == 't':
                    a = interfeis.t_start(self)
                    if self.check_click(a[0], (156, 393), pygame.image.load("iz/text.0.1.png"),
                                        pygame.image.load("iz/text.1.1.png")):
                        self.sl = 'game'
                        self.n = 0
                        self.ur_kart = 0
                        self.hp_schot = 't'
                        self.game_start()
                        self.kaloda_kart = [0, 0, 0, 0, 0, 0]
                        image_fon = pygame.image.load("iz/fon_sistem_blok.png")
                        self.fon.blit(image_fon, (474, 711))
                        self.sistem_text()
                        self.hp_schot_mob = 8
                        self.magazin_schot = 2
                        self.magazin_schot_t = [0, 0, 0, 0, 0, 0]
                        self.random_magazin = [0, 0, 0, 0, 0, 0]
                        self.y = 'none'
                        self.ur_2 = 0
                        ur.ur(self)
                    elif self.check_click(a[1], (156, 441), pygame.image.load("iz/text.0.2.png"),
                                          pygame.image.load("iz/text.2.2.png")):
                        self.sl = 'schot'
                        self.kj = 1
                        self.schot_r()
                    elif self.check_click(a[2], (156, 489), pygame.image.load("iz/text.0.3.png"),
                                          pygame.image.load("iz/text.3.3.png")):
                        exit_while = False
                        break

                if self.sl == 'schot':
                    rows = shot_pr.schot_0(self, rows)

                if self.event.type == pygame.QUIT:
                    exit_while = False
                    break

            if self.sl == 't':
                interfeis.kaster(self)
            if self.anim_I > 0 and not (self.sl in ['teknologi', 'kaloda']) and self.pob_m == 0:
                anim.anim_I_y(self)
            if self.anim_MOB > 0 and self.anim_I == 0 and self.pob_m == 0 \
                    and not (self.sl in ['teknologi', 'kaloda']):
                anim.anim_MOB_y(self)
            v.tick(60)
            pygame.display.flip()


if __name__ == '__main__':
    MD().while_game()
