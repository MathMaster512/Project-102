import cv2
import dropbox
import time
import random


start_time = time.time()

def take_snapshot() :
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result) :
        ret, frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    
    return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.Bn73tIPCEHAFtwfrhUQ7AS8MaTifr1bsfE8TEb2BS6tqUS7URCfeobR6bsV6Rjf2lYWVFWMvnMwPHRaBRAr2NHZQk4q8Da-UE7kxRjGRZ8hZ-TJMivA3EXjhxAjU5CsDvoS9-74ahNAF"
    file = img_name
    file_from = file
    file_to = "/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, "rb") as f:
       
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")


def main() :
    while(True):
        if((time.time()-start_time) >=5) :
            name = take_snapshot()
            upload_file(name)

main()
