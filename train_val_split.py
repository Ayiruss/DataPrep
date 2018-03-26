import os
import os.path
from shutil import copyfile

def createDirectory(path):
    if not os.path.exists(path):
        os.mkdir(path)


main_dir = 'COMP/all'
train_percent = 70
valid_percent = 30
test_percent = 0

if (int(train_percent + valid_percent + test_percent) > 100):
    print("The Split between train-valid-test is not proper")
    print(quit)

CENT = 100

TRAIN_LMT = train_percent / CENT
VALID_LMT = valid_percent / CENT
TEST_LMT = test_percent / CENT

train_dir = main_dir.replace("/all", "/train")
val_dir = main_dir.replace("/all", "/val")
test_dir = main_dir.replace("/all", "/test")

createDirectory(train_dir)
createDirectory(test_dir)
createDirectory(val_dir)

#main_dir = os.path.join(main_dir, 'clean_amzon')

i = 0

for class_name in os.listdir(main_dir):
    if class_name == ".DS_Store":
        continue
    src_dir = os.path.join(main_dir, class_name)
    NOF = len(os.listdir(src_dir))
    print(class_name , ' - ', NOF)
    print(int((TRAIN_LMT) * NOF))
    dest = None
    i = 0
    if class_name not in ('test', 'train', 'valid'):
        createDirectory(os.path.join(test_dir, class_name))
        createDirectory(os.path.join(train_dir, class_name))
        createDirectory(os.path.join(val_dir, class_name))
        for file_name in os.listdir(src_dir):

            if i > int((TRAIN_LMT) * NOF):
                dest = os.path.join(val_dir, class_name, file_name)
            else:
                dest = os.path.join(train_dir, class_name, file_name)

            src = os.path.join(src_dir, file_name)

            copyfile(src, dest)

            i = i + 1

print('Symlink Generation Completed')
