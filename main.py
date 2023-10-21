from colorama import init, Fore, Back
import os
from tools import remove_background as rb
from menus import images as images_manager
from translation_lang import en_us as lang_eng
from translation_lang import pt_br as lang_pt
from menus import youtube as yt_manager
choices = [
    '[1]',
    '[2]',
    '[3]'
]

main_language = 'en_us'


def ___init():
    global main_language
    global choices
    init()
    running = True
    while running:
        if main_language == 'en_us':
            choices = lang_eng.choices_en()
            print(Fore.RED + lang_eng.en_lang())
        elif main_language == 'pt_br':
            choices = lang_pt.menu_choices_pt()
            print(Fore.RED + lang_pt.pt_lang())

        for i in range(len(choices)):
            print(Fore.LIGHTWHITE_EX + choices[i])

        choice = input(Fore.RED + "-->")

        if choice == "1":
            images_manager.___checkImageContents(main_language)
            running = True
        elif choice == "2":
            yt_manager.___checkYoutubeContents(main_language)
            running = True
        elif choice == "3":
            if main_language == 'en_us':
                main_language = 'pt_br'
                running = True
            elif main_language == 'pt_br':
                main_language = 'en_us'
                running = True


if __name__ == '__main__':
    ___init()
