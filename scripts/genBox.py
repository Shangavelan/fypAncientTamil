import os
os.chdir('data')
print(os.listdir('./'));
number_of_files = len(os.listdir('./'))
for i in range(0, number_of_files):
   os.system(f"tesseract -l tam atam.anc.exp{i}.jpeg atam.anc.exp{i} batch.nochop makebox")

#export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/
