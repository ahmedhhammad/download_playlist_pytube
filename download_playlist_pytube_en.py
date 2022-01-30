#اللهم صلي وسلم علي سيدنا محمد

from pytube import Playlist
from pytube import YouTube

p = Playlist(input("Enter the playlist link : "))

Download_Dir = str(input("Enter the directory to save your downloades like this ( E:\files\download ) : "))
print(f'PlayList : {p.title}')



start = int(input("\n" + "number of first video : "))-1
end = int(input("number of last video : "))
quality = str(input("download quality like ( 360 , 480 , 720 )"))

for video in p.videos[start:end]:

    video.streams.get_by_resolution(f"{quality}p").download(output_path=Download_Dir)
    

    yt = YouTube(p.video_urls[start])
    
    size_Mg = int(yt.streams.get_by_resolution(f"{quality}p").filesize)/(1024*1024)
    
    print(f"Successfully Downloaded | {video.title} " + " | File_Size = " + str("{:.2f}".format(size_Mg)) + "MB")


    start+=1


