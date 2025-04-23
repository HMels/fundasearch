# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 12:43:54 2025

@author: Mels
"""

from funda_scraper import FundaScraper  #https://pypi.org/project/funda-scraper/

if __name__ == "__main__": 
    scraper = FundaScraper(
        area="rotterdam", 
        want_to="buy", 
        find_past=False,        # Set to True to find historical data; the default is False.
        page_start=1,           # Indicate which page to start scraping from; the default is 1.
        n_pages=3,              # Indicate how many pages to scrape; the default is 1.
        #min_price=0, 
        max_price=270000,
        min_floor_area=55,
        max_floor_area=85#,
        # sort, 
        # property_type           # Specify the desired property type(s).
    )
    df = scraper.run(raw_data=False, save=True, filepath="test.csv")
    df.head()

