import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Fetch data from the web
url = 'https://www.tiobe.com/tiobe-index/'
response = requests.get(url)
html_content = response.content

# Step 2: Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table', {'class': 'table table-striped table-top20'})

# Extracting the data
data = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    rank = cols[0].text.strip()
    language = cols[3].text.strip()
    rating = cols[4].text.strip()
    data.append([rank, language, rating])

# Step 3: Process and analyze the data
df = pd.DataFrame(data, columns=['Rank', 'Language', 'Rating'])
df['Rating'] = df['Rating'].str.replace('%', '').astype(float)

# Step 4: Visualize the results
plt.figure(figsize=(10, 6))
plt.bar(df['Language'], df['Rating'], color='skyblue')
plt.xlabel('Programming Language')
plt.ylabel('Popularity Rating (%)')
plt.title('Top Programming Languages (TIOBE Index)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the plot as an image
plt.savefig('programming_languages_popularity.png')

# Show the plot
plt.show()
