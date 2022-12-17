import requests
from bs4 import BeautifulSoup
import time

URL = 'https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/list/?id=BAC-BUDJ-O-090300'


def get_response():
    while True:
        try:
            response = requests.get(URL)
            response.raise_for_status()
            return response

        except Exception as Err:
            print(f'{Err}. Запрос будет повторен через 5 секунд')
            time.sleep(5)


def main():
    response = get_response()
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find('table', class_='data table-ranged with-hover sortable js-fixed js-table-data')
    lines = quotes
    table = []
    acc = 0
    for line in lines:
        table.append([])
        datas = line.find_all('td')
        for data in datas:
            table[acc].append(str(data.content))
        acc+=1
        print("KEK")

    print("OK")


if __name__ == "__main__":
    main()