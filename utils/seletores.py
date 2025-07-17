import pandas as pd

def selecionar_colunas_recomendador(df: pd.DataFrame) -> pd.DataFrame:
    """
    Seleciona e retorna um subconjunto temático de colunas para recomendação de perfis.

    Args:
        df (pd.DataFrame): DataFrame original com todas as colunas da pesquisa.

    Returns:
        pd.DataFrame: DataFrame reduzido com as colunas selecionadas.
    """
    colunas_por_grupo = {
        "metadados": [col for col in df.columns if col.startswith('0.a')],
        "info_pessoal": [
            '1.b_genero', '1.c_cor/raca/etnia', '1.d_pcd', '1.g_vive_no_brasil',
            '1.h_pais_onde_mora', '1.i_estado_onde_mora', '1.l_nivel_de_ensino', '1.m_área_de_formação'
        ],
        "perfil_profissional": [
            '2.a_situação_de_trabalho', '2.d_atua_como_gestor', '2.e_cargo_como_gestor',
            '2.f_cargo_atual', '2.g_nivel', '2.h_faixa_salarial',
            '2.i_tempo_de_experiencia_em_dados', '2.j_tempo_de_experiencia_em_ti',
            '2.s_modelo_de_trabalho_ideal', '2.t_atitude_em_caso_de_retorno_presencial', '2.r_modelo_de_trabalho_atual'
        ],
        "gestor": ['3.c_responsabilidades_como_gestor', '3.d_desafios_como_gestor'],
        "funcao": ['4.a_funcao_de_atuacao', '4.a.1_atuacao_em_dados'],
        "ferramentas": [col for col in df.columns if col.startswith('4.b')],
        "fontes": [col for col in df.columns if col.startswith('4.c')],
        "linguagens": [col for col in df.columns if col.startswith('4.d')],
        "bancos": [col for col in df.columns if col.startswith('4.g')],
        "cloud": [col for col in df.columns if col.startswith('4.h')],
        "ia_generativa": [col for col in df.columns if col.startswith('4.l')],
        "copilot": [col for col in df.columns if col.startswith('4.m')],
        "oportunidade": ['5.b_oportunidade_buscada'],
        "eng_atividades": [col for col in df.columns if col.startswith('6.a')],
        "eng_etl": [col for col in df.columns if col.startswith('6.b')],
        "eng_datalake": [col for col in df.columns if col.startswith('6.d')],
        "eng_datawarehouse": [col for col in df.columns if col.startswith('6.f')],
        "eng_qualidade": [col for col in df.columns if col.startswith('6.g')],
        "ana_atividades": [col for col in df.columns if col.startswith('7.a')],
        "ana_ferramentas": [col for col in df.columns if col.startswith('7.b')],
        "ana_autonomia": [col for col in df.columns if col.startswith('7.c')],
        "ds_atividades": [col for col in df.columns if col.startswith('8.a')],
        "ds_tecnicas": [col for col in df.columns if col.startswith('8.b')],
        "ds_tecnologias": [col for col in df.columns if col.startswith('8.c')],
    }

    colunas_selecionadas = sum(colunas_por_grupo.values(), [])
    return df[colunas_selecionadas].copy()
