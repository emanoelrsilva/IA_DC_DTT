# Módulos PBL – Assistente POSI

# Módulo 1 – Definição do assistente e limites de escopo
## Problema a ser resolvido
“Precisamos de um assistente que responda dúvidas frequentes sobre um produto interno, sem explodir custo nem latência, e com respostas previsíveis.”

## Escopo do assistente (definição explícita)
Nome: Assistente POSI

### Domínio inicial de conhecimento
- Uso do Portal POSI
- Funcionalidades principais
- Problemas comuns e FAQs
- Não responde: questões legais, financeiras, estratégicas ou fora do portal

### Tipo de perguntas esperadas
- “Como abrir um ticket de TI?”
- “Onde vejo o status da minha solicitação?”
- “Qual o SLA padrão?”

### Restrições
- Latência baixa
- Custo por conversa limitado
- Respostas em formato padronizado

### Resultado esperado
- Prompt contratual do assistente
- Tabela de decisão de modelos por tarefa
- Simulação simples de custo por conversa

---

# Módulo 2 – Roteamento multi-modelo e controle de custo
## Problema a ser resolvido
“O assistente funciona, mas usar sempre o mesmo modelo é caro e ineficiente.”

## Escopo das melhorias
Nome: LLM Gateway do POSI

### Features a adicionar
- Classificação automática do tipo de requisição: simples factual, analítica complexa, extração estruturada
- Roteamento para modelos diferentes conforme a necessidade
- Fallback diante de erros de timeout, quota, resposta inválida
- Orçamento por usuário e por sessão

### Tipo de decisões a automatizar
- Quando usar modelo mini vs maior
- Quando regenerar com schema vs trocar de provedor
- Quando interromper por budget e retornar resposta degradada

### Resultado esperado
- Redução de custo estimada em 30% ou mais mantendo qualidade percebida
- Nenhuma requisição “morre” sem fallback registrado

---

# Módulo 3 – Orquestração e fluxos de negócio
## Problema a ser resolvido
“O assistente responde, mas não executa processos nem segue fluxos reais do suporte interno.”

## Escopo das melhorias
Nome: Workflow POSI

### Features a adicionar
- Classificação de intenção: suporte, dúvida técnica, solicitação
- Decisão de uso de base de conhecimento
- Resposta padronizada com validação estrutural
- Criação de ticket estruturado quando aplicável

### Fluxo alvo
- classify → decide_rag → answer → validate → output
- Se for solicitação, criar TicketRequest e retornar protocolo

### Resultado esperado
- Fluxo automatizado sem intervenção manual
- Saídas válidas por schema em mais de 95% dos casos

---

# Módulo 4 – Base de conhecimento corporativa (RAG)
## Problema a ser resolvido
“O assistente não conhece os documentos corporativos e começa a alucinar.”

## Escopo das melhorias
Nome: RAG POSI

### Features a adicionar
- Ingestão de PDFs heterogêneos, incluindo OCR quando necessário
- Chunking inteligente com política definida por tamanho e seções
- Vetorização densa e busca esparsa
- Qdrant como base vetorial com metadados ricos
- Respostas com citações rastreáveis

### Fluxo alvo de consulta
- Docling → chunk → embeddings → Qdrant
- Consulta híbrida (densa + esparsa) com retorno de trechos e ids

### Resultado esperado
- Respostas com base em fontes oficiais
- Citações coerentes e rastreáveis
- Recall aceitável em conjunto de 20 perguntas de validação

---

# Módulo 4.2 – Busca híbrida para termos exatos e semântica
## Problema a ser resolvido
“Algumas perguntas exigem termos exatos, outras são semânticas. A busca atual não atende bem aos dois casos.”

## Escopo das melhorias
Nome: Híbrido POSI

### Features a adicionar
- Comparativo denso vs esparso vs híbrido
- Regras de seleção para dar mais peso ao BM25 quando houver termos exatos, códigos e ids
- Combinação de scores com pesos configuráveis

### Resultado esperado
- Melhoria de recall para consultas com termos exatos
- Manutenção da qualidade semântica em perguntas abertas

---

# Módulo 5 – Re-ranking para melhorar precisão
## Problema a ser resolvido
“O RAG traz muito contexto e parte relevante se perde entre trechos irrelevantes.”

## Escopo das melhorias
Nome: Reranker POSI

### Features a adicionar
- Re-ranking dos candidatos recuperados
- Seleção final de top-k mais preciso para geração
- Suporte a queries longas e comparativas

### Fluxo alvo
- retrieve → rerank → select → generate
- Rerank do top 50 para top 6–8 antes da geração

### Resultado esperado
- Redução de “contexto lixo” no top-k
- Melhor consistência em perguntas longas e comparativas
- Relatório de trade-off entre ganho de qualidade e latência

---

# Módulo 6 – Qualidade e observabilidade
## Problema a ser resolvido
“O sistema parece melhor, mas não há evidências e nem visibilidade do pipeline.”

## Escopo das melhorias
Nome: Observabilidade POSI

### Features a adicionar
- Dataset de avaliação com mínimo de 30 QAs
- Pipeline de avaliação automatizada do RAG
- Tracing por etapa: retrieval, rerank, generation
- Painel simples com custo médio por pergunta, taxa de erro e latência por etapa

### Resultado esperado
- Identificação dos 3 maiores gargalos com evidência
- Comparação entre versões do pipeline mostrando evolução de qualidade

---

# Módulo 7 – Produto interno utilizável
## Problema a ser resolvido
“O protótipo só roda localmente e depende de você. Usuários internos não conseguem testar.”

## Escopo das melhorias
Nome: App POSI

### Features a adicionar
- UI simples de chat
- Autenticação e histórico de conversas
- Logging básico para debugging em produção
- Deploy em ambiente controlado
- Fallback opcional para web search quando base interna falhar

### Resultado esperado
- Aplicação acessível a usuários internos sem intervenção do desenvolvedor
- Logs suficientes para depurar um caso real em menos de 10 minutos

---

# Módulo 8 – Governança, versionamento e segurança
## Problema a ser resolvido
“Mudanças pequenas quebram o sistema e não há reprodutibilidade nem segurança.”

## Escopo das melhorias
Nome: Governança POSI

### Features a adicionar
- Versionamento de prompts, configs de RAG e datasets de avaliação
- Feature flags para ligar e desligar componentes
- Guardrails de segurança por agente
- Filtros de PII e toxicidade
- Circuit breakers de custo por sessão e por usuário

### Resultado esperado
- Capacidade de reproduzir resultados antigos
- Rollback rápido de mudanças ruins
- Prevenção de runaway cost e proteção de dados sensíveis

---

# Capstone – Assistente corporativo confiável e auditável
## Problema final a ser resolvido
“Entregar um assistente corporativo útil, confiável, auditável e sustentável, pronto para uso interno.”

## Escopo final
Nome: POSI Copiloto Corporativo

### Requisitos consolidados
- Multiagente: triagem, resposta e auditoria
- RAG híbrido com reranking
- Observabilidade e avaliação automatizada
- Deploy simples e governança mínima aplicada
- Política de custos e segurança ativa

### Entregáveis
- Demo funcional
- Documento de arquitetura
- Relatório de qualidade e custos
- Registro de versões
- Checklist de segurança
