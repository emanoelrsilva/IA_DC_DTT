# Enunciado do Módulo 1
## Fundamentos e definição de um assistente corporativo com IA generativa

### Contexto geral do projeto
A **Aurora Consulting Group (ACG)** é uma empresa fictícia de consultoria e serviços corporativos com mais de 3.000 colaboradores distribuídos em diferentes áreas de negócio. Para suportar suas operações internas, a ACG utiliza diversos sistemas próprios, mantidos por times de TI e Operações.

Um dos principais sistemas internos é o **Aurora Service Portal (ASP)**, um portal corporativo usado por todos os colaboradores para:
- abrir solicitações de suporte (TI, acessos, equipamentos)
- acompanhar status de tickets
- consultar informações básicas sobre processos internos
- entender regras operacionais como SLAs e fluxos de atendimento

Atualmente, o conhecimento sobre o ASP está espalhado em manuais, wikis e comunicações informais. Como resultado:
- o time de suporte recebe muitas perguntas repetidas
- as respostas variam dependendo de quem responde
- novos colaboradores têm dificuldade para se orientar
- há perda de produtividade operacional

A liderança da ACG decidiu iniciar um projeto incremental de **IA Generativa**, começando com um assistente interno simples, que será evoluído ao longo do tempo.

---

### Objetivo do Módulo 1
Desenvolver a **primeira versão funcional de um assistente corporativo**, com foco em **controle, previsibilidade e custo**, e não em abrangência de conhecimento. Este módulo estabelece a base do sistema que será incrementado nos próximos módulos.

---

## Produto interno abordado
**Nome do produto:** Aurora Service Portal (ASP)

### Descrição resumida
O ASP é um portal web interno utilizado para:
- abertura de tickets de TI
- acompanhamento de solicitações
- consulta a informações operacionais básicas

### Fluxo simplificado de abertura de ticket de TI (conhecimento disponível)
O fluxo padrão para abertura de um ticket de TI no ASP é:
1. Acessar o Aurora Service Portal
2. Clicar na opção “Nova Solicitação”
3. Selecionar a categoria “TI”
4. Descrever o problema encontrado
5. Definir a prioridade
6. Enviar a solicitação

Esse fluxo é considerado **verdadeiro e estável** para fins deste módulo.

---

## Escopo do sistema no Módulo 1

### Nome do sistema
**Assistente ASP – Versão 1**

### Papel do assistente
O assistente deve:
- responder dúvidas frequentes sobre o uso do ASP
- explicar fluxos operacionais básicos
- organizar informações conhecidas em linguagem clara e padronizada

### Fonte de conhecimento
No Módulo 1, **toda a base de conhecimento do assistente deve estar explicitamente definida no prompt**. O assistente **não pode** consultar documentos externos, bases de dados ou sistemas.

### Domínio de conhecimento permitido
- Uso básico do Aurora Service Portal
- Fluxo de abertura de tickets de TI
- Conceitos simples como prioridade e status de ticket
- Informações que estejam explicitamente descritas no prompt

### Fora de escopo
O assistente **não deve**:
- responder perguntas fora do ASP
- inventar informações não fornecidas no prompt
- responder questões legais, financeiras ou estratégicas
- assumir integrações com sistemas reais

Se uma pergunta estiver fora do escopo ou não houver informação suficiente no prompt, o assistente deve **declarar explicitamente que não possui essa informação**.

---

## Tipos de perguntas que o sistema deve responder
- “Como abrir um ticket de TI no ASP?”
- “Quais são os passos para registrar um problema técnico?”
- “O que significa definir a prioridade de um ticket?”
- “Onde acompanho o status de uma solicitação?”

## Tipos de perguntas que o sistema deve recusar ou limitar
- “Qual o SLA oficial para tickets críticos?” (se não estiver no prompt)
- “Quem aprovou a política atual do ASP?”
- “Como funciona o orçamento do time de TI?”

---

## Regras de negócio do Módulo 1
- O assistente deve responder sempre em **formato padronizado**, usando tópicos.
- O tom deve ser profissional e neutro.
- A resposta deve ser consistente entre execuções.
- O custo por conversa deve ser estimável e controlado.
- O assistente deve priorizar modelos menores sempre que possível.
- O assistente **não deve** extrapolar conhecimento.

---

## Limitações intencionais do módulo
Este módulo **não inclui**:
- busca em documentos (RAG)
- histórico de conversas
- roteamento multi-modelo
- fallback
- observabilidade
- governança ou versionamento

Essas capacidades serão introduzidas progressivamente nos próximos módulos.

---

## Resultado esperado ao final do Módulo 1
Ao final deste módulo, deve existir:
- um assistente funcional com escopo bem definido
- um prompt contratual contendo:
  - contexto do produto
  - regras de comportamento
  - formato de saída
- uma explicação clara de qual modelo foi escolhido e por quê
- uma estimativa simples de custo por resposta

O sucesso do módulo **não é medido pela quantidade de conhecimento**, mas pela **clareza de escopo, previsibilidade das respostas e controle de custo**.
