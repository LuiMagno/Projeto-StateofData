# utils/filtros.py
CARGO_ATUAL = "2.f_cargo_atual"
CARGO_DESEJADO = "5.b_oportunidade_buscada"

# Mapeamento de sinônimos para buscas
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

FILTROS_DISPONIVEIS = {
    #  Informações gerais do candidato
    "cargo_geral": MASTER_MAP,
    "cargo_atual": "2.f_cargo_atual",
    "cargo_desejado": "5.b_oportunidade_buscada",   
    "senioridade": "2.g_nivel",
    "experiencia_dados": "2.i_tempo_de_experiencia_em_dados",
    "experiencia_ti": "2.j_tempo_de_experiencia_em_ti",
    "modelo_trabalho_atual": "2.r_modelo_de_trabalho_atual",
    "modelo_trabalho_ideal": "2.s_modelo_de_trabalho_ideal",
    "faixa_salarial": "2.h_faixa_salarial",
    "uf_onde_mora": "1.i.1_uf_onde_mora",
    "regiao_onde_mora": "1.i.2_regiao_onde_mora",
    "satisfacao": "2.k_satisfeito_atualmente",

    #  Habilidades técnicas — Linguagens de Programação
    "linguagens_programacao": [
        "4.d.1_SQL",
        "4.d.2_R",
        "4.d.3_Python",
        "4.d.4_C/C++/C#",
        "4.d.5_.NET",
        "4.d.6_Java",
        "4.d.7_Julia",
        "4.d.8_SAS/Stata",
        "4.d.9_Visual Basic/VBA",
        "4.d.10_Scala",
        "4.d.11_Matlab",
        "4.d.12_Rust",
        "4.d.13_PHP",
        "4.d.14_JavaScript",
        "4.d.15_Não utilizo nenhuma das linguagens listadas"
    ],

    #  Habilidades técnicas — Bancos de Dados
    "bancos_de_dados": [
        "4.g.1_MySQL",
        "4.g.2_Oracle",
        "4.g.3_SQL SERVER",
        "4.g.4_Amazon Aurora ou RDS",
        "4.g.5_DynamoDB",
        "4.g.6_CoachDB",
        "4.g.8_MongoDB",
        "4.g.9_MariaDB",
        "4.g.12_PostgreSQL",
        "4.g.13_ElasticSearch",
        "4.g.22_Google BigQuery",
        "4.g.24_Amazon Redshift",
        "4.g.25_Amazon Athena",
        "4.g.26_Snowflake",
        "4.g.27_Databricks"
    ],

    #  Habilidades técnicas — Cloud Computing
    "clouds": [
        "4.h.1_Amazon Web Services (AWS)",
        "4.h.2_Google Cloud (GCP)",      # <-- valor real no dataset
        "4.h.3_Azure (Microsoft)",
        "4.h.4_Oracle Cloud",
        "4.h.5_IBM",
        "4.h.6_Servidores On Premise/Não utilizamos Cloud",
        "4.h.7_Cloud Própria"
    ],

    #  Ferramentas de BI
    "bi_tools": [
        "4.j.1_Microsoft PowerBI",
        "4.j.2_Qlik View/Qlik Sense",
        "4.j.3_Tableau",
        "4.j.4_Metabase",
        "4.j.5_Superset",
        "4.j.6_Redash",
        "4.j.7_Looker",
        "4.j.8_Looker Studio(Google Data Studio)",
        "4.j.9_Amazon Quicksight",
        "4.j.17_Fazemos todas as análises utilizando apenas Excel ou planilhas do google"
    ],

    #  Preferências e critérios culturais
    "planos_mudar_emprego": "2.n_planos_de_mudar_de_emprego_6m",
    "criterios_escolha_emprego": "2.o_criterios_para_escolha_de_emprego",
}
