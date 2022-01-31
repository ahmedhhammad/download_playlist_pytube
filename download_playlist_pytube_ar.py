#اللهم صلي وسلم علي سيدنا محمد

from pytube import Playlist
from pytube import YouTube

p = Playlist(input("رابط قائمة التشغيل : "))

Download_Dir = str(input("اكتب مسار الملف الي هتحمل فيه الفيديوهات زي كدا مثلا ( E:\files\download ) : "))
print(f'قائمة التشغيل  : {p.title}')



start = int(input("\n" + "رقم اول فيديو : "))-1
end = int(input("رقم اخر فيديو : "))
quality = str(input("جودة التحميل مثلا (360 او 480 او 720 ) : "))

for video in p.videos[start:end]:

    # دة عشان ابتدي احمل الفيديوهات وبأختار الجودة 
    video.streams.get_by_resolution(f"{quality}p").download(output_path=Download_Dir)
    
    ## هنا جبت اللينك من البلاي ليست وعاملته كانه لينك فيديو عادي عشان اقدر احدد حجم الملف
    # الخاص بالمكتبه كويس هتفهم انا لفيت اللفه دي ليه documentation لو قرأت ال  
    #كان ممكن احصل علي البيانات الي عايزها باستخدام 
    #  تانية بس كانت هتستهلك وقت ومعالجة اكتر for loop
    
    yt = YouTube(p.video_urls[start])
    
    ##هنا قدرت اجيب حجم الملف المحمل كاضافة بيانات للمستخدم مش اكتر بالجودة  المعينه محولة لميجا بايت
    size_Mg = int(yt.streams.get_by_resolution(f"{quality}p").filesize)/(1024*1024)
    
    # دي مجرد بيانات هتظهر للمستخدم اثناء تحميل كل فيديو بحيث يبقي متابع البرنامج
    print(f"Successfully Downloaded | {video.title} " + " | File_Size = " + str("{:.2f}".format(size_Mg)) + "MB")

    #دي عشان اتابع احجام الفيديوهات اعمل تريس للبرنامج هتعرف فايدتها
    # ;)
    start+=1


