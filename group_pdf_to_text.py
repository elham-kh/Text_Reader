from PDF_to_text import convert_pdf_to_txt
import os


#directory_add = 'D:/PostDoc Research/GitLab/sustainable_finance/Elham/TCFD_Downloader/webscraping'
directory_add = 'D:/PostDoc Research/GitLab/sustainable_finance/Elham/TCFD_Downloader/TCFD'
arr = os.listdir(directory_add)

for pdf_file in arr:
    if pdf_file.endswith(".pdf"):
        dir_pdf = directory_add + '/' + str(pdf_file)
        text = convert_pdf_to_txt(dir_pdf).encode('utf-8', errors='ignore')

        # A text file is created and flushed 
        dir_txt = directory_add + '/txtFiles/' + str(pdf_file.split('.')[0]) + '.txt'
        file = open(dir_txt, "wb") 
        file.write(text) 
        file.close() 