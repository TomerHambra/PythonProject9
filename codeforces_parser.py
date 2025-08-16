import json
import streamlit as st
import requests
from parser import Status


def fetch_user(list_of_ids, handle):
    if handle == None:
        return -1
    http_req = f'https://codeforces.com/api/user.status?handle={handle}&from=1&count=1000000000'
    client = requests.session()
    response = client.get(http_req)
    if not response:
        return -2
    response_json = json.loads(response.text)
    if response_json['status'] != 'OK':
        return -3
    results = reversed(response_json['result'])

    condensed = {}
    for result in results:
        ids = str(result.get('contestId', '')) + result['problem'].get('index', '')

        if ids in list_of_ids:
            ver = result.get('verdict', '')
            condensed[ids] = Status.AC if ver == 'OK' else Status.NAT if not ver else Status.AT
    # print(condensed)
    for id in list_of_ids:
        if id not in condensed:
            condensed[id] = Status.NAT
    # print(condensed)
    return condensed


if __name__ == '__main__':
    print(fetch_user(['2042C', '808G'], 'Tomerh1307'))

