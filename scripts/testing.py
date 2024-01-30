import os 
os.chdir('data')
os.system('tesseract atam.anc.exp0.png ../testOut/output -l atam')