import requests
import cloudscraper
import re
import time


def main():
    scraper = cloudscraper.create_scraper()
    f = open('parsed.txt', 'r')
    wrt = open('stats.txt', 'w')
    f.readline()
    step = 0
    for line in f:
        step += 1
        line = line.split(' ')
        response = scraper.get(line[0])
        if response.text.find('404 — Страница не найдена') != -1:
            continue
        if response.text.find('ic_thumbs-up-disabled') != -1:
            continue
        date_list = re.findall(r'20..,', response.text)
        if date_list.count('2022,') == 0:
            continue
        wrt.write(line[0] + ',')
        point = response.text.find("badge-text js-marks-plus")
        likes = response.text[point:point + 100].split('>')[1].split('<')[0]
        wrt.write(str(likes)+',')
        point = response.text.find("follow-count")
        followers = response.text[point:point + 50].split('\"')[1]
        wrt.write(str(followers)+',')
        if response.text.find('Автор отключил возможность просматривать и оставлять отзывы') != -1:
            wrt.write('-1,')
        else:
            point = response.text.find("#ic_bubble-dark")
            comments = response.text[point:point + 800].split('>')[3].split('<')[0]
            comments = ''.join([i for i in comments if i.isdigit() == 1])
            wrt.write(str(comments) + ',')
        point = response.text.find("#ic_bookmark")
        bookmarks = response.text[point:point + 800].split('>')[3].split('<')[0]
        bookmarks = ''.join([i for i in bookmarks if i.isdigit() == 1])
        wrt.write(str(bookmarks) + ';')
        point = response.text.find("badge-with-icon direction")
        direction = response.text[point:point + 800].split('\"')[2].split(' —')[0]
        wrt.write(str(direction) + ',')
        point = response.text.find("badge-with-icon badge-rating")
        rating = response.text[point:point + 800].split('>')[2].split('<')[0]
        wrt.write(rating)
        if step % 10 == 0:
            print(step)
        wrt.write('\n')


if __name__ == '__main__':
    main()
