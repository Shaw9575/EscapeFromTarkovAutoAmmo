from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QCheckBox, QPushButton, QTextEdit
from PyQt5.QtCore import Qt, pyqtSignal, QObject
import Shell

class Stream(QObject):
    """Redirects console output to text widget."""
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))

class c_demo(QWidget):
    def __init__(self, window):
        # 1. 简单的绘制一个窗口
        super().__init__(window)
        window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        window.setAttribute(Qt.WA_TranslucentBackground)
        window.setWindowTitle('QCheckBox')
        window.setGeometry(300, 300, 300, 250)

        sys.stdout = Stream(newText=self.onUpdateText)

        #子弹列表
        self.cb1 = QCheckBox('7N31', window)
        self.cb1.move(20, 20)
        self.cb1.setStyleSheet("color:yellow")
        self.cb1.toggle()
        self.cb1.setChecked(False)

        self.cb2 = QCheckBox('995', window)
        self.cb2.move(20, 35)
        self.cb2.setStyleSheet("color:yellow")
        self.cb2.toggle()
        self.cb2.setChecked(False)

        self.cb3 = QCheckBox('855A1', window)
        self.cb3.move(20, 50)
        self.cb3.setStyleSheet("color:yellow")
        self.cb3.toggle()
        self.cb3.setChecked(False)

        self.cb4 = QCheckBox('AP SX', window)
        self.cb4.move(20, 65)
        self.cb4.setStyleSheet("color:yellow")
        self.cb4.toggle()
        self.cb4.setChecked(False)

        self.cb5 = QCheckBox('M61', window)
        self.cb5.move(20, 80)
        self.cb5.setStyleSheet("color:yellow")
        self.cb5.toggle()
        self.cb5.setChecked(False)

        self.cb6 = QCheckBox('SS190', window)
        self.cb6.move(20, 95)
        self.cb6.setStyleSheet("color:yellow")
        self.cb6.toggle()
        self.cb6.setChecked(False)

        self.cb7 = QCheckBox('M381', window)
        self.cb7.move(100, 20)
        self.cb7.setStyleSheet("color:yellow")
        self.cb7.toggle()
        self.cb7.setChecked(False)

        self.cb8 = QCheckBox('BS', window)
        self.cb8.move(100, 35)
        self.cb8.setStyleSheet("color:yellow")
        self.cb8.toggle()
        self.cb8.setChecked(False)

        self.cb9 = QCheckBox('Lab White', window)
        self.cb9.move(100, 50)
        self.cb9.setStyleSheet("color:yellow")
        self.cb9.toggle()
        self.cb9.setChecked(False)

        #自动购买按钮
        self.b1 = QPushButton("Start", window)
        self.b1.move(20, 110)
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b1.clicked.connect(self.startShell)

        #清楚勾选按钮
        self.b1 = QPushButton("ClearAll", window)
        self.b1.move(20, 130)
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b1.clicked.connect(self.clearAll)

        self.process = QTextEdit(self, readOnly=True)
        self.process.setStyleSheet("color:yellow;background:transparent;border-width:0;border-style:outset")
        self.process.ensureCursorVisible()
        self.process.setLineWrapColumnOrWidth(350)
        self.process.setLineWrapMode(QTextEdit.FixedPixelWidth)
        self.process.setFixedWidth(350)
        self.process.setFixedHeight(200)
        self.process.move(20, 160)
        print("开始前请务必将跳蚤市场调整为仅商人!\n否则后果自负\n移动鼠标即可退出")

    def clearAll(self):
        self.cb1.setChecked(False)
        self.cb2.setChecked(False)
        self.cb3.setChecked(False)
        self.cb4.setChecked(False)
        self.cb5.setChecked(False)
        self.cb6.setChecked(False)
        self.cb7.setChecked(False)
        self.cb8.setChecked(False)
        self.cb9.setChecked(False)


    def startShell(self):
        flags = [self.cb1.checkState(), self.cb2.checkState(), self.cb3.checkState(), self.cb4.checkState(),
                self.cb5.checkState(), self.cb6.checkState(), self.cb7.checkState(), self.cb8.checkState(), self.cb9.checkState()]
        AutoAmmo = Shell.TarkovShell()
        AutoAmmo.listener(flags)

    def onUpdateText(self, text):
        """Write console output to text widget."""
        cursor = self.process.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.process.setTextCursor(cursor)
        self.process.ensureCursorVisible()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Dialog_main = QDialog()
    ui = c_demo(Dialog_main)
    Dialog_main.show()
    sys.exit(app.exec_())

