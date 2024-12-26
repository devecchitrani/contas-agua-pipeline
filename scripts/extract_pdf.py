import pdfplumber

# Coordenadas das regiões para extração
COORDINATES = {
    "data_leitura": (166.00009999999997, 403.12, 220.02009999999999, 417.12),
    "unidade": (470.0, 87.69000000000005, 503.22, 97.69000000000005),
    "medidor_numero": (120.0, 117.69000000000005, 204.14, 127.69000000000005),
    "leitura": (260.0, 147.69000000000005, 292.93, 157.69000000000005),
    "leitura_anterior": (130.0, 147.69000000000005, 162.93, 157.69000000000005),
    "consumo": (375.0, 147.69000000000005, 397.81, 157.69000000000005),
    "valor_conta": (462.94, 222.69000000000005, 485.75, 232.69000000000005),
}

def extract_data_from_pdf(pdf_path):
    """
    Extrai dados de um único PDF com base em coordenadas predefinidas.
    """
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[0]  # Seleciona a primeira página do PDF
        extracted_data = {}

        # Iterar sobre as coordenadas definidas
        for field, bbox in COORDINATES.items():
            # Recorta a região e extrai o texto
            cropped_page = page.within_bbox(bbox)
            text = cropped_page.extract_text() if cropped_page else None
            extracted_data[field] = text.strip() if text else None

    return extracted_data

def process_all_pdfs(pdf_dir):
    """
    Lê todos os PDFs em um diretório, extrai os dados e retorna uma lista de dicionários.
    """
    import os
    all_data = []

    # Iterar sobre todos os arquivos na pasta
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith(".pdf"):  # Verifica se é um arquivo PDF
            pdf_path = os.path.join(pdf_dir, pdf_file)
            print(f"Processando arquivo: {pdf_file}")
            try:
                # Extrai os dados do PDF
                data = extract_data_from_pdf(pdf_path)
                all_data.append(data)
            except Exception as e:
                print(f"Erro ao processar {pdf_file}: {e}")

    return all_data
