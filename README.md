# Question and Answer Website for Finding Movies

Project Question and Answer Website for Finding Movies has 5 repository
1. qa-web-frontend: เป็นโค้ดฝั่ง frontend (หลัก) ที่เอาไว้สร้าง web UI สำหรับผู้ใช้ทั่วไป 
2. qa-web-admin: เป็นโค้ดฝั่ง frontend ที่เอาไว้สร้าง web UI สำหรับผู้ใช้ที่เป็นแอดมิน(ซึ่งหมายถึงผู้พัฒนาโครงงานนี้เอง)สำหรับใช้ในการควบคุม API ของ qa-web-ml
3. qawebBackend: เป็นโค้ดฝั่ง Backend (หลัก) ที่เอาไว้สร้าง API สำหรับ qa-web-frontend
4. qa-web-ml: เป็นโค้ดฝั่ง Backend ที่เอาไว้สร้าง API สำหรับ Machine Learning ของระบบตอบชื่อภาพยนตร์อัตโนมัติในเว็บไซต์ 
5. qa-web-ml-resource: เป็นโค้ดที่เอาไว้จัดการข้อมูลเพื่อป้อนข้อมูลภาพยนตร์ในช่วงเริ่มต้นให้กับระบบแนะนำชื่อภาพยนตร์

## Description for this repository (qa-web-ml-resource)

### Install
1. Clone this repository

### Using
1.Download wav file
2.Use FuncTrimWavFile to trim long wav to shorter file
3.Use FuncSpeechToText to convert wav to text file
3.Use FuncConcatText to concat trim text to one text file
4.Use main.py to add movie data to ML database
