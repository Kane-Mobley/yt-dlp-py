import os
import urllib.request
import zipfile
print("Downloading yt-dlp and ffmpeg exe's and setting up Assets folder...")
yt_dlpURL = 'https://github.com/yt-dlp/yt-dlp/releases/download/2024.09.27/yt-dlp.exe'
ffmpegURL = 'https://github.com/GyanD/codexffmpeg/releases/download/2024-10-02-git-358fdf3083/ffmpeg-2024-10-02-git-358fdf3083-full_build.zip'
yt_dlp_Path = './Assets/yt-dlp.exe'
ffmpeg_Path = './Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build.zip'
urllib.request.urlretrieve(yt_dlpURL, yt_dlp_Path)
urllib.request.urlretrieve(ffmpegURL, ffmpeg_Path)
with zipfile.ZipFile(ffmpeg_Path, 'r') as zip_ref:
    zip_ref.extractall("./Assets/")
os.remove("./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build.zip")
package = "inquirer"
print("done....")
print("checking inquirer install.....")
try:
    import inquirer
    print(package+" has been installed already")
    input("Press enter to close...")
except:
    print("Package not available, running install command")
    os.system("pip install "+ package)
    input("Press enter to close...")