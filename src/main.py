# src/main.py

import os
from dotenv import load_dotenv
from importer import import_eap_from_txt, import_plano_de_acao_excel
from eap import print_eap

def main():
    # Carregar variáveis de ambiente
    load_dotenv()
    # openai.api_key = os.getenv('OPENAI_API_KEY')  # Não necessário neste teste

    print("Bem-vindo ao Agente de Gestão de Projetos!")
    print("Selecione uma opção:")
    print("1. Importar EAP de arquivo TXT")
    print("2. Importar Plano de Ação de arquivo Excel")
    choice = input("Opção: ")

    if choice == "1": ## Importar EAP

        # Exemplo de importação de EAP
        eap_file = input("Digite o caminho para o arquivo TXT com a EAP: ")
        eap_tree = import_eap_from_txt(eap_file)
        if eap_tree:
            print("EAP importada com sucesso!")
            print_eap(eap_tree)
        else:
            print("Falha ao importar a EAP.")

    elif choice == "2": ## Importar plano de ação
        excel_file = input("Digite o caminho para o arquivo Excel com o Plano de Ação: ")
        tasks = import_plano_de_acao_excel(excel_file)
        if tasks:
            print("Plano de Ação importado com sucesso!")
            # Exibir as tarefas importadas
            for task in tasks:
                print(task)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
