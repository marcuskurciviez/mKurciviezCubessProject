import sys

import requests
import secrets
from requests.auth import HTTPBasicAuth


def get_wufoo_data()->dict:
    url = "http://mkurciviez.wufoo.com/api/v3/forms/cubess-project-proposal-submission/entries/json"
    response = requests.get(url, auth=HTTPBasicAuth(secrets.wufoo_key, 'pass'))
    print(response.text)

    if response.status_code != 200:
        print(f"Data retrieval failed, response code: {response.status_code} with the error message: {response.reason}")
        sys.exit(-1)
    json_repsonse = response.json()
    return json_repsonse


def write_data_to_file():
    data = get_wufoo_data()['Entries']

    with open("data.txt", "w") as outfile:
        for item in data:
            for key, value in item.items():
                outfile.write(f"{key}:{value}\n")

            print_file("wufoo_data.txt")


def print_file(file_name):
    with open(file_name) as f:
        print(f.read())


if __name__ == '__main__':
    write_data_to_file()
