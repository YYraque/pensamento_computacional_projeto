import tkinter as tk
from tkinter import messagebox, simpledialog

# --- VARIÁVEIS GLOBAIS (Para salvar os dados na memória) ---
veiculos = []  # Lista para armazenar os veículos cadastrados (máximo 3)
dados_customizacao = {}
agendamento_compra = {}
agendamento_test_drive = {}
dados_atendimento = {}
loja_fisica = ""
feedback_reclamacao = {}

# --- FUNÇÕES DAS OPÇÕES DO MENU ---

def cadastrar_veiculo():
    if len(veiculos) >= 3:
        messagebox.showerror("Erro", "❌ Sistema cheio! Limite de 3 itens Atingido.")
        return
    
    # Substitutos para o input() -> Caixas de diálogo de texto
    nome = simpledialog.askstring("Cadastro", "Digite o Nome do Veículo:")
    if not nome: return # Se o usuário cancelar, interrompe
    
    descricao = simpledialog.askstring("Cadastro", "Digite a Descrição do Produto:")
    marca = simpledialog.askstring("Cadastro", "Digite a Marca do Veículo:")
    
    veiculos.append({"nome": nome, "descricao": descricao, "marca": marca})
    messagebox.showinfo("Sucesso", f"🚗 Veículo '{nome}' cadastrado com sucesso!")

def escolher_customizacao():
    cor = simpledialog.askstring("Customização", "Digite a Cor que Deseja:")
    aro = simpledialog.askstring("Customização", "Digite o Modelo do aro que Deseja:")
    aerofolio = simpledialog.askstring("Customização", "Digite o Modelo de Aerofólio que Deseja:")
    
    global dados_customizacao
    dados_customizacao = {"cor": cor, "aro": aro, "aerofolio": aerofolio}
    messagebox.showinfo("Sucesso", "🎨 Customização salva!")

def escolher_horario():
    horario = simpledialog.askstring("Horário", "Selecione o horário (Ex: 14:00):")
    agendamento_compra["horario"] = horario
    messagebox.showinfo("Sucesso", f"⏰ Horário {horario} selecionado!")

def finalizar_agendamento():
    data = simpledialog.askstring("Finalizar", "Digite o dia e o mês que Deseja Realizar a Compra:")
    agendamento_compra["data"] = data
    messagebox.showinfo("Sucesso", "📅 Agendamento de compra finalizado!")

def agendar_test_drive():
    horario = simpledialog.askstring("Test-Drive", "Selecione o horário do Test-Drive:")
    agendamento_test_drive["horario"] = horario
    messagebox.showinfo("Sucesso", f"🏎️ Test-drive agendado para às {horario}!")

def finalizar_test_drive():
    data = simpledialog.askstring("Finalizar Test-Drive", "Digite o dia e o mês que Deseja Realizar o Test-Drive:")
    agendamento_test_drive["data"] = data
    messagebox.showinfo("Sucesso", "📅 Agendamento de Test-Drive finalizado!")

def chat_atendente():
    nome = simpledialog.askstring("Atendimento", "Digite seu nome:")
    email = simpledialog.askstring("Atendimento", "Digite seu email:")
    telefone = simpledialog.askstring("Atendimento", "Digite seu Número de Telefone:")
    
    global dados_atendimento
    dados_atendimento = {"nome": nome, "email": email, "telefone": telefone}
    messagebox.showinfo("Encaminhando", "💬 Encaminhando para um chat com um atendente... Aguarde.")

def escolher_loja():
    global loja_fisica
    loja_fisica = simpledialog.askstring("Loja Física", "Digite o Endereço da Loja Física:")
    messagebox.showinfo("Sucesso", f"📍 Loja selecionada: {loja_fisica}")

def enviar_feedback():
    feed = simpledialog.askstring("Feedback", "Digite aqui sua experiência:")
    reclamacao = simpledialog.askstring("Reclamação", "Conte-nos o porquê sua experiência foi ruim (Se aplicável):")
    
    global feedback_reclamacao
    feedback_reclamacao = {"feedback": feed, "reclamacao": reclamacao}
    messagebox.showinfo("Obrigado", "🙏 Feedback enviado com sucesso!")

def sair_sistema():
    if messagebox.askyesno("Sair", "Deseja realmente sair do sistema?"):
        janela.destroy() # Fecha a janela principal do Tkinter

# --- CONFIGURAÇÃO DA JANELA PRINCIPAL ---

janela = tk.Tk()
janela.title("Primus Motors - Sistema de Agendamento")
janela.geometry("500x550")
janela.configure(bg="#2c3e50") # Cor de fundo estilosa (Azul escuro)

# Título Principal na Tela
titulo = tk.Label(janela, text="Primus Motors", font=("Helvetica", 20, "bold"), fg="#ecf0f1", bg="#2c3e50")
titulo.pack(pady=15)

subtitulo = tk.Label(janela, text="Selecione a opção desejada no menu abaixo:", font=("Helvetica", 10), fg="#bdc3c7", bg="#2c3e50")
subtitulo.pack(pady=5)

# Estilo padrão dos botões
estilo_botao = {
    "font": ("Helvetica", 10, "bold"),
    "fg": "#ffffff",
    "bg": "#34495e",
    "activebackground": "#1abc9c",
    "activeforeground": "#ffffff",
    "width": 45,
    "bd": 2,
    "relief": "groove"
}

# --- CRIAÇÃO DOS BOTÕES ---
tk.Button(janela, text="1 - Cadastrar veículo, por marcas", command=cadastrar_veiculo, **estilo_botao).pack(pady=4)
tk.Button(janela, text="2 - Escolhendo a cor e modificações", command=escolher_customizacao, **estilo_botao).pack(pady=4)
tk.Button(janela, text="3 - Escolhendo o horário", command=escolher_horario, **estilo_botao).pack(pady=4)
tk.Button(janela, text="4 - Finalizar agendamento do horário", command=finalizar_agendamento, **estilo_botao).pack(pady=4)
tk.Button(janela, text="5 - Agendar test-drive", command=agendar_test_drive, **estilo_botao).pack(pady=4)
tk.Button(janela, text="6 - Finalizar agendamento do test-drive", command=finalizar_test_drive, **estilo_botao).pack(pady=4)
tk.Button(janela, text="7 - Encaminhar para um chat com um atendente", command=chat_atendente, **estilo_botao).pack(pady=4)
tk.Button(janela, text="8 - Escolher loja física onde finalizar compra", command=escolher_loja, **estilo_botao).pack(pady=4)
tk.Button(janela, text="9 - Enviar feedback/Enviar Reclamação", command=enviar_feedback, **estilo_botao).pack(pady=4)

# Botão de Sair destacado em vermelho
botao_sair = tk.Button(janela, text="0 - Sair", command=sair_sistema, font=("Helvetica", 10, "bold"), fg="#ffffff", bg="#c0392b", activebackground="#e74c3c", width=45, bd=2, relief="groove")
botao_sair.pack(pady=15)

# Inicia o loop da interface gráfica
janela.mainloop()