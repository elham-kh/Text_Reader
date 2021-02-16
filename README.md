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
