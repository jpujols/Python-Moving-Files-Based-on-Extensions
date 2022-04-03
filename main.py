import glob
import shutil

from_dir = '/home/username/Downloads'
to_dir = {
    '/home/username/Pictures': ['jpg','png','gif'],
    '/home/username/Documents': ['doc','docx','pdf','xls']
}
for destination, extensions in to_dir.items():
    for ext in extensions:
        for file in glob.glob(from_dir + '*.' + ext):
            print(file)
            shutil.move(file, to_dir)