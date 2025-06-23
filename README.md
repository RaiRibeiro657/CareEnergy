# CareEnergy  
**Simulador de Sistema Inteligente de Gerenciamento de Energia com Automação e Interface Manual**

## Descrição

CARENERGY é uma prova de conceito funcional que simula um sistema de gerenciamento de energia residencial. Ele prioriza cargas essenciais com base no nível da bateria e permite controle manual das cargas por meio de uma interface interativa simples, desenvolvida com Streamlit.

## Objetivos

- Automatizar o desligamento de cargas secundárias quando a energia estiver em nível crítico.
- Permitir controle manual das cargas através de uma interface gráfica.
- Visualizar, em tempo real, o consumo de energia e o nível da bateria.
- Comprovar a viabilidade técnica da automação energética em um ambiente simulado.

## Tecnologias Utilizadas

- Python 3
- Streamlit
- Pandas

## Como Funciona

- O usuário pode ligar/desligar cargas críticas e secundárias usando checkboxes.
- A cada atualização, o sistema consome energia da bateria com base nas cargas ativas.
- Se o nível da bateria for inferior a 30%, a carga secundária é desligada automaticamente.
- Um gráfico exibe a evolução do nível da bateria ao longo do tempo.
