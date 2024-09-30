{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e40002f-c0d4-4680-8f25-c3e11edede7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "def fetch_gdp_data(url):\n",
    "    \"\"\"\n",
    "    Fetches GDP and population data for cities from a Wikipedia page.\n",
    "\n",
    "    Args:\n",
    "    - url (str): The URL of the Wikipedia page to scrape.\n",
    "\n",
    "    Returns:\n",
    "    - DataFrame: A pandas DataFrame containing the scraped data.\n",
    "    \"\"\"\n",
    "    # Make a request to the specified URL\n",
    "    response = requests.get(url)\n",
    "    # Parse the HTML content of the page\n",
    "    soup = BeautifulSoup(response.text, 'lxml')\n",
    "    # Use pandas to extract tables from the HTML\n",
    "    tables = pd.read_html(str(soup))\n",
    "    # Assuming the target table with GDP and population data is the first one\n",
    "    gdp_table = tables[0]\n",
    "    return gdp_table\n",
    "\n",
    "def save_to_excel(dataframe, filename):\n",
    "    \"\"\"\n",
    "    Saves the given DataFrame to an Excel file.\n",
    "\n",
    "    Args:\n",
    "    - dataframe (DataFrame): The pandas DataFrame to save.\n",
    "    - filename (str): The name of the Excel file to create.\n",
    "    \"\"\"\n",
    "    # Save the DataFrame to an Excel file without the index\n",
    "    dataframe.to_excel(filename, index=False)\n",
    "    print(f'Data saved to {filename}')\n",
    "\n",
    "# URL of the Wikipedia page containing the list of cities by GDP\n",
    "url = \"https://en.wikipedia.org/wiki/List_of_cities_by_GDP_population\"\n",
    "\n",
    "# Fetch the GDP data from the Wikipedia page\n",
    "gdp_data = fetch_gdp_data(url)\n",
    "\n",
    "# The filename for the output Excel file\n",
    "filename = 'cities_by_gdp.xlsx'\n",
    "\n",
    "# Save the scraped data to an Excel file\n",
    "save_to_excel(gdp_data, filename)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
