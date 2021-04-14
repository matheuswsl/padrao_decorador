#!/bin/python3

import tkinter as tk

class LabelBotoes(tk.Frame):

    def __init__(self, janela, *args, **kwargs):
        self.janela = janela
        super().__init__(janela,*args, **kwargs)

    def criar_itens(self):
        texto = 'Testando o padrão Decorador'
        conteudo = tk.StringVar()
        texto_alterado = FuncaoBotoes(texto)
        conteudo.set(texto_alterado.texto)
        label = tk.Label(self.janela, textvariable = conteudo)
        label.grid(row=0,column=0,columnspan=3,sticky='news')
        negrito = tk.Button(self.janela, text='Negrito', command=(
                lambda: conteudo.set(FuncaoNegrito(texto_alterado).funcao_principal())))
        negrito.grid(row=1,column=0,sticky='news')
        italico = tk.Button(self.janela, text='Itálico', command=(
                lambda: conteudo.set(FuncaoItalico(texto_alterado).funcao_principal())))
        italico.grid(row=1,column=1,sticky='news')
        underline = tk.Button(self.janela, text='Grifado', command=(
                lambda: conteudo.set(FuncaoGrifado(texto_alterado).funcao_principal())))
        underline.grid(row=1,column=2,sticky='news')
        
    def grid(self, *args, **kwargs):
        super().grid(*args, **kwargs)

class FuncaoBotoes:

    def __init__(self, texto):
        self.texto = texto

    def funcao_principal(self):
        return self.texto

class FuncaoNegrito(FuncaoBotoes):

    def __init__(self, wraped):
        self.wraped = wraped

    def funcao_principal(self):
        self.wraped.texto = '<b>{}</b>'.format(self.wraped.funcao_principal())
        return self.wraped.texto

class FuncaoItalico(FuncaoBotoes):

    def __init__(self, wraped):
        self.wraped = wraped

    def funcao_principal(self):
        self.wraped.texto = '<i>{}</i>'.format(self.wraped.funcao_principal())
        return self.wraped.texto

class FuncaoGrifado(FuncaoBotoes):

    def __init__(self, wraped):
        self.wraped = wraped

    def funcao_principal(self):
        self.wraped.texto = '<u>{}</u>'.format(self.wraped.funcao_principal())
        return self.wraped.texto

if '__name__' == '__main__':
    janela = tk.Tk()
    frame = LabelBotoes(janela)
    frame.grid(row=0,column=0, sticky='news')
    frame.criar_itens()
    janela.mainloop()
