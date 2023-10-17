# -*- coding: utf-8 -*-
"""
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y4M9k1EKJRbJALbeyjJioy_P8o3U7-LL
"""

from collections import Counter
import matplotlib.pyplot as plt
from os import name

class Tarefa:

  def __init__(self, nome, prioridade, status="A Fazer"):
    self.nome = nome
    self.prioridade = prioridade
    self.status = status
    self.dependencias = []


  def adicionar_dependencia(self, tarefa):
    self.dependencias.append(tarefa)


  def concluir_tarefa(self):
    self.status = "Concluído"


  def atualizar_status(self, novo_status):
    self.novo_status = novo_status

class Projeto:

  def __init__(self, nome):
    self.nome = nome
    self.tarefas = []
    self.subprojetos = []


  def adicionar_tarefa(self, tarefa):
    self.tarefas.append(tarefa)


  def remover_tarefa(self, tarefa):
    if tarefa in self.tarefas:
      self.tarefas.remove(tarefa)


  def concluir_tarefa(self, tarefa):
    if tarefa in self.tarefas:
      tarefa.concuir_tarefa()


  def atualizar_status_tarefa(self, tarefa, novo_status):
    if tarefa in self.tarefas:
      tarefa.atualizar_status(novo_status)


  def visualizacao_tarefas(self):
    status_tarefas = [tarefa.status for tarefa in self.tarefas]
    prioridades_tarefas = [tarefa.prioridade for tarefa in self.tarefas]

    contagem_status = Counter(status_tarefas)
    contagem_prioridades = Counter(prioridades_tarefas)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.bar(contagem_status.keys(), contagem_status.values(), color=['red', 'yellow', 'green'])
    plt.title('Status das Tarefas')
    plt.xlabel('Status')
    plt.ylabel('Número de Tarefas')
    plt.subplot(1, 2, 2)
    plt.bar(contagem_prioridades.keys(), contagem_prioridades.values(), color=['blue', 'orange', 'purple'])
    plt.title('Prioridades das Tarefas')
    plt.xlabel('Prioridade')
    plt.ylabel('Número de Tarefas')
    plt.tight_layout()
    plt.show()

def criar_tarefa():
  nome = input("Nome da tarefa: ")
  prioridade = input("Prioridade da Tarefa ('Baixa' - 'Média' - 'Urgente'): ")
  status = input("Status da Tarefas ('A Fazer' - 'Em Andamento' - 'Concluida'): ")
  return Tarefa(nome, prioridade, status)




def menu_adicionar_tarefa(projeto):
  tarefa = criar_tarefa()
  projeto.adicionar_tarefa(tarefa)
  print(f'Tarefa {tarefa.nome} adicionada ao projeto.')



def menu_remover_tarefa(projeto):
  nome_tarefa = input('Tarefa que deseja remover: ')
  tarefa_encontrada = None

  for tarefa in projeto.tarefas:
    if tarefa.nome == nome_tarefa:
      tarefa_encontrada = tarefa
      break

  if tarefa_encontrada:
    projeto.remover_tarefa(tarefa_encontrada)
    print(f'Tarefa {tarefa_encontrada.nome} removida com sucesso!')
  else:
    print('Tarefa não encontrada.')



def menu_concluir_tarefa(projeto):
  nome_tarefa = input("Tarefa a ser Concluída: ")
  terefa_encontrada = None

  for tarefa in projeto.tarefa:
    if tarefa.nome == nome_tarefa:
      tarefa_encontrada = tarefa
      break

  if tarefa_encontrada:
    projeto.concluir_tarefa(tarefa_encontrada)
    print(f'Tarefa {tarefa_encontrada.nome} Concluída!')
  else:
    print('Tarefa não encontrada.')



def menu_atualizar_status_tarefa(projeto):
  nome_tarefa = input('Farefa a ser Atualizada: ')
  tarefa_encontrada = None

  for tarefa in projeto.tarefas:
    if tarefa.nome == nome_tarefa:
      tarefa_encontrada = tarefa
      break

  if tarefa_encontrada:
    novo_status = input("Digite as Opções ('A Fazer' - 'Em Andamento' - 'Concluida')")
    projeto.atualizar_status_tarefa(tarefa_encontrada, novo_status)
    print(f'Status da Tarefa {tarefa_encontrada.nome} atualizada para {novo_status}.')
  else:
    print('Tarefa não encontrada.')

def main():
  projeto_principal = Projeto('To do List')

  while True:
    print("\n----- MENU -----")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Concluir Tarefas")
    print("4. Atualizar Status da Tarefa")
    print("5. Visualizar Tarefas")
    print("6. SAIR")

    escolha = input("Escolha uma Opção: ")
    if escolha == '1':
      menu_adicionar_tarefa(projeto_principal)

    elif escolha == '2':
      menu_remover_tarefa(projeto_principal)

    elif escolha == '3':
      menu_concluir_tarefa(projeto_principal)

    elif escolha == '4':
      menu_atualizar_status_tarefa(projeto_principal)

    elif escolha == '5':
      projeto_principal.visualizacao_tarefas()

    elif escolha == '6':
      print("Programa Encerrado")
      break

    else:
      print("Opção Inválida")

  if name == 'main':
    main()

main()

