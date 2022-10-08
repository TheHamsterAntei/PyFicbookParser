import requests
import cloudscraper
import re
import time


session = requests.Session()

session.proxies = {
    'http:': '185.162.230.84:80',
    'https': '20.111.54.16:8123'
}

def main():
    scraper = cloudscraper.create_scraper()
    count = 0
    f = open('parsed.txt', 'r')
    for line in f:
        max_id = int(line)
        break
    content = f.read()
    f.close()
    f = open('parsed.txt', 'w')
    f.write('12500000\n')
    f.write(content)
    for i in range(max_id, 12500000):
        time.sleep(0.01)
        print(str(12500000 - i) + " осталось")
        response = scraper.get("https://ficbook.net/readfic/" + str(i))
        if response.text.find('404 — Страница не найдена') != -1:
            continue
        date_list = re.findall(r'20..,', response.text)
        if date_list.count('2022,') == 0:
            continue
        likes = response.text.find("badge-text js-marks-plus")
        likes_num = response.text[likes:likes+100].split('>')[1].split('<')[0]
        f.write("https://ficbook.net/readfic/" + str(i) + " : " + str(likes_num) + " лайков\n")


if __name__ == '__main__':
    main()
