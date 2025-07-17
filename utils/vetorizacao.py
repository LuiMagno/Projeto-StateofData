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

    # 🟡 Mapeia tempo de experiência para números
    mapa_experiencia = {
        "Menos de 1 ano": 0.5,
        "de 1 a 2 anos": 1.5,
        "de 2 a 3 anos": 2.5,
        "de 3 a 4 anos": 3.5,
        "de 4 a 5 anos": 4.5,
        "de 5 a 6 anos": 5.5,
        "de 6 a 7 anos": 6.5,
        "de 7 a 8 anos": 7.5,
        "de 8 a 9 anos": 8.5,
        "de 9 a 10 anos": 9.5,
        "Mais de 10 anos": 12
    }

    if "2.i_tempo_de_experiencia_em_dados" in df.columns:
        df["experiencia_dados_anos"] = df["2.i_tempo_de_experiencia_em_dados"].map(mapa_experiencia)
    if "2.j_tempo_de_experiencia_em_ti" in df.columns:
        df["experiencia_ti_anos"] = df["2.j_tempo_de_experiencia_em_ti"].map(mapa_experiencia)

    #  Remove colunas textuais que foram convertidas
    df = df.drop(columns=["2.i_tempo_de_experiencia_em_dados", "2.j_tempo_de_experiencia_em_ti"], errors="ignore")

    #  Converte colunas categóricas para dummies
    df_dummies = pd.get_dummies(df, drop_first=False)

    #  Remove colunas completamente nulas (caso haja)
    df_vetorizado = df_dummies.dropna(axis=1, how="all")

    #  Remove colunas completamente nulas (caso haja)
    df_vetorizado = df_dummies.dropna(axis=1, how="all")

    #  Preenche eventuais NaNs restantes com 0
    df_vetorizado = df_vetorizado.fillna(0)

    return df_vetorizado
