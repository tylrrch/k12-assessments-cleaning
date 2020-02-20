# Splits a large pdf containing multple COGAT test reports
# into individual reports and names the files with their 
# corresponding student id (if one is found)
import PyPDF2 as pydf

def PDFSplit(pdfs, output_dir, num_pages = 1):
    # count of no student id found exceptions
    no_id_count = 0

    for pdf in pdfs:
        # create pdf object
        pdf_file = open(pdf, 'rb')
        pdf_reader = pydf.PdfFileReader(pdf_file)

        # number of pages to include in each
        start = 0

        # get pages and write pdf output
        for i in range(pdf_reader.numPages): 

            pdf_writer = pydf.PdfFileWriter()

            # setting split end position
            end = start + num_pages
            try: 
                for page in range(start,end): 
                    pdf_writer.addPage(pdf_reader.getPage(page))
            except: 
                break
            
            # get the student id for file name
            page = pdf_reader.getPage(start)
            page_data = page.extractText()
            student_id = page_data.split("Norms: \n", 1)[1].split("\n", 1)[0]
            
            try:
                int(student_id)
            except:
                no_id_count += 1
                student_id = "no_id_found_" + str(no_id_count)
                
            # output pdf file name 
            outputpdf = output_dir + student_id + '.pdf'

            # writing split pdf pages to pdf file 
            with open(outputpdf, "wb") as f: 
                pdf_writer.write(f) 
    
            start = end 
            
        pdf_file.close() 
              
def main(): 
    pdfs = ['']
      
    output_dir = ''

    PDFSplit(pdfs, output_dir) 
  
if __name__ == "__main__": 
    main() 
