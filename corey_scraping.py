from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scraping.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Headline", 'Summary', 'Video_Link'])
for article in soup.find_all('article'):
    headline = article.h2.a.text
    summary = article.find('div', class_='entry-content').p.text
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    csv_writer.writerow([headline, summary, yt_link])
csv_file.close()
