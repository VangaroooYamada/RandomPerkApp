import sys
import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.config import Config
Config.set('graphics', 'fullscreen', False)
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '600')
from kivy.properties import StringProperty
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


def DupliCheck(num, *perks):

    for i in perks:
        if num == i:
            return False

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
        '   Config menu can open by up-right Button.\n'
        '\n'
        '[size=24][b]Contact[/b][/size]\n'
        '   e-mail: vangarooo.yamada@gmail.com\n'
        '   I\'d like to get your feedback.\n'
        '\n'
        '\n'
        '[size=14]version: 1.0.0-beta[/size]'
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

    perk1_src = StringProperty('BlankPerk')
    perk2_src = StringProperty('BlankPerk')
    perk3_src = StringProperty('BlankPerk')
    perk4_src = StringProperty('BlankPerk')
    port_src = StringProperty('Unknown')
    item_src = StringProperty('BlankItem')
    addon1_src = StringProperty('BlankAddon')
    addon2_src = StringProperty('BlankAddon')
    offering_src = StringProperty('BlankOffering')

    tmpP1 = tmpP2 = tmpP3 = tmpP4 = ''
    tmpA1 = tmpA2 = ''

    def back_main(self):
        sm.current = 'main_scr'

    def to_config(self):
        sm.current = 'scfg_scr'

    def chara_rand(self):
        self.port_src = random.choice(svr_lists.svr_portrait)

    def all_rand(self):
        self.chara_rand()
        self.perk_rand()
        self.item_allrand()
        self.offering_rand()

    def perk_rand(self):
        self.perk1_rand()
        self.perk2_rand()
        self.perk3_rand()
        self.perk4_rand()

    def perk1_rand(self):
        tmp_first, tmp_last = 0, len(svr_lists.svr_perk)
        if sm.get_screen('scfg_scr').ids['sw_1'].active:
            if sm.get_screen('scfg_scr').ids['sw_2'].active:
                tmp_first = 11
        else:
            if sm.get_screen('scfg_scr').ids['sw_2'].active:
                tmp_first, tmp_last = 11, len(svr_lists.svr_perk) - 1
            else:
                tmp_last = len(svr_lists.svr_perk) - 1

        self.tmpP1 = \
            random.choice(svr_lists.svr_perk[tmp_first:tmp_last:])

        if (DupliCheck(self.tmpP1, self.tmpP2, self.tmpP3, self.tmpP4)
                or self.tmpP1 == 'BlankPerk'):
            self.perk1_src = self.tmpP1
        else:
            self.perk1_rand()

    def perk2_rand(self):
        tmp_first, tmp_last = 0, len(svr_lists.svr_perk)
        if sm.get_screen('scfg_scr').ids['sw_1'].active:
            if sm.get_screen('scfg_scr').ids['sw_2'].active:
                tmp_first = 11
        else:
            if sm.get_screen('scfg_scr').ids['sw_2'].active:
                tmp_first, tmp_last = 11, len(svr_lists.svr_perk) - 1
            else:
                tmp_last = len(svr_lists.svr_perk) - 1

        self.tmpP2 = \
            random.choice(svr_lists.svr_perk[tmp_first:tmp_last:])

        if (DupliCheck(self.tmpP2, self.tmpP1, self.tmpP3, self.tmpP4)
                or self.tmpP2 == 'BlankPerk'):
            self.perk2_src = self.tmpP2
        else:
            self.perk2_rand()

    def perk3_rand(self):
        tmp_first, tmp_last = 0, len(svr_lists.svr_perk)
        if sm.get_screen('scfg_scr').ids['sw_1'].active:
            if sm.get_screen('scfg_scr').ids['sw_2'].active:
                tmp_first = 11
        else:
            if sm.get_screen('scfg_scr').ids['sw_2'].active:
                tmp_first, tmp_last = 11, len(svr_lists.svr_perk) - 1
            else:
                tmp_last = len(svr_lists.svr_perk) - 1

        self.tmpP3 = \
            random.choice(svr_lists.svr_perk[tmp_first:tmp_last:])

        if (DupliCheck(self.tmpP3, self.tmpP1, self.tmpP2, self.tmpP4)
                or self.tmpP1 == 'BlankPerk'):
            self.perk3_src = self.tmpP3
        else:
            self.perk3_rand()

    def perk4_rand(self):
        tmp_first, tmp_last = 0, len(svr_lists.svr_perk)
        if sm.get_screen('scfg_scr').ids['sw_1'].active:
            if sm.get_screen('scfg_scr').ids['sw_2'].active:
                tmp_first = 11
        else:
            if sm.get_screen('scfg_scr').ids['sw_2'].active:
                tmp_first, tmp_last = 11, len(svr_lists.svr_perk) - 1
            else:
                tmp_last = len(svr_lists.svr_perk) - 1

        self.tmpP4 = \
            random.choice(svr_lists.svr_perk[tmp_first:tmp_last:])

        if (DupliCheck(self.tmpP4, self.tmpP1, self.tmpP2, self.tmpP3)
                or self.tmpP4 == 'BlankPerk'):
            self.perk4_src = self.tmpP4
        else:
            self.perk4_rand()

    def item_allrand(self):
        self.item_rand()
        self.addon1_rand()
        self.addon2_rand()

    def item_rand(self):
        if sm.get_screen('scfg_scr').ids['sw_3'].active:
            self.item_src = random.choice(svr_lists.svr_item)
        else:
            self.item_src = random.choice(svr_lists.svr_item[:-1:])

        self.addon1_src = 'BlankAddon'
        self.addon2_src = 'BlankAddon'

    def addon1_rand(self):
        if self.item_src.startswith('Flashlight'):
            if sm.get_screen('scfg_scr').ids['sw_4'].active:
                self.tmpA1 = random.choice(svr_lists.svr_addon[0])
            else:
                self.tmpA1 = random.choice(svr_lists.svr_addon[0][:-1:])

            if self.tmpA1 == self.tmpA2:
                self.addon1_rand()
            else:
                self.addon1_src = self.tmpA1

        elif self.item_src.startswith('Key'):
            if sm.get_screen('scfg_scr').ids['sw_4'].active:
                self.tmpA1 = random.choice(svr_lists.svr_addon[1])
            else:
                self.tmpA1 = random.choice(svr_lists.svr_addon[1][:-1:])

            if self.tmpA1 == self.tmpA2:
                self.addon1_rand()
            else:
                self.addon1_src = self.tmpA1

        elif self.item_src.startswith('Map'):
            if sm.get_screen('scfg_scr').ids['sw_4'].active:
                self.tmpA1 = random.choice(svr_lists.svr_addon[2])
            else:
                self.tmpA1 = random.choice(svr_lists.svr_addon[2][:-1:])

            if self.tmpA1 == self.tmpA2:
                self.addon1_rand()
            else:
                self.addon1_src = self.tmpA1

        elif self.item_src.startswith('MedKit'):
            if sm.get_screen('scfg_scr').ids['sw_4'].active:
                self.tmpA1 = random.choice(svr_lists.svr_addon[3])
            else:
                self.tmpA1 = random.choice(svr_lists.svr_addon[3][:-1:])

            if self.tmpA1 == self.tmpA2:
                self.addon1_rand()
            else:
                self.addon1_src = self.tmpA1

        elif self.item_src.startswith('ToolBox'):
            if sm.get_screen('scfg_scr').ids['sw_4'].active:
                self.tmpA1 = random.choice(svr_lists.svr_addon[4])
            else:
                self.tmpA1 = random.choice(svr_lists.svr_addon[4][:-1:])

            if self.tmpA1 == self.tmpA2:
                self.addon1_rand()
            else:
                self.addon1_src = self.tmpA1

    def addon2_rand(self):
        if self.item_src.startswith('Flashlight'):
            if sm.get_screen('scfg_scr').ids['sw_4'].active:
                self.tmpA2 = random.choice(svr_lists.svr_addon[0])
            else:
                self.tmpA2 = random.choice(svr_lists.svr_addon[0][:-1:])

            if self.tmpA2 == self.tmpA1:
                self.addon2_rand()
            else:
                self.addon2_src = self.tmpA2

        elif self.item_src.startswith('Key'):
            if sm.get_screen('scfg_scr').ids['sw_4'].active:
                self.tmpA2 = random.choice(svr_lists.svr_addon[1])
            else:
                self.tmpA2 = random.choice(svr_lists.svr_addon[1][:-1:])

            if self.tmpA2 == self.tmpA1:
                self.addon2_rand()
            else:
                self.addon2_src = self.tmpA2

        elif self.item_src.startswith('Map'):
            if sm.get_screen('scfg_scr').ids['sw_4'].active:
                self.tmpA2 = random.choice(svr_lists.svr_addon[2])
            else:
                self.tmpA2 = random.choice(svr_lists.svr_addon[2][:-1:])

            if self.tmpA2 == self.tmpA1:
                self.addon2_rand()
            else:
                self.addon2_src = self.tmpA2

        elif self.item_src.startswith('MedKit'):
            if sm.get_screen('scfg_scr').ids['sw_4'].active:
                self.tmpA2 = random.choice(svr_lists.svr_addon[3])
            else:
                self.tmpA2 = random.choice(svr_lists.svr_addon[3][:-1:])

            if self.tmpA2 == self.tmpA1:
                self.addon2_rand()
            else:
                self.addon2_src = self.tmpA2

        elif self.item_src.startswith('ToolBox'):
            if sm.get_screen('scfg_scr').ids['sw_4'].active:
                self.tmpA2 = random.choice(svr_lists.svr_addon[4])
            else:
                self.tmpA2 = random.choice(svr_lists.svr_addon[4][:-1:])

            if self.tmpA2 == self.tmpA1:
                self.addon2_rand()
            else:
                self.addon2_src = self.tmpA2

    def offering_rand(self):
        if sm.get_screen('scfg_scr').ids['sw_5'].active:
            self.offering_src = random.choice(svr_lists.svr_offering)
        else:
            self.offering_src = random.choice(svr_lists.svr_offering[:-1:])


class KillerScreen(Screen):

    perk1_src = StringProperty('BlankPerk')
    perk2_src = StringProperty('BlankPerk')
    perk3_src = StringProperty('BlankPerk')
    perk4_src = StringProperty('BlankPerk')
    port_src = StringProperty('Unknown')
    addon1_src = StringProperty('BlankAddon')
    addon2_src = StringProperty('BlankAddon')
    offering_src = StringProperty('BlankOffering')

    tmpP1 = tmpP2 = tmpP3 = tmpP4 = ''
    tmpA1 = tmpA2 = ''
    killer_num = 999

    def back_main(self):
        sm.current = 'main_scr'

    def to_config(self):
        sm.current = 'kcfg_scr'

    def chara_rand(self):
        self.killer_num = random.randint(0, len(klr_lists.klr_portrait) - 1)
        self.port_src = klr_lists.klr_portrait[self.killer_num]
        self.addon1_src = 'BlankAddon'
        self.addon2_src = 'BlankAddon'

    def all_rand(self):
        self.chara_rand()
        self.perk_rand()
        self.addon_rand()
        self.offering_rand()

    def perk_rand(self):
        self.perk1_rand()
        self.perk2_rand()
        self.perk3_rand()
        self.perk4_rand()

    def perk1_rand(self):
        tmp_first, tmp_last = 0, len(klr_lists.klr_perk)
        if sm.get_screen('kcfg_scr').ids['sw_1'].active:
            if sm.get_screen('kcfg_scr').ids['sw_2'].active:
                tmp_first = 12
        else:
            if sm.get_screen('kcfg_scr').ids['sw_2'].active:
                tmp_first, tmp_last = 12, len(klr_lists.klr_perk) - 1
            else:
                tmp_last = len(klr_lists.klr_perk) - 1

        self.tmpP1 = \
            random.choice(klr_lists.klr_perk[tmp_first:tmp_last:])

        if (DupliCheck(self.tmpP1, self.tmpP2, self.tmpP3, self.tmpP4)
                or self.tmpP1 == 'BlankPerk'):
            self.perk1_src = self.tmpP1
        else:
            self.perk1_rand()

    def perk2_rand(self):
        tmp_first, tmp_last = 0, len(klr_lists.klr_perk)
        if sm.get_screen('kcfg_scr').ids['sw_1'].active:
            if sm.get_screen('kcfg_scr').ids['sw_2'].active:
                tmp_first = 12
        else:
            if sm.get_screen('kcfg_scr').ids['sw_2'].active:
                tmp_first, tmp_last = 12, len(klr_lists.klr_perk) - 1
            else:
                tmp_last = len(klr_lists.klr_perk) - 1

        self.tmpP2 = \
            random.choice(klr_lists.klr_perk[tmp_first:tmp_last:])

        if (DupliCheck(self.tmpP2, self.tmpP1, self.tmpP3, self.tmpP4)
                or self.tmpP2 == 'BlankPerk'):
            self.perk2_src = self.tmpP2
        else:
            self.perk2_rand()

    def perk3_rand(self):
        tmp_first, tmp_last = 0, len(klr_lists.klr_perk)
        if sm.get_screen('kcfg_scr').ids['sw_1'].active:
            if sm.get_screen('kcfg_scr').ids['sw_2'].active:
                tmp_first = 12
        else:
            if sm.get_screen('kcfg_scr').ids['sw_2'].active:
                tmp_first, tmp_last = 12, len(klr_lists.klr_perk) - 1
            else:
                tmp_last = len(klr_lists.klr_perk) - 1

        self.tmpP3 = \
            random.choice(klr_lists.klr_perk[tmp_first:tmp_last:])

        if (DupliCheck(self.tmpP3, self.tmpP1, self.tmpP2, self.tmpP4)
                or self.tmpP3 == 'BlankPerk'):
            self.perk3_src = self.tmpP3
        else:
            self.perk3_rand()

    def perk4_rand(self):
        tmp_first, tmp_last = 0, len(klr_lists.klr_perk)
        if sm.get_screen('kcfg_scr').ids['sw_1'].active:
            if sm.get_screen('kcfg_scr').ids['sw_2'].active:
                tmp_first = 12
        else:
            if sm.get_screen('kcfg_scr').ids['sw_2'].active:
                tmp_first, tmp_last = 12, len(klr_lists.klr_perk) - 1
            else:
                tmp_last = len(klr_lists.klr_perk) - 1

        self.tmpP4 = \
            random.choice(klr_lists.klr_perk[tmp_first:tmp_last:])

        if (DupliCheck(self.tmpP4, self.tmpP1, self.tmpP2, self.tmpP3)
                or self.tmpP4 == 'BlankPerk'):
            self.perk4_src = self.tmpP4
        else:
            self.perk4_rand()

    def addon_rand(self):
        self.addon1_rand()
        self.addon2_rand()

    def addon1_rand(self):
        if self.killer_num == 999:
            return

        if sm.get_screen('kcfg_scr').ids['sw_3'].active:
            self.tmpA1 = \
                random.choice(klr_lists.klr_addon[self.killer_num])
        else:
            self.tmpA1 = \
                random.choice(klr_lists.klr_addon[self.killer_num][:-1:])

        if self.tmpA1 == self.tmpA2 and self.tmpA1 != 'BlankAddon':
            self.addon1_rand()
        else:
            self.addon1_src = self.tmpA1

    def addon2_rand(self):
        if self.killer_num == 999:
            return

        if sm.get_screen('kcfg_scr').ids['sw_3'].active:
            self.tmpA2 = \
                random.choice(klr_lists.klr_addon[self.killer_num])
        else:
            self.tmpA2 = \
                random.choice(klr_lists.klr_addon[self.killer_num][:-1:])

        if self.tmpA2 == self.tmpA1 and self.tmpA2 != 'BlankAddon':
            self.addon2_rand()
        else:
            self.addon2_src = self.tmpA2

    def offering_rand(self):
        if sm.get_screen('kcfg_scr').ids['sw_4'].active:
            self.offering_src = random.choice(klr_lists.klr_offering)
        else:
            self.offering_src = random.choice(klr_lists.klr_offering[:-1:])


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
