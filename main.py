import sys
import requests
import secrets
from requests.auth import HTTPBasicAuth
import json


"""This function serves the purpose of the GET request to the wufoo form, using the secrets key to retrieve the 
form submissions. Runs through a if statement for a status code if any errors occur."""
def get_wufoo_data() -> dict:  # comment to test workflow
    url = "http://mkurciviez.wufoo.com/api/v3/forms/cubess-project-proposal-submission/entries/json"
    url = "https://jsantore.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"
    response = requests.get(url, auth=HTTPBasicAuth(secrets.wufoo_key, 'pass'))
    print(response.text)

    if response.status_code != 200:
        print(f"Data retrieval failed, response code: {response.status_code} with the error message: {response.reason}")
        sys.exit(-1)
    json_response = response.json()
    return json_response


"""Function will write data to a file, uses the json library to 'pretty print' the outputted data."""
def write_data_to_file():
    with open("wufoo_data.txt", "w") as outfile:
        text = ["Marcus Kurciviez \n", "Wufoo Form Data \n"]
        outfile.writelines(text)
        json.dump(get_wufoo_data(), outfile, indent=3, sort_keys=True)

def read_data():
    f = open("wufoo_data.txt", "r")
    print(f.readline())

if __name__ == '__main__':
    write_data_to_file()
    read_data()
