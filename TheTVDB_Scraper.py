import requests
import pandas as pd
from bs4 import BeautifulSoup

# Download contents of the web page
url = 'https://thetvdb.com/series/breaking-bad/seasons/official/5'
data = requests.get(url).text

# Create Beautiful Soup Object
soup = BeautifulSoup(data, 'html.parser')

# Get the right table
tables = soup.find_all('table')
table = soup.find('table', class_='table table-bordered')

# Setup DataFrame
#df = pd.DataFrame(columns=['episode_num', 'episode'])
#episode_num = []
episode = []
data = []
#data.append(episode_num)
data.append(episode)

# Collecting Data
for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')

    if columns:
        #episode_num.append(columns[0].text.strip())
        episode.append(columns[1].text.strip())

df = pd.DataFrame(data).transpose()
#df.columns = ['ep_num', 'ep_name']
df.columns = ['ep_name']
df.to_csv(r'C:\Users\johnp\Downloads\episodes.txt', header=None, index=None, sep='\t', mode='a')



