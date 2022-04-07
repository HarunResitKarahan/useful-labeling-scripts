import os
import shutil


currentdir = os.getcwd()
for key in os.listdir():
    if os.path.splitext(os.path.basename(key))[1] == '':
        os.chdir(os.getcwd() + '\\' + os.path.basename(key) + '\XML')
        supdir = currentdir + "\\" + os.path.basename(key)
        print(supdir)
        for item in os.listdir():
            # print(os.getcwd() + '\\' + item)
            shutil.copy(os.getcwd() + r'\\' + item, supdir)

        os.chdir(currentdir)