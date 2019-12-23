import sys
import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.config import Config
Config.set('graphics', 'fullscreen', False)
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '600')
from kivy.properties import StringProperty, ListProperty
from kivy.resources import resource_add_path
import random

import svr_lists
import klr_lists

if hasattr(sys, "_MEIPASS"):
    resource_add_path(sys._MEIPASS)

sm = ScreenManager(transition=SlideTransition())


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def DupliCheck(num, perks):
    obj = perks[num]

    for i, p in enumerate(perks):
        if i == num:
            continue
        elif p == obj:
            return False
        else:
            continue

    return True


class MainScreen(Screen):

    def to_help(self):
        sm.current = 'help_scr'

    def survivor_selected(self):
        sm.current = 'svr_scr'

    def killer_selected(self):
        sm.current = 'klr_scr'


class HelpScreen(Screen):

    help_sentence = (
        '[size=24][b]Info[/b][/size]\n'
        '    This is Random Perk App for Dead by Daylight.\n'
        '   (Unofficial)\n'
        '\n'
        '[size=24][b]Usage[/b][/size]\n'
        '   Please choose Button which role you play\n'
        '   and you can select Charactor, Perk, \n'
        '   Offering and so on at random.\n'
        '\n'
        '   [b]Label(such as "Perk")[/b]: shuffle all at once by category\n'
        '   [b]Icon(suck as Perk Icon)[/b]: shuffle one each\n'
        '   [b]"All" Button[/b]: shuffle all\n'
        '\n'
        '   You can set up detailed Settings in Config menu.\n'
        '   Please open Config menu by up-right Button.\n'
        '\n'
        '[size=24][b]Contact[/b][/size]\n'
        '   e-mail: vangarooo.yamada@gmail.com\n'
        '   I\'d like to get your feedback.\n'
        '\n'
        '\n'
        '[size=14]version: 1.0.4-beta[/size]'
    )

    def back_main(self):
        sm.current = 'main_scr'


class SvrConfigScreen(Screen):

    def back_prev(self):
        sm.current = 'svr_scr'


class KlrConfigScreen(Screen):

    def back_prev(self):
        sm.current = 'klr_scr'


class SurvivorScreen(Screen):

    perks_src = ListProperty(['Blank'] * 4)
    port_src = StringProperty('Unknown')
    item_src = StringProperty('Blank')
    addons_src = ListProperty(['Blank'] * 2)
    offering_src = StringProperty('Blank')

    tmpP = [''] * 4
    tmpA = [''] * 2

    def back_main(self):
        sm.current = 'main_scr'

    def to_config(self):
        sm.current = 'scfg_scr'

    def chara_rand(self):
        self.port_src = random.choice(svr_lists.svr_portrait)

    def all_rand(self):
        self.chara_rand()
        self.perk_allrand()
        self.item_allrand()
        self.offering_rand()

    def perk_allrand(self):
        for i in range(4):
            self.perk_rand(i)

    def perk_rand(self, num):
        blankP = 2 * (sm.get_screen('scfg_scr').ids['pb_1'].state == 'down')\
            + 4 * (sm.get_screen('scfg_scr').ids['pb_2'].state == 'down')\
            + 10 * (sm.get_screen('scfg_scr').ids['pb_3'].state == 'down')

        perk_list = svr_lists.svr_perkC + svr_lists.svr_perkU\
            + svr_lists.svr_blank * blankP

        if sm.get_screen('scfg_scr').ids['sw_1'].active:
            if sm.get_screen('scfg_scr').ids['sw_2'].active:
                perk_list = svr_lists.svr_perkU + svr_lists.svr_blank * blankP
        else:
            if sm.get_screen('scfg_scr').ids['sw_2'].active:
                perk_list = svr_lists.svr_perkU
            else:
                perk_list = svr_lists.svr_perkC + svr_lists.svr_perkU

        self.tmpP[num] = \
            random.choice(perk_list)

        if not (sm.get_screen('scfg_scr').ids['sw_6'].active):
            if self.tmpP[num] == 'SprintBurst':
                if 'DeadHard' in self.tmpP or 'Lithe' in self.tmpP:
                    self.perk_rand(num)
                    return
            elif self.tmpP[num] == 'DeadHard' or self.tmpP[num] == 'Lithe':
                if 'SprintBurst' in self.tmpP:
                    self.perk_rand(num)
                    return

        if (DupliCheck(num, self.tmpP) or self.tmpP[num] == 'Blank'):
            self.perks_src[num] = self.tmpP[num]
        else:
            self.perk_rand(num)

    def item_allrand(self):
        self.item_rand()
        self.addon_rand(0)
        self.addon_rand(1)

    def item_rand(self):
        if sm.get_screen('scfg_scr').ids['sw_3'].active:
            self.item_src = random.choice(
                svr_lists.svr_item + svr_lists.svr_blank)
        else:
            self.item_src = random.choice(svr_lists.svr_item)

        self.addons_src[0] = 'Blank'
        self.addons_src[1] = 'Blank'

    def addon_rand(self, num):
        item_num = 5

        if self.item_src.startswith('Flashlight'):
            item_num = 0
        elif self.item_src.startswith('Key'):
            item_num = 1
        elif self.item_src.startswith('Map'):
            item_num = 2
        elif self.item_src.startswith('MedKit'):
            item_num = 3
        elif self.item_src.startswith('ToolBox'):
            item_num = 4
        else:
            return

        if sm.get_screen('scfg_scr').ids['sw_4'].active:
            self.tmpA[num] = random.choice(
                svr_lists.svr_addon[item_num] + svr_lists.svr_blank)
        else:
            self.tmpA[num] = random.choice(svr_lists.svr_addon[item_num])

        if self.tmpA[0] == self.tmpA[1]:
            self.addon_rand(num)
        else:
            self.addons_src[num] = self.tmpA[num]

    def offering_rand(self):
        if sm.get_screen('scfg_scr').ids['sw_5'].active:
            self.offering_src = random.choice(
                svr_lists.svr_offering + svr_lists.svr_blank)
        else:
            self.offering_src = random.choice(svr_lists.svr_offering)


class KillerScreen(Screen):

    perks_src = ListProperty(['Blank'] * 4)
    port_src = StringProperty('Unknown')
    addons_src = ListProperty(['Blank'] * 2)
    offering_src = StringProperty('Blank')

    tmpP = [''] * 4
    tmpA = [''] * 2
    killer_num = 999

    def back_main(self):
        sm.current = 'main_scr'

    def to_config(self):
        sm.current = 'kcfg_scr'

    def chara_rand(self):
        self.killer_num = random.randint(0, len(klr_lists.klr_portrait) - 1)
        self.port_src = klr_lists.klr_portrait[self.killer_num]
        self.addons_src[0] = 'Blank'
        self.addons_src[1] = 'Blank'

    def all_rand(self):
        self.chara_rand()
        self.perk_allrand()
        self.addon_allrand()
        self.offering_rand()

    def perk_allrand(self):
        for i in range(4):
            self.perk_rand(i)

    def perk_rand(self, num):
        blankP = 2 * (sm.get_screen('kcfg_scr').ids['pb_1'].state == 'down')\
            + 4 * (sm.get_screen('kcfg_scr').ids['pb_2'].state == 'down')\
            + 10 * (sm.get_screen('kcfg_scr').ids['pb_3'].state == 'down')

        perk_list = klr_lists.klr_perkC + klr_lists.klr_perkU\
            + klr_lists.klr_blank * blankP

        if sm.get_screen('kcfg_scr').ids['sw_1'].active:
            if sm.get_screen('kcfg_scr').ids['sw_2'].active:
                perk_list = klr_lists.klr_perkU + klr_lists.klr_blank * blankP
        else:
            if sm.get_screen('kcfg_scr').ids['sw_2'].active:
                perk_list = klr_lists.klr_perkU
            else:
                perk_list = klr_lists.klr_perkC + klr_lists.klr_perkU

        self.tmpP[num] = \
            random.choice(perk_list)

        if (DupliCheck(num, self.tmpP) or self.tmpP[num] == 'Blank'):
            self.perks_src[num] = self.tmpP[num]
        else:
            self.perk_rand(num)

    def addon_allrand(self):
        self.addon_rand(0)
        self.addon_rand(1)

    def addon_rand(self, num):
        if self.killer_num == 999:
            return

        if sm.get_screen('kcfg_scr').ids['sw_3'].active:
            self.tmpA[num] = \
                random.choice(
                    klr_lists.klr_addon[self.killer_num] + klr_lists.klr_blank)
        else:
            self.tmpA[num] = \
                random.choice(klr_lists.klr_addon[self.killer_num])

        if self.tmpA[0] == self.tmpA[1] and self.tmpA[num] != 'Blank':
            self.addon_rand(num)
        else:
            self.addons_src[num] = self.tmpA[num]

    def offering_rand(self):
        if sm.get_screen('kcfg_scr').ids['sw_4'].active:
            self.offering_src = random.choice(
                klr_lists.klr_offering + klr_lists.klr_blank)
        else:
            self.offering_src = random.choice(klr_lists.klr_offering)


class RandomPerkApp(App):

    title = 'Random Perk App for DbD'

    def build(self):
        sm.add_widget(MainScreen(name='main_scr'))
        sm.add_widget(SurvivorScreen(name='svr_scr'))
        sm.add_widget(KillerScreen(name='klr_scr'))
        sm.add_widget(SvrConfigScreen(name='scfg_scr'))
        sm.add_widget(KlrConfigScreen(name='kcfg_scr'))
        sm.add_widget(HelpScreen(name='help_scr'))
        sm.current = 'main_scr'
        return sm


if __name__ == '__main__':
    RandomPerkApp().run()
