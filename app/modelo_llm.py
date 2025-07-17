# app/modelo_llm.py

from transformers import pipeline
import textwrap

llm = pipeline("text2text-generation", model="google/flan-t5-large")

def gerar_explicacao_llm(vaga: dict, candidato: dict) -> str:
    """
    Gera explicação de compatibilidade entre vaga e candidato com modelo LLM.

    Args:
        vaga (dict): Dados da vaga.
        candidato (dict): Dados do candidato.

    Returns:
        str: Explicação gerada pela LLM.
    """
    # 🔻 Reduz o dicionário do candidato para os campos curtos
    candidato_reduzido = {
        k: v for k, v in candidato.items()
        if isinstance(v, (str, int, float)) and len(str(v)) < 80
    }

    # 🧠 Gera prompt enxuto
    prompt = f"""
Você é um especialista de RH técnico. Avalie o match entre a seguinte vaga e o seguinte candidato:

📌 Vaga:
{formatar_dicionario(vaga)}

👤 Candidato:
{formatar_dicionario(candidato_reduzido)}

Diga se esse candidato é adequado ou não, explicando os pontos fortes e eventuais lacunas.
"""

    # 🔒 Truncar para até 512 tokens (~2048 caracteres) com margem de segurança
    prompt = truncar_prompt(prompt, max_tokens=100)

    try:
        resposta = llm(prompt, max_new_tokens=100, do_sample=False)[0]["generated_text"]
        return resposta.strip()
    except Exception as e:
        return f"[Erro ao gerar explicação com LLM: {str(e)}]"

def formatar_dicionario(dados: dict) -> str:
    linhas = []
    for chave, valor in dados.items():
        nome = chave.split("_")[-1] if "_" in chave else chave
        linhas.append(f"- {nome}: {valor}")
    return "\n".join(linhas)

def truncar_prompt(prompt: str, max_tokens: int = 100) -> str:
    max_chars = max_tokens * 4  # margem segura (~400 caracteres)
    return prompt[:max_chars].rsplit("\n", 1)[0] + "\n..." if len(prompt) > max_chars else prompt
