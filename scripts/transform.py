import pandas as pd

def transform_data(data):
    """
    Recebe uma lista de dicionários com dados extraídos e retorna um DataFrame limpo.
    """
    # Converter a lista de dicionários em um DataFrame
    df = pd.DataFrame(data)

    # Substituir vírgulas por pontos e converter para numérico
    for col in ['leitura', 'leitura_anterior', 'consumo', 'valor_conta']:
        df[col] = df[col].str.replace(',', '.')
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Converter data para formato datetime
    df['data_leitura'] = pd.to_datetime(df['data_leitura'], format='%d/%m/%Y', errors='coerce')

    # Criar coluna adicional de análise
    df['conta_minima'] = df['consumo'] < 10

    # Ordenar por data e resetar o índice
    df = df.sort_values(by='data_leitura', ascending=True).reset_index(drop=True)

    return df
