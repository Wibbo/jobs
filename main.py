import urllib.request
from bs4 import BeautifulSoup
from searchterm import SearchTerm
from AppConfig import AppConfig
import sys
import csv

searchItems = []


def read_config_file(ini_file_name):
    """ Read parameters from the application config file.
    :param ini_file_name: The name of the ini file to read.
    :return: An object that represents the configuration parameters.
    """
    try:  # Changed something.
        params = AppConfig(ini_file_name)
    except FileNotFoundError as ff:
        print(ff)
        sys.exit()
    except KeyError as ke:
        print(f'Cannot find {ke} parameter in the ini file, The application cannot continue.')
        sys.exit()
    except ValueError as ve:
        print(ve)
        sys.exit()
    except Exception as e:  # noqa
        print(f'An unexpected error has occurred, The application cannot continue.')
        sys.exit()
    else:
        return params


def add_verticals(search):
    """ Looks at the items in the general section and stores the values for each search.
    :param search:
    :return:
    """
    generalTable = soup.find('table', id='Skill-Set-General')
    generalRows = generalTable.find_all('tr')
    index = 0

    for tr in generalRows:
        td = tr.find_all('td')

        if index > len(generalRows) - 1:
            break

        if len(td) > 2:
            if index > len(search.verticals) - 1:
                break

            search.verticals[index] = td[2].text
            index += 1


def get_job_trend(soup_ref):
    """ Retrieves the url for a job trending graph on the search results page.
    :param soup_ref: A reference to the related BeautifulSoup object.
    :return: A string containing the url for the job trend image.
    """
    rootUrl = 'https://www.itjobswatch.co.uk'
    trendDiv = soup_ref.find('div', class_='trendChart')
    childImg = trendDiv.findChildren('img', recursive=False)

    return rootUrl + childImg[0]['src']


def add_summary_details(soup_ref, searchObject):
    summaryTable = soup_ref.find('table', class_='summary')
    summaryRows = summaryTable.find_all('tr')

    cols = summaryRows[0].find_all('th', class_='title')
    searchObject.name = cols[0].contents[0]

    cols = summaryRows[4].find_all('td')
    searchObject.jobCount = cols[1].text

    cols = summaryRows[5].find_all('td')
    searchObject.jobPercent = cols[1].text

    cols = summaryRows[8].find_all('td')
    searchObject.medianSalary = cols[1].text

    cols = summaryRows[9].find_all('td')
    searchObject.salaryChange = cols[1].text


def create_entry_values(tech_search):
    entries = [tech_search.name, tech_search.jobPercent, tech_search.jobCount,
               tech_search.medianSalary, tech_search.salaryChange]

    for i in range(cfg.max_sectors):
        entries.append(tech_search.verticals[i])

    entries.append(tech_search.jobImageUrl)

    return entries


cfg = read_config_file('search.ini')

for url in cfg.urlList:
    page = urllib.request.urlopen(url[1].replace(' ', '%20'))
    soup = BeautifulSoup(page, 'html.parser')

    searchTerm = SearchTerm(cfg.max_sectors)

    # Get required details from it jobs watch site & store them.
    add_verticals(searchTerm)
    searchTerm.jobImageUrl = get_job_trend(soup)
    add_summary_details(soup, searchTerm)

    searchItems.append(searchTerm)

with open('results.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Technology', 'Job count', 'Job %', 'Salary', 'Salary change', 'Sector 1', 'Sector 2', 'Sector 3', 'Sector 4', 'Sector 5', 'Sector 6', 'Job trend graph'])

    for search in searchItems:
        search_entries = create_entry_values(search)
        writer.writerow(search_entries)












#for tr in summaryRows:
#    td = tr.find_all('td')
#    cols = [i.text for i in td]

pass

