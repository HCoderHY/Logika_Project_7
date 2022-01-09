import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
app = QApplication([])
win = QWidget()
win.setWindowTitle('Eazy Editor')
win.resize(1000,800)
lb_image = QLabel('Image')
btn_dir = QPushButton('Folder')
btn_left = QPushButton('Left')
btn_right = QPushButton('Right')
btn_mirror = QPushButton('Mirror')
btn_blur = QPushButton('Blur')
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
row.addWidget(btn_blur)
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
class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)
    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_m(self):
        self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    def showImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w,h,Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()
workimage = ImageProcessor()
def showChosenImage(self):
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)
btn_bw.clicked.connect(workimage.do_bw)
btn_mirror.clicked.connect(workimage.do_m)
btn_blur.clicked.connect(workimage.do_blur)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
lw_files.currentRowChanged.connect(showChosenImage)
win.setLayout(main_layout)
win.show()
app.exec_()
