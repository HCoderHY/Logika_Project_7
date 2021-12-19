# from PIL import Image
# from PIL import ImageFilter
# from PIL import ImageEnhance
# with Image.open('original.jpg') as pic_original:
# 	print(pic_original.size)
# 	print(pic_original.format)
# 	print(pic_original.mode)
# 	pic_original.show()
# 	pic_gray = pic_original.convert('L')
# 	pic_gray.save("gray.jpg")
# 	print("\nGray Image\n")
# 	print(pic_gray.size)
# 	print(pic_gray.format)
# 	print(pic_gray.mode)
# 	pic_gray.show()
# 	pic_blur = pic_original.filter(ImageFilter.BLUR)
# 	pic_blur.save("blur.jpg")
# 	print("\nBlur Image"\n)
# 	print(pic_blur.size)
# 	print(pic_blur.format)
# 	print(pic_blur.mode)
# 	pic_blur.show()
# 	print("\nMirrow Image\n")
# 	pic_mirrow = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
# 	pic_mirrow.save("pic_mirrow.jpg")
# 	pic_mirrow.show()
import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
app = QApplication([])
win = QWidget()
win.setWindowTitle('Eazy Editor')
win.resize(700,500)
lb_image = QLabel('Image')
btn_dir = QPushButton('Folder')
btn_left = QPushButton('Left')
btn_right = QPushButton('Right')
btn_mirror = QPushButton('Mirror')
btn_sharp = QPushButton('Sharp')
btn_bw = QPushButton('B/W')
lw_files = QListWidget()
row = QHBoxLayout()
main_layout = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()
col_1.addWidget(btn_dir)
col_1.addWidget(lw_files)
row.addWidget(btn_left)
row.addWidget(btn_right)
row.addWidget(btn_mirror)
row.addWidget(btn_sharp)
row.addWidget(btn_bw)
col_2.addWidget(lb_image)
col_2.addLayout(row)
main_layout.addLayout(col_1, 1)
main_layout.addLayout(col_2, 4)
workdir = ''
def chooseWorkDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def filter(files, extensions):
    results = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                results.append(file)
    return results
def showFileNamesList():
    chooseWorkDir()
    extensions = ['.jpg', '.png', '.jpeg', '.gif', '.bmp', '.webp']
    filenames = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)
btn_dir.clicked.connect(showFileNamesList)
win.setLayout(main_layout)
win.show()
app.exec_()
