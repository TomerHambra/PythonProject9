import requests
from bs4 import BeautifulSoup
from enum import Enum


class Status(Enum):
    AC = 0
    AT = 1
    NAT = 2

BASE_URL = 'https://cses.fi/problemset/user/'

LOGIN_URL = 'https://cses.fi/login'


def get_task_from_url(url):
    return int(url.rstrip('/').split('/')[-1])


def get_user_info(user_id):
    client = requests.session()
    request1 = client.get(LOGIN_URL)
    soup2 = BeautifulSoup(request1.text, 'lxml')
    csrf = soup2.select('input[name="csrf_token"]')[0]['value']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': LOGIN_URL
    }
    request2 = client.post(LOGIN_URL, data={'csrf_token': csrf, 'nick': 'subclient1307', 'pass': 'Toto2000!'}, headers=headers)
    # print(request2.text)
    url = BASE_URL + user_id
    req = client.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    result = {}
    ac = soup.select('td > a.full')
    at = soup.select('td > a.zero')
    nat = soup.select("td > a[class='task-score icon']")
    for task in ac:
        tid = get_task_from_url(task['href'])
        result[tid] = Status.AC
    for task in at:
        tid = get_task_from_url(task['href'])
        result[tid] = Status.AT
    for task in nat:
        tid = get_task_from_url(task['href'])
        result[tid] = Status.NAT
    return result


