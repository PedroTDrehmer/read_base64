import base64
import PyPDF2
from io import BytesIO
import re

# Lê o conteúdo base64 do arquivo 'base64.txt'
with open("base64.txt", "r") as file:
    pdf_base64 = file.read()

# Ajusta o preenchimento base64, caso necessário
padding = len(pdf_base64) % 4
if padding != 0:
    pdf_base64 += '=' * (4 - padding)

# Decodifica o conteúdo base64 para obter os dados binários do PDF
pdf_data = base64.b64decode(pdf_base64)

# Usa BytesIO para tratar os dados binários como um arquivo
pdf_file = BytesIO(pdf_data)

# Lê o PDF usando PyPDF2
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extrai o texto da primeira página
page = pdf_reader.pages[0]
text = page.extract_text()

# Regex para procurar o campo "Valor Total do Documento" e o valor logo abaixo
match = re.search(r'Valor Total do Documento\s*([\d\.,]+)', text)

if match:
    valor_total = match.group(1)  # Captura o valor encontrado
    print(f"Valor Total do Documento: {valor_total}")
else:
    print("Campo 'Valor Total do Documento' não encontrado.")
