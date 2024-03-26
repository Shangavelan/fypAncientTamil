import os 
os.chdir('data')
#os.system('tesseract atam.anc.exp0.jpg ../testOut/output1 -l tam')
os.system('tesseract atam.anc.exp0.jpg ../testOut/output1 -l atam')

#export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/