import os
from shutil import copyfile


PATH = 'COMP/dress'
LABEL_PATH = 'IMG_LABELS/'
DATA_PATH = 'DATA/'
for folder in os.listdir(PATH):
    IMG_PATH = os.path.join(PATH, folder)
    for filename in os.listdir(IMG_PATH):
        source = os.path.join(IMG_PATH, filename)
        destination = os.path.join(DATA_PATH, filename)
        copyfile(source, destination)
        label_name = filename + '.txt'
        label_destination = os.path.join(LABEL_PATH, label_name)
        f= open(label_destination,"w+")
        f.write(folder)
        f.close()
