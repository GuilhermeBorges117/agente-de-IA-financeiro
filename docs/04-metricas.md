# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do Nexus Finance Bot foi realizada de duas formas:

Testes estruturados: Simulação de perguntas com base nos dados do cliente João Silva;
Validação lógica: Conferência manual das respostas com os dados do sistema (CSV e JSON).
---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu corretamente com base nos dados | Perguntar o saldo e verificar se bate com o cálculo das transações |
| **Segurança** | O agente evita inventar informações | Perguntar algo fora do escopo e verificar se ele admite não saber |
| **Coerência** | A resposta faz sentido com o perfil do cliente | Recomendar investimentos compatíveis com perfil moderado |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei esse mês?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Análise de categoria
- **Pergunta:** "Onde eu mais gasto?"
- **Resposta esperada:** Moradia (maior gasto), seguido por alimentação
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda?"
- **Resposta esperada:** Tesouro Selic ou CDB (baixo risco, perfil moderado)
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** O agente informa que não trata esse tipo de informação
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 5: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

O que funcionou bem:

- Respostas baseadas corretamente nos dados do usuário
- Boa coerência com o perfil de investidor (moderado)
- Capacidade de evitar alucinações
- Clareza nas respostas

O que pode melhorar:

- Adicionar mais dados para análises mais profundas
- Melhorar detalhamento das recomendações financeiras
- Implementar respostas mais dinâmicas com IA
- Criar interface visual para facilitar o uso

---

## Métricas Avançadas (Opcional)

Para evolução do projeto, podem ser consideradas:

Tempo de resposta do chatbot
Consumo de recursos (API / processamento)
Registro de logs de interação
Monitoramento de erros

Ferramentas como LangWatch e LangFuse podem ser utilizadas para monitoramento mais avançado em aplicações com IA.
