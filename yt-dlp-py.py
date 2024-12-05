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
    
def batchUploadVideo(batchFilePath, format):
    subprocess.run(["./Assets/yt-dlp", "-f", format, "--ffmpeg-location", "./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffmpeg.exe", "-P","Output", "-a", batchFilePath])

def batchUploadSound(batchFilePath):
    subprocess.run(["./Assets/yt-dlp", "-x","--audio-format","mp3","--ffmpeg-location", "./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffmpeg.exe", "-P","Output", "-a", batchFilePath])

def linkUploadVideo(youTubeLink, format):
    subprocess.run(["./Assets/yt-dlp", "-f", format, "--ffmpeg-location", "./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffmpeg.exe", "-P","Output", youTubeLink])

def linkUploadSound(youTubeLink):
    subprocess.run(["./Assets/yt-dlp", "-x","--audio-format","mp3","--ffmpeg-location", "./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffmpeg.exe", "-P","Output", youTubeLink])

typeQuestion = [
    inquirer.List(
        "type",
        message="What type of import are you using?",
        choices=[ImportType.BATCH, ImportType.LINK],
    ),
]
typeState = inquirer.prompt(typeQuestion)
pprint(typeState)
match typeState["type"]:
 case ImportType.BATCH:
    batchFilePath = "./Input/URLS.txt"
    formatQuestions = promptForFormat()
    state = inquirer.prompt(formatQuestions)
    # TODO - are both of the below lines needed?
    pprint(state["format"])
    pprint(state["format"])
    match state["format"]:
        case FileFormat.MP4:
            batchUploadVideo(batchFilePath, FileFormat.MP4)
        case FileFormat.WEBM:
            batchUploadVideo(batchFilePath, FileFormat.WEBM)
        case FileFormat.MP3:
            batchUploadSound(batchFilePath)
        case _:
            print("Please select valid download option and try again")
 case ImportType.LINK:   
    youTubeLink = str(input("PASTE YOUR YOUTUBE LINK: "))
    formatQuestions = promptForFormat()
    state = inquirer.prompt(formatQuestions)
    pprint(state["format"])
    match state["format"]:
        case FileFormat.MP4:
            linkUploadVideo(youTubeLink, FileFormat.MP4)
        case FileFormat.WEBM:
            linkUploadVideo(youTubeLink, FileFormat.WEBM)
        case FileFormat.MP3:
            linkUploadSound(youTubeLink)
        case _:
            print("Please select valid download option and try again")

input("Press enter to continue.....")