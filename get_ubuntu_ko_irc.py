"""
irclogs.ubuntu.com 에 호스팅된 ubuntu-ko 채널을 바로 볼 수 있습니다.
AUTHOR : github.com/minwook-shin
VERSION : 1.1.1
LICENSE : GPL 3
"""
from _datetime import datetime
import time
import codecs
import urllib.request
import re

print("본 프로그램은 주기적으로 ubuntu-ko IRC 로그를 가지고오는 프로그램입니다.")
today_date = datetime.today().strftime("%Y/%m/%d")
u = ("https://irclogs.ubuntu.com/" + today_date + "/%23ubuntu-ko.txt")
print("오늘은", u, "에서 가져옵니다.")
times = int(input("채팅을 재갱신할 시간을 선택해주세요(초):"))
while True:
    down = urllib.request.urlretrieve(u, "ubuntu-ko.txt")
    f = codecs.open("ubuntu-ko.txt", "r", "utf-8")
    text = f.read()
    filter_text = re.sub("<bridgebot1>", "[S]", text)
    print(filter_text)
    time.sleep(times)
