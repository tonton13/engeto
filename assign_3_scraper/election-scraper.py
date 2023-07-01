"""
election-scrapper.py: a third project for Engento Online Python Academy.
author: Anton Chirkov
email: tonton.chirkov@gmail.com
discord: TonTon#9968
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys


def scrape_election(web_link, output_file):
    df = pd.DataFrame()
    codes, sub_web_links, locations = get_locations_and_links(web_link)
    df["code"] = codes
    df["location"] = locations
    registered = []
    envelopes = []
    valid = []
    sub_web_link = sub_web_links
    party_data = []
    links_appear_data = []
    scraper_first_run = True
    for web_link in sub_web_link:
        voters, given_e, correct_e, parties, link_data = get_data_from_sub_link(web_link, scraper_first_run)
        registered.append(voters)
        envelopes.append(given_e)
        valid.append(correct_e)
        if scraper_first_run:
            party_data = parties
        scraper_first_run = False
        links_appear_data.append(link_data)
    df["registered"] = registered
    df["envelopes"] = envelopes
    df["valid"] = valid
    result_list = {party: [vote[i] for vote in links_appear_data] for i, party in enumerate(party_data)}
    df_2 = pd.DataFrame(result_list)
    frames = [df, df_2]
    frames_result = pd.concat(frames, axis=1)
    frames_result.set_index("code", inplace=True)
    frames_result.to_csv(output_file)


def get_locations_and_links(web_link):
    code = []
    sub_web_links = []
    locations = []
    request_result = requests.get(web_link)
    page_content = request_result.text
    soup = BeautifulSoup(page_content, 'html.parser')
    url = web_link[:web_link.rfind('/')]
    for table in soup.find_all('td'):
        if table.get('class') == ["cislo"]:
            for a_link in table.find_all('a'):
                sub_web_links.append(url + "/" + a_link.get('href'))
                code.append(a_link.text)
        if table.get('class') == ["overflow_name"]:
            locations.append(table.text)
    return code, sub_web_links, locations


def get_data_from_sub_link(web_link, is_first_time_start):
    parties_names = []
    link_data = []
    amount_of_voters = None
    envelopes_given = None
    correct_envelopes = None
    request_result = requests.get(web_link)
    page_content = request_result.text
    soup = BeautifulSoup(page_content, 'html.parser')
    headers_for_voters = ['sa2']
    headers_for_envelopes_given = ['sa3']
    headers_for_correct_envelopes = ['sa5']
    headers_for_valid_votes = ['t1sa2', 't1sb3']
    headers_for_valid_votes_2 = ['t2sa2', 't2sb3']
    for element in soup.find_all('td'):
        if element.get('class') == ["cislo"] and (element.get('headers') == headers_for_voters):
            number = int("".join([char for char in element.text if char.isdigit()]))
            amount_of_voters = number
        if element.get('class') == ["cislo"] and (element.get('headers') == headers_for_envelopes_given):
            number = int("".join([char for char in element.text if char.isdigit()]))
            envelopes_given = number
        if element.get('class') == ["cislo"] and (element.get('headers') == headers_for_correct_envelopes):
            number = int("".join([char for char in element.text if char.isdigit()]))
            correct_envelopes = number
        if element.get('class') == ["cislo"] and (element.get('headers') == headers_for_valid_votes):
            number = int("".join([char for char in element.text if char.isdigit()]))
            link_data.append(number)
        if element.get('class') == ["cislo"] and (element.get('headers') == headers_for_valid_votes_2):
            number = int("".join([char for char in element.text if char.isdigit()]))
            link_data.append(number)
        if is_first_time_start and element.get('class') == ['overflow_name']:
            parties_names.append(element.text)
    return amount_of_voters, envelopes_given, correct_envelopes, parties_names, link_data


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("You need to input 2 arguments: web link and output file")
        sys.exit(1)
    scrape_election(sys.argv[1], sys.argv[2])

