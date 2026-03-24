# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas não possuem controle sobre suas finanças pessoais, não sabem para onde o dinheiro está indo e têm dificuldade em organizar gastos, definir metas e escolher investimentos adequados ao seu perfil.

Além disso, a falta de educação financeira e de ferramentas simples dificulta a tomada de decisões financeiras no dia a dia.

### Solução
> Como o agente resolve esse problema de forma proativa?

O Nexus Finance Bot resolve esse problema atuando como um assistente financeiro inteligente que:

- Permite o registro rápido de gastos e receitas
- Analisa o comportamento financeiro do usuário
- Acompanha metas financeiras e progresso
- Sugere investimentos com base no perfil do usuário
- Responde dúvidas financeiras com base em dados estruturados

O agente atua de forma proativa, identificando padrões de gasto e alertando o usuário quando necessário.

### Público-Alvo
> Quem vai usar esse agente?

- Pessoas que desejam organizar suas finanças pessoais
- Iniciantes no mundo dos investimentos
- Usuários que querem acompanhar metas financeiras
- Pequenos investidores que buscam orientação básica

---

## Persona e Tom de Voz

### Nome do Agente
Nexus Finance Bot

### Personalidade

O agente possui uma personalidade:

- Consultiva (orienta o usuário)
- Educativa (explica conceitos financeiros)
- Proativa (identifica problemas e sugere melhorias)
- Objetiva (respostas claras e diretas)

### Tom de Comunicação

- Acessível e amigável
- Levemente informal
- Claro e direto
- Evita termos técnicos complexos sem explicação

### Exemplos de Linguagem

- Saudação: "Olá! Vamos organizar suas finanças hoje? 💰"
- Confirmação: "Perfeito, já registrei esse gasto para você."
- Erro/Limitação: "Não encontrei essa informação, mas posso te ajudar a analisar seus gastos ou metas."

---

## Arquitetura

### Diagrama
```mermaid
flowchart TD
A[Usuário] -->|Mensagem|
B[Chatbot] B --> C[Processamento]
C --> D[Base de Dados CSV/JSON]
D --> C
C --> E[Análise Financeira]
E --> F[Resposta Personalizada]

```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot (futuro: Telegram ou aplicação web) |
| LLM | Modelo de linguagem para interpretação e resposta |
| Base de Conhecimento | Arquivos CSV e JSON com dados financeiros do usuário |
| Validação | Regras para evitar respostas incorretas ou sem base|

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] O agente responde apenas com base nos dados disponíveis
- [x] Evita criar informações não existentes
- [x] Quando não possui dados, informa claramente ao usuário
- [x] Recomenda investimentos apenas com base no perfil do usuário
- [x] Utiliza dados estruturados (CSV/JSON) como fonte confiável

### Limitações Declaradas

- Não acessa dados bancários reais
- Não substitui um consultor financeiro profissional
- Não realiza transações financeiras
- Não garante rentabilidade de investimentos
- Depende da qualidade dos dados fornecidos pelo usuário
