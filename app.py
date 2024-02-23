from flask import Flask, render_template, request
import requests
import os   
import sys
import datetime
import pandas as pd
from requests_html import HTML

app = Flask(__name__)
base_dir = os.path.dirname(__file__)

def url_to_text(url, filename="world.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world-{year}.html", "w", encoding="utf-8") as f:
                f.write(html_text)
        return html_text
    return None

def parse_and_extract(url, name='2024'):
    html_text = url_to_text(url)
    if html_text is None:
        return False
    r_html = HTML(html=html_text)
    table_class = ".imdb-scroll-table "
    r_table = r_html.find(table_class)
    table_data = []
    header_name = []
    if len(r_table) == 0:
        return False
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_row = rows[0]
    header_col = header_row.find('th')
    header_name = [x.text for x in header_col]
    for row in rows[1:]:
        cols = row.find("td")
        row_data = [col.text for col in cols]
        table_data.append(row_data)
    df = pd.DataFrame(table_data, columns=header_name)
    path = os.path.join(base_dir, 'data')
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join('data', f'{name}.csv')
    df.to_csv(filepath, index=False)
    return True

def run(start_year=None, years_ago=0):
    if start_year is None:
        now = datetime.datetime.now()
        start_year = now.year
    for i in range(0, years_ago+1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}/"
        finished = parse_and_extract(url, name=start_year)
        if finished:
            print(f"Finished {start_year}")
        else:
            print(f"{start_year} doesn't exist")
        start_year -= 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    start_year = request.form.get('start_year')
    years_ago = request.form.get('years_ago')
    run(start_year=int(start_year), years_ago=int(years_ago))
    return 'Scraping completed successfully!'

if __name__ == "__main__":
    app.run(debug=True)
