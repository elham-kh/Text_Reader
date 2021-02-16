
# import module 
from pdf2image import convert_from_path 
import os
  
 # change the current directory to the directory where the running script file (.py) exists
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Store Pdf with convert_from_path function 
images = convert_from_path('D:/PostDoc Research/GitLab/sustainable_finance/Elham/TEXT_Reader/G.pdf',dpi=350,
                            output_folder='D:/PostDoc Research/GitLab/sustainable_finance/Elham/TEXT_Reader/Page', fmt ='png', poppler_path=r'C:/Users/Elham/Anaconda3/pkgs/poppler-20.12.1/Library/bin') 

# change the current directory to the directory where the running script file (.py) exists
os.chdir(os.path.dirname(os.path.abspath(__file__)))

i = 1
for page in images:
    image_name = "Page_" + str(i) + ".png"  
    page.save(image_name, "PNG")
    i = i+1    

