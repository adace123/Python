from bs4 import BeautifulSoup
from random import choice
from csv import DictReader, DictWriter
import requests
import os

def scrape_quotes():
    with open('quotes.csv','a', newline='', encoding='utf-8') as quote_file:
        headers = ["Quote", "Author", "URL"]
        writer = DictWriter(quote_file, fieldnames=headers)
        writer.writeheader()
        for i in range(10):
            url = requests.get(f"http://quotes.toscrape.com/page/{i + 1}").text
            soup = BeautifulSoup(url, "html.parser")
            quote_page = soup.select('.quote')
            for quote in quote_page:
                writer.writerow({
                    "Quote": quote.select_one(".text").get_text(),
                    "Author": quote.select_one(".author").get_text(),
                    "URL": f"http://quotes.toscrape.com{quote.select_one('a')['href']}"
                })

def read_quotes():
    with open('quotes.csv', 'r', encoding='utf-8') as quote_file:
        reader = DictReader(quote_file)
        return list(reader)


def quote_guess():
    if os.stat("quotes.csv").st_size == 0:
        scrape_quotes()
    quotes = read_quotes()
    keep_playing = "y"

    while keep_playing == "y":
        guesses = 4  
        random_quote = choice(quotes)
        print(f"\nHere's a quote:\n{random_quote['Quote']}\n")
        guess = None
        while guesses > 0 and guess != random_quote["Author"]:
            guess = input(f"\nWho said this? Guesses remaining: {guesses}. ")
            if guess == random_quote["Author"]:
                keep_playing = input("That's correct! Would you like to play again? ")
                
            else:
                guesses -= 1
                print("Here's a hint: ", sep='')
                if guesses == 3:
                    author_url = requests.get(random_quote["URL"]).text
                    author_info = BeautifulSoup(author_url, "html.parser")
                    born_date = author_info.select_one(".author-born-date").get_text()
                    print(f"The author was born on {born_date}.\n", sep='')
                elif guesses == 2:
                    print(f"The author's first name starts with {random_quote['Author'][0]}.\n", sep='')
                elif guesses == 1:
                    print(f"The author's last name starts with {random_quote['Author'].split()[1][0]}.\n")
                else: 
                    print(f"Sorry. You're out of guesses. The answer was {random_quote['Author']}.")
                    keep_playing = input("Would you like to play again? ")
    print("Thanks for playing!")

quote_guess()
