import os.path
from pytube import YouTube
from tools import speaker


def ___download_from_youtube_link(url, name, audio, video, language):
    inc = ""
    fin = ""
    if language == "pt_br":
        inc = 'Iniciando download.'
        fin = 'Donwload concluído.'
    elif language == "en_us":
        inc = 'Inicitalizing download'
        fin = 'Download successfully complete.'

    speaker.speak(inc, language)
    youtubeVideo = YouTube(url)
    if audio and not video:
        full_path_to_save = 'files_generated/youtube/audio_only/'
        youtubeVideo = youtubeVideo.streams.filter(
            only_audio=True).get_audio_only()
        try:
            download_file = youtubeVideo.download(output_path=full_path_to_save)

            new_file = name + '.mp3'
            os.rename(download_file, new_file)
        except Exception as error:
            print(f'Error: {error}')

    elif audio and video:
        youtubeVideo = youtubeVideo.streams.filter().get_highest_resolution()
        try:
            download_file = youtubeVideo.download(output_path='files_generated/youtube/audio_and_video/')
            new_file = name + '.mp4'
            os.rename(download_file, new_file)
        except Exception as error:
            print(f"Error: {error}")

    speaker.speak(fin, language)
