import codecs
import re
import sys
import urllib.request
import emoji
from _datetime import datetime


from PyQt5.QtWidgets import (QWidget, QPushButton,QLabel,
                             QHBoxLayout, QVBoxLayout, QApplication, QTextEdit)

ver = "1.0.0"


class UKI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        refresh_button = QPushButton("Refresh ubuntu-ko")
        info_label = QLabel()
        refresh_button.clicked.connect(self.refresh_button_pushed)
        self.output = QTextEdit()
        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()
        h_box3 = QHBoxLayout()
        h_box1.addWidget(refresh_button)
        h_box2.addWidget(info_label)
        h_box3.addWidget(self.output)
        v_box = QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        self.setLayout(v_box)
        self.setGeometry(1400, 300, 500, 700)
        self.setWindowTitle('Ubuntu-Ko Irc in PyQt')
        self.show()

    def refresh_button_pushed(self):
        today_date = datetime.today().strftime("%Y/%m/%d")
        u = ("https://irclogs.ubuntu.com/" + today_date + "/%23ubuntu-ko.txt")
        down = urllib.request.urlretrieve(u, "ubuntu-ko.txt")
        f = codecs.open("ubuntu-ko.txt", "r", "utf-8")
        text = f.read()
        filter_slack = emoji.emojize(re.sub("<bridgebot>", "[Slack]", text))
        self.output.setText(filter_slack)


app = QApplication(sys.argv)
ex = UKI()
sys.exit(app.exec_())
