from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import StudentCreationForm
import PyPDF2


def register(request):
    if request.method == "POST":
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = StudentCreationForm()
    return render(request, 'core/register.html', {'form': form})

def home(request):
    return render(request, 'core/home.html')



def api_page(request):
    return render(request, 'core/api_page.html')

def update_details(request):
    return render(request, 'core/update_details.html')

def tasks(request):
    return render(request, 'core/tasks.html')


# views.py
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from pdf2docx import Converter  # Install pdf2docx library: pip install pdf2docx

# views.py
from django.conf import settings

from django.shortcuts import render
import PyPDF2
import os





def chatbot(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        # Example PDF search functionality
        pdf_path = r'C:\Users\fatso\Documents\chatbot\Final Policy document_LICs New Jeevan Shanti_V05_logo.pdf'
        pdf_text = read_pdf(pdf_path)  # Implement this function to read PDF

        # Perform search in PDF
        search_results = search_in_pdf(pdf_text, query)

        return render(request, 'core/chatbot.html', {'search_results': search_results, 'query': query})

    return render(request, 'core/chatbot.html')

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def search_in_pdf(text, query):
    lines = text.split('\n')
    results = [line for line in lines if query.lower() in line.lower()]
    return results


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Document
from .forms import DocumentForm
import fitz  # PyMuPDF
from io import BytesIO
from docx import Document as DocxDocument

def convert_pdf_to_word(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_document = form.save()
            pdf_path = pdf_document.pdf_file.path
            
            # Convert PDF to Word
            doc = fitz.open(pdf_path)
            word_file = BytesIO()
            docx_document = DocxDocument()
            
            for page_num in range(doc.page_count):
                page = doc.load_page(page_num)
                text = page.get_text()
                docx_document.add_paragraph(text)
            
            docx_document.save(word_file)
            word_file.seek(0)
            
            response = HttpResponse(word_file, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename="{pdf_document.title}.docx"'
            
            return response
    else:
        form = DocumentForm()
    
    return render(request, 'core/convert_pdf_to_word.html', {'form': form})

