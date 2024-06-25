# URL Status Checker

A command-line tool to parse a file of URLs and display the HTTP status code and request time.

## Usage

Run the tool with an input file containing URLs:

`python download.py -i urls.csv`

### Input File Format

The input file should be a CSV with a pipe separator (`|`). Example:

Neti|http://www.neti.ee

Google|http://www.google.com

### Output

The tool will output the HTTP status code and the time taken for each request:

"Neti", HTTP 200, time 0.5 seconds

"Google", HTTP 200, time 0.6 seconds

### Help

To display the help message:

`python download.py -h`
