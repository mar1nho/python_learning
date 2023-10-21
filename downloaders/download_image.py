import urllib.request
from tools import speaker


def __download_image(url, file_name, language):
    if language == "pt_br":
        speaker.speak("Iniciando download", language)
        full_path_to_save = 'files_generated/images/saved_from_url/' + file_name + '.jpg'
        urllib.request.urlretrieve(url, full_path_to_save)
        speaker.speak('Download concluído!', language)
    elif language == "en_us":
        speaker.speak("Downloading the image...", language)
        full_path_to_save = 'files_generated/images/saved_from_url/' + file_name + '.jpg'
        urllib.request.urlretrieve(url, full_path_to_save)
        speaker.speak('Downloaded successfully the image.!', language)