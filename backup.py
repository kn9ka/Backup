#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, zipfile, shutil, time
from zipfile import ZIP_DEFLATED

# for files archive
def doprocess(source_folder, target_zip):
    zipf = zipfile.ZipFile(target_zip, 'w', ZIP_DEFLATED)
    i = 0
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            try:
                zipf.write(os.path.join(subdir, file))
                print("[OK] ", file)
            except:
                print("[ERROR] ", file)
                i += 1

    print("Created", target_zip)
    if i > 0:
        print("\n" + "Some Errors[" + repr(i) + "] were founded" )

# for files copy
def docopy(source_folder, target_folder):
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            print(os.path.join(subdir, file))
            shutil.copy2(os.path.join(subdir, file), target_folder)


''' 

# EXAMPLE
if __name__ == '__main__':
    print("\n" + '[' + time.strftime('%d%m%Y') + ']' + "\n" + "Starting execution..")
    source_folder = 'path/to/start-folder'
    target_zip = 'path/to/destination-folder'
    doprocess(source_folder, target_zip) 
    
'''
