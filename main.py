import colorama, random
from colorama import Fore, Style

# Inicializa o colorama (necessário para funcionar em diferentes sistemas)
colorama.init()

def exibir_status_reservatorio(nivel_selecionado):
    """
    Função responsável por mapear o nível à cor e exibir a mensagem.
    """
    # Lista de dicionários para organizar os dados do sistema
    monitoramento = [
        {"nivel": 1, "situacao": "MUITO BAIXO (CRÍTICO)", "cor": Fore.RED},
        {"nivel": 2, "situacao": "BAIXO", "cor": Fore.YELLOW},
        {"nivel": 3, "situacao": "MÉDIO", "cor": Fore.GREEN},
        {"nivel": 4, "situacao": "ALTO", "cor": Fore.CYAN},
        {"nivel": 5, "situacao": "MUITO ALTO (ALERTA)", "cor": Fore.BLUE},
    ]

    # Procura o nível correspondente na lista
    for item in monitoramento:
        if item["nivel"] == nivel_selecionado:
            print(f"Status do Reservatório: {item['cor']}{item['situacao']}{Style.RESET_ALL}")
            return

    print("Nível inválido informado.")

# --- Simulação de Ambiente Real ---
def simular_sistema():
    print("=== SISTEMA DE MONITORAMENTO DE ÁGUA - INICIANDO... ===\n")
 
    # Lista com os níveis possíveis
    niveis_disponiveis = [1, 2, 3, 4, 5]

    # Seleciona de forma randômica apenas UM nível da lista
    nivel_sorteado = random.choice(niveis_disponiveis)

       
    print("Checando sensores...")
    print(f'Após leitura dos sensores, foi detectado o nível: {nivel_sorteado}')

    # Chama a função para exibir o status com a cor correspondente
    exibir_status_reservatorio(nivel_sorteado)
    
    print("\n=== MONITORAMENTO CONCLUÍDO ===")

if __name__ == "__main__":
    simular_sistema()