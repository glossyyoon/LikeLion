import telegram, requests, os
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

now = datetime.datetime.now()
bot = telegram.Bot(token = '1224505639:AAE7k5HzmeamkFL8HtDC-3G86YYzK_8DyhQ')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def telegram_bot():
    url = 'https://algumon.com/'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    name = soup.select('div.post-group > div.product-body.clearfix > div > p:nth-child(2) > span > a')
    latest = name[0].text.strip()
    print(latest)
    latest_link = "https://algumon.com"+str(name[0].attrs['href'])
    with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+', encoding="utf-8") as f_read:
        before = f_read.readline()
        if before != latest:
            bot.sendMessage(chat_id =1211989675, text = "다른데요?")
        else:
            bot.sendMessage(chat_id = 1211989675, text = latest_link)
        f_read.close()

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+', encoding="utf-8") as f_write:
        f_write.write(latest)
        f_write.close()



sched = BlockingScheduler()
telegram_bot()
sched.add_job(telegram_bot, 'interval', seconds=10)
sched.start()