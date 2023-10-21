from downloaders import download_youtube as yt
from colorama import init, Fore, Back


def ___checkYoutubeContents(main_language):
    en = 'en_us'
    pt = 'pt_br'
    if main_language == pt:
        print(Fore.RED + "Selecione uma das opções abaixo")
        print(Fore.LIGHTCYAN_EX + "[1] Baixar audio apenas  [2] Baixar vídeo e audio")
        choice = input()
        url = input(Fore.LIGHTGREEN_EX + "Insira o link do vídeo: ")
        name = input(Fore.LIGHTGREEN_EX + "Dê um nome ao arquivo: ")
        if choice == '1':
            yt.___download_from_youtube_link(url, name, True, False, main_language)
        if choice == '2':
            yt.___download_from_youtube_link(url, name, True, True, main_language)

    if main_language == en:
        print(Fore.RED + "Select the options bellow")
        print(Fore.LIGHTCYAN_EX + "[1] Download Ony Audio  [2] Download Audio and Video")
        choice = input()
        url = input(Fore.LIGHTGREEN_EX + "Insert video link: ")
        name = input(Fore.LIGHTGREEN_EX + "Name the archive: ")
        if choice == '1':
            yt.___download_from_youtube_link(url, name, True, False, main_language)
        if choice == '2':
            yt.___download_from_youtube_link(url, name, True, True, main_language)
