from customtkinter import *

poligono = "Escolha"
calculo = "Escolha"
resultado = "---"

def selecionarp(value) :
    global poligono
    global calculo
    poligono = value

    trip.pack_forget()
    quap.pack_forget()
    retp.pack_forget()
    escolhac.set("Escolha")
    calculo = "Escolha"

    limpartela()

    if poligono == "Triângulo" :
        trip.pack(side="right", fill="both", expand=True)
        trip.grid_columnconfigure(1, weight=1)
        trip.grid_columnconfigure(2, weight=1)
        trip.grid_rowconfigure(1, weight=1)
        trip.grid_rowconfigure(8, weight=1)
    elif poligono == "Quadrado" :
        quap.pack(side="right", fill="both", expand=True)
        quap.grid_columnconfigure(1, weigth=1)
        trip.grid_columnconfigure(2, weight=1)
        quap.grid_rowconfigure(1, weight=1)
        quap.grid_rowconfigure(4, weight=1)
    elif poligono == "Retângulo" :
        retp.pack(side="right", fill="both", expand=True)
        retp.grid_columnconfigure(1, weight=1)
        retp.grid_columnconfigure(2, weight=1)
        retp.grid_rowconfigure(1, weight=1)
        retp.grid_rowconfigure(8, weight=1)

def limpartela() :

    bstri.grid_forget()
    bstrie.grid_forget()
    l1tri.grid_forget()
    l1trie.grid_forget()
    l2tri.grid_forget()
    l2trie.grid_forget()
    altri.grid_forget()
    altrie.grid_forget()
    protri.grid_forget()
    protrie.grid_forget()
    lqua.grid_forget()
    lquae.grid_forget()
    cret.grid_forget()
    crete.grid_forget()
    lret.grid_forget()
    lrete.grid_forget()
    proret.grid_forget()
    prorete.grid_forget()

def selecionarc (value) :
    global calculo
    calculo = value

    limpartela()

    if poligono == "Triângulo" :
        if calculo == "Perímetro" :
            bstri.grid(column=1, row=2, pady=(0, 10))
            bstrie.grid(column=1, row=3)

            l1tri.grid(column=1, row=4, pady=(150, 10), padx=350)
            l1trie.grid(column=1, row=5)

            l2tri.grid(column=1, row=6, pady=(150, 10),)
            l2trie.grid(column=1, row=7)
        elif calculo == "Área" :
            bstri.grid(column=1, row=2, pady=(0, 10))
            bstrie.grid(column=1, row=3)

            altri.grid(column=2, row=2, pady=(0, 10))
            altrie.grid(column=2, row=3)
        elif calculo == "Volume" :
            bstri.grid(column=1, row=2, pady=(0, 10))
            bstrie.grid(column=1, row=3)

            altri.grid(column=1, row=4, pady=(150, 10), padx=350)
            altrie.grid(column=1, row=5)

            protri.grid(column=1, row=6, pady=(150, 10))
            protrie.grid(column=1, row=7)
    elif poligono == "Quadrado" :
        lqua.grid(column=1, row=2, pady=(400, 10), padx=350)
        lquae.grid(column=1, row=3)
    elif poligono == "Retângulo" :
        if calculo == "Perímetro" :
            cret.grid(column=1, row=2, pady=(0, 10))
            crete.grid(column=1, row=3)

            lret.grid(column=1, row=4, pady=(100, 10), padx=410)
            lrete.grid(column=1, row=5)
        elif calculo == "Área" :
            cret.grid(column=1, row=2, pady=(0, 10))
            crete.grid(column=1, row=3)

            lret.grid(column=1, row=4, pady=(100, 10), padx=410)
            lrete.grid(column=1, row=5)
        elif calculo == "Volume" :
            cret.grid(column=1, row=2, pady=(0, 10))
            crete.grid(column=1, row=3)

            lret.grid(column=1, row=4, pady=(150, 10), padx=410)
            lrete.grid(column=1, row=5)

            proret.grid(column=1, row=6, pady=(150, 10))
            prorete.grid(column=1, row=7)


def calcular() :
    global resultado

    try :
        if poligono == "Triângulo" :
            b = float(bstrie.get())
            if calculo == "Perímetro" :
                l1 = float(l1trie.get())
                l2 = float(l2trie.get())
                resultado = f"{b + l1 + l2:.2f}"
            elif calculo == "Área" :
                a = float(altrie.get())
                resultado = f"{(b * a) / 2:.2f}²"
            elif calculo == "Volume" :
                a = float(altrie.get())
                p = float(protrie.get())
                resultado = f"{((b * a) / 2) * p:.2f}³"
        elif poligono == "Quadrado" :
            l = float(lquae.get())
            if calculo == "Perímetro" :
                resultado = l * 4
            elif calculo == "Área" :
                resultado = f"{l ** 2:.2f}²"
            elif calculo == "Volume" :
                resultado = f"{l ** 3:.2f}³"
        elif poligono == "Retângulo" :
            c = float(crete.get())
            l = float(lrete.get())
            if calculo == "Perímetro":
                resultado = (c * 2) + (l * 2)
            elif calculo == "Área" :
                resultado = f"{c * l:.2f}²"
            elif calculo == "Volume" :
                p = float(prorete.get())
                resultado = f"{(c * l) * p:.2f}³"


        resultl.configure(text=str(resultado))
            
    except ValueError :
        resultado = "Erro!!! Insira apenas números!"
        resultl.configure(text=str(resultado))

# Configuração de Aparência
set_appearance_mode("System")

# Criação da Janela Principal
janela = CTk(fg_color=("gray60", "#1b1a38"))
janela.title("Calculadora de Polígonos")
janela.after(1, lambda: janela.state("zoomed"))
inicial = CTkFrame(janela, fg_color="transparent")
inicial.pack(side="left", fill="y")
result = CTkFrame(janela, fg_color=("gray50", "#15152c"), height=150, corner_radius=15)
result.pack(side="bottom", fill="x")
trip = CTkFrame(janela, fg_color=("gray70", "#2E2C4E"), border_width=30, border_color=("gray60", "#1b1a38"), corner_radius=50)
trip.pack(side="right", fill="both", expand=True)
quap = CTkFrame(janela, fg_color=("gray70", "#2E2C4E"), border_width=30, border_color=("gray60", "#1b1a38"), corner_radius=50)
retp = CTkFrame(janela, fg_color=("gray70", "#2E2C4E"), border_width=30, border_color=("gray60", "#1b1a38"), corner_radius=50)

# Criação de Campos Iniciais

CTkLabel(
    inicial,
    text="Selecione o Polígono que será calculado",
    font=("Helvetica", 30),
    text_color=("gray90", "gray80")
).grid(column=1, row=1, pady=(400, 40), padx=(100, 100))

escolhap = CTkComboBox(
    inicial,
    values=["Escolha", "Triângulo", "Quadrado", "Retângulo"],
    command=selecionarp,
    font=("Arial", 35, ),
    width=250,
    height=55,
    text_color=("gray90", "gray60"),
    fg_color=("gray50", "#1a1933"),
    state="readonly",
    border_color=("gray55", "#15142c"),
    border_width=10,
    button_color=("gray55", "#15142c"),
    corner_radius=10
)
escolhap.grid(column=1, row=2, padx=(100, 100))
escolhap.set("Escolha")

escolhac = CTkComboBox(
    inicial,
    values=["Escolha", "Perímetro", "Área", "Volume"],
    command=selecionarc,
    font=("Arial", 35),
    width=250,
    height=55,
    text_color=("gray90", "gray60"),
    fg_color=("gray50", "#1a1933"),
    state="readonly",
    border_color=("gray55", "#15142c"),
    border_width=10,
    button_color=("gray55", "#15142c"),
    corner_radius=10
)
escolhac.grid(column=1, row=3, pady=(40, 0), padx=(100, 100))
escolhac.set("Escolha")

# Aparência do Resultado

resultl = CTkLabel(
    result,
    text=resultado,
    font=("Arial", 20),
    width=450,
    height=40,
    fg_color=("gray40", "#2E2C4E"),
    text_color=("gray90", "gray80"),
    corner_radius=10
)
resultl.grid(column=1, row=1, pady=20, padx=(200, 100))

resultb = CTkButton(
    result,
    text="Calcular",
    font=("Arial", 20),
    width=200,
    height=40,
    fg_color=("gray40", "#2E2C4E"),
    command=calcular,
    corner_radius=10,
    text_color=("gray90", "gray80"),
    hover_color=("gray20", "#2E2C4E")
)

resultb.grid(column=2, row=1, pady=20, padx=(100, 200))

# Criação da janela do Triângulo

bstri = CTkLabel(
    trip,
    text="Insira a base do seu triângulo:",
    font=("Arial", 25),
    justify="center",
)

bstrie = CTkEntry(
    trip,
    placeholder_text="Insira...",
    font=("Arial", 20),
    width=200,
    height=40
)

l1tri = CTkLabel(
    trip,
    text="Insira o primeiro lado do seu triângulo:",
    font=("Arial", 25),
    justify="center"
)

l1trie = CTkEntry(
    trip,
    placeholder_text="Insira...",
    font=("Arial", 20),
    width=200,
    height=40
)

l2tri = CTkLabel(
    trip,
    text="Insira o segundo lado do seu triângulo:",
    font=("Arial", 25)
)

l2trie = CTkEntry(
    trip,
    placeholder_text="Insira...",
    font=("Arial", 20),
    width=200,
    height=40
)

altri = CTkLabel(
    trip,
    text="Insira a altura do seu triângulo",
    font=("Arial", 25)
)

altrie = CTkEntry(
    trip,
    placeholder_text="Insira...",
    font=("Arial", 20),
    width=200,
    height=40
)

protri = CTkLabel(
    trip,
    text="Insira a profundidade do seu triângulo",
    font=("Arial", 25)
)

protrie = CTkEntry(
    trip,
    placeholder_text="Insira...",
    font=("Arial", 20),
    width=200,
    height=40
)

# Criação da janela do quadrado

lqua = CTkLabel(
    quap,
    text="Insira o comprimento do lado do seu quadrado",
    font=("Arial", 25)
)

lquae = CTkEntry(
    quap,
    placeholder_text="Insira...",
    font=("Arial", 20),
    width=200,
    height=40
)

# Criação da janela do retângulo

cret = CTkLabel(
    retp,
    text="Insira o comprimento do seu retângulo",
    font=("Arial", 25)
)

crete = CTkEntry(
    retp,
    placeholder_text="Insira...",
    font=("Arial", 20),
    width=200,
    height=40
)

lret = CTkLabel(
    retp,
    text="Insira o largura do seu retângulo",
    font=("Arial", 25)
)

lrete = CTkEntry(
    retp,
    placeholder_text="Insira...",
    font=("Arial", 20),
    width=200,
    height=40
)

proret = CTkLabel(
    retp,
    text="Insira a profundidade do seu retângulo",
    font=("Arial", 25)
)

prorete = CTkEntry(
    retp,
    placeholder_text="Insira...",
    font=("Arial", 20),
    width=200,
    height=40
)

# Iniciar a Aplicação
janela.mainloop()