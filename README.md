# text reader
text reader is a Python package extracting text from PDF.

## Installation

1) Converting PDF to Image:

This module converts a PDF to a PIL object. To install this module type the below command in the terminal.

```bash
pip install pdf2image
```

## Approach:

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

1. **image** - 8-bit, single-channel binary source image. The image may be modified by the function.
2. **rho** - Distance resolution of the accumulator in pixels.
3. **theta** - Angle resolution of the accumulator in radians.
4. **threshold** - Accumulator threshold parameter. Only those lines are returned that get enough votes
5. **line** - Output vector of lines. Here is set to None, the value is saved to linesP
6. **minLineLength** - Minimum line length. Line segments shorter than that are rejected.
7. **maxLineGap** - Maximum allowed gap between points on the same line to link them.

3) Converting img to pdf

[img2pdf](https://github.com/jbarlow83/img2pdf/blob/master/README.md)
=======

Lossless conversion of raster images to PDF. You should use img2pdf if your
priorities are (in this order):

 1. **always lossless**: the image embedded in the PDF will always have the
    exact same color information for every pixel as the input
 2. **small**: if possible, the difference in filesize between the input image
    and the output PDF will only be the overhead of the PDF container itself
 3. **fast**: if possible, the input image is just pasted into the PDF document
    as-is without any CPU hungry re-encoding of the pixel data

Conventional conversion software (like ImageMagick) would either:

 1. not be lossless because lossy re-encoding to JPEG
 2. not be small because using wasteful flate encoding of raw pixel data
 3. not be fast because input data gets re-encoded

Another advantage of not having to re-encode the input (in most common
situations) is, that img2pdf is able to handle much larger input than other
software, because the raw pixel data never has to be loaded into memory.

The following table shows how img2pdf handles different input depending on the
input file format and image color space.

| Format               | Colorspace                     | Result        |
| -------------------- | ------------------------------ | ------------- |
| JPEG                 | any                            | direct        |
| JPEG2000             | any                            | direct        |
| PNG (non-interlaced) | any                            | direct        |
| TIFF (CCITT Group 4) | monochrome                     | direct        |
| any                  | any except CMYK and monochrome | PNG Paeth     |
| any                  | monochrome                     | CCITT Group 4 |
| any                  | CMYK                           | flate         |

For JPEG, JPEG2000, non-interlaced PNG and TIFF images with CCITT Group 4
encoded data, img2pdf directly embeds the image data into the PDF without
re-encoding it. It thus treats the PDF format merely as a container format for
the image data. In these cases, img2pdf only increases the filesize by the size
of the PDF container (typically around 500 to 700 bytes). Since data is only
copied and not re-encoded, img2pdf is also typically faster than other
solutions for these input formats.

For all other input types, img2pdf first has to transform the pixel data to
make it compatible with PDF. In most cases, the PNG Paeth filter is applied to
the pixel data. For monochrome input, CCITT Group 4 is used instead. Only for
CMYK input no filter is applied before finally applying flate compression.

Usage
-----

The images must be provided as files because img2pdf needs to seek in the file
descriptor.

If no output file is specified with the `-o`/`--output` option, output will be
done to stdout. A typical invocation is:

	$ img2pdf img1.png img2.jpg -o out.pdf

The detailed documentation can be accessed by running:

	$ img2pdf --help

Bugs
----

 - If you find a JPEG, JPEG2000, PNG or CCITT Group 4 encoded TIFF file that,
   when embedded into the PDF cannot be read by the Adobe Acrobat Reader,
   please contact me.

 - I have not yet figured out how to determine the colorspace of JPEG2000
   files.  Therefore JPEG2000 files use DeviceRGB by default. For JPEG2000
   files with other colorspaces, you must explicitly specify it using the
   `--colorspace` option.

 - Input images with alpha channels are not allowed. PDF only supports
   transparency using binary masks but is unable to store 8-bit transparency
   information as part of the image itself. But img2pdf will always be lossless
   and thus, input images must not carry transparency information.

 - img2pdf uses PIL (or Pillow) to obtain image meta data and to convert the
   input if necessary. To prevent decompression bomb denial of service attacks,
   Pillow limits the maximum number of pixels an input image is allowed to
   have. If you are sure that you know what you are doing, then you can disable
   this safeguard by passing the `--pillow-limit-break` option to img2pdf. This
   allows one to process even very large input images.

Installation
------------

On a Debian- and Ubuntu-based systems, img2pdf can be installed from the
official repositories:

	$ apt install img2pdf

If you want to install it using pip, you can run:

	$ pip3 install img2pdf

If you prefer to install from source code use:

	$ cd img2pdf/
	$ pip3 install .

To test the console script without installing the package on your system,
use virtualenv:

	$ cd img2pdf/
	$ virtualenv ve
	$ ve/bin/pip3 install .

You can then test the converter using:

	$ ve/bin/img2pdf -o test.pdf src/tests/test.jpg

For Microsoft Windows users, PyInstaller based .exe files are produced by
appveyor. If you don't want to install Python before using img2pdf you can head
to appveyor and click on "Artifacts" to download the latest version:
https://ci.appveyor.com/project/josch/img2pdf

GUI
---

There exists an experimental GUI with all settings currently disabled. You can
directly convert images to PDF but you cannot set any options via the GUI yet.
If you are interested in adding more features to the PDF, please submit a merge
request. The GUI is based on tkinter and works on Linux, Windows and MacOS.

![](screenshot.png)

Library
-------

The package can also be used as a library:

	import img2pdf

	# opening from filename
	with open("name.pdf","wb") as f:
		f.write(img2pdf.convert('test.jpg'))

	# opening from file handle
	with open("name.pdf","wb") as f1, open("test.jpg") as f2:
		f1.write(img2pdf.convert(f2))

	# using in-memory image data
	with open("name.pdf","wb") as f:
		f.write(img2pdf.convert("\x89PNG...")

	# multiple inputs (variant 1)
	with open("name.pdf","wb") as f:
		f.write(img2pdf.convert("test1.jpg", "test2.png"))

	# multiple inputs (variant 2)
	with open("name.pdf","wb") as f:
		f.write(img2pdf.convert(["test1.jpg", "test2.png"]))

	# convert all files ending in .jpg inside a directory
	dirname = "/path/to/images"
	with open("name.pdf","wb") as f:
		imgs = []
		for fname in os.listdir(dirname):
			if not fname.endswith(".jpg"):
				continue
			path = os.path.join(dirname, fname)
			if os.path.isdir(path):
				continue
			imgs.append(path)
		f.write(img2pdf.convert(imgs))

	# convert all files ending in .jpg in a directory and its subdirectories
	dirname = "/path/to/images"
	with open("name.pdf","wb") as f:
		imgs = []
		for r, _, f in os.walk(dirname):
			for fname in f:
				if not fname.endswith(".jpg"):
					continue
				imgs.append(os.path.join(r, fname))
		f.write(img2pdf.convert(imgs))


	# convert all files matching a glob
	import glob
	with open("name.pdf","wb") as f:
		f.write(img2pdf.convert(glob.glob("/path/to/*.jpg")))

	# writing to file descriptor
	with open("name.pdf","wb") as f1, open("test.jpg") as f2:
		img2pdf.convert(f2, outputstream=f1)

	# specify paper size (A4)
	a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
	layout_fun = img2pdf.get_layout_fun(a4inpt)
	with open("name.pdf","wb") as f:
		f.write(img2pdf.convert('test.jpg', layout_fun=layout_fun))

Comparison to ImageMagick
-------------------------

Create a large test image:

	$ convert logo: -resize 8000x original.jpg

Convert it into PDF using ImageMagick and img2pdf:

	$ time img2pdf original.jpg -o img2pdf.pdf
	$ time convert original.jpg imagemagick.pdf

Notice how ImageMagick took an order of magnitude longer to do the conversion
than img2pdf. It also used twice the memory.

Now extract the image data from both PDF documents and compare it to the
original:

	$ pdfimages -all img2pdf.pdf tmp
	$ compare -metric AE original.jpg tmp-000.jpg null:
	0
	$ pdfimages -all imagemagick.pdf tmp
	$ compare -metric AE original.jpg tmp-000.jpg null:
	118716

To get lossless output with ImageMagick we can use Zip compression but that
unnecessarily increases the size of the output:

	$ convert original.jpg -compress Zip imagemagick.pdf
	$ pdfimages -all imagemagick.pdf tmp
	$ compare -metric AE original.jpg tmp-000.png null:
	0
	$ stat --format="%s %n" original.jpg img2pdf.pdf imagemagick.pdf
	1535837 original.jpg
	1536683 img2pdf.pdf
	9397809 imagemagick.pdf

Comparison to pdfLaTeX
----------------------

pdfLaTeX performs a lossless conversion from included images to PDF by default.
If the input is a JPEG, then it simply embeds the JPEG into the PDF in the same
way as img2pdf does it. But for other image formats it uses flate compression
of the plain pixel data and thus needlessly increases the output file size:

	$ convert logo: -resize 8000x original.png
	$ cat << END > pdflatex.tex
	\documentclass{article}
	\usepackage{graphicx}
	\begin{document}
	\includegraphics{original.png}
	\end{document}
	END
	$ pdflatex pdflatex.tex
	$ stat --format="%s %n" original.png pdflatex.pdf
	4500182 original.png
	9318120 pdflatex.pdf

Comparison to podofoimg2pdf
---------------------------

Like pdfLaTeX, podofoimg2pdf is able to perform a lossless conversion from JPEG
to PDF by plainly embedding the JPEG data into the pdf container. But just like
pdfLaTeX it uses flate compression for all other file formats, thus sometimes
resulting in larger files than necessary.

	$ convert logo: -resize 8000x original.png
	$ podofoimg2pdf out.pdf original.png
	stat --format="%s %n" original.png out.pdf
	4500181 original.png
	9335629 out.pdf

It also only supports JPEG, PNG and TIF as input and lacks many of the
convenience features of img2pdf like page sizes, borders, rotation and
metadata.

Comparison to Tesseract OCR
---------------------------

Tesseract OCR comes closest to the functionality img2pdf provides. It is able
to convert JPEG and PNG input to PDF without needlessly increasing the filesize
and is at the same time lossless. So if your input is JPEG and PNG images, then
you should safely be able to use Tesseract instead of img2pdf. For other input,
Tesseract might not do a lossless conversion. For example it converts CMYK
input to RGB and removes the alpha channel from images with transparency. For
multipage TIFF or animated GIF, it will only convert the first frame.


4) Converting scanned pdf to readable pdf

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
