import subprocess
from pprint import pprint
import inquirer
from classes import FileFormat, ImportType

def promptForFormat():
    return [inquirer.List(
            "format",
            message="What format do you need?",
            choices=[FileFormat.MP4, FileFormat.MP3, FileFormat.WEBM],
            )]
def promptForImportType():
    return [inquirer.List(
            "type",
            message="What type of import are you using?",
            choices=[ImportType.BATCH, ImportType.LINK],
            )]
    
def batchUploadVideo(batchFilePath, format):
    subprocess.run(["./Assets/yt-dlp", "-f", format, "--ffmpeg-location", "./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffmpeg.exe", "-P","Output", "-a", batchFilePath])

def batchUploadSound(batchFilePath):
    subprocess.run(["./Assets/yt-dlp", "-x","--audio-format","mp3","--ffmpeg-location", "./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffmpeg.exe", "-P","Output", "-a", batchFilePath])

def linkUploadVideo(youTubeLink, format):
    subprocess.run(["./Assets/yt-dlp", "-f", format, "--ffmpeg-location", "./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffmpeg.exe", "-P","Output", youTubeLink])

def linkUploadSound(youTubeLink):
    subprocess.run(["./Assets/yt-dlp", "-x","--audio-format","mp3","--ffmpeg-location", "./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffmpeg.exe", "-P","Output", youTubeLink])

def uploadMedia(format, media, videoUploadFunc, soundUploadFunc):
    match format:
        case FileFormat.MP4:
            videoUploadFunc(media, FileFormat.MP4)
        case FileFormat.WEBM:
            videoUploadFunc(media, FileFormat.WEBM)
        case FileFormat.MP3:
            soundUploadFunc(media)
        case _:
            print("Please select valid download option and try again")


typeQuestion = [
    inquirer.List(
        "type",
        message="What type of import are you using?",
        choices=[ImportType.BATCH, ImportType.LINK],
    ),
]
typeState = inquirer.prompt(promptForImportType())
pprint(typeState)
match typeState["type"]:
 case ImportType.BATCH:
    batchFilePath = "./Input/URLS.txt"
    state = inquirer.prompt(promptForFormat())
    format = state["format"]
    # TODO - are both of the below lines needed?
    pprint(format)
    uploadMedia(format, batchFilePath, batchUploadVideo, batchUploadSound)
 case ImportType.LINK:   
    youTubeLink = str(input("PASTE YOUR YOUTUBE LINK: "))
    state = inquirer.prompt(promptForFormat())
    format = state["format"]
    pprint(format)
    uploadMedia(format, youTubeLink, linkUploadVideo, linkUploadSound)

input("Press enter to continue.....")