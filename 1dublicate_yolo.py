from msvcrt import getwch
import os

value = "0 0.500000 0.500000 0.990000 0.990000"

currentdir = os.getcwd()
for key in os.listdir():
    if os.path.splitext(os.path.basename(key))[1] == '':
        os.chdir(os.getcwd() + r'\\' + os.path.basename(key))

        for item in os.listdir():
            # print(os.path.basename(key))
            with open('classes' + '.txt', 'w') as f:
                f.write(os.path.basename(key))
            if os.path.splitext(os.path.basename(item))[1] == '.png':
                with open(os.path.splitext(os.path.basename(item))[0] + '.txt', 'w') as f:
                    f.write(value)
        os.chdir(currentdir)