
# utils/limpeza.py

import pandas as pd

def carregar_dados(caminho_arquivo="../data/Final Dataset - State of Data 2024 - Kaggle - df_survey_2024.csv") -> pd.DataFrame:
    """
    Carrega o dataset da pesquisa State of Data 2024 e retorna um DataFrame.

    Args:
        caminho_arquivo (str): Caminho para o arquivo CSV.

    Returns:
        pd.DataFrame: DataFrame carregado.
    """
    try:
        df = pd.read_csv(caminho_arquivo)
        print(f"[INFO] Dados carregados com sucesso: {df.shape[0]} linhas e {df.shape[1]} colunas.")
        return df
    except Exception as e:
        print(f"[ERRO] Falha ao carregar os dados: {e}")
        return pd.DataFrame()

# utils/limpeza.py
def normalizar_cargos(df):
    df["cargo_normalizado"] = (
        df["2.f_cargo_atual"]
        .fillna('')
        .str.lower()
        .str.normalize('NFKD')
        .str.encode('ascii', errors='ignore')
        .str.decode('utf-8')
    )
    return df