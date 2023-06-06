import sys
import requests
import string
from bs4 import BeautifulSoup

special_chars = "»©"


def get_text(data: requests.models.Response) -> str:
    """Get word strings from website.
    Keyword arguments:
        data - requests module Response model
    Return word strings.
    """
    soup = BeautifulSoup(data.text, 'html.parser')

    return soup.text


def drop_special_chars(data: list) -> list:
    """Returns a "cleaned" list containing no punctuation.
    Keyword arguments:
        data - list of strings to be formatted
    """
    cleaned_list = [word.strip(string.punctuation + special_chars) for word in data]
    cleaned_list = set(cleaned_list)
    return list(cleaned_list)


def output_list(data: list) -> None:
    """iterates through and prints the provided list"""
    if data:
        for item in data:
            if item:
                print(item)


def main() -> None:
    response = None

    try:
        if sys.argv[1]:
            try:
                url = sys.argv[1]
                response = requests.get(url)
            except requests.exceptions.MissingSchema:
                print(f"[!] Provide a URL schema (https/http://google.com).")
            except requests.exceptions.InvalidSchema:
                print(f"[!] Provide a valid URL schema (https://google.com)\n--> You provided {url}")
            except requests.exceptions.ConnectionError:
                print(f"[!] Name resolution failure for {url}. Check that you have provided a proper web address.")

        if response:
            text = get_text(response)
            text = text.split()
            text = drop_special_chars(text)

            output_list(text)

    except IndexError:
        print(f"[!] Provide an URL for the first argument (python3 webr.py <url>).")


if __name__ == "__main__":
    main()
