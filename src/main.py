# src/main.py

import os
from dotenv import load_dotenv
from importer import import_eap_from_txt
from eap import print_eap

def main():
    # Carregar variáveis de ambiente
    load_dotenv()
    # openai.api_key = os.getenv('OPENAI_API_KEY')  # Não necessário neste teste

    print("Bem-vindo ao Agente de Gestão de Projetos!")

    # Exemplo de importação de EAP
    eap_file = input("Digite o caminho para o arquivo TXT com a EAP: ")
    eap_tree = import_eap_from_txt(eap_file)
    if eap_tree:
        print("EAP importada com sucesso!")
        print_eap(eap_tree)
    else:
        print("Falha ao importar a EAP.")

if __name__ == "__main__":
    main()
