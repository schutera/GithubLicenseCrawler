
# ///////////////////////GITHUBLICENSECRAWLER

# This script is intended to crawl license information of repositories through the GitHub API.
# Taking a text file with requirements.txt format
# the script will return a csv with the associated license information.
# Contact: mark.schutera@gmail.com

import csv
import requests
import time

URL = "https://api.github.com/search/repositories?q="  # The basic URL to use the GitHub API for repo search
QUERY = "+in:name"  # The query for repository name.

DELAY_BETWEEN_QUERIES = 10  # The time to wait between queries to GitHub (to avoid be banned)
INPUT_CSV_FILE = "./requirements.txt"  # Path to the CSV file read as an input with the repository requirements
OUTPUT_CSV_FILE = "./licenses.csv"  # Path to the CSV file generated as output

# Input CSV file which will contain information about repositories
csv_input_file = open(INPUT_CSV_FILE, newline='')
repositories = csv.reader(csv_input_file, delimiter=',')

# Output CSV file which will contain information about licenses
csv_output_file = open(OUTPUT_CSV_FILE, 'w', newline='')
licenses = csv.writer(csv_output_file, delimiter=',')

for repos in repositories:
    for repo in repos:
        repo, _, _ = repo.partition('==')
        print('Assessing: ', repo)
        url = URL + repo + QUERY
        print(url)
        try:
            response = requests.get(url)
            response_dict = response.json()
            # Delay so you do not get banned.
            time.sleep(DELAY_BETWEEN_QUERIES)
            # take first repository of the query and check whether the names are the same
            if repo.lower() == response_dict['items'][0]['name'].lower():
                repo_url = response_dict['items'][0]['html_url']
                license_name = response_dict['items'][0]['license']['name']
                license_url = response_dict['items'][0]['license']['url']
                license_entry = [repo, repo_url, license_name, license_url]
                licenses.writerow(license_entry)
                # print(license_entry)
                print('.. done')
            else:
                license_entry = [repo, '_', '_', '_']
                licenses.writerow(license_entry)
                print('Warning - Something went wrong when accessing repository: ', repo)
        except Exception as e:
            license_entry = [repo, '_', '_', '_']
            licenses.writerow(license_entry)
            print('Warning - Something went wrong when requesting: ', repo)
            print(e)

licenses.writerow(['This file has been generated with licenseFinder v0.1 - Contact: mark.schutera@gmail.com'])
