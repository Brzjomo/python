#!/usr/bin/python
# -*- coding: gbk -*-
import os 
import time 
import sys 
import getpass

num = ''

output= '''
    1.����brzjomo.xml
    
    2.����HackNet�浵
    
    3.����MadGamesTycoon�浵1
    
    4.py4
    
    5.py5
    
    6.py6
    
    7.py7
    
    8.py8
    
    9.py9

    0.�˳�

'''

print (output)

while num !='0':#�����˳�����
	print ('---------------------------------------------')
	num=input(" ѡ����Ҫִ�еĲ���: ")
	print ('---------------------------------------------')
	if num =='0':
		print ()
		print ('�����˳�')
		print ()
		
	if num == '1':
		#���ݵ�Դ�ļ�·�� 
		source = ['D:/ED����/brzjomo.xml'] 
		#���ݵ��ļ����ŵĵط� 
		target_dir = 'E:/����/' 
		#�����ļ������� 
		target = target_dir + time.strftime('%Y-%m%d-%H%M')+'.7z' 
		#zip_command="7z a %s %s" %(target,' '.join(source))  
		zip_command="7z a %s %s" %(target,' '.join(source)) 
		if os.system(zip_command) == 0: 
		 print ('�ɹ������' + " " + "---" + target + "---")
		 print ('---------------------------------------------')
		else: 
		 print ('---------------------------------------------')
		 print ('���ʧ�ܣ�')
		 print ('����·���ͻ��������Ƿ���ȷ��')
		time.sleep(3)
		print (output)

	if num == '2':
        #���ݵ�Դ�ļ�·�� 
		source = ['C:/Users/'+getpass.getuser()+'/Documents/My" "Games/Hacknet/Accounts/save_Brzjomo.xml'] 
		#���ݵ��ļ����ŵĵط� 
		target_dir = 'G:/����/HackNet/' 
		#�����ļ������� 
		target = target_dir + time.strftime('%Y-%m%d-%H%M')+'.7z' 
		#zip_command="7z a %s %s" %(target,' '.join(source))  
		zip_command="7z a %s %s" %(target,' '.join(source)) 
		if os.system(zip_command) == 0: 
		 print ('�ɹ������' + " " + "---" + target + "---")
		 print ('---------------------------------------------')
		else: 
		 print ('---------------------------------------------')
		 print ('���ʧ�ܣ�')
		 print ('����·���ͻ��������Ƿ���ȷ��')
		time.sleep(5)
		print (output)

	if num == '3':
		#���ݵ�Դ�ļ�·�� 
		source = ['C:/Users/'+getpass.getuser()+'/AppData/LocalLow/Eggcode/Mad" "Games" "Tycoon/savegame0.txt'] 
		#���ݵ��ļ����ŵĵط� 
		target_dir = 'L:/����/Game�浵/MadGamesTycoon/' 
		#�����ļ������� 
		target = target_dir + time.strftime('%Y-%m%d-%H%M')+'.7z' 
		#zip_command="7z a %s %s" %(target,' '.join(source))  
		zip_command="7z a %s %s" %(target,' '.join(source)) 
		if os.system(zip_command) == 0: 
		 print ('�ɹ������' + " " + "---" + target + "---")
		 print ('---------------------------------------------')
		else: 
		 print ('---------------------------------------------')
		 print ('���ʧ�ܣ�')
		 print ('---------------------------------------------')
		 print ('����·���ͻ��������Ƿ���ȷ���Ƿ�װ7z�����')
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

	time.sleep(0.2)#������С������

if __name__ == '__main__':#���˳�����һ����ʾ������Ȼûʲô��
    for i in range(1,75):
        sys.stdout.write('0'+'=>'+"\b\b")
        sys.stdout.flush()
        time.sleep(0.027)

