import os

PATH = 'COMP/val'
total = 0
for folder in os.listdir(PATH):
	print(folder)
	print(len([name for name in os.listdir(os.path.join(PATH,folder))]))
	total = total + len([name for name in os.listdir(os.path.join(PATH,folder))])
print(total)

