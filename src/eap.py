# src/eap.py

class EAPNode:
    def __init__(self, title):
        self.title = title
        self.subtasks = []

    def add_subtask(self, node):
        self.subtasks.append(node)

def build_eap_tree(eap_structure):
    root = None
    stack = []
    for item in eap_structure:
        node = EAPNode(item['title'])
        level = item['level']

        if level == 0:
            root = node
            stack = [node]
        else:
            while len(stack) > level:
                stack.pop()
            if stack:
                parent = stack[-1]
                parent.add_subtask(node)
                stack.append(node)
            else:
                print(f"Erro: Nível hierárquico inconsistente ao processar '{node.title}' no nível {level}.")
                continue
    return root

def print_eap(node, level=0):
    print('    ' * level + '- ' + node.title)
    for subtask in node.subtasks:
        print_eap(subtask, level + 1)
