# Movieswebsitescraper
![markus-spiske-Skf7HxARcoc-unsplash](https://github.com/MananChandna/movieswebsitescraper/assets/139998502/98a86aba-d4e4-4280-97fb-e465c59fc419)


<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Web Scraper Description</title>
</head>
<body>

<h2>Imports:</h2>
<p>The script imports necessary libraries such as <code>requests</code>, <code>os</code>, <code>sys</code>, <code>datetime</code>, <code>pandas</code>, and <code>HTML</code> from <code>requests_html</code>.</p>

<h2>url_to_text Function:</h2>
<p>This function takes a URL as input, retrieves the HTML content from that URL using the <code>requests</code> library, and returns the HTML content as text. Optionally, it can save the HTML content to a file.</p>

<h2>parse_and_extract Function:</h2>
<p>This function parses the HTML content of a given URL using <code>requests_html</code>, extracts the table containing box office data, and converts it into a Pandas DataFrame. It then saves this DataFrame as a CSV file in a directory named "data".</p>

<h2>run Function:</h2>
<p>This function orchestrates the scraping process. It takes two optional arguments: <code>start_year</code> and <code>years_ago</code>. It iterates over the years starting from <code>start_year</code> going back for <code>years_ago</code> years. For each year, it constructs the URL for that year's box office data, calls <code>parse_and_extract</code> to scrape and save the data, and prints whether the process for a particular year is finished or if the year doesn't exist.</p>

<h2>Main Block:</h2>
<p>In the main block, it reads command-line arguments to determine the starting year and how many years to go back. Then, it calls the <code>run</code> function with these arguments.</p>

</body>
</html>

