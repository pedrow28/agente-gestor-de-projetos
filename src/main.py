# src/main.py

import os
from dotenv import load_dotenv
from importer import import_eap_from_txt, import_plano_de_acao_excel
from eap import print_eap
from project import Task, Project
from storage import save_project, load_project

def main():
    # Carregar variáveis de ambiente
    load_dotenv()
    # openai.api_key = os.getenv('OPENAI_API_KEY')  # Não necessário neste teste

    print("Bem-vindo ao Agente de Gestão de Projetos!")
    print("Selecione uma opção:")
    print("1. Importar EAP de arquivo TXT")
    print("2. Importar Plano de Ação de arquivo Excel")
    print("3. Carregar projeto existente")
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
            project_name = input("Digite o nome do projeto: ")
            project = Project(project_name)
            for task_data in tasks:
                task = Task(
                    task_id=task_data['ID da Tarefa'],
                    description=task_data['Descrição da Tarefa'],
                    responsible=task_data['Responsável'],
                    start_date=task_data['Data de Início'],
                    end_date=task_data['Data de Término'],
                    status=task_data['Status'],
                    priority=task_data['Prioridade']
                )
                project.add_task(task)

                save_option = input("Deseja salvar o projeto? (s/n): ")
                if save_option.lower() == "s":
                    save_path = input("Digite o caminho para salvar o projeto (ex: data/projeto.json): ")
                    save_project(project, save_path)
                    print(f"Projeto salvo em {save_path}.")



            print(f"Projeto '{project.name}' criado com {len(project.tasks)} tarefas.")




            for task in tasks:
                print(task)
    
    elif choice == "3": ## Carregar projeto
        load_path = input("Digite o caminho do arquivo do projeto (ex: data/projeto.json): ")
        project = load_project(load_path)
        print(f"Projeto '{project.name}' carregado com {len(project.tasks)} tarefas.")
        # Aqui você pode adicionar opções para manipular o projeto carregado

    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
