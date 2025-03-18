import zipfile
import shutil

# CREATE ZIP FILE
# my_zip = zipfile.ZipFile('file_compressed.zip', 'w')

# ADD CONTENT INTO ZIP FILE
# my_zip.write('text_a.txt')
# my_zip.write('text_b.txt')

# CLOSE ZIP
# my_zip.close()

# EXTRACT FILES FROM A ZIP
zip_open = zipfile.ZipFile('file_compressed.zip', 'r')
zip_open.extractall()

# SHUTIL
dir_origin = '/home/mrrobot/Documents/PycharmProjects/PythonProject'
file_dest = 'All_Compressed'

# COMPRESS files / directories
# shutil.make_archive(file_dest, 'zip', dir_origin)

# EXTRACT .zip
shutil.unpack_archive('All_Compressed.zip', 'Extraction_Finish', 'zip')








