import tkinter as tk
n_antigo = operacao = percentual = count = 0

def add(n,tela):
    global count
    if count != 0:
        tela.delete(0, tk.END)
        count = 0
    current = tela.get()
    if n =='.' and n in current:
        pass
    else:
        tela.delete(0,tk.END)
        tela.insert(0,str(current) + str(n))

def delete(tela):
    tela.delete(0,tk.END)

def back(tela):
    global count
    if count == 0:
        current = tela.get().strip()
        current = current[:-1]
        tela.delete(0,tk.END)
        tela.insert(0,str(current))
    else:
        pass

def porcentagem(tela):
    global n_antigo
    global percentual
    current = tela.get()
    try:
        current = int(current) * int(n_antigo)/100
        percentual = current
        print(current)
    except:
        current = float(current) * float(n_antigo)/100
        percentual = current
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
    global percentual
    global count
    if percentual == 0:
        n_atual = tela.get()
    else:
        n_atual = percentual
    if operacao == 'adicao':
        try:
            soma = float(n_antigo) + float(n_atual)
            if int(soma) == float(soma):
                soma = int(soma)
            tela.delete(0,tk.END)
            tela.insert(0,str(soma))
        except:
            tela.insert('ERRO!')
    elif operacao == 'subtracao':
        try:
            sub = float(n_antigo) - float(n_atual)
            if int(sub) == float(sub):
                sub = int(sub)
            tela.delete(0,tk.END)
            tela.insert(0,str(sub))
        except:
            tela.insert('ERRO!')
    elif operacao == 'multiplicacao':
        try:
            mult = float(n_antigo) * float(n_atual)
            if int(mult) == float(mult):
                mult = int(mult)
            tela.delete(0,tk.END)
            tela.insert(0,str(mult))
        except:
            tela.insert('ERRO!')
    elif operacao == 'divisao':
        try:
            div = float(n_antigo) / float(n_atual)
            if int(div) == float(div):
                div = int(div)
            tela.delete(0,tk.END)
            tela.insert(0,str(div))
        except:
            tela.insert('ERRO!')
    else:
        pass
    percentual = 0
    count += 1