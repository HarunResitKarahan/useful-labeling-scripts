import os

currentdir = os.getcwd()
for key in os.listdir():
    if os.path.splitext(os.path.basename(key))[1] == '':
        os.chdir(os.getcwd() + r'\\' + os.path.basename(key))
        for item in os.listdir():
            if os.path.splitext(os.path.basename(item))[1] == '.txt':
                os.remove(os.path.basename(item))

        os.chdir(currentdir)