import os

for di, sdi, fi in os.walk('c:\\'):
	print('Folder: ' + di)
	print('Subfolders in ' + di + ': ' + str(sdi))
	print('Files: ' + str(fi))
	print()
            
