"""
****************

Test Assignment

As a user I want use command line tool to parse file of urls and see http status code and how many seconds the request
took.

Command line tool has options -i <input-file>

Input file is csv file with separator pipe, example of a file

Neti|http://www.neti.ee

Google|http://www.google.com



CSV first column is name and second is url.

As a user I want to see the http status code and request time(1 decimals) in console like this

./download.py -i urls.csv

“Neti”, HTTP 200, time 0.5 seconds

“Google”, HTTP 200, time 0.6 seconds



option -h will show the help of the script.

If page is not reachable in 2 seconds print "Skipping <url>"

To parse command line arguments use click https://pypi.org/project/click/

****************
"""
import click
import requests


def read_urls_from_file(filename: str) -> list:
    """
    Read a file and extract URLs.

    Parameters:
        filename (str): The name of the file to be read.

    Returns:
        list: A list of tuples, where each tuple contains the name and URL extracted from a line in the file.
    """
    data = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            if '|' in line:
                name, url = line.strip().split('|', 1)
                data.append((name.strip(), url.strip()))

    return data


def fetch_url_status(url: str) -> tuple:
    """
    Fetches the status code and response time of a given URL.

    Parameters:
        url (str): The URL to fetch.

    Returns:
        tuple: A tuple containing the status code and response time of the URL.
    """
    try:
        response = requests.get(url, timeout=2)
        return response.status_code, round(response.elapsed.total_seconds(), 1)
    except requests.exceptions.RequestException:
        return -1, -1


def print_response(name: str, url: str, response: tuple):
    """
    Print the HTTP response information for a given name, URL, and response tuple.

    Parameters:
        name (str): The name of the response.
        url (str): The URL associated with the response.
        response (tuple): A tuple containing HTTP response information.

    Returns:
        None
    """
    if response[0] == -1:
        print(f'Skipping {url}')
    else:
        print(f'"{name}", HTTP {response[0]}, time {response[1]} seconds')


def print_help(ctx, _, value):
    if value:
        click.echo(ctx.get_help(), color=ctx.color)
        ctx.exit()


@click.command()
@click.option('-i', 'input_file', required=True, help='Input file in csv format with separator pipe.')
@click.option('-h', '--help', is_flag=True, is_eager=True, expose_value=False, callback=print_help,
              help='Show this message and exit.')
def process_urls_from_file(input_file):
    url_data = read_urls_from_file(input_file)
    for name, url in url_data:
        response = fetch_url_status(url)
        print_response(name, url, response)


if __name__ == '__main__':
    process_urls_from_file()
