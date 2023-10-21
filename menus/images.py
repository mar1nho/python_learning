from colorama import init, Fore, Back
from tools import remove_background as rb
from translation_lang import pt_br as lang_pt
from translation_lang import en_us as lang_eng
from downloaders import download_image as download


def ___checkImageContents(main_language):
    en = 'en_us'
    pt = 'pt_br'
    if main_language == pt:
        msg = lang_pt.select_options_bellow_pt()
        print(Fore.RED + msg)
        msg = lang_pt.image_options_pt()
        print(Fore.LIGHTBLUE_EX + msg)
        choice = input(Fore.GREEN)
        if choice == "1":
            url = input(Fore.YELLOW + lang_pt.select_image_url_pt())
            name = input(Fore.YELLOW + lang_pt.select_image_name_pt())
            download.__download_image(url, name, main_language)
        elif choice == "2":
            directory = input(Fore.YELLOW + lang_pt.select_image_directory_pt())
            name = input(Fore.YELLOW + lang_pt.select_image_name_pt())
            rb.___remove_background(directory, name, main_language)

    elif main_language == en:
        msg = lang_eng.selectOptions_en()
        print(Fore.RED + msg)
        msg = lang_eng.optionsBlue_en()
        print(Fore.LIGHTBLUE_EX + msg)
        choice = input(Fore.GREEN)
        if choice == "1":
            url = input(Fore.YELLOW + lang_eng.selectUrl_en())
            name = input(Fore.YELLOW + lang_eng.selectName_en())
            download.__download_image(url, name, main_language)
        elif choice == "2":
            directory = input(Fore.YELLOW + lang_eng.selectDirectory_en())
            name = input(Fore.YELLOW + lang_eng.selectName_en())
            rb.___remove_background(directory, name, main_language)
