from ClassFetchData import fetch_data_from_facebook_db, fetch_data_from_imdb_db, fetch_data_from_yt_db
from FuncWordTokenize import wordTokenize, countDuplicate
from FuncSave2DB import saveKeyword2db
from FuncCountKeyword import countKeyword

#=========== Start feed data to my system ===============
# fetch_data = fetch_data_from_facebook_db()
# tableName = 'moviefrompost'
# id = fetch_data[0][0]
# postId = fetch_data[0][1]
# tmdbId = fetch_data[0][2]
# detail = fetch_data[0][3]

# fetch_data = fetch_data_from_imdb_db()
# tableName = 'moviefromimdb'
# id = fetch_data[0][0]

#============ที่ต้องแก้==================
# 1.ชื่อ txt
# 2.tmdbId
# 3.isFromIMDB
# 4.isFromYouTube
#====================================
f = open("imdbText/youngone.txt", "r",  encoding="utf8")
text = f.read()
f.close()
tmdbId = 215379
isFromIMDB = 1
isFromYouTube = 0
detail = text
postId = None

#fetch_data = fetch_data_from_yt_db()
# tableName = 'moviefromyt'
# id = fetch_data[0][0]
# tmdbId = fetch_data[0][1]
# detail = fetch_data[0][2]
# postId = 'NULL'


keywordList = wordTokenize(detail)
#print(keywordList)

object_list = countDuplicate(keywordList)
#print(object_list)

saveKeyword2db(object_list,tmdbId,postId, isFromIMDB, isFromYouTube)
countKeyword(list(set(keywordList)))