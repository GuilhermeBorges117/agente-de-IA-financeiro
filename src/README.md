# Código da Aplicação

Esta pasta contém a implementação do Nexus Finance Bot, um assistente financeiro inteligente capaz de analisar dados, calcular saldo, acompanhar metas e sugerir investimentos.

## Estrutura Sugerida

```
src/
├── main.py            # Aplicação principal (simulação do chatbot via terminal)
├── data_loader.py     # Responsável por carregar arquivos CSV e JSON
├── financeiro.py      # Lógica de cálculos financeiros (saldo, gastos, categorias)
└── recomendador.py    # Sistema de recomendação de investimentos
```

## 🧠 Funcionalidades Implementadas

- 📊 Leitura de dados financeiros (CSV e JSON)
- 💰 Cálculo de saldo do usuário
- 📉 Análise de gastos totais
- 📂 Agrupamento de despesas por categoria
- 📈 Recomendação de investimentos baseada no perfil

---

## ⚙️ Tecnologias Utilizadas

- Python
- Manipulação de arquivos CSV (csv)
- Manipulação de JSON (json)

---

## 🚀 Como Rodar a Aplicação

1. Acesse a pasta src
cd src
2. Execute o programa
python main.py

---

## 💬 Comandos Disponíveis

Durante a execução, você pode digitar:

- saldo → Mostra o saldo atual
- gastos → Mostra o total gasto
- categoria → Mostra gastos por categoria
- investir → Sugere investimentos
- sair → Encerra o programa

---

## Próximas Melhorias

- Integração com Telegram
- Interface web com Streamlit
- Uso de IA para respostas mais inteligentes
- Dashboard com gráficos financeiros

---

## 📌 Observação

Este projeto utiliza dados simulados armazenados na pasta data/ e tem como objetivo demonstrar conceitos de análise de dados e construção de agentes inteligentes.
