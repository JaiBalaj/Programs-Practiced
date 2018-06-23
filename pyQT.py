import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.openFileNameDialog()

    def convert_bytes(self,num):
        """
        this function will convert bytes to MB.... GB... etc
        """
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0

    def file_size(self,file_path):
        if os.path.isfile(file_path):
            file_info = os.stat(file_path)
            return self.convert_bytes(file_info.st_size)

    def jpeg_res(self,filename):
        with open(filename, 'rb') as img_file:
            print(img_file)
            # height of image (in 2 bytes) is at 164th position
            img_file.seek(163)

            # read the 2 bytes
            a = img_file.read(2)

            # calculate height
            height = (a[0] << 8) + a[1]

            # next 2 bytes is width
            a = img_file.read(2)

            # calculate width
            width = (a[0] << 8) + a[1]

        print("The resolution of the image is", width, "x", height)

    def openFileNameDialog(self):
        from scipy.misc import imread
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Select an Image", "::",
                                                  "Image File (*.PNG *.JPG *.JPEG)", options=options)
        if fileName:
            print(fileName)
            print(self.file_size(fileName))
            print(self.jpeg_res(fileName))
            img=imread(fileName,mode='RGB')
            print(img.shape)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())