#!/usr/bin/python
# -*- coding: gbk -*-
import os 
import time 
import sys 
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
else: 
  print ('���ʧ�ܣ�')
  print ('����·���ͻ��������Ƿ���ȷ��')
time.sleep(3)
