import json
import streamlit as st
import requests


def fetch_user(list_of_ids, handle):
    http_req = f'https://codeforces.com/api/user.status?handle={handle}&from=1&count=1000000000'
    client = requests.session()
    response = client.get(http_req)
    if not response:
        return

    response_json = json.loads(response.text)
    if response_json['status'] != 'OK':
        return -1

    results = reversed(response_json['result'])
    condensed = {}
    for result in results:
        ids = str(result.get('contestId', '')) + result['problem'].get('index', '')
        if ids in list_of_ids:
            ver = result.get('verdict', '')
            condensed[ids] = 0 if ver == 'OK' else 2 if not ver else 1

    return condensed


if __name__ == '__main__':
    print(fetch_user(['2042C', '808G'], 'Tomerh1307'))

