import os
from extract_pdf import process_all_pdfs
from transform import transform_data
from load_duckdb import load_to_duckdb

def main():
    # Diretório contendo os PDFs
    pdf_dir = r"C:\Users\gtran\Desktop\contas_agua_projeto\data\pdfs"
    db_path = r"C:\Users\gtran\Desktop\contas_agua_projeto\database\contas_agua.db"
    table_name = "contas_agua"

    # Processar todos os PDFs e extrair dados
    raw_data = process_all_pdfs(pdf_dir)

    # Transformar os dados extraídos em um DataFrame limpo
    df = transform_data(raw_data)

    # Mostrar o DataFrame consolidado
    print("\nPrévia do DataFrame:")
    print(df)

    # Carregar no banco DuckDB
    load_to_duckdb(df, db_path, table_name)

    # Salvar em CSV (opcional)
    output_dir = r"C:\Users\gtran\Desktop\contas_agua_projeto\data\processed"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'extracted_data.csv')
    df.to_csv(output_path, index=False)

    print(f"\nOs dados foram salvos em '{output_path}'.")

if __name__ == "__main__":
    main()
