#اللهم صلي وسلم علي سيدنا محمد

#Make sure that pytube is installed
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install" ,"--upgrade", package])
install("Pytube")

from pytube import Playlist
from pytube import YouTube

Download_Dir = str(input("Enter the directory to save your downloades example: ( E:\Files\download ) : "))

def download_playlist():    
    p = Playlist(input("Enter the playlist link : "))
    print(f'PlayList : {p.title}')
    
    start = int(input("\n" + "number of first video : "))-1
    end = int(input("number of last video : "))
    quality = str(input("download quality like ( 360 , 480 , 720 ) : "))

    for video in p.videos[start:end]:

        video.streams.get_by_resolution(f"{quality}p").download(output_path=Download_Dir)
        
        yt = YouTube(p.video_urls[start])
        
        size_Mg = int(yt.streams.get_by_resolution(f"{quality}p").filesize)/(1024*1024)
        
        print(f"Successfully Downloaded | {video.title} " + " | File_Size = " + str("{:.2f}".format(size_Mg)) + "MB")

        start+=1
              
def decision():
    global the_decision
    
    print("\n"+"Do you want to download more? ")
    print("If Yes press y || If No press n")
    the_decision = input("(yes or no) : ")
    
    return the_decision

download_playlist()     
decision()

while str(the_decision) == "y":
    download_playlist()     
    decision()
