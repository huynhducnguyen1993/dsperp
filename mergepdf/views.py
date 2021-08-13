
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
import PyPDF2
from django.http import FileResponse
from PyPDF2 import *
import os
import zipfile

# Create your views here.
def pdf_extract(request):
    print(request.POST)
    if request.method == 'POST':
        content = request.POST.get('select_pdf')
        
        if 'extractpdf' in request.POST and content =="1":
            # If you submit via POST
            form = PdfUploadForm(request.POST, request.FILES)

            if form.is_valid():
            
                f = form.cleaned_data['file']
               
                pdfFileObj = PyPDF2.PdfFileReader(f)

              
                page_num_list = form.cleaned_data['page'].split(',')

               
                zf = zipfile.ZipFile(os.path.join('media', 'extracted_pages.zip'), 'w')

                for page_num in page_num_list:
                    if page_num:
               
                        page_index = int(page_num) - 1

                
                        pageObj = pdfFileObj.getPage(page_index) 
                        if pageObj:
                            pdfWriter = PyPDF2.PdfFileWriter()

                            pdfWriter.addPage(pageObj)

                
                            pdf_file_path = os.path.join('media', 'extracted_page_{}.pdf'.format(page_num))
                
                            with open(pdf_file_path, 'wb') as pdfOutputFile:
                                pdfWriter.write(pdfOutputFile)
                    
                            zf.write(pdf_file_path)
                        else:
                            return HttpResponse("Lỗi Không Mong Muốn    ")
                    else:
                        return HttpResponse("Lỗi Không Mong Muốn    ")

                zf.close()

              
                response = FileResponse(open(os.path.join('media', 'extracted_pages.zip'), 'rb'))
                response['content_type'] = "application/zip"
                response['Content-Disposition'] = 'attachment; filename="trang_pdf_duoc_tach.zip"'
                return response

            else:
        
                 form = PdfUploadForm()
       

        if 'extractpdf' in request.POST and content == "2":
            form = PdfUploadForm(request.POST, request.FILES)
            if form.is_valid():
                
                f = form.cleaned_data['file']
                
                pdfFileObj = PyPDF2.PdfFileReader(f)

                page_range = form.cleaned_data['page'].split('-')
                page_start = int(page_range[0])
                page_end = int(page_range[1])

                # Extracted pdf file path
                pdf_file_path = os.path.join('media', 'extracted_page_{}-{}.pdf'.format(page_start, page_end))
                pdfOutputFile = open(pdf_file_path, 'ab+')

               
                pdfWriter = PyPDF2.PdfFileWriter()

                for page_num in range(page_start, page_end + 1):
                   
                    page_index = int(page_num) - 1

                   
                    pageObj = pdfFileObj.getPage(page_index) 
                    pdfWriter.addPage(pageObj)

                pdfWriter.write(pdfOutputFile)
                pdfOutputFile.close()

                extractedPage = open(pdf_file_path, 'rb')
                response = FileResponse(extractedPage)
                response['content_type'] = "application/octet-stream"
                response['Content-Disposition'] = 'attachment; filename="extracted_pages.pdf"'

                return response
            else:
                    form = PdfUploadForm()
                
    
                    

        if 'mergepdf' in request.POST:
            form_merge = Pdfmerge(request.POST, request.FILES)
            if form_merge.is_valid():
                # 1 Get upload files
                file = request.FILES.getlist('file')
                pdfMerger = PyPDF2.PdfFileMerger()
                for f in file:
                    
                    pdfFileObj =PyPDF2.PdfFileReader(f)
                   
                    pdfMerger.append(pdfFileObj)
                
                # Merge file object is written to merged_file.pdf
                with open(os.path.join('media', 'merged_file.pdf'), 'wb') as pdfOutputFile:
                    pdfMerger.write(pdfOutputFile)

                # Open merger merged_file.pdf, by HttpResponse output
                response = FileResponse(open(os.path.join('media', 'merged_file.pdf'), 'rb'))
                response['content_type'] = "application/octet-stream"
                response['Content-Disposition'] = 'attachment; filename="merged_file.pdf"'

                return response

            else:
                # If submitting by POST, but the form does not pass validation
                form_merge = Pdfmerge()
               
            
    else:
                # If the user does not pass the POST, submitting to generate an empty form
                form = PdfUploadForm()
                form_merge =Pdfmerge()
                context = {
                    'form':form,
                    'form_merge':form_merge,
                }
                return render(request, 'mergepdf/pdf.html',context)
        

     