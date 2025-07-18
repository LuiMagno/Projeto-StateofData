# utils/filtros.py

import pandas as pd

# 🎯 Colunas de cargo
CARGO_ATUAL = "2.f_cargo_atual"
CARGO_DESEJADO = "5.b_oportunidade_buscada"

#  Função para detectar linguagens diretamente do DataFrame
def detectar_linguagens(df: pd.DataFrame) -> list:
    return sorted([col for col in df.columns if col.startswith("4.d.")])

def detectar_bancos(df: pd.DataFrame) -> list:
    return sorted([col for col in df.columns if col.startswith("4.g.")])

def detectar_clouds(df: pd.DataFrame) -> list:
    return sorted([col for col in df.columns if col.startswith("4.h.")])

def detectar_bi_tools(df: pd.DataFrame) -> list:
    return sorted([col for col in df.columns if col.startswith("4.j.")])


# Mapeamento de sinônimos para buscas por cargo
MASTER_MAP = {
    "cientista": {
        "colunas": [CARGO_ATUAL, CARGO_DESEJADO],
        "sinonimos": [
            "Cientista de Dados", 
            "Data Scientist",
            "ML Engineer",
            "AI Engineer",
            "Machine Learning"
        ]
    },
    "analista": {
        "colunas": [CARGO_ATUAL, CARGO_DESEJADO],
        "sinonimos": [
            "Analista de Dados",
            "Data Analyst",
            "Analista BI",
            "BI Analyst"
        ]
    },
    "engenheiro": {
        "colunas": [CARGO_ATUAL],
        "sinonimos": [
            "Engenheiro de Dados",
            "Data Engineer",
            "Arquiteto de Dados",
            "Data Architect"
        ]
    }
}

# ⚠️ Inicialmente as linguagens estarão vazias, mas você vai preenchê-las depois no notebook com detectar_linguagens()
FILTROS_DISPONIVEIS = {
    "cargo_geral": MASTER_MAP,
    "cargo_atual": CARGO_ATUAL,
    "cargo_desejado": CARGO_DESEJADO,   
    "senioridade": "2.g_nivel",
    "experiencia_dados": "2.i_tempo_de_experiencia_em_dados",
    "experiencia_ti": "2.j_tempo_de_experiencia_em_ti",
    "modelo_trabalho_atual": "2.r_modelo_de_trabalho_atual",
    "modelo_trabalho_ideal": "2.s_modelo_de_trabalho_ideal",
    "faixa_salarial": "2.h_faixa_salarial",
    "uf_onde_mora": "1.i.1_uf_onde_mora",
    "regiao_onde_mora": "1.i.2_regiao_onde_mora",
    "satisfacao": "2.k_satisfeito_atualmente",

    # Será sobrescrito com detectar_linguagens(df)
    "linguagens_programacao": [],

    # Outros filtros 
    "bancos_de_dados": [],

    "clouds": [],

    "bi_tools": [],

    "planos_mudar_emprego": "2.n_planos_de_mudar_de_emprego_6m",
    "criterios_escolha_emprego": "2.o_criterios_para_escolha_de_emprego",
}

# 🚦 Função principal para aplicar os filtros
def aplicar_filtros(df: pd.DataFrame, filtros_dict: dict) -> pd.DataFrame:
    df_filtrado = df.copy()

    for chave, valor in filtros_dict.items():
        if not valor:
            continue

        #  Filtro de cargos por sinônimos
        if chave == "cargo_geral" and isinstance(valor, str) and valor in MASTER_MAP:
            config = MASTER_MAP[valor]
            cond = pd.Series(False, index=df_filtrado.index)
            for col in config["colunas"]:
                for termo in config["sinonimos"]:
                    cond = cond | df_filtrado[col].str.contains(termo, case=False, na=False)
            df_filtrado = df_filtrado[cond]

        #  Filtros com múltiplas colunas binárias (listas)
        elif isinstance(valor, list):
            for col in valor:
                if col in df_filtrado.columns:
                    df_filtrado = df_filtrado[df_filtrado[col] == 1.0]

        #  Filtros simples (campo:valor)
        elif chave in FILTROS_DISPONIVEIS:
            coluna = FILTROS_DISPONIVEIS[chave]
            if coluna in df_filtrado.columns:
                df_filtrado = df_filtrado[df_filtrado[coluna] == valor]

    return df_filtrado
