# utils/vetorizacao.py

import pandas as pd

def vetorizar_perfis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma o DataFrame de perfis em vetores binários e numéricos para recomendação.

    Args:
        df (pd.DataFrame): DataFrame contendo as colunas selecionadas do perfil.

    Returns:
        pd.DataFrame: DataFrame vetorizado.
    """
    df = df.copy()


    #  Converte colunas categóricas para dummies
    df_dummies = pd.get_dummies(df, drop_first=False)

    #  Remove colunas completamente nulas (caso haja)
    df_vetorizado = df_dummies.dropna(axis=1, how="all")

    #  Remove colunas completamente nulas (caso haja)
    df_vetorizado = df_dummies.dropna(axis=1, how="all")

    #  Preenche eventuais NaNs restantes com 0
    df_vetorizado = df_vetorizado.fillna(0)

    return df_vetorizado