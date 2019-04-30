import requests
from bs4 import BeautifulSoup
import re
import os
import urlmanager


def mkdir(path):
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False


if __name__ == "__main__":
    container = urlmanager.Urlmanager("https://en.wikipedia.org/wiki/Biological_engineering")
    pre = "https://en.wikipedia.org"
    # print(container.get_url())
    # print(container.get_len())
    deep = 0
    regex = re.compile(r'^(/wiki/)((?!:).)*$')
    s = requests.session()
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/73.0.3683.86 Safari/537.36 "
    }

    # soup = s.get(container.get_url(), headers=header)
    # soup = BeautifulSoup(soup.text, 'lxml')
    # for link in soup.find('div', {'id': 'bodyContent'}).find_all('a', href=regex):
    #     if 'href' in link.attrs:
    #         print(link.attrs['href'])

    while deep < 2:
        iter_len = container.get_len()
        for i in range(iter_len):
            url = container.get_url()
            print(url)
            print(container.get_len())
            soup = s.get(url, headers=header)
            soup = BeautifulSoup(soup.text, 'lxml')
            title = list(soup.select("#firstHeading"))
            a = soup.find('div', {'id': 'bodyContent'}).find_all('a', href=regex)
            p = soup.find_all('p')
            for t in title:
                t = t.text
                if mkdir("./" + t):
                    file_main = open(t + "/" + t + ".txt", 'w+', encoding='utf-8')
                    for p_text in p:
                        file_main.write(p_text.text + "\n")
                    sub_title = soup.find_all('h2')
                    for j in sub_title:
                        m = j.text
                        file = open(t + "/" + m + ".txt", 'w+', encoding='utf-8')
                        # print(m)
                        p1 = j.find_next_siblings()
                        for k in p1:
                            if k.name != 'h2':
                                # print(k.text)
                                file.write(k.text + "\n")
                            else:
                                break
                        file.close()
                    file_main.close()
            for link in a:
                if 'href' in link.attrs:
                    new_url = pre + link.attrs['href']
                    print(new_url)
                    container.add_url(new_url)
            container.del_url(url)
        deep += 1
        print(deep)
