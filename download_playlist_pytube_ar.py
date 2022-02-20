#اللهم صلي وسلم علي سيدنا محمد

#للتاكد ان مكتبة pytube مثبتة
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install" ,"--upgrade", package])
install("Pytube")

from pytube import Playlist
from pytube import YouTube

Download_Dir = str(input("اكتب مسار الملف الي هتحمل فيه الفيديوهات زي كدا مثلا ( E:\Files\download ) : "))

def download_playlist():    
    p = Playlist(input("رابط قائمة التشغيل : "))
    print(f'قائمة التشغيل  : {p.title}')
    
    start = int(input("\n" + "رقم اول فيديو : "))-1
    end = int(input("رقم اخر فيديو : "))
    quality = str(input("جودة التحميل مثلا (360 او 480 او 720 ) : "))

    for video in p.videos[start:end]:

        # دة عشان ابتدي احمل الفيديوهات وبأختار الجودة 
        video.streams.get_by_resolution(f"{quality}p").download(output_path=Download_Dir)
        
        ## هنا جبت اللينك من البلاي ليست وعاملته كانه لينك عادي وبجيب منه البيانات يدوي
        # الخاص بالمكتبه كويس هتفهم انا لفيت اللفه دي ليه documentation لو قرأت ال  
        yt = YouTube(p.video_urls[start])
        
        ##هنا قدرت اجيب حجم الملف كاضافة للمستخدم مش اكتر بالجودة  المعينه وحولته لميجا بايت
        size_Mg = int(yt.streams.get_by_resolution(f"{quality}p").filesize)/(1024*1024)
        
        # دي مجرد بيانات هتظهر للمستخدم اثناء تحميل كل فيديو بحيث يبقي متابع البرنامج
        print(f"Successfully Downloaded | {video.title} " + " | File_Size = " + str("{:.2f}".format(size_Mg)) + "MB")

        #دي عشان اتابع احجام الفيديوهات اعمل تريس للبرنامج هتعرف فايدتها
        # ;)
        start+=1
              
# دي عشان يقرر هيكمل تحميل تاني ولا يقفل البرنامج
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
