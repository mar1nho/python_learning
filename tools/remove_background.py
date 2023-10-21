from rembg import remove
from PIL import Image
from tools import speaker as bot


def ___remove_background(directory, name, main_language):
    if main_language == "pt_br":
        bot.speak('Iniciando remoção', main_language)
        print("Iniciando remoção")
        try:
            img = Image.open(directory)
            R = remove(img)
            path = "files_generated/images/no_background/" + name + '.png'
            valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
            if not path.lower().endswith(valid_extensions):
                bot.speak('Extensão inválida', main_language)
                raise ValueError("Invalid file extension for 'name' parameter")

            bot.speak('Fundo removido', main_language)
            print("Fundo removido com sucesso.")
            R.save(path)
        except FileNotFoundError as error:
            print(f"O arquivo não pôde ser encontrado: {error}")
            bot.speak("Arquivo não encontrado.")
        except ValueError as error:
            print(f"Erro ao salvar a imagem: {error}")
            bot.speak("Erro ao salvar imagem.")
        except Exception as error:
            bot.speak("Erro não esperado")
            print(f"Ocorreu um erro inesperado: {error}")

    elif main_language == "en_us":
        bot.speak('Removing background...', main_language)
        print("Initializing removing.")
        try:
            img = Image.open(directory)
            R = remove(img)
            path = "files_generated/images/no_background/" + name + '.png'
            valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
            if not path.lower().endswith(valid_extensions):
                bot.speak('Invalid extension', main_language)
                raise ValueError("Invalid file extension for 'name' parameter")

            bot.speak('Background removed', main_language)
            print("Background successfully removed.")
            R.save(path)
        except FileNotFoundError as error:
            print(f"File not found: {error}")
            bot.speak("Image not found.")
        except ValueError as error:
            print(f"Error saving image: {error}")
            bot.speak("Error saving the image.")
        except Exception as error:
            bot.speak("Unexpected error, check log for more infos.")
            print(f"Unexpected error occurred: {error}")