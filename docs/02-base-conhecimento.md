# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

---

## Adaptações nos Dados

Os dados mockados foram adaptados para simular um cenário mais próximo da realidade de um usuário comum.

As principais adaptações incluem:

Inclusão de categorias de gastos (alimentação, transporte, lazer)
Definição de metas financeiras no perfil do usuário
Organização de produtos financeiros por nível de risco
Estruturação do histórico de atendimento com temas e status de resolução

Essas adaptações permitem que o agente forneça respostas mais contextualizadas e úteis.

---

## Estratégia de Integração

Estratégia de Integração
Como os dados são carregados?

Os arquivos CSV e JSON são carregados diretamente no sistema utilizando Python no início da execução da aplicação.

CSV: carregados como listas ou estruturas tabulares
JSON: carregados como dicionários

Esses dados ficam disponíveis em memória para consulta durante a interação com o usuário.

### Como os dados são usados no prompt?

Os dados não são totalmente inseridos no system prompt.

O agente utiliza uma abordagem híbrida:

Parte dos dados (perfil do usuário) pode ser incluída no contexto inicial
Dados dinâmicos (transações, histórico) são consultados conforme a necessidade
As respostas são geradas com base nas informações relevantes recuperadas no momento da pergunta

Isso evita sobrecarga de contexto e melhora a precisão das respostas.

---

## Exemplo de Contexto Montado

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
