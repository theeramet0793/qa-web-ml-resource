import os

#===== CONST ==========================
src_directory = 'movieText/readyornot'
dest_file = 'readyornot_full_text.txt' #don't forget to create .txt file in fulltext first
#=====================================
def sortedFile(fileList):
  arr = []
  for filename in file_list:
    sep = filename.replace('.','_').split('_') 
    for x in sep:
      if(x.isdigit()):
        arr.insert(int(x)-1, filename)
  return arr
#=====================================
file_list = []
for filename in os.listdir(src_directory):
    f = os.path.join(src_directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        file_list.append(filename)

mysortedFile = (sortedFile(file_list))

for filename in mysortedFile:
  f = open(src_directory+'/'+filename, "r",  encoding="utf8")
  text = f.read()
  f.close()
  f = open("fullText/"+dest_file, "a", encoding="utf-8")
  f.write(text)
  f.close()