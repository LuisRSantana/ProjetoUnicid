import tkinter as tk
from tkinter import ttk

# Função para criar a interface
def criar_interface():
    # Janela principal
    root = tk.Tk()
    root.title("Cupcake App")
    root.geometry("800x600")
    root.configure(bg="black")

    # Barra de navegação
    nav_frame = tk.Frame(root, bg="black")
    nav_frame.pack(fill=tk.X, pady=10)

    menu_buttons = ["Home", "Sobre Nós", "Cardápios e Sabores", "Como Encomendar", "Depoimentos", "Login Site"]
    for button_text in menu_buttons:
        tk.Button(
            nav_frame,
            text=button_text,
            bg="black",
            fg="white",
            font=("Arial", 10, "bold"),
            bd=0,
            highlightthickness=0
        ).pack(side=tk.LEFT, padx=10)

    # Área para fotos
    foto_frame = tk.Frame(root, bg="black")
    foto_frame.pack(fill=tk.BOTH, expand=True, pady=20)

    tk.Label(
        foto_frame,
        text="Foto dos cupcakes",
        bg="black",
        fg="white",
        font=("Arial", 16, "bold")
    ).pack(expand=True)

    # Carrinhos de ação
    action_frame = tk.Frame(root, bg="black")
    action_frame.pack(fill=tk.X, pady=20)

    actions = ["Escolha seu Cupcake", "Fazer pedido", "Consulte Valores"]
    for action in actions:
        frame = tk.Frame(action_frame, bg="black")
        frame.pack(side=tk.LEFT, padx=30, expand=True)

        cart_icon = tk.Label(frame, text="🛒", bg="black", fg="white", font=("Arial", 24))
        cart_icon.pack()

        tk.Label(
            frame,
            text=action,
            bg="black",
            fg="white",
            font=("Arial", 12)
        ).pack()

    # Rodar o aplicativo
    root.mainloop()


# Executar a função
if __name__ == "__main__":
    criar_interface()
