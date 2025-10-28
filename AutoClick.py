# save_as: auto_click_sequence_hotkey.py
import pyautogui
import time
from pynput import keyboard

pyautogui.FAILSAFE = True  # mover o mouse para (0,0) também interrompe

# Flag de controle
stop_flag = False

# ----------------------------
# Função para capturar pontos
# ----------------------------
def capturar_pontos():
    print("=== CAPTURA DE PONTOS ===")
    print("Mova o mouse até cada ponto desejado e pressione Enter para registrar.")
    print("Quando terminar, digite 'fim' e pressione Enter para encerrar.\n")

    pontos = []
    while True:
        val = input("Pressione Enter para capturar ou digite 'fim' para sair: ").strip().lower()
        if val == "fim":
            break
        pos = pyautogui.position()
        pontos.append(pos)
        print(f"Ponto registrado: ({pos.x}, {pos.y})")
    return pontos


# ----------------------------
# Listener de teclado (F8)
# ----------------------------
def on_press(key):
    global stop_flag
    try:
        if key == keyboard.Key.f8:
            print("\n🛑 Tecla F8 pressionada — parando o script com segurança...")
            stop_flag = True
            return False  # encerra o listener
    except:
        pass


# ----------------------------
# Loop de cliques
# ----------------------------
def loop_cliques(pontos):
    global stop_flag
    print("\n=== MODO CLIQUES ===")
    print("O script vai começar em 3 segundos...")
    print("Pressione F8 ou mova o mouse para o canto superior esquerdo (0,0) para parar.")
    time.sleep(3)

    try:
        while not stop_flag:
            for pos in pontos:
                if stop_flag:
                    break
                pyautogui.moveTo(pos.x, pos.y, duration=0.05)
                pyautogui.click()
                print(f"Clique em ({pos.x}, {pos.y})")
                time.sleep(0.1)

    except pyautogui.FailSafeException:
        print("\n🛑 Script interrompido (FAILSAFE ativado).")
    print("✅ Loop encerrado com segurança.")


# ----------------------------
# Programa principal
# ----------------------------
if __name__ == "__main__":
    pontos = capturar_pontos()
    if not pontos:
        print("Nenhum ponto registrado. Encerrando.")
        quit()

    # Inicia listener da tecla F8 em paralelo
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    loop_cliques(pontos)