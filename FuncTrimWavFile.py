from pydub import AudioSegment
import math

#== CONST == (1000 = 1 second)
foldername='readyornot'
moviename = 'readyornot'
src_path = 'sound/readyornot.wav' #don't forget to create folder in 'trim' fisrt
start_time = 00000
end_time = 30000
segment_lenght = 30000
#===========================

audio = AudioSegment.from_wav(src_path)
print('================ INFO ====================')
print('seconds = ',audio.duration_seconds)
print('each segment = ',segment_lenght/1000,' seconds')
all_time = audio.duration_seconds * 1000;
print('trim count = ',math.ceil(all_time/segment_lenght))

count = 1
while( end_time <= all_time):
  trimmed_audio = audio[start_time:end_time]
  trimmed_audio.export("trim/"+foldername+"/"+moviename+"_"+str(count)+".wav", format="wav")
  
  count+=1
  start_time+=segment_lenght
  end_time+=segment_lenght

remain_time = all_time - start_time
end_time += remain_time;

if(start_time < end_time):
  trimmed_audio = audio[start_time:end_time]
  trimmed_audio.export("trim/"+foldername+"/"+moviename+"_"+str(count)+".wav", format="wav")
print('============== FINISH ===================')