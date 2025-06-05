import tkinter as tk
n_antigo = operacao = porcentual = 0

def add(n,tela):
    current = tela.get()
    tela.delete(0,tk.END)
    tela.insert(0,str(current) + str(n))

def delete(tela):
    tela.delete(0,tk.END)

def back(tela):
    current = tela.get().strip()
    new_current = ''
    for i in range(0,len(current)):
        if i >= (len(current) - 1):
            pass
        else:
            new_current = str(new_current) + str(current[i])
    current = new_current
    tela.delete(0,tk.END)
    tela.insert(0,str(current))

def porcentagem(tela):
    global n_antigo
    global porcentual
    current = tela.get()
    try:
        current = int(current) * int(n_antigo)/100
        porcentual = current
        print(current)
    except:
        current = float(current) * float(n_antigo)/100
        porcentual = current
        print(current)

def somar(tela):
    global operacao
    global n_antigo
    operacao = 'adicao'
    n_antigo = tela.get()
    tela.delete(0,tk.END)

def subtrair(tela):
    global operacao
    global n_antigo
    operacao = 'subtracao'
    n_antigo = tela.get()
    tela.delete(0,tk.END)

def multiplicar(tela):
    global operacao
    global n_antigo
    operacao = 'multiplicacao'
    n_antigo = tela.get()
    tela.delete(0,tk.END)

def dividir(tela):
    global operacao
    global n_antigo
    operacao = 'divisao'
    n_antigo = tela.get()
    tela.delete(0,tk.END)

def igual(tela):
    global operacao
    global n_antigo
    global porcentual
    if porcentual == 0:
        n_atual = tela.get()
    else:
        n_atual = porcentual
    if operacao == 'adicao':
        try:
            soma = float(n_antigo) + float(n_atual)
            tela.delete(0,tk.END)
            tela.insert(0,str(soma))
        except:
            tela.insert('ERRO!')
    elif operacao == 'subtracao':
        try:
            subtracao = float(n_antigo) - float(n_atual)
            tela.delete(0,tk.END)
            tela.insert(0,str(subtracao))
        except:
            tela.insert('ERRO!')
    elif operacao == 'multiplicacao':
        try:
            mult = float(n_antigo) * float(n_atual)
            tela.delete(0,tk.END)
            tela.insert(0,str(mult))
        except:
            tela.insert('ERRO!')
    elif operacao == 'divisao':
        try:
            mult = float(n_antigo) / float(n_atual)
            tela.delete(0,tk.END)
            tela.insert(0,str(mult))
        except:
            tela.insert('ERRO!')
    porcentual = 0