import os


PATH = 'COMP/dress'

f= open('labels.txt',"w+")

for folder in os.listdir(PATH):
    f.write(folder)
    f.write('\n')
f.close()
