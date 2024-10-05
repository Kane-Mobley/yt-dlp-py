import subprocess
from pprint import pprint
import inquirer
typeQuestion = [
    inquirer.List(
        "type",
        message="What type of import are you using?",
        choices=["batch", "link"],
    ),
]
typeState = inquirer.prompt(typeQuestion)
pprint(typeState)
if typeState["type"] == "batch":
    batchFilePath = "./Input/URLS.txt"
    formatQuestions = [
        inquirer.List(
            "format",
            message="What format do you need?",
            choices=["mp4", "mp3", "webm"],
            ),
            ]
    state = inquirer.prompt(formatQuestions)
    pprint(state["format"])
    pprint(state["format"])
    if state["format"] != 'mp3':
        subprocess.run(["./Assets/yt-dlp", "-f", state["format"], "--ffmpeg-location", "./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffmpeg.exe", "-P","Output", "-a", batchFilePath])
        input("Press enter to continue.....")
    elif state["format"] == 'mp3':
        subprocess.run(["./Assets/yt-dlp", "-x","--audio-format","mp3","--ffmpeg-location", "./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffmpeg.exe", "-P","Output", "-a", batchFilePath])
        input("Press enter to continue.....")
    else:
        print("Please select valid download option and try again")
        input("Press enter to continue.....")
elif typeState["type"] == "link":
    youTubeLink = str(input("PASTE YOUR YOUTUBE LINK: "))
    formatQuestions = [
        inquirer.List(
            "format",
            message="What format do you need?",
            choices=["mp4", "mp3", "webm"],
        ),
    ]
    state = inquirer.prompt(formatQuestions)
    pprint(state["format"])
    if state["format"] != 'mp3':
        subprocess.run(["./Assets/yt-dlp", "-f", state["format"], "--ffmpeg-location", "./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffmpeg.exe", "-P","Output", youTubeLink])
        input("Press enter to continue.....")
    elif state["format"] == 'mp3':
        subprocess.run(["./Assets/yt-dlp", "-x","--audio-format","mp3","--ffmpeg-location", "./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffmpeg.exe", "-P","Output", youTubeLink])
        input("Press enter to continue.....")
    else:
        print("Please select valid download option and try again")
        input("Press enter to continue.....")