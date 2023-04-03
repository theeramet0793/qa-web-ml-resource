import collections
import json
from flask_restful import Resource
import pymysql
from flask import request, Response
from Const import connectionHost, connectionUser, connectionPassword, connectionDatabase

def saveKeyword2db( object_list, tmdbId, postId, isFromIMDB, isFromYouTube):
  connection = pymysql.connect(host=connectionHost, user=connectionUser, password=connectionPassword,db=connectionDatabase)
  mycursor = connection.cursor()
  
  #Mark raw data row that already used
  # mycursor.execute("\
  # UPDATE "+tableName+"\
  # SET isUsed = 1\
  # WHERE id = %s",(id_in_table))
  # connection.commit()
  
  #Loop for save keyword to db
  for object_word in object_list:
    mycursor.execute("\
      INSERT INTO Keywordmovie(tmdbId, keyword, freq, fromPostId, isFromIMDB, isFromYouTube)\
      VALUES(%s,%s,%s,%s,%s,%s)",( tmdbId, object_word['word'], str(object_word['freq']), postId, isFromIMDB, isFromYouTube) )
    connection.commit()
  
  connection.close()
