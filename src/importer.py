# src/importer.py

from eap import EAPNode, build_eap_tree, print_eap
import pandas as pd

## Importação EAP


def import_eap_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    eap_structure = []
    for line in lines:
        line = line.strip()
        if line:
            # Dividir a linha em número e título
            parts = line.split(' ', 1)
            if len(parts) == 2:
                number_part, title = parts
                level = number_part.count('.') - 1  # Ajuste aqui
                if level < 0:
                    level = 0  # Prevenir níveis negativos
                print(f"Nível: {level}, Título: {title}")  # Debugging
                eap_structure.append({'level': level, 'title': title})
            else:
                print(f"Formato da linha incorreto: {line}")
                continue

    eap_tree = build_eap_tree(eap_structure)
    return eap_tree


## Importação excel

def import_plano_de_acao_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        # Verificar colunas
        colunas = [
            "ID da Tarefa", "Descrição da Tarefa", "Responsável",
            "Data de Início", "Data de Término", "Status", "Prioridade"
        ]
        if not all(column in df.columns for column in colunas):
            print("Erro: A planilha não está no formato padrão.")
            return None
        # Dataframe para dicionários
        tasks = df.to_dict(orient='records')
        return tasks
    except Exception as e:
        print(f"Erro ao importar o plano de ação: {e}")
        return None