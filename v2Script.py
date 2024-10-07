import os
import urllib.request
import zipfile
import shutil
from pprint import pprint
ffmpegPath = './Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build.zip'
ffmpegURL = 'https://github.com/GyanD/codexffmpeg/releases/download/2024-10-02-git-358fdf3083/ffmpeg-2024-10-02-git-358fdf3083-full_build.zip'
assetsPath = './Assets/'
inputPath = './Input/'
outputPath = './Output'
mods = ['inquirer','yt_dlp']
# yt-dlp and inquierer check
try:
    import yt_dlp
    print(mods[1]+' is installed')
except:
    print('Package not available, running install command...')
    os.system('pip install '+ mods[1])
try:
    import inquirer
    print(mods[0]+' is installed')
except:
    print('Package not available, running install command...')
    os.system('pip install '+ mods[0])
# required directories check
try:
    print('Creating Assets....')
    os.mkdir(assetsPath)
    urllib.request.urlretrieve(ffmpegURL, ffmpegPath)
    with zipfile.ZipFile(ffmpegPath, 'r') as zip_ref:
        zip_ref.extractall('./Assets/')
    os.remove(ffmpegPath)
    shutil.move("./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffmpeg.exe","./Assets/")
    shutil.move("./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffprobe.exe","./Assets/")
    shutil.rmtree("./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/")

except:
    print('Assets Directory Already Exists....')
try :
    print('Creating Input Directory....')
    os.mkdir(inputPath)
    with open(inputPath + '/URLs.json', 'w') as file:
        file.write({'url':'https://www.youtube.com/watch?v=2XjouKSkSeM'})
except:
    print('Input Directory Already Exists....')
try :
    print('Creating Output Directory....')
    os.mkdir(outputPath)
except:
    print('Output Directory Already Exists....')
print('Requirements met...Running yt-dlp-py....')
# begin code for downloader
typeQuestion = [
    inquirer.List(
        'type',
        message='What type of import are you using?',
        choices=['batch', 'link'],
    ),
]
typeState = inquirer.prompt(typeQuestion)
pprint(typeState['type'])
if typeState['type'] == 'batch':
    batchFilePath = './Input/URLS.txt'
    formatQuestions = [
        inquirer.List(
            'format',
            message='What format do you need? (More formats coming later)',
            choices=['mp3'],
            ),
            ]
    state = inquirer.prompt(formatQuestions)
    pprint(state['format'])

elif typeState['type'] == 'link':
    youTubeLink = str(input('PASTE YOUR YOUTUBE LINK: '))
    formatQuestions = [
        inquirer.List(
            'format',
            message='What format do you need? (More formats coming later)',
            choices=['mp3'],
            ),
            ]
    state = inquirer.prompt(formatQuestions)
    pprint(state['format'])
    def format_selector(ctx):
        ''' Select the best video and the best audio that won't result in an mkv.
        NOTE: This is just an example and does not handle all cases '''
        formats = ctx.get('formats')[::-1]
        best_video = next(f for f in formats
                          if f['vcodec'] != 'none' and f['acodec'] == 'none')
        audio_ext = {'mp4': 'm4a', 'webm': 'webm'}[best_video['ext']]
        best_audio = next(f for f in formats if (
            f['acodec'] != 'none' and f['vcodec'] == 'none' and f['ext'] == audio_ext))
        yield {
            'format_id': f'{best_video['format_id']}+{best_audio['format_id']}',
            'ext': best_video['ext'],
            'requested_formats': [best_video, best_audio],
            'protocol': f'{best_video['protocol']}+{best_audio['protocol']}'
        }
    ydl_opts = {
        'format': format_selector,
        'output' : "Output",
        'postprocessors': [{  # Extract audio using ffmpeg
        'ffmpeg-location': './Assets/ffmpeg.exe',
        'key': 'FFmpegExtractAudio',
        'preferredcodec': state['format'],
    }]
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(youTubeLink)