#!/usr/bin/python
# -*- coding: utf-8 -*-
import os 
import time 
import sys 
import getpass

num = ''

output= '''
    1.备份brzjomo.xml
    
    2.备份HackNet存档
    
    3.备份MadGamesTycoon存档1
    
    4.py4
    
    5.py5
    
    6.py6
    
    7.py7
    
    8.py8
    
    9.py9

    0.退出

'''

print (output)

while num !='0':#定义退出数字
	print ('---------------------------------------------')
	num=input(" 选择需要执行的操作: ")
	print ('---------------------------------------------')
	if num =='0':
		print ()
		print ('正在退出')
		print ()
		
	if num == '1':
		#备份的源文件路径 
		source = ['D:/ED汉化/brzjomo.xml'] 
		#备份的文件所放的地方 
		target_dir = 'E:/备份/' 
		#备份文件的名字 
		target = target_dir + time.strftime('%Y-%m%d-%H%M')+'.7z' 
		#zip_command="7z a %s %s" %(target,' '.join(source))  
		zip_command="7z a %s %s" %(target,' '.join(source)) 
		if os.system(zip_command) == 0: 
		 print ('成功打包至' + " " + "---" + target + "---")
		 print ('---------------------------------------------')
		else: 
		 print ('---------------------------------------------')
		 print ('打包失败！')
		 print ('请检查路径和环境变量是否正确！是否安装7z软件！')
		time.sleep(3)
		print (output)

	if num == '2':
        #备份的源文件路径 
		source = ['C:/Users/'+getpass.getuser()+'/Documents/My" "Games/Hacknet/Accounts/save_Brzjomo.xml'] 
		#备份的文件所放的地方 
		target_dir = 'G:/备份/HackNet/' 
		#备份文件的名字 
		target = target_dir + time.strftime('%Y-%m%d-%H%M')+'.7z' 
		#zip_command="7z a %s %s" %(target,' '.join(source))  
		zip_command="7z a %s %s" %(target,' '.join(source)) 
		if os.system(zip_command) == 0: 
		 print ('成功打包至' + " " + "---" + target + "---")
		 print ('---------------------------------------------')
		else: 
		 print ('---------------------------------------------')
		 print ('打包失败！')
		 print ('请检查路径和环境变量是否正确！是否安装7z软件！')
		time.sleep(5)
		print (output)

	if num == '3':
		#备份的源文件路径 
		source = ['C:/Users/'+getpass.getuser()+'/AppData/LocalLow/Eggcode/Mad" "Games" "Tycoon/savegame0.txt'] 
		#备份的文件所放的地方 
		target_dir = 'L:/备份/Game存档/MadGamesTycoon/' 
		#备份文件的名字 
		target = target_dir + time.strftime('%Y-%m%d-%H%M')+'.7z' 
		#zip_command="7z a %s %s" %(target,' '.join(source))  
		zip_command="7z a %s %s" %(target,' '.join(source)) 
		if os.system(zip_command) == 0: 
		 print ('成功打包至' + " " + "---" + target + "---")
		 print ('---------------------------------------------')
		else: 
		 print ('---------------------------------------------')
		 print ('打包失败！')
		 print ('---------------------------------------------')
		 print ('请检查路径和环境变量是否正确！是否安装7z软件！')
		 print ('---------------------------------------------')
		time.sleep(5)
		print (output)

	if num == '4':
	 print ("py4")

	if num == '5':
	 print ("py5")

	if num == '6':
	 print ("py6")

	if num == '7':
	 print ("py7")

	if num == '8':
	 print ("py8")

	if num == '9':
	 print ("py9")

	time.sleep(0.2)#定义最小输入间隔

if __name__ == '__main__':#给退出增加一个显示条，虽然没什么用
    for i in range(1,75):
        sys.stdout.write('0'+'=>'+"\b\b")
        sys.stdout.flush()
        time.sleep(0.027)

