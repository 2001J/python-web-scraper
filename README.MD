# Python Web Scraper

A simple Python web scraper that fetches webpage content, extracts text data, and saves it to a CSV file.

## Features

- Fetches webpage content using HTTP requests
- Extracts and parses text data
- Exports results to CSV format
- Built with BeautifulSoup4 and Requests

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

### macOS/Linux

1. **Clone the repository**
   ```bash
   git clone https://github.com/2001J/python-web-scraper.git
   cd python-web-scraper
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Windows

1. **Clone the repository**
   ```bash
   git clone https://github.com/2001J/python-web-scraper.git
   cd python-web-scraper
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the scraper:
```bash
python scraper.py
```

The scraped data will be saved to `quotes.csv`.

## Deactivating the Virtual Environment

When you're done, deactivate the virtual environment:
```bash
deactivate
```

## Dependencies

- `beautifulsoup4` - HTML parsing
- `requests` - HTTP library

See `requirements.txt` for version details.

## License

This project is open source and available under the MIT License.
