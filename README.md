# text reader
text reader is a Python package extracting text from PDF.

## Installation

1) Converting PDF to Image:

This module converts a PDF to a PIL object. To install this module type the below command in the terminal.

```bash
pip install pdf2image
```

##Approach:

    - Import the pdf2image module
    - Store a PFD with convert_from_path()
    - Save image with save()


poppler: This module allows to read, render, or modify PDF documents. Windows users will have to build or download poppler for Windows. click [here](https://github.com/oschwartz10612/poppler-windows/releases/) to download

You will then have to add the bin/ folder to PATH or use

```Python
poppler_path = r”C:\path\to\poppler-xx\bin”
```
as an argument in convert_from_path.

You can also install poppler package via anaconda

```bash
conda install -c conda-forge poppler
```

If you are stuck, please update conda before installing :

```bash
conda update conda
conda update anaconda
```

2) Converting Image to Text

First, use the package manager [pip](https://pip.pypa.io/en/stable/) to install pytesseract using the command line

```bash
pip install pytesseract
```
Then, head to [this](https://github.com/UB-Mannheim/tesseract/wiki) website, download and install the Tesseract OCR executable. We will need to know where we install this, as we will need to let your python script know.

To read text from an image, you may divide the process into three processes, namely cells detection, region of interest (ROI) selection, and text extraction.

### Cells Detection

Finding horizontal and vertical lines, using Hough Line Transform, an OpenCV library. For mode detail, please visit this [link](https://docs.opencv.org/master/d9/db0/tutorial_hough_lines.html).


### Hough Line Transform

In OpenCV, there are two types of this algorithm, namely standard Hough Line Transform and probabilistic Hough Line Transform. The standard one will give you the line equation, so you do not know the beginning and end of the line. While the probabilistic line transform will give you the list of lines, in which a line is a list of the beginning and end coordinate.

For the HoughLinesP function, there are several input arguments:

    1.**image** — 8-bit, single-channel binary source image. The image may be modified by the function.
    2.**rho** — Distance resolution of the accumulator in pixels.
    3.**theta** — Angle resolution of the accumulator in radians.
    4.**threshold** — Accumulator threshold parameter. Only those lines are returned that get enough votes
    5.**line** — Output vector of lines. Here is set to None, the value is saved to linesP
    6.**minLineLength** — Minimum line length. Line segments shorter than that are rejected.
    7.**maxLineGap** — Maximum allowed gap between points on the same line to link them.

## Example Usage

```python
from sec_edgar_downloader import Downloader

# Initialize a downloader instance.
# If no argument is passed to the constructor, the package
# will attempt to locate the user's downloads folder.
dl = Downloader("/path/to/valid/save/location")

# Get all 8-K filings for Apple (ticker: AAPL)
dl.get("8-K", "AAPL")

# Get all 8-K filings for Apple, including filing amends (8-K/A)
dl.get("8-K", "AAPL", include_amends=True)

# Get all 8-K filings for Apple after January 1, 2017 and before March 25, 2017
# Note: before_date and after_date strings must be in the form "YYYYMMDD"
dl.get("8-K", "AAPL", after_date="20170101", before_date="20170325")

# Get the five most recent 8-K filings for Apple
dl.get("8-K", "AAPL", 5)

# Get all 10-K filings for Microsoft (ticker: MSFT)
dl.get("10-K", "MSFT")

# Get the latest 10-K filing for Microsoft
dl.get("10-K", "MSFT", 1)

# Get the latest 10KSB filing for Ubiquitech Software
dl.get("10KSB", "0001411460", 1)

# Get all 10-Q filings for Visa (ticker: V)
dl.get("10-Q", "V")

# Get all 13F-NT filings for the Vanguard Group (CIK: 0000102909)
dl.get("13F-NT", "0000102909")

# Get all 13F-HR filings for the Vanguard Group
dl.get("13F-HR", "0000102909")

# Get all SC 13G filings for Apple
dl.get("SC 13G", "AAPL")

# Get all SD filings for Apple
dl.get("SD", "AAPL")

# Get the latest supported filings, if available, for Apple
for filing_type in dl.supported_filings:
    dl.get(filing_type, "AAPL", 1)

# Get the latest supported filings, if available, for a
# specified list of tickers and CIKs
symbols = ["AAPL", "MSFT", "0000102909", "V", "FB"]
for s in symbols:
    for filing_type in dl.supported_filings:
        dl.get(filing_type, s, 1)
```

## Supported SEC Filings

   - 4
   - 8-K
   - 10-K
   - 10KSB
   - 10-Q
   - 13F-NT and 13F-HR
   - 20-F
   - SC 13G
   - SD
   - S-1
   - DEF 14A
