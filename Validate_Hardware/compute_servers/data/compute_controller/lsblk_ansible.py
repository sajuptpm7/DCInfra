# ansible commands for each ip 
import os
import time
for i in range(4,16):
	cm = "ansible 10.140.210." + str(i) + " -a lsblk >> lsblk_details.txt"
	os.system(cm)
	#time.sleep(2)	 
