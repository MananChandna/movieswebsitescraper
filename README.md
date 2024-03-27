# Movieswebsitescraper
![image](https://github.com/MananChandna/movieswebsitescraper/assets/139998502/95b3fb30-92a4-419f-bc48-23949a1db613)


# Web Scraper Description

## Imports:
The script imports necessary libraries such as `requests`, `os`, `sys`, `datetime`, `pandas`, and `HTML` from `requests_html`.

## url_to_text Function:
This function takes a URL as input, retrieves the HTML content from that URL using the `requests` library, and returns the HTML content as text. Optionally, it can save the HTML content to a file.

## parse_and_extract Function:
This function parses the HTML content of a given URL using `requests_html`, extracts the table containing box office data, and converts it into a Pandas DataFrame. It then saves this DataFrame as a CSV file in a directory named "data".

## run Function:
This function orchestrates the scraping process. It takes two optional arguments: `start_year` and `years_ago`. It iterates over the years starting from `start_year` going back for `years_ago` years. For each year, it constructs the URL for that year's box office data, calls `parse_and_extract` to scrape and save the data, and prints whether the process for a particular year is finished or if the year doesn't exist.

## Main Block:
In the main block, it reads command-line arguments to determine the starting year and how many years to go back. Then, it calls the `run` function with these arguments.

<h2>Contact</h2>
    <p>If you have any questions or suggestions regarding this project, feel free to contact me via <a href="https://www.linkedin.com/in/manan-chandna-697588257/">LinkedIn</a>.</p>
