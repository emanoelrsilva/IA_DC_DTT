# Plano de Estudos | IA DC DTT
### Plano PBL para a Tech Stack de IA

## Módulo 1 (Semana 1) – Fundamentos e arquitetura de LLM em produção
### Problema 1.1: “Assistente de Suporte com Restrições de Custo”
Você precisa criar um assistente que responda dúvidas de um produto interno.   
Restrições:  
• Latência baixa  
• Custo por conversa limitado  
• Respostas consistentes, com formato padronizado  
#### O que você aprende (da stack)
• Como LLMs lidam com contexto, tokens e custo  
• Quando usar modelo grande vs mini  
• Estrutura de prompt e contratos de saída  
#### Entregáveis
• Prompt padrão com:   
o instruções de sistema  
o regras de tom  
o formato de resposta (tópicos)  
• Tabela de decisão “modelo por tarefa” (ex: classificação, sumarização, 
resposta final)  
• Simulação de custo (estimativa simples por tamanho de resposta)  
#### Critérios de sucesso
• Respostas seguem o formato em mais de 90% dos casos  
• Explicação clara do porquê de cada modelo ser usado
Reflexão (PBL)  
• O que falhou com prompts livres?  
• Onde o custo explodiria e por quê?  

## Módulo 2 (Semana 1) – Núcleo de inteligência + LLM Gateway (roteamento, fallback, budgets)
### Problema 2.1: “Roteamento multi-modelo para reduzir custo sem perder qualidade”
Você tem 3 tipos de requisição:  
1. Pergunta simples factual  
2. Pergunta complexa analítica  
3. Extração estruturada (campos)  
Você precisa rotear automaticamente para:  
• modelo mini quando der  
• modelo maior quando necessário  
• fallback quando um modelo falhar  
#### O que você aprende
• Padrão de LLM Gateway (LifeLLM como referência)  
• Rate limits, budgets por usuário e por feature  
• Fallback por tipo de erro (timeout, quota, resposta inválida) Entregáveis  
• Especificação do roteador (regras e thresholds)  
• Política de fallback (o que acontece em cada falha)  
• Relatório simples de custo: antes e depois do roteamento  
#### Critérios de sucesso
• Redução de custo total estimada (meta: 30% ou mais) mantendo qualidade percebida  
• Nenhuma requisição “morre” sem fallback  
#### Reflexão
• Quando o roteamento errou e por quê?  
• Qual sinal você usou para decidir “complexo vs simples”?  

## Módulo 3 (Semana 2) – Orquestração (LangChain), workflows (LangGraph) e schemas (Pydantic)
### Problema 3.1: “Triagem e resolução com múltiplos passos”
O assistente precisa:  
1. Classificar a intenção do usuário (suporte, dúvida técnica, solicitação)  
2. Decidir se precisa buscar base de conhecimento  
3. Produzir resposta padronizada  
4. Se for solicitação, gerar “ticket” estruturado  
#### O que você aprende
• LangChain para tools e chains  
• LangGraph para estado e fluxo com branching  
• Pydantic para validar output e evitar respostas quebradas  
#### Entregáveis
• Workflow em LangGraph com estados:  
o classify -> decide_rag -> answer -> validate -> output  
• Schemas Pydantic:  
o AnswerResponse  
o TicketRequest (se aplicável)  
• Logs de validação: quantas respostas foram rejeitadas pelo schema  
#### Critérios de sucesso
• Fluxo funciona sem intervenção manual  
• Saída estruturada é válida em mais de 95% dos casos  
• Você consegue explicar o grafo para alguém em 3 minutos Reflexão  
• Quais falhas de schema foram mais comuns?  
• Onde o LangGraph te ajudou que chain linear não ajudaria?  
## Módulo 4 (Semana 3) – RAG e Memória (Qdrant, Fastembed, Docling)
### Problema 4.1: “Base de conhecimento corporativa com PDFs heterogêneos”
Você tem PDFs com tabelas, textos longos e documentos escaneados.  
Objetivo:  
• responder com base em fontes  
• reduzir alucinação  
• suportar atualização incremental do acervo  
#### O que você aprende
• Docling para parsing e normalização  
• Chunking inteligente  
• Qdrant: collections, payloads, filtros e named vectors  
• Busca híbrida: densa + esparsa (Fastembed BM25/SPLADE)  
#### Entregáveis
• Pipeline de ingestão:  
o Docling -> chunk -> embeddings -> Qdrant  
• Política de chunking:   
o tamanho alvo, overlap, heurísticas por seção  
• Consulta RAG que retorna:   
o resposta + citações de trechos (id do chunk)  
#### Critérios de sucesso
• Você consegue responder com trechos coerentes e rastreáveis  
• Recall aceitável em perguntas variadas (você define um conjunto de 20 perguntas)  
#### Reflexão
• Quais documentos quebraram seu parser?  
• O chunking por tamanho foi suficiente? Onde falhou?  
### Problema 4.2: “Busca híbrida para termos exatos e semântica” 
Existem perguntas que exigem termos exatos (“código X”, “cláusula Y”), outras  são semânticas.  
Você precisa combinar as duas.  
#### Entregáveis
• Comparativo: denso vs esparso vs híbrido  
• Regras de seleção (quando dar peso maior para BM25)  
## Módulo 5 (Semana 4) – Re-ranking (BGE Reranker, ColBERT)
### Problema 5.1: “Top-k ruim: o RAG acha contexto irrelevante”
Mesmo com híbrido, o top-k vem misturado, e a resposta piora. Você precisa:  
• aplicar re-ranking  
• melhorar precisão do contexto final  
#### O que você aprende
• Diferença entre retrieval e ranking  
• BGE-Reranker para melhorar precisão  
• ColBERT para queries longas e comparativas  
#### Entregáveis
• Pipeline: retrieve -> rerank -> select -> generate  
• Métrica antes/depois:  
o context precision  
o answer relevance (mesmo que qualitativo no começo)  
• Relatório de trade-off:  
o ganho de qualidade vs latência  
#### Critérios de sucesso
• Redução perceptível de “contexto lixo” nos top chunks  
• Melhor consistência nas respostas para perguntas longas  
#### Reflexão
• O re-ranking resolveu ou só mascarou chunking ruim?  
• Quando ColBERT vale o custo/complexidade?  
## Módulo 6 (Semana 5) – Qualidade e Observabilidade (RAGAS, LangSmith, Langfuse)
### Problema 6.1: “Você não consegue provar que o sistema está bom”
Seu líder pergunta: “melhorou mesmo ou parece melhor?”. Você precisa criar:  
• avaliação automatizada  
• tracing por etapa  
• análise de custo por fluxo  
#### O que você aprende
• RAGAS para avaliar qualidade do RAG  
• LangSmith para tracing e custos  
• Langfuse para observabilidade OSS e feedback  
#### Entregáveis
• Dataset de avaliação (mínimo 30 QAs)  
• Pipeline de eval (RAGAS) com relatório  
• Tracing habilitado para cada etapa:  
o retrieval  
o rerank  
o generation  
• Painel simples com:   
o custo médio por pergunta  
o taxa de erro  
o latência por etapa  
#### Critérios de sucesso
• Você consegue apontar os 3 maiores gargalos com evidência  
• Você consegue mostrar evolução entre duas versões do pipeline  
#### Reflexão
• Quais métricas te enganaram?  
• O que você mediu que realmente correlacionou com “boa resposta”?  
## Módulo 7 (Semana 6) – Infra, Deploy e Produto (Docker, Azure ACR/App Services, Supabase, Tavily, Streamlit/Lovable)
### Problema 7.1: “Protótipo que vira produto interno”
Você precisa entregar uma aplicação acessível para usuários internos com:  
• UI simples  
• histórico e autenticação  
• logging básico  
• deploy em ambiente controlado  
#### O que você aprende
• Dockerização  
• Deploy no Azure App Services + ACR  
• Supabase para usuários, sessões e logs  
• Tavily Search para grounding externo quando a base interna falhar  
• Streamlit/Lovable para UI rápida  
#### Entregáveis
• App rodando com:  
o login simples  
o chat com histórico  
o opção “usar web search” (Tavily) em fallback  
• Pipeline CI básico (build e push da imagem)  
#### Critérios de sucesso
• Usuário consegue testar sem você estar presente  
• Logs permitem debugar um caso real em menos de 10 minutos Reflexão  
• Onde a UX atrapalhou a qualidade percebida?  
• O que você faria diferente no fluxo de fallback para web?  
## Módulo 8 (Semana 7) - Governança, versionamento e segurança (MLflow/DVC, feature flags, guardrails)
### Problema 8.1: “Mudou prompt, mudou tudo, e ninguém sabe por quê”
Você precisa versionar:  
• prompts  
• datasets de eval  
• configurações do RAG  
• parâmetros do retriever/reranker  
E precisa ter:  
• feature flags (liga/desliga componentes)  
• guardrails por agente  
• filtros PII/toxicidade  
• circuit breakers de custo  
#### O que você aprende
• MLflow/DVC para versionamento de pipelines e artefatos  
• Gestão de experimentos e rollback  
• Segurança e governança por policy  
#### Entregáveis
• Registro versionado:  
o prompt v1, v2…  
o config do RAG  
o dataset de eval  
• Feature flags:  
o reranker on/off  
o hybrid search on/off  
o web fallback on/off  
• Guardrails:   
o policy por agente (o que pode/não pode fazer)  
o bloqueio de PII (masking e detecção)  
o circuit breaker: limite de custo por sessão  
#### Critérios de sucesso
• Você consegue reproduzir um resultado antigo  
• Você consegue dar rollback de uma mudança ruim em minutos  
• Você consegue impedir um “runaway cost”  
#### Reflexão
• Qual parte da governança doeu mais implementar?  
• Quais guardrails realmente fizeram diferença?  
## Capstone PBL
### Problema final: “Assistente corporativo confiável e auditável”
#### Requisitos:
• Multiagente (triagem + resposta + auditoria)  
• RAG híbrido + reranking  
• Observabilidade e eval automatizada  
• Deploy simples e governança mínima  
• Política de custos e segurança  
#### Entregável final:
• Demo funcional  
• Documento de arquitetura  
• Relatório de qualidade (RAGAS) e custos  
• Registro de versões (MLflow/DVC)  
• Checklist de segurança  