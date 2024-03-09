import pygame
import random
import sqlite3


def start():
    global fon
    pygame.init()
    pygame.display.set_caption('MD')
    pygame.display.set_icon(pygame.image.load('iconka.png'))
    fon = pygame.display.set_mode([624, 792])
    clock = pygame.time.Clock()
    image_fon = pygame.image.load("fon_start.png")
    fon.blit(image_fon, (0, 0))
    image_text1 = pygame.image.load("text.0.1.png")
    r_text1 = fon.blit(image_text1, (156, 393))

    image_text2 = pygame.image.load("text.0.2.png")
    r_text2 = fon.blit(image_text2, (156, 441))

    image_text3 = pygame.image.load("text.0.3.png")
    r_text3 = fon.blit(image_text3, (156, 489))
    return [r_text1, r_text2, r_text3, clock]


def magazin():
    global imeg_kart, random_magazin
    image_fon = pygame.image.load("fon_magazin.png")
    fon.blit(image_fon, (0, 0))
    t0, t1, t2, t3, t4 = 0, 0, 0, 0, 0
    if random_magazin[5] == 0:
        k1_1 = [2, 2, 3, 3, 3]
        k1_2 = [2, 2, 2, 3, 3]
        k2_1 = [2, 2, 2, 3, 3, 3, 4, 5]
        k3_2 = [4, 5]
        random_magazin = [random.choice(k1_1), random.choice(k1_2), random.choice(k2_1),
                          random.choice(k2_1), random.choice(k3_2), 1]
    ty = pygame.image.load("fon_kart_magazin_0.0.png")
    ty1 = pygame.image.load("fon_kart_magazin_t.0.png")
    if magazin_schot_t[5] == 0:
        image_0 = pygame.image.load("chench_hp_0.0.png")
        z1 = fon.blit(image_0, (389, 433))
    else:
        image_1 = pygame.image.load("chench_hp_1.0.png")
        z1 = fon.blit(image_1, (389, 433))
    if magazin_schot_t[0] == 0:
        fon.blit(imeg_kart[random_magazin[0]], (90, 207))
        t0 = fon.blit(ty, (87, 204))
    if magazin_schot_t[1] == 0:
        fon.blit(imeg_kart[random_magazin[1]], (243, 207))
        t1 = fon.blit(ty, (240, 204))
    if magazin_schot_t[2] == 0:
        fon.blit(imeg_kart[random_magazin[2]], (396, 207))
        t2 = fon.blit(ty, (393, 204))
    if magazin_schot_t[3] == 0:
        fon.blit(imeg_kart[random_magazin[3]], (90, 417))
        t3 = fon.blit(ty, (87, 414))
    if magazin_schot_t[4] == 0:
        fon.blit(imeg_kart[random_magazin[4]], (243, 417))
        t4 = fon.blit(ty, (240, 414))
    return z1, t0, t1, t2, t3, t4, ty, ty1


def HP():
    image_text0 = pygame.image.load("hp_fon.png")
    fon.blit(image_text0, (6, 6))
    if hp_schot == 8:
        image_text = pygame.image.load("hp_100%.png")
        fon.blit(image_text, (6, 6))
    elif hp_schot == 7:
        image_text = pygame.image.load("hp_85%.png")
        fon.blit(image_text, (6, 6))
    elif hp_schot == 6:
        image_text = pygame.image.load("hp_70%.png")
        fon.blit(image_text, (6, 6))
    elif hp_schot == 5:
        image_text = pygame.image.load("hp_55%.png")
        fon.blit(image_text, (6, 6))
    elif hp_schot == 4:
        image_text = pygame.image.load("hp_40%.png")
        fon.blit(image_text, (6, 6))
    elif hp_schot == 3:
        image_text = pygame.image.load("hp_30%.png")
        fon.blit(image_text, (6, 6))
    elif hp_schot == 2:
        image_text = pygame.image.load("hp_20%.png")
        fon.blit(image_text, (6, 6))
    elif hp_schot == 1:
        image_text = pygame.image.load("hp_10%.png")
        fon.blit(image_text, (6, 6))


def kaster():  # imeg_kaster
    global namber_kaster
    kq = namber_kaster % 24
    if 0 <= kq <= 4:
        fon.blit(imeg_kaster[0], (380, 242))
    elif 5 <= kq <= 9:
        fon.blit(imeg_kaster[1], (380, 242))
    elif 10 <= kq <= 14:
        fon.blit(imeg_kaster[2], (380, 242))
    elif 15 <= kq <= 19:
        fon.blit(imeg_kaster[3], (380, 242))
    else:
        fon.blit(imeg_kaster[4], (380, 242))
    namber_kaster += 1


def kaloda():
    fon_1 = pygame.image.load("fon_kaloda.png")
    fon.blit(fon_1, (6, 6))
    fon_1 = pygame.image.load("fon_kaloda_exit_0.1.png")
    r = fon.blit(fon_1, (576, 9))
    p = 0
    j = 0
    qo = [(36, 121), (36, 306), (36, 492), (309, 121), (309, 306), (309, 492)]
    for i in kaloda_kart:
        if i > 0:
            fon.blit(imeg_kart[j], qo[p])
            fon.blit(imeg_kart_t[i - 1], (qo[p][0] + 158, qo[p][1] + 50))
            p += 1
        j += 1
    return r


def check_click(text, b, st, kn):
    global preset
    mouses_pos = pygame.mouse.get_pos()
    if text.collidepoint(mouses_pos):
        fon.blit(kn, b)
        if pygame.mouse.get_pressed()[0]:
            preset = True
        elif preset:
            preset = False
            return True
    else:
        fon.blit(st, b)


def game_start(st):
    image_fon = pygame.image.load("fon_karta.png")
    if st == 0:
        fon.blit(image_fon, (0, -792))
    else:
        fon.blit(image_fon, (0, 0))


def sistem_text():
    image_text = pygame.image.load("option_0.1.png")
    text_option = fon.blit(image_text, (546, 714))

    image_text = pygame.image.load("karti_0.1.png")
    text_karti = fon.blit(image_text, (486, 714))

    return [text_option, text_karti]


def schot_r():
    image_fon = pygame.image.load("schot_fon.png")
    fon.blit(image_fon, (0, 0))

    image_text = pygame.image.load("nazad_sl_schot_0.1.png")
    r_text_schot = fon.blit(image_text, (450, 549))
    return r_text_schot


def teknologi_r():
    image_fon = pygame.image.load("fon_texnologi.png")
    fon.blit(image_fon, (72, 297))

    image_text = pygame.image.load("otmena_0.1.png")
    otmena = fon.blit(image_text, (507, 300))

    image_text0 = pygame.image.load("text_exit_sl1_0.1.png")
    exit_sl1 = fon.blit(image_text0, (138, 351))

    image_text1 = pygame.image.load("text_exit_0.1.png")
    exit_w = fon.blit(image_text1, (138, 399))

    return [otmena, exit_sl1, exit_w]


def mob(n0):
    if n0 == 1:
        image_game = pygame.image.load("slizen_0.1.png")
        fon.blit(image_game, (98, 201))
        return 1
    elif n0 == 2:
        image_game = pygame.image.load("slizen_0.0.png")
        fon.blit(image_game, (98, 201))
        return 1
    elif n0 == 3:
        image_game = pygame.image.load("kamen_t.0.png")
        fon.blit(image_game, (98, 201))
        return 1
    elif n0 == 4:
        image_game = pygame.image.load("kamen_0.0.png")
        fon.blit(image_game, (98, 201))
        return 2


def mob_hp(hp_schot_mob):
    if hp_schot_mob == 8:
        image_text = pygame.image.load("hp_100%.png")
        fon.blit(image_text, (99, 174))
    elif hp_schot_mob == 7:
        image_text = pygame.image.load("hp_85%.png")
        fon.blit(image_text, (99, 174))
    elif hp_schot_mob == 6:
        image_text = pygame.image.load("hp_70%.png")
        fon.blit(image_text, (99, 174))
    elif hp_schot_mob == 5:
        image_text = pygame.image.load("hp_55%.png")
        fon.blit(image_text, (99, 174))
    elif hp_schot_mob == 4:
        image_text = pygame.image.load("hp_40%.png")
        fon.blit(image_text, (99, 174))
    elif hp_schot_mob == 3:
        image_text = pygame.image.load("hp_30%.png")
        fon.blit(image_text, (99, 174))
    elif hp_schot_mob == 2:
        image_text = pygame.image.load("hp_20%.png")
        fon.blit(image_text, (99, 174))
    elif hp_schot_mob == 1:
        image_text = pygame.image.load("hp_10%.png")
        fon.blit(image_text, (99, 174))


def game(p, d, n0):
    global hp_schot_mob, kaloda_d, kaloda_s, imeg_kart, y, patarn_mobs, patarn, hp_schot, schit_f, n, ur_kart, \
        anim_I, anim_MOB, schot_t, anim_I_0
    ty = pygame.image.load("fon_kart_magazin_0.0.png")
    ty1 = pygame.image.load("fon_kart_magazin_t.0.png")
    if hp_schot_mob > 0:
        image_fon = pygame.image.load("fon_game.png")
        fon.blit(image_fon, (0, 0))
        fon.blit(patarn_mobs[patarn], (438, 162))
        fr = mob(n0)
        if anim_I > 0:
            schot_t += 1
            fon.blit(anim_I_0[7 - anim_I], (200, 250))
            if schot_t == 7:
                schot_t = 0
                anim_I -= 1
            if anim_I == 0:
                if hp_schot_mob > 0:
                    image_fon = pygame.image.load("fon_game.png")
                    fon.blit(image_fon, (0, 0))
                    fon.blit(patarn_mobs[patarn], (438, 162))
                    mob(n0)
        if kaloda_d:
            image_0 = pygame.image.load("sp_kart.png")
            fon.blit(image_0, (153, 504))
        if anim_I == 0 and anim_MOB == 0 and kaloda_d and check_click(p, (150, 501), ty, ty1):
            y = kaloda_d[0]
            kaloda_d = kaloda_d[1:]
            kaloda_s.append(y)
            if not kaloda_d:
                image_fon = pygame.image.load("fon_game.png")
                fon.blit(image_fon, (0, 0))
                mob(n0)
            if y in [0, 2]:
                if patarn == 1:
                    print('net')
                    anim_I = 7
                elif patarn == 2:
                    hp_schot -= fr
                    hp_schot_mob -= 1
                    anim_I = 7
                    anim_MOB = 7
                else:
                    hp_schot_mob -= 1
                    anim_I = 7
            elif y == 4:
                if patarn == 1:
                    print('net')
                    anim_I = 7
                elif patarn == 2:
                    hp_schot -= fr
                    hp_schot_mob -= 2
                    anim_I = 7
                    anim_MOB = 7
                else:
                    hp_schot_mob -= 2
                    anim_I = 7
            elif y == 5:
                if patarn == 2:
                    hp_schot_mob -= 1
                    anim_MOB = 7
            elif y in [1, 3]:
                if patarn == 2:
                    anim_MOB = 7
            if patarn == 3:
                if hp_schot_mob < 8:
                    hp_schot_mob += 1
            if ur_kart < 3:
                yu = [0, 0, 0, 1, 1, 2, 2]
                random.shuffle(yu)
                patarn = yu[0]
            else:
                yu = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3]
                random.shuffle(yu)
                patarn = yu[0]
            image_game = pygame.image.load("mod_patarn_fon.png")
            fon.blit(image_game, (438, 162))
            fon.blit(patarn_mobs[patarn], (438, 162))
            mob(n0)
            if hp_schot_mob > 0 and kaloda_d:
                image = pygame.image.load("sp_kart.png")
                fon.blit(image, (153, 504))
            mob_hp(hp_schot_mob)
        if kaloda_s:
            fon.blit(imeg_kart[y], (354, 504))
        if anim_I == 0 and anim_MOB == 0 and kaloda_s and check_click(d, (351, 501), ty, ty1):
            kaloda_d = kaloda_d + kaloda_s
            kaloda_s = []
            random.shuffle(kaloda_d)
            image_fon = pygame.image.load("fon_game.png")
            fon.blit(image_fon, (0, 0))
            image = pygame.image.load("sp_kart.png")
            fon.blit(image, (153, 504))
            image_game = pygame.image.load("mod_patarn_fon.png")
            fon.blit(image_game, (438, 162))
            fon.blit(patarn_mobs[patarn], (438, 162))
            mob(n0)
            if kaloda_d:
                image = pygame.image.load("sp_kart.png")
                fon.blit(image, (153, 504))
        mob_hp(hp_schot_mob)
    if hp_schot_mob <= 0:
        anim_I = 0
        anim_MOB = 0
        image_fon = pygame.image.load("fon_pb_boi.png")
        fon.blit(image_fon, (0, 0))
        image_r = pygame.image.load("pb_boi_t.0.png")
        image_r0 = pygame.image.load("pb_boi_0.0.png")
        r = fon.blit(image_r, (162, 459))
        if check_click(r, (162, 459), image_r, image_r0):
            schit_f = 0
            ur_kart += 1
            hp_schot_mob = 8
            game_start(n)
            ur()
    if hp_schot_mob > 0 and anim_MOB > 0 and anim_I == 0:
        schot_t += 1
        fon.blit(anim_MOB_0[7 - anim_MOB], (180, 0))
        if schot_t == 7:
            schot_t = 0
            anim_MOB -= 1
        if anim_MOB == 0:
            if hp_schot_mob > 0:
                image_fon = pygame.image.load("fon_game.png")
                fon.blit(image_fon, (0, 0))
                fon.blit(patarn_mobs[patarn], (438, 162))
                mob(n0)
                if kaloda_d:
                    image = pygame.image.load("sp_kart.png")
                    fon.blit(image, (153, 504))
                if kaloda_s:
                    fon.blit(imeg_kart[y], (354, 504))
                mob_hp(hp_schot_mob)
    if hp_schot <= 0:
        anim_I = 0
        anim_MOB = 0


def kaloda_d_patarn():
    global kaloda_kart, kaloda_d, kaloda_s
    u = -1
    kaloda_d = []
    kaloda_s = []
    for i in kaloda_kart:
        u += 1
        for j in range(i):
            kaloda_d.append(u)
    random.shuffle(kaloda_d)


def ur():
    global hp_schot, kaloda_kart, n, ur_2
    if ur_kart == 0:
        image_text = pygame.image.load("karta_ur_t.0.png")
        image_text0 = pygame.image.load("karta_ur_0.0.png")
        t = fon.blit(image_text, (216, 600))
        return [t, (216, 600), image_text, image_text0]
    elif ur_kart == 1:
        image_text_0 = pygame.image.load("kn_ur_0.1.png")
        fon.blit(image_text_0, (190, 600))
        image_text = pygame.image.load("karta_ur_t.1.png")
        image_text0 = pygame.image.load("karta_ur_0.1.png")
        t = fon.blit(image_text, (252, 408))
        hp_schot = 8
        HP()
        kaloda_kart = [2, 2, 0, 0, 0, 0]
        return [t, (252, 408), image_text, image_text0]
    elif ur_kart == 2:
        image_text_0 = pygame.image.load("kn_ur_0.1.png")
        fon.blit(image_text_0, (190, 600))
        fon.blit(image_text_0, (220, 408))
        image_text = pygame.image.load("karta_ur_t.2.png")
        image_text0 = pygame.image.load("karta_ur_0.2.png")
        t = fon.blit(image_text, (216, 216))
        return [t, (216, 216), image_text, image_text0]
    elif ur_kart == 3:
        image_text_0 = pygame.image.load("kn_ur_0.1.png")
        fon.blit(image_text_0, (190, 600))
        fon.blit(image_text_0, (220, 408))
        fon.blit(image_text_0, (180, 216))
        image_text = pygame.image.load("karta_ur_t.3.png")
        image_text0 = pygame.image.load("karta_ur_0.3.png")
        t = fon.blit(image_text, (252, 24))
        return [t, (252, 24), image_text, image_text0]
    elif ur_kart == 4:
        image_text = pygame.image.load("karta_ur_t.4.png")
        image_text0 = pygame.image.load("karta_ur_0.4.png")
        t = fon.blit(image_text, (216, 624))
        return [t, (216, 624), image_text, image_text0]
    elif ur_kart == 5:
        hp_schot = 8
        image_text_0 = pygame.image.load("kn_ur_0.1.png")
        fon.blit(image_text_0, (190, 624))
        image_text = pygame.image.load("karta_ur_t.5.png")
        image_text0 = pygame.image.load("karta_ur_0.5.png")
        t = fon.blit(image_text, (255, 432))
        return [t, (255, 432), image_text, image_text0]
    elif ur_kart == 6:
        image_text_0 = pygame.image.load("kn_ur_0.1.png")
        fon.blit(image_text_0, (190, 624))
        fon.blit(image_text_0, (220, 432))
        image_text = pygame.image.load("karta_ur_t.6.png")
        image_text0 = pygame.image.load("karta_ur_t.6.png")
        t = fon.blit(image_text, (219, 240))
        return [t, (219, 240), image_text, image_text0]
    elif ur_kart == 7:
        image_text_0 = pygame.image.load("kn_ur_0.1.png")
        fon.blit(image_text_0, (190, 624))
        fon.blit(image_text_0, (220, 432))
        fon.blit(image_text_0, (199, 240))
        image_text = pygame.image.load("karta_ur_t.7.png")
        image_text0 = pygame.image.load("karta_ur_0.7.png")
        t = fon.blit(image_text, (252, 48))
        return [t, (252, 48), image_text, image_text0]


def ur_fon():
    global hp_schot, magazin_schot, magazin_schot_t, random_magazin, hp_schot_mob, kaloda_s
    game_start(n)
    if ur_kart == 0:
        image_fon = pygame.image.load("fon_kaster_0.1.png")
        fon.blit(image_fon, (0, 0))

        image_0 = pygame.image.load("kaster_0.1.png")
        image_1 = pygame.image.load("kaster_1.1.png")
        h = fon.blit(image_0, (245, 350))
        return [[h, (245, 350), image_0, image_1], 1]
    elif ur_kart == 1:
        image_fon = pygame.image.load("fon_game.png")
        fon.blit(image_fon, (0, 0))
        image_0 = pygame.image.load("kolid_kart.png")
        er = fon.blit(image_0, (153, 504))
        er1 = fon.blit(image_0, (354, 504))
        game(er, er1, 1)
        if not kaloda_s:
            image_1 = pygame.image.load("sp_kart.png")
            fon.blit(image_1, (153, 504))
        return [er, er1, 1, 2]
    elif ur_kart == 2:
        hp_schot_mob = 8
        sr = magazin()
        image_2 = pygame.image.load("magazin_exit_t.0.png")
        image_3 = pygame.image.load("magazin_exit_0.0.png")
        z = fon.blit(image_2, (90, 614))
        image_4 = pygame.image.load("chench_hp_0.0.png")
        image_5 = pygame.image.load("chench_hp_t.0.png")
        return [[z, (90, 614), image_2, image_3],
                [sr[0], (389, 433), image_4, image_5],
                [sr[1], (87, 204), sr[6], sr[7]],
                [sr[2], (240, 204), sr[6], sr[7]],
                [sr[3], (393, 204), sr[6], sr[7]],
                [sr[4], (87, 414), sr[6], sr[7]],
                [sr[5], (240, 414), sr[6], sr[7]],
                7]
    elif ur_kart == 3:
        image_fon = pygame.image.load("fon_game.png")
        fon.blit(image_fon, (0, 0))
        image_0 = pygame.image.load("kolid_kart.png")
        er = fon.blit(image_0, (153, 504))
        er1 = fon.blit(image_0, (354, 504))
        game(er, er1, 2)
        if not kaloda_s:
            image = pygame.image.load("sp_kart.png")
            fon.blit(image, (153, 504))
        magazin_schot_t = [0, 0, 0, 0, 0, 0]
        magazin_schot = 2
        random_magazin = [0, 0, 0, 0, 0, 0]
        return [er, er1, 2, 2]
    elif ur_kart == 4:
        hp_schot_mob = 8
        image_fon = pygame.image.load("fon_kaster_0.2.png")
        fon.blit(image_fon, (0, 0))

        image_0 = pygame.image.load("kaster_0.1.png")
        image_1 = pygame.image.load("kaster_1.1.png")
        h = fon.blit(image_0, (245, 350))
        return [[h, (245, 350), image_0, image_1], 1]
    elif ur_kart == 5:
        image_fon = pygame.image.load("fon_game.png")
        fon.blit(image_fon, (0, 0))
        image_0 = pygame.image.load("kolid_kart.png")
        er = fon.blit(image_0, (153, 504))
        er1 = fon.blit(image_0, (354, 504))
        game(er, er1, 3)
        if not kaloda_s:
            image = pygame.image.load("sp_kart.png")
            fon.blit(image, (153, 504))
        return [er, er1, 3, 2]
    elif ur_kart == 6:
        hp_schot_mob = 8
        sr = magazin()
        image_2 = pygame.image.load("magazin_exit_t.0.png")
        image_3 = pygame.image.load("magazin_exit_0.0.png")
        z = fon.blit(image_2, (90, 614))
        image_4 = pygame.image.load("chench_hp_0.0.png")
        image_5 = pygame.image.load("chench_hp_t.0.png")
        return [[z, (90, 614), image_2, image_3],
                [sr[0], (389, 433), image_4, image_5],
                [sr[1], (87, 204), sr[6], sr[7]],
                [sr[2], (240, 204), sr[6], sr[7]],
                [sr[3], (393, 204), sr[6], sr[7]],
                [sr[4], (87, 414), sr[6], sr[7]],
                [sr[5], (240, 414), sr[6], sr[7]],
                7]
    elif ur_kart == 7:
        image_fon = pygame.image.load("fon_game.png")
        fon.blit(image_fon, (0, 0))
        image_0 = pygame.image.load("kolid_kart.png")
        er = fon.blit(image_0, (153, 504))
        er1 = fon.blit(image_0, (354, 504))
        game(er, er1, 4)
        if not kaloda_s:
            image = pygame.image.load("sp_kart.png")
            fon.blit(image, (153, 504))
        return [er, er1, 4, 2]


def dannie():
    global preset, sl, ur_kart, n, ur_2, hp_schot, namber_kaster, imeg_kaster, imeg_kart_t, kaloda_kart,\
        magazin_schot, magazin_schot_t, random_magazin, schit_f, imeg_kart, time_ur, hp_schot_mob, kaloda_s,\
        kaloda_d, y, patarn, patarn_mobs, anim_I, anim_MOB, schot_t, anim_I_0, anim_MOB_0, kj, me
    preset = False
    y, me, patarn = 'none', 'none', 'none'
    sl = 't'
    n, kj, anim_I, anim_MOB, ur_kart, schit_f, schot_t, ur_2, time_ur, namber_kaster = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    hp_schot, hp_schot_mob = 8, 8
    magazin_schot = 2
    kaloda_d, kaloda_s = [], []
    magazin_schot_t, kaloda_kart, random_magazin = [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]
    imeg_kart = [pygame.image.load("nach_karta_ur.png"), pygame.image.load("nach_karta_z.png"),
                 pygame.image.load("karta_tir_1_ur.png"), pygame.image.load("karta_tir_1_z.png"),
                 pygame.image.load("karta_tir_2_ur.png"), pygame.image.load("karta_tir_2_z.png")]
    imeg_kart_t = [pygame.image.load("kaloda_1.png"), pygame.image.load("kaloda_2.png"),
                   pygame.image.load("kaloda_3.png"), pygame.image.load("kaloda_4.png"),
                   pygame.image.load("kaloda_5.png"), pygame.image.load("kaloda_6.png")]
    imeg_kaster = [pygame.image.load('kaster_t.0.1.png'), pygame.image.load('kaster_t.0.2.png'),
                   pygame.image.load('kaster_t.0.3.png'), pygame.image.load('kaster_t.0.4.png'),
                   pygame.image.load('kaster_t.0.5.png')]
    patarn_mobs = [pygame.image.load("mod_patarn_fon.png"), pygame.image.load("mod_patarn_chit.png"),
                   pygame.image.load("mod_patarn_mech.png"), pygame.image.load("mod_patarn_hp.png")]
    anim_I_0 = [pygame.image.load('ur_modam_0.0.png'), pygame.image.load('ur_modam_0.1.png'),
                pygame.image.load('ur_modam_0.2.png'), pygame.image.load('ur_modam_0.3.png'),
                pygame.image.load('ur_modam_0.4.png'), pygame.image.load('ur_modam_0.5.png'),
                pygame.image.load('ur_modam_0.6.png')]
    anim_MOB_0 = [pygame.image.load('ur_modam_1.0.png'), pygame.image.load('ur_modam_1.1.png'),
                pygame.image.load('ur_modam_1.2.png'), pygame.image.load('ur_modam_1.3.png'),
                pygame.image.load('ur_modam_1.4.png'), pygame.image.load('ur_modam_1.5.png'),
                pygame.image.load('ur_modam_1.6.png')]


global preset, sl, ur_kart, n, ur_2, hp_schot, namber_kaster, imeg_kaster, imeg_kart_t, kaloda_kart, magazin_schot,\
    magazin_schot_t, random_magazin, schit_f, imeg_kart, time_ur, hp_schot_mob, kaloda_s, kaloda_d,\
    y, patarn, patarn_mobs, anim_I, anim_MOB, kj, me
a = start()
dannie()

while anim_I > 0 or anim_MOB > 0 or ur_2 == 1 or pygame.event.wait().type != pygame.QUIT:
    if sl == 'game' and schit_f == 1 and ur_2 != 1 and not hp_schot in [0, -1]:
        if f == 'none':
            schit_f = 0
            ur_kart += 1
            game_start(n)
            ur()
        elif f[-1] == 2:
            game(f[0], f[1], f[2])
        elif f[-1] == 1:
            if check_click(f[0][0], f[0][1], f[0][2], f[0][3]):
                schit_f = 0
                ur_kart += 1
                game_start(n)
                ur()
        elif f[-1] == 7:
            ur_fon()
            if magazin_schot != 0:
                if magazin_schot_t[5] != 1 and check_click(f[1][0], f[1][1], f[1][2], f[1][3]):
                    magazin_schot -= 1
                    hp_schot = 8
                    fon.blit(pygame.image.load("chench_hp_1.0.png"), (389, 433))
                    magazin_schot_t[5] = 1
                if magazin_schot_t[0] != 1 and check_click(f[2][0], f[2][1], f[2][2], f[2][3]):
                    magazin_schot_t[0] = 1
                    magazin_schot -= 1
                    fon.blit(pygame.image.load("fon_kart_magazin_1.0.png"), f[2][1])
                    kaloda_kart[random_magazin[0]] += 1
                if magazin_schot_t[1] != 1 and check_click(f[3][0], f[3][1], f[3][2], f[3][3]):
                    magazin_schot_t[1] = 1
                    magazin_schot -= 1
                    fon.blit(pygame.image.load("fon_kart_magazin_1.0.png"), f[3][1])
                    kaloda_kart[random_magazin[1]] += 1
                if magazin_schot_t[2] != 1 and check_click(f[4][0], f[4][1], f[4][2], f[4][3]):
                    magazin_schot_t[2] = 1
                    magazin_schot -= 1
                    fon.blit(pygame.image.load("fon_kart_magazin_1.0.png"), f[4][1])
                    kaloda_kart[random_magazin[2]] += 1
                if magazin_schot_t[3] != 1 and check_click(f[5][0], f[5][1], f[5][2], f[5][3]):
                    magazin_schot_t[3] = 1
                    magazin_schot -= 1
                    fon.blit(pygame.image.load("fon_kart_magazin_1.0.png"), f[5][1])
                    kaloda_kart[random_magazin[3]] += 1
                if magazin_schot_t[4] != 1 and check_click(f[6][0], f[6][1], f[6][2], f[6][3]):
                    magazin_schot_t[4] = 1
                    magazin_schot -= 1
                    fon.blit(pygame.image.load("fon_kart_magazin_1.0.png"), f[6][1])
                    kaloda_kart[random_magazin[4]] += 1
            if check_click(f[0][0], f[0][1], f[0][2], f[0][3]):
                schit_f = 0
                ur_kart += 1
                game_start(n)
                ur()

    if sl == 'game' and schit_f == 0 and ur_2 != 1 and ur_kart < 8 and not hp_schot in [0, -1]:
        s = ur()
        if ur_kart == 4 and ur_2 == 0:
            n = 1
            ur_2 = 1
        if check_click(s[0], s[1], s[2], s[3]):
            yu = [0, 0, 1, 2]
            random.shuffle(yu)
            patarn = yu[0]
            schit_f = 1
            f = ur_fon()
            image_fon = pygame.image.load("fon_sistem_blok.png")
            fon.blit(image_fon, (474, 711))
            y = 'none'
            hp_schot_mob = 8
            sistem_text()
            kaloda_d_patarn()

    if sl == 'game' and ur_2 != 1 and ur_kart < 8 and not hp_schot in [0, -1] and hp_schot_mob > 0:
        if hp_schot != 't':
            HP()
        image_fon = pygame.image.load("fon_sistem_blok.png")
        fon.blit(image_fon, (474, 711))
        kn = sistem_text()
        if check_click(kn[0], (546, 714), pygame.image.load("option_0.1.png"), pygame.image.load("option_1.1.png")):
            sl = 'teknologi'
            teknologi_r()
        elif check_click(kn[1], (486, 714), pygame.image.load("karti_0.1.png"), pygame.image.load("karti_1.1.png")):
            sl = 'kaloda'
            kaloda()

    if hp_schot in [0, -1]:
        image_fon = pygame.image.load("fon_sm.png")
        fon.blit(image_fon, (6, 6))
        w = 0
        fr = 1
        for i in kaloda_kart:
            w += i * fr
            if i % 2 == 0:
                fr += 1
        w += ur_kart
        w = str(w)
        if len(w) == 1:
            image_text = pygame.image.load(f"schot_0.{w}.png")
            fon.blit(image_text, (171, 480))
            image_text0 = pygame.image.load("schot_0.0.png")
            fon.blit(image_text0, (195, 480))
            fon.blit(image_text0, (219, 480))
        else:
            image_text = pygame.image.load(f"schot_0.{w[0]}.png")
            fon.blit(image_text, (171, 480))
            image_text = pygame.image.load(f"schot_0.{w[1]}.png")
            fon.blit(image_text, (195, 480))
            image_text0 = pygame.image.load("schot_0.0.png")
            fon.blit(image_text0, (219, 480))
            fon.blit(image_text0, (243, 480))

        image_text1 = pygame.image.load("text_exit_sl1_0.1.png")
        image_text1_0 = pygame.image.load("text_exit_sl1_1.1.png")
        exit_sl1 = fon.blit(image_text1, (138, 594))

        image_text2 = pygame.image.load("text_exit_0.1.png")
        image_text2_0 = pygame.image.load("text_exit_1.1.png")
        exit_w = fon.blit(image_text2, (138, 642))
        if check_click(exit_sl1, (138, 594), image_text1, image_text1_0):
            c = sqlite3.connect('schot.db')
            cu = c.cursor()
            cu.execute("INSERT INTO schot(name) VALUES(?)", [f'{w} {0}'])
            c.commit()
            cu.close()
            c.close()
            sl = 't'
            n = 0
            ur_kart = 0
            schit_f = 0
            hp_schot = 't'
            start()
        elif check_click(exit_w, (138, 642), image_text2, image_text2_0):
            c = sqlite3.connect('schot.db')
            cu = c.cursor()
            cu.execute("INSERT INTO schot(name) VALUES(?)", [f'{w} {0}'])
            c.commit()
            cu.close()
            c.close()
            break

    if ur_kart == 8 and not hp_schot in [0, -1]:
        image_fon = pygame.image.load("exit_fon.png")
        g = fon.blit(image_fon, (0, 0))
        if check_click(g, (0, 0), pygame.image.load("exit_fon.png"), pygame.image.load("exit_fon.png")):
            ur_kart += 1
            image_fon = pygame.image.load("fon_pb.png")
            fon.blit(image_fon, (6, 6))
            print(kaloda_kart, ur_kart)
            w = 0
            fr = 1
            for i in kaloda_kart:
                w += i * fr
                if i % 2 == 0:
                    fr += 1
            w += ur_kart
            w = str(w)
            if len(w) == 1:
                image_text = pygame.image.load(f"schot_0.{w}.png")
                fon.blit(image_text, (171, 480))
                image_text = pygame.image.load("schot_0.0.png")
                fon.blit(image_text, (195, 480))
                fon.blit(image_text, (219, 480))
            else:
                image_text = pygame.image.load(f"schot_0.{w[0]}.png")
                fon.blit(image_text, (171, 480))
                image_text = pygame.image.load(f"schot_0.{w[1]}.png")
                fon.blit(image_text, (195, 480))
                image_text = pygame.image.load("schot_0.0.png")
                fon.blit(image_text, (219, 480))
                fon.blit(image_text, (243, 480))

    elif ur_kart == 9 and not hp_schot in [0, -1]:
        image_fon = pygame.image.load("fon_pb.png")
        fon.blit(image_fon, (6, 6))
        print(kaloda_kart, ur_kart)
        w = 0
        fr = 1
        for i in kaloda_kart:
            w += i * fr
            if i % 2 == 0:
                fr += 1
        w += ur_kart
        w = str(w)
        if len(w) == 1:
            image_text = pygame.image.load(f"schot_0.{w}.png")
            fon.blit(image_text, (171, 480))
            image_text = pygame.image.load("schot_0.0.png")
            fon.blit(image_text, (195, 480))
            fon.blit(image_text, (219, 480))
        else:
            image_text = pygame.image.load(f"schot_0.{w[0]}.png")
            fon.blit(image_text, (171, 480))
            image_text = pygame.image.load(f"schot_0.{w[1]}.png")
            fon.blit(image_text, (195, 480))
            image_text = pygame.image.load("schot_0.0.png")
            fon.blit(image_text, (219, 480))
            fon.blit(image_text, (243, 480))

        image_text = pygame.image.load("text_exit_sl1_0.1.png")
        exit_sl1 = fon.blit(image_text, (138, 594))

        image_text = pygame.image.load("text_exit_0.1.png")
        exit_w = fon.blit(image_text, (138, 642))
        if check_click(exit_sl1, (138, 594), pygame.image.load("text_exit_sl1_0.1.png"),
                    pygame.image.load("text_exit_sl1_1.1.png")):
            c = sqlite3.connect('schot.db')
            cu = c.cursor()
            cu.execute("INSERT INTO schot(name) VALUES(?)", [f'{w} {1}'])
            c.commit()
            cu.close()
            c.close()
            sl = 't'
            n = 0
            ur_kart = 0
            schit_f = 0
            hp_schot = 't'
            start()
            kaster()
        elif check_click(exit_w, (138, 642), pygame.image.load("text_exit_0.1.png"),
                         pygame.image.load("text_exit_1.1.png")):
            c = sqlite3.connect('schot.db')
            cu = c.cursor()
            cu.execute("INSERT INTO schot(name) VALUES(?)", [f'{w} {1}'])
            c.commit()
            cu.close()
            c.close()
            break

    if ur_2 == 1:
        image_fon = pygame.image.load("fon_karta.png")
        fon.blit(image_fon, (0, -792 + time_ur))
        image_text = pygame.image.load("kn_ur_0.1.png")
        fon.blit(image_text, (190, 600 + time_ur))
        fon.blit(image_text, (220, 408 + time_ur))
        fon.blit(image_text, (180, 216 + time_ur))
        fon.blit(image_text, (230, 24 + time_ur))
        if time_ur == 792:
            ur_2 = 2
            time_ur = 0
            game_start(n)
            image_fon = pygame.image.load("fon_sistem_blok.png")
            fon.blit(image_fon, (474, 711))
            sistem_text()
            HP()
        time_ur += 3

    if sl == 'teknologi':
        kn = teknologi_r()
        sistem_text()
        if check_click(kn[0], (507, 300), pygame.image.load("otmena_0.1.png"), pygame.image.load("otmena_1.1.png")):
            sl = 'game'
            if schit_f == 0:
                game_start(n)
                ur()
            else:
                ur_fon()
            image_fon = pygame.image.load("fon_sistem_blok.png")
            fon.blit(image_fon, (474, 711))
            sistem_text()
            if hp_schot != 't':
                HP()
        elif check_click(kn[1], (138, 351), pygame.image.load("text_exit_sl1_0.1.png"),
                         pygame.image.load("text_exit_sl1_1.1.png")):
            sl = 't'
            n = 0
            namber_kaster = 0
            ur_kart = 0
            schit_f = 0
            hp_schot = 't'
            start()
            kaster()
        elif check_click(kn[2], (138, 399), pygame.image.load("text_exit_0.1.png"),
                         pygame.image.load("text_exit_1.1.png")):
            break

    if sl == 'kaloda':
        t = kaloda()
        if check_click(t, (576, 9), pygame.image.load("fon_kaloda_exit_0.1.png"),
                       pygame.image.load("fon_kaloda_exit_1.1.png")):
            sl = 'game'
            if schit_f == 0:
                game_start(n)
                ur()
            else:
                ur_fon()
            image_fon = pygame.image.load("fon_sistem_blok.png")
            fon.blit(image_fon, (474, 711))
            sistem_text()
            if hp_schot != 't':
                HP()

    if sl == 't':
        kaster()
        if check_click(a[0], (156, 393), pygame.image.load("text.0.1.png"), pygame.image.load("text.1.1.png")):
            sl = 'game'
            n = 0
            ur_kart = 0
            hp_schot = 't'
            game_start(n)
            kaloda_kart = [0, 0, 0, 0, 0, 0]
            image_fon = pygame.image.load("fon_sistem_blok.png")
            fon.blit(image_fon, (474, 711))
            sistem_text()
            hp_schot_mob = 8
            magazin_schot = 2
            magazin_schot_t = [0, 0, 0, 0, 0, 0]
            random_magazin = [0, 0, 0, 0, 0, 0]
            y = 'none'
            ur_2 = 0
            ur()
        elif check_click(a[1], (156, 441), pygame.image.load("text.0.2.png"), pygame.image.load("text.2.2.png")):
            sl = 'schot'
            kj = 1
            schot_r()
        elif check_click(a[2], (156, 489), pygame.image.load("text.0.3.png"), pygame.image.load("text.3.3.png")):
            break

    if sl == 'schot':
        r_text_schot = schot_r()
        if kj == 1:
            c = sqlite3.connect('schot.db')
            cu = c.cursor()
            cu.execute("SELECT * FROM schot")
            rows = cu.fetchall()
            cu.close()
            c.close()
            kj = 0
        if rows:
            me = sorted(rows)
            me = me[::-1]
            if me[0][0].split()[1] == '0':
                image_fon = pygame.image.load("death_p.png")
            else:
                image_fon = pygame.image.load("win_p.png")
            if len(me[0][0].split()[0]) == 1:
                image_text = pygame.image.load(f"schot_0.{me[0][0].split()[0]}.png")
                fon.blit(image_text, (209, 362))
                image_text0 = pygame.image.load("schot_0.0.png")
                fon.blit(image_text0, (233, 362))
                fon.blit(image_text0, (257, 362))
            else:
                image_text = pygame.image.load(f"schot_0.{me[0][0].split()[0][0]}.png")
                fon.blit(image_text, (209, 362))
                image_text_0 = pygame.image.load(f"schot_0.{me[0][0].split()[0][1]}.png")
                fon.blit(image_text_0, (233, 362))
                image_text0 = pygame.image.load("schot_0.0.png")
                fon.blit(image_text0, (257, 362))
                fon.blit(image_text0, (281, 362))
            fon.blit(image_fon, (139, 339))
            if len(me) > 1:
                if me[1][0].split()[1] == '0':
                    image_fon = pygame.image.load("death_p.png")
                else:
                    image_fon = pygame.image.load("win_p.png")
                if len(me[1][0].split()[0]) == 1:
                    image_text = pygame.image.load(f"schot_0.{me[1][0].split()[0]}.png")
                    fon.blit(image_text, (209, 434))
                    image_text0 = pygame.image.load("schot_0.0.png")
                    fon.blit(image_text0, (233, 434))
                    fon.blit(image_text0, (257, 434))
                else:
                    image_text = pygame.image.load(f"schot_0.{me[1][0].split()[0][0]}.png")
                    fon.blit(image_text, (209, 434))
                    image_text_0 = pygame.image.load(f"schot_0.{me[1][0].split()[0][1]}.png")
                    fon.blit(image_text_0, (233, 434))
                    image_text0 = pygame.image.load("schot_0.0.png")
                    fon.blit(image_text0, (257, 434))
                    fon.blit(image_text0, (281, 434))
                fon.blit(image_fon, (139, 411))
            if len(me) > 2:
                if me[2][0].split()[1] == '0':
                    image_fon = pygame.image.load("death_p.png")
                else:
                    image_fon = pygame.image.load("win_p.png")
                if len(me[2][0].split()[0]) == 1:
                    image_text = pygame.image.load(f"schot_0.{me[2][0].split()[0]}.png")
                    fon.blit(image_text, (209, 506))
                    image_text0 = pygame.image.load("schot_0.0.png")
                    fon.blit(image_text0, (233, 506))
                    fon.blit(image_text0, (257, 506))
                else:
                    image_text = pygame.image.load(f"schot_0.{me[2][0].split()[0][0]}.png")
                    fon.blit(image_text, (209, 506))
                    image_text_0 = pygame.image.load(f"schot_0.{me[2][0].split()[0][1]}.png")
                    fon.blit(image_text_0, (233, 506))
                    image_text0 = pygame.image.load("schot_0.0.png")
                    fon.blit(image_text0, (257, 506))
                    fon.blit(image_text0, (281, 506))
                fon.blit(image_fon, (139, 483))
        if check_click(r_text_schot, (450, 549), pygame.image.load("nazad_sl_schot_0.1.png"),
                       pygame.image.load("nazad_sl_schot_1.1.png")):
            sl = 't'
            start()
            kaster()
            namber_kaster = 0

    a[3].tick(60)
    pygame.display.flip()
pygame.quit()
