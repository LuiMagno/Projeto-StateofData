# app/recomendador.py
import pandas as pd
from utils.filtros import FILTROS_DISPONIVEIS

class RecomendadorRH:
    def __init__(self, df: pd.DataFrame):
        self.df_original = df.copy()
        self.df_filtrado = df.copy()

    def aplicar_filtros(self, criterios: dict):
        """Aplica os filtros especificados e retorna apenas os candidatos que atendem a TODOS os critérios"""
        df_trabalho = self.df_original.copy()
        filtro_geral = pd.Series(True, index=df_trabalho.index)

        print("\n[LOG] Aplicando filtros com interseção (AND):")

        for chave, valor in criterios.items():
            if chave == "cargo_geral":
                try:
                    if valor in FILTROS_DISPONIVEIS["cargo_geral"]:
                        mapa = FILTROS_DISPONIVEIS["cargo_geral"][valor]
                        filtro_local = pd.Series(False, index=df_trabalho.index)

                        for coluna in mapa["colunas"]:
                            if coluna not in df_trabalho.columns:
                                print(f"⚠️ Coluna '{coluna}' não encontrada")
                                continue

                            for termo in mapa["sinonimos"]:
                                matches = df_trabalho[coluna].astype(str).str.contains(
                                    termo, case=False, na=False
                                )
                                filtro_local |= matches

                        filtro_geral &= filtro_local
                        print(f"✅ Cargo geral '{valor}': {filtro_local.sum()} matches")
                except Exception as e:
                    print(f"⚠️ Erro ao processar cargo_geral: {str(e)}")
                continue

            # Processa outros filtros
            filtro_local = self._gerar_filtro(df_trabalho, chave, valor)
            filtro_geral &= filtro_local

        self.df_filtrado = df_trabalho[filtro_geral]
        print(f"\n🎯 Total de candidatos qualificados (todos critérios): {len(self.df_filtrado)}")
        return self.df_filtrado

    def _gerar_filtro(self, df, chave, valor):
        """Gera um filtro booleano para um critério"""
        if chave not in FILTROS_DISPONIVEIS:
            print(f"❌ Filtro '{chave}' não configurado")
            return pd.Series(True, index=df.index)  # Não filtra ninguém por padrão

        config = FILTROS_DISPONIVEIS[chave]

        if isinstance(config, list):
            print(f"🔧 Processando múltiplos valores para {chave}")
            filtro = pd.Series(False, index=df.index)
            for item in valor:
                cols_match = [c for c in config if str(item).lower() in c.lower()]
                for col in cols_match:
                    if col not in df.columns:
                        print(f"⚠️ Coluna '{col}' não encontrada")
                        continue
                    matches = df[col].fillna(0) >= 1
                    filtro |= matches
                    print(f"✅ {matches.sum()} matches em {col}")
            return filtro
        else:
            print(f"🔍 Processando filtro simples: {chave}")
            if config not in df.columns:
                print(f"⚠️ Coluna '{config}' não encontrada")
                return pd.Series(True, index=df.index)
            matches = df[config].astype(str).str.contains(str(valor), case=False, na=False)
            print(f"✅ {matches.sum()} matches em {config}")
            return matches

    def top_n(self, n=10):
        """Retorna os top N candidatos"""
        return self.df_filtrado.head(n)

    def contar_candidatos(self):
        """Retorna o número de candidatos filtrados"""
        return len(self.df_filtrado)
