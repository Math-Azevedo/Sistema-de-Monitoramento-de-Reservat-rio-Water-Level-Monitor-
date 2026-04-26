# 🌊 Sistema de Monitoramento de Reservatório (Water Level Monitor)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

Este projeto é um simulador de terminal desenvolvido para monitorar os níveis de água de um reservatório. O sistema utiliza lógica de programação estruturada para categorizar riscos e fornece feedback visual imediato através de cores, auxiliando na tomada de decisão rápida em ambientes de monitoramento.

## 📌 Sobre o Projeto
O desafio consistiu em criar um sistema que processa diferentes níveis de entrada (de 1 a 5) e associa cada um a uma mensagem de alerta específica e uma cor correspondente. A aplicação foca na experiência do usuário (UX) via CLI (Command Line Interface), garantindo que os alertas críticos sejam destacados visualmente para evitar falhas humanas de interpretação.

## 🚀 Funcionalidades
- **Mapeamento de Estados:** Conversão de níveis numéricos em estados descritivos (Crítico a Alerta).
- **Feedback Colorido:** Integração com a biblioteca `colorama` para alertas visuais dinâmicos no terminal.
- **Simulação Randômica:** Lógica implementada com o módulo `random` para simular leituras aleatórias de sensores.
- **Gestão de Estilo:** Restauro automático das definições de cor padrão do terminal após a execução (`Style.RESET_ALL`).
- **Código Modular:** Estrutura baseada em funções reutilizáveis e dicionários, facilitando a escalabilidade do sistema.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** [Python 3.x](https://www.python.org/)
- **Bibliotecas Externas:** - `colorama`: Responsável pela estilização de cores ANSI no terminal.
- **Módulos Nativos:**
  - `random`: Utilizado para a geração de dados aleatórios na simulação.

## 📊 Regras de Negócio e Níveis
O sistema segue a seguinte progressão de risco e sinalização:

| Nível | Situação | Cor Visual | Risco |
| :--- | :--- | :--- | :--- |
| **1** | Muito Baixo (Crítico) | Vermelho | 🔴 Elevado |
| **2** | Baixo | Amarelo | 🟡 Moderado |
| **3** | Médio | Verde | 🟢 Estável |
| **4** | Alto | Ciano | 🔵 Seguro |
| **5** | Muito Alto (Alerta) | Azul | 🔵 Atenção |

## ⚙️ Como Instalar e Rodar

### 1. Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina. Você pode verificar rodando: 
```bash
python --version

2. Instalação
Clone o repositório e instale a biblioteca necessária:
# Clone o repositório
git clone [https://github.com/seu-usuario/monitoramento-reservatorio.git](https://github.com/seu-usuario/monitoramento-reservatorio.git)

# Entre na pasta
cd monitoramento-reservatorio

# Instale as dependências
pip install -r requirements.txt

3. Execução
Para iniciar a simulação do monitoramento, execute:
python main.py

_______________________________________________________________________________________________________________

📂 Estrutura do Projeto
main.py: Arquivo principal contendo a lógica do sistema e simulação de sensores.

requirements.txt: Arquivo com a dependência colorama e sua versão específica.

README.md: Documentação completa do projeto.
_______________________________________________________________________________________________________________

✒️ Desenvolvedor
Matheus Azevedo Estudante de Desenvolvimento de Sistemas

GitHub | LinkedIn

"A simplicidade é o último grau de sofisticação." - Projeto desenvolvido para fins acadêmicos e composição de portfólio.
