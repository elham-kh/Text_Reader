#pip install pdfminer.six
import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os 

# change the current directory to the directory where the running script file (.py) exists
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def convert_pdf_to_txt(path):
    '''Convert pdf content from a file path to text

    :path the file path
    '''
    rsrcmgr = PDFResourceManager()
    codec = 'utf-8'
    laparams = LAParams()

    with io.StringIO() as retstr:
        with TextConverter(rsrcmgr, retstr, codec=codec,
                           laparams=laparams) as device:
            with open(path, 'rb') as fp:
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                password = ""
                maxpages = 0
                caching = True
                pagenos = set()

                for page in PDFPage.get_pages(fp,
                                              pagenos,
                                              maxpages=maxpages,
                                              password=password,
                                              caching=caching,
                                              check_extractable=False):
                    interpreter.process_page(page)

                return retstr.getvalue()


if __name__ == "__main__":
    text = convert_pdf_to_txt('D:/PostDoc Research/GitLab/sustainable_finance/Elham/TEXT_Reader/Climate.pdf').encode('utf-8', errors='ignore')
    


    # A text file is created and flushed 
    file = open("final.txt", "wb") 
    file.write(text) 
    file.close() 