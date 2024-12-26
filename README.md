# **Pipeline de Contas de Água**

Este projeto automatiza o processo de extração, transformação e carregamento (ETL) de dados de contas de água em formato PDF para um banco de dados DuckDB. Ele organiza as informações de consumo e custos, permitindo análises e visualizações eficientes.


## **Estrutura do Projeto**
A estrutura do projeto foi organizada para separar as funções principais:

```
contas_agua_projeto/
├── data/
│   ├── pdfs/          # PDFs das contas de água
│   ├── processed/     # Dados processados (CSV, etc.)
├── database/
│   ├── contas_agua.db # Banco de dados DuckDB
├── scripts/
│   ├── extract_pdf.py # Script para extrair dados dos PDFs
│   ├── transform.py   # Script para transformar os dados extraídos
│   ├── load_duckdb.py # Script para carregar os dados no banco
│   ├── main.py        # Pipeline completo (ETL)
├── README.md          # Descrição do projeto
├── .gitignore         # Arquivos/pastas ignorados pelo Git
└── requirements.txt   # Dependências do projeto
```


## **Funcionalidades**
- **Extração**: Leitura dos PDFs para extrair informações como data de leitura, consumo e valor da conta.
- **Transformação**: Limpeza, formatação e validação dos dados.
- **Carregamento**: Armazenamento dos dados estruturados no banco de dados DuckDB.
- **Automação**: Monitoramento de novos PDFs para processamento automático.


## **Tecnologias Utilizadas**
- **Linguagem**: Python
- **Bibliotecas**:
  - `pdfplumber`: Extração de dados dos PDFs.
  - `pandas`: Manipulação e transformação dos dados.
  - `duckdb`: Armazenamento em banco de dados analítico.
  - `watchdog`: Monitoramento de novos arquivos.


## **Pré-requisitos**
- Python 3.12.5 ou superior.
- Dependências listadas no arquivo `requirements.txt`.


## **Instalação**
1. Clone o repositório:
   ```
   git clone https://github.com/seuusuario/contas-agua-projeto.git
   cd contas-agua-projeto
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```


## **Como Usar**
1. Certifique-se de que os PDFs das contas estão na pasta `data/pdfs/`.
2. Execute o pipeline principal:
   ```
   python scripts/main.py
   ```
3. Verifique os dados processados: Os dados transformados estarão disponíveis no banco `database/contas_agua.db`.


## **Automação**
Para monitorar automaticamente novos PDFs, utilize o script de monitoramento:
```
python scripts/monitor_pdfs.py
```


## **Próximos Passos**
- Adicionar visualizações interativas usando **Streamlit** ou **Dash**.
- Criar previsões de consumo com modelos de Machine Learning.
- Expandir o projeto para gerenciar múltiplos apartamentos ou unidades.


## **Contribuição**
Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests**.


## **Licença**
Este projeto é de uso pessoal e está disponível sob a licença MIT.


Se você tem dúvidas ou sugestões, entre em contato ou deixe um comentário! 😊
