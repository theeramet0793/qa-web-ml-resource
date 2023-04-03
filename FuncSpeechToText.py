
import speech_recognition as sr
import os

#===== CONST ==========================
src_directory = 'trim/readyornot'
dest_folder = 'readyornot' #don't forget to create folder in movieText fisrt
#=====================================

for filename in os.listdir(src_directory):
    f = os.path.join(src_directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        #print(f)
        myfile=sr.AudioFile(f)
        r = sr.Recognizer()
        with myfile as source:
            audio = r.record(source)

        try:
            print('==================================================')
            print('START GOOGLE RECOGNIZE FOR: '+filename)
            s = r.recognize_google(audio_data=audio, language="th-TH", show_all=True)
            print('FINISH GOOGLE RECOGNIZE')
            alternativeList = s['alternative']
            transcript0 = alternativeList[0]
            transcript0Value = transcript0['transcript']
            #print(transcript0Value)
            print('CREATING '+filename[:len(filename)-4]+'.txt')
            f = open("movieText/"+dest_folder+"/"+filename[:len(filename)-4]+".txt", "x", encoding="utf-8")
            f.write(transcript0Value)
            f.close()
            print("FINISH")
        except Exception as e:
            print("Exception: "+str(e))
print("============ Finish All ===============")

