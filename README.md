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

    1. **image** — 8-bit, single-channel binary source image. The image may be modified by the function.
    2. **rho** — Distance resolution of the accumulator in pixels.
    3. **theta** — Angle resolution of the accumulator in radians.
    4. **threshold** — Accumulator threshold parameter. Only those lines are returned that get enough votes
    5. **line** — Output vector of lines. Here is set to None, the value is saved to linesP
    6. **minLineLength** — Minimum line length. Line segments shorter than that are rejected.
    7. **maxLineGap** — Maximum allowed gap between points on the same line to link them.

# [OCRmyPDF](https://github.com/jbarlow83/OCRmyPDF)
OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched or copy-pasted.

```bash
ocrmypdf                      # it's a scriptable command line program
   -l eng+fra                 # it supports multiple languages
   --rotate-pages             # it can fix pages that are misrotated
   --deskew                   # it can deskew crooked PDFs!
   --title "My PDF"           # it can change output metadata
   --jobs 4                   # it uses multiple cores by default
   --output-type pdfa         # it produces PDF/A by default
   input_scanned.pdf          # takes PDF input (or images)
   output_searchable.pdf      # produces validated PDF output
```

[See the release notes for details on the latest changes](https://ocrmypdf.readthedocs.io/en/latest/release_notes.html).

## Main features

- Generates a searchable [PDF/A](https://en.wikipedia.org/?title=PDF/A) file from a regular PDF
- Places OCR text accurately below the image to ease copy / paste
- Keeps the exact resolution of the original embedded images
- When possible, inserts OCR information as a "lossless" operation without disrupting any other content
- Optimizes PDF images, often producing files smaller than the input file
- If requested, deskews and/or cleans the image before performing OCR
- Validates input and output files
- Distributes work across all available CPU cores
- Uses [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) engine to recognize more than [100 languages](https://github.com/tesseract-ocr/tessdata)
- Scales properly to handle files with thousands of pages
- Battle-tested on millions of PDFs

For details: please consult the [documentation](https://ocrmypdf.readthedocs.io/en/latest/).

## Motivation

I searched the web for a free command line tool to OCR PDF files: I found many, but none of them were really satisfying:

- Either they produced PDF files with misplaced text under the image (making copy/paste impossible)
- Or they did not handle accents and multilingual characters
- Or they changed the resolution of the embedded images
- Or they generated ridiculously large PDF files
- Or they crashed when trying to OCR
- Or they did not produce valid PDF files
- On top of that none of them produced PDF/A files (format dedicated for long time storage)

...so I decided to develop my own tool.

## Installation

Linux, Windows, macOS and FreeBSD are supported. Docker images are also available.

Users of Debian 9 or later or Ubuntu 16.10 or later may simply

```bash
apt-get install ocrmypdf
```

and users of Fedora 29 or later may simply

```bash
dnf install ocrmypdf
```

and Homebrew users (macOS, Linux, Windows Subsystem for Linux) may simply

```bash
brew install ocrmypdf
```

For everyone else, [see our documentation](https://ocrmypdf.readthedocs.io/en/latest/installation.html) for installation steps.

## Languages

OCRmyPDF uses Tesseract for OCR, and relies on its language packs. For Linux users, you can often find packages that provide language packs:

```bash
# Display a list of all Tesseract language packs
apt-cache search tesseract-ocr

# Debian/Ubuntu users
apt-get install tesseract-ocr-chi-sim  # Example: Install Chinese Simplified language pack

# Arch Linux users
pacman -S tesseract-data-eng tesseract-data-deu # Example: Install the English and German language packs

# brew macOS users
brew install tesseract-lang
```

You can then pass the `-l LANG` argument to OCRmyPDF to give a hint as to what languages it should search for. Multiple languages can be requested.

## Documentation and support

Once OCRmyPDF is installed, the built-in help which explains the command syntax and options can be accessed via:

```bash
ocrmypdf --help
```

Our [documentation is served on Read the Docs](https://ocrmypdf.readthedocs.io/en/latest/index.html).

Please report issues on our [GitHub issues](https://github.com/jbarlow83/OCRmyPDF/issues) page, and follow the issue template for quick response.

## Requirements

In addition to the required Python version (3.6+), OCRmyPDF requires external program installations of Ghostscript, Tesseract OCR, QPDF, and Leptonica. OCRmyPDF is pure Python, but uses CFFI to portably generate library bindings. OCRmyPDF works on pretty much everything: Linux, macOS, Windows and FreeBSD.

## Press & Media

- [Going paperless with OCRmyPDF](https://medium.com/@ikirichenko/going-paperless-with-ocrmypdf-e2f36143f46a)
- [Converting a scanned document into a compressed searchable PDF with redactions](https://medium.com/@treyharris/converting-a-scanned-document-into-a-compressed-searchable-pdf-with-redactions-63f61c34fe4c)
- [c't 1-2014, page 59](https://heise.de/-2279695): Detailed presentation of OCRmyPDF v1.0 in the leading German IT magazine c't
- [heise Open Source, 09/2014: Texterkennung mit OCRmyPDF](https://heise.de/-2356670)
- [heise Durchsuchbare PDF-Dokumente mit OCRmyPDF erstellen](https://www.heise.de/ratgeber/Durchsuchbare-PDF-Dokumente-mit-OCRmyPDF-erstellen-4607592.html)
- [Excellent Utilities: OCRmyPDF](https://www.linuxlinks.com/excellent-utilities-ocrmypdf-add-ocr-text-layer-scanned-pdfs/)

## Business enquiries

OCRmyPDF would not be the software that it is today without companies and users choosing to provide support for feature development and consulting enquiries. We are happy to discuss all enquiries, whether for extending the existing feature set, or integrating OCRmyPDF into a larger system.
