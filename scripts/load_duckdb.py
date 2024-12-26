import duckdb
import os

def load_to_duckdb(df, db_path, table_name):
    """
    Carrega um DataFrame pandas no banco de dados DuckDB em uma tabela especificada.

    Args:
        df (pd.DataFrame): O DataFrame a ser carregado.
        db_path (str): Caminho para o arquivo do banco de dados DuckDB.
        table_name (str): Nome da tabela no banco de dados.

    Returns:
        None
    """
    # Garantir que o diretório do banco exista
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Validação do DataFrame
    required_columns = [
        "data_leitura", "unidade", "medidor_numero", "leitura", "leitura_anterior", "consumo", "valor_conta", "conta_minima"
    ]
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"O DataFrame não contém todas as colunas necessárias: {required_columns}")

    # Conectar ao banco de dados DuckDB
    conn = duckdb.connect(db_path)

    # Criar a tabela, se não existir
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            data_leitura DATE,
            unidade VARCHAR,
            medidor_numero VARCHAR,
            leitura FLOAT,
            leitura_anterior FLOAT,
            consumo FLOAT,
            valor_conta FLOAT,
            conta_minima BOOLEAN,
            PRIMARY KEY (data_leitura, unidade, medidor_numero)
        )
    """)

    # Registrar o DataFrame como uma tabela temporária no DuckDB
    conn.register("temp_df", df)

    # Remover registros duplicados com base na chave primária
    conn.execute(f"""
        DELETE FROM {table_name}
        WHERE EXISTS (
            SELECT 1
            FROM temp_df
            WHERE {table_name}.data_leitura = temp_df.data_leitura
            AND {table_name}.unidade = temp_df.unidade
            AND {table_name}.medidor_numero = temp_df.medidor_numero
        )
    """)
    
    # Inserir os novos registros
    conn.execute(f"INSERT INTO {table_name} SELECT * FROM temp_df")
    
    # Fechar a conexão
    conn.close()

    print(f"Dados carregados na tabela '{table_name}' do banco de dados '{db_path}'.")
