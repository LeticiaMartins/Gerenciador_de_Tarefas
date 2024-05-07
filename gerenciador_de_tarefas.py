
#interagir com o usuário
def interagir_usuario(): 
  tarefas = []

  while True:
    print("\n=== PAINEL DE CONTROLE ===")
    print("1. Adicionar nova tarefa")
    print("2. Visualizar todas as tarefas")
    print("3. Marcar uma tarefa como concluída")
    print("4. Remover uma tarefa")
    print("5. Sair do programa")

    acao = int(input("O que você deseja fazer agora? "))

    if acao == 1:
      nova_tarefa = input("Digite a nova tarefa: ")
      add_tarefa(tarefas, nova_tarefa)
    elif acao == 2:
      visualizar_tarefas(tarefas)
    elif acao == 3:
      visualizar_tarefas(tarefas)
      indice = int(input("Digite o número da tarefa concluída: "))
      marcar_tarefa_concluida(tarefas, indice)
    elif acao == 4:
      visualizar_tarefas(tarefas)
      indice = int(input("Digite o número da tarefa a ser removida: "))
      remover_tarefa(tarefas, indice)
    elif acao == 5:
      break
    else:
      print("Opção inválida. Por favor, escolha uma opção válida.")

#Adicionar tarefa
def add_tarefa(tarefas, descricao):
  tarefas.append({'descricao': descricao, 'concluida': False})
  print("Tarefa adicionada com sucesso!")

#Visualizar tarefas
def visualizar_tarefas(tarefas):
  if not tarefas:
        print("Nenhuma tarefa para mostrar.")
  else:
    print("Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
      print(f"{i}. {'[x]' if tarefa['concluida'] else '[ ]'} {tarefa['descricao']}")

#Marcar tarefa como concluida
def marcar_tarefa_concluida(tarefas, indice):
    if 1 <= indice <= len(tarefas):
        tarefas[indice - 1]['concluida'] = True
        print("Tarefa marcada como concluída.")
    else:
        print("Índice da tarefa inválido.")

#Remover tarefa
def remover_tarefa(tarefas, indice):
    if 1 <= indice <= len(tarefas):
        tarefas.pop(indice - 1)
        print("Tarefa removida com sucesso.")
    else:
        print("Índice da tarefa inválido.")

interagir_usuario()