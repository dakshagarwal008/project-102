import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject =cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imageName = "img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        start_time = time.time
        result = False
    return imageName 
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destoryAllWindows()

def Upload_file(imageName):
    access_token = "sl.BERAcFGG_4SNND6NKzCu_z27Iy2GrPo343sTuxh6vISF7bK-RuiSlZXVlDwAJ9fSG-mK8RPvOReCK5rViCZLKGpR6tz4YiQQ1PJDDBGl4quy2tEP-VMfO4Kgn_1sUJA7UUq1mAfTTJHb"
    file = imageName
    file_from = file
    file_to = "/Daksh102-project/"+(imageName)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file Uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            Upload_file(name)
main()