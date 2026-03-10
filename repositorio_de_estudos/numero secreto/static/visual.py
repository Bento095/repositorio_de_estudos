
import sys


def exibir_titulo():
    
    print("\n꒻ꄲꍌꄲ ꒯ꄲ ꋊ꒤ꂵꏂꋪꄲ ꇙꏂꉔꋪꏂ꓄ꄲ\n" \
    "\n")

def exibir_opcoes():
    print("1 - Jogar")
    print("2 - Sair")
    numero = input("Escolha uma opção: ")
    return numero


        
def sair():
    print("Encerrando...")
    sys.exit()
