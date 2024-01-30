import os
#open jtesseditor
os.chdir('../projectFolder/jTessBoxEditor')
print(os.listdir())
os.system('java -Xms128m -Xmx1024m -jar jTessBoxEditor.jar')