# CronoCheck — PRD v1.2 (Fase 00)
Status: Redigido, aguardando validação técnica (revisão humana). Não aprovado.
Persistência: baseline v1.2 versionada na `main` pelo PR #1 em 14/10/2026. O PRD continua aguardando validação técnica e aprovação formal.
Fonte normativa: CRONOCHECK_BLUEPRINT_V1.md (este PRD detalha, não substitui, o blueprint).

## 1. Problema e contexto
Cronogramas são importados, alterados e analisados por diferentes profissionais, mas falhas de
estrutura, dependências, versões e rastreabilidade são difíceis de detectar e explicar; revisões
manuais são lentas e decisões frequentemente ficam fora do histórico do planejamento.
[Hipótese herdada do blueprint — ainda não confirmada por entrevista com usuário real.]

## 2. Visão e objetivos do produto
Plataforma que importa cronogramas, normaliza dados, executa regras determinísticas de auditoria,
mostra evidências, coordena revisões e compara versões, sem alterar automaticamente o arquivo
original. Objetivo do MVP: entregar integralmente o escopo da seção 5.

## 3. Público-alvo e hipóteses de usuário
Planejadores de obras e projetos, coordenadores de planejamento e auditores técnicos.
[Hipótese — requer validação na Fase 00; ver personas-jtbd.md.]

## 4. Proposta de valor e diferenciais
Explicabilidade (cada achado mostra regra, entradas, cálculo/condição e resultado), não
destrutividade (importações e auditorias geram novas versões; a origem é preservada) e
reprodutibilidade (mesmas entradas e versão das regras produzem os mesmos achados).
Diferencial frente à revisão manual: auditoria determinística versionada e rastreável — hipótese de
valor, a confirmar com uso real.

## 5. Escopo do MVP e exclusões
**Incluído no MVP (blueprint A.5, sem alteração):**
- Contas/acesso com papel por projeto; cadastro de projetos.
- Importação .xlsx com modelo de colunas documentado; mapeamento assistido e pré-visualização.
- Armazenamento do arquivo de origem com hash SHA-256 e versão de cronograma normalizada.
- Auditorias determinísticas versionadas: datas inválidas, IDs duplicados, referências inexistentes,
  predecessoras circulares, atividades desconectadas conforme política e inconsistências simples de
  duração/dependência.
- Fila de achados com filtros, detalhes e evidências por regra; estados de revisão e justificativas.
- Histórico de auditorias e eventos de negócio; comparação básica entre duas versões.
- Dashboard operacional e exportação CSV/PDF de resultados resumidos.
- Ambientes local/teste/produção, logs estruturados, testes automatizados, backup e processo de
  lançamento.

**Fora do MVP (blueprint A.6, sem alteração):** leitura nativa de `.mpp`, integração online com
Project/Primavera, edição automática do cronograma, CPM multicritério com calendários complexos,
Monte Carlo, IA generativa, marketplace de plugins, modo offline, cobrança/SaaS multiempresa e
microsserviços — possibilidades para a fase 09, não promessas.

Nenhum item do MVP foi removido ou rebaixado nesta revisão.

## 6. Jornadas operacionais
Jornada primária: Entrar → Selecionar projeto → Importar XLSX → Mapear colunas → Conferir
prévia/validar → Confirmar versão → Executar auditoria → Revisar achados → Registrar decisões →
Comparar versões → Exportar relatório. Cenários detalhados CU-01 a CU-05 em personas-jtbd.md.

## 7. Requisitos funcionais — prioridade revisada (correção do Prompt 001.2)
Três eixos separados: (1) obrigatoriedade para o lançamento do MVP, definida pelo blueprint;
(2) ordem de implementação, proposta técnica; (3) opcional/pós-MVP — nenhum RF está neste eixo.
A v1.1 rotulou RF-08 a RF-11 como "should/could-have"; isso é CORRIGIDO aqui.

| ID | Requisito | Obrigatório para o lançamento do MVP (blueprint) | Ordem de implementação proposta | Observação / divergência |
|---|---|---|---|---|
| RF-01 | Autenticar usuário e verificar permissões em cada projeto | Sim | 1 | Sem divergência. |
| RF-02 | Cadastrar, listar e consultar projetos | Sim | 2 | Sem divergência. |
| RF-03 | Receber XLSX e validar extensão, conteúdo, limites e permissões | Sim | 3 | Sem divergência. |
| RF-04 | Mapear colunas e mostrar prévia antes da gravação | Sim | 4 | Sem divergência. |
| RF-05 | Persistir arquivo original, hash e snapshot normalizado versionado | Sim | 5 | Sem divergência. |
| RF-06 | Executar regras de auditoria determinísticas e versionadas | Sim | 6 | Núcleo de valor. |
| RF-07 | Exibir regra, evidências e tarefas relacionadas em cada achado | Sim | 7 | Sustenta explicabilidade. |
| RF-08 | Classificar, atribuir, comentar e decidir achados | Sim (A.5: estados de revisão e justificativas) | 8 | Revisão humana permanece obrigatória; só a ordem é técnica. |
| RF-09 | Comparar versões e sinalizar alterações relevantes | Sim (A.5: comparação básica entre duas versões) | 9 | "Básica" limita o escopo da função, não sua obrigatoriedade. |
| RF-10 | Exportar resultados de auditoria em formato legível e estruturado | Sim (A.5: exportação CSV/PDF) | 10 | Implementado ao final por depender de RF-07, não por ser dispensável. |
| RF-11 | Consultar histórico de ações e execuções | Sim (A.5: histórico de auditorias e eventos) | 11 (base AuditEvent em F03-E04) | Base de auditabilidade/versionamento; não pode ser reduzido unilateralmente. |

Divergência registrada como proposta de decisão (não aprovada) — PD-01 / OQ-06: a ORDEM de
implementação de RF-08 a RF-11 após RF-06/07 é sequenciamento técnico, não redução de prioridade de
negócio. Qualquer rebaixamento para pós-MVP exigiria decisão explícita do responsável pelo produto,
o que não ocorreu e não está proposto.

## 8. Requisitos funcionais — critérios de aceite operacionais
Formato: condição inicial → ação/verificação → resultado esperado → evidência.

| ID | Condição inicial | Ação/procedimento de verificação | Resultado esperado | Evidência necessária |
|---|---|---|---|---|
| RF-01 | Usuário A membro do projeto X; usuário B não membro; usuário não autenticado | Autenticar cada um e requisitar recurso do projeto X | A acessa; B recebe 403/404 sem vazamento; não autenticado recebe 401 | Saída de teste automatizado com os três casos |
| RF-02 | Usuário autenticado sem projetos | Criar, listar e consultar projeto via API e UI | Projeto aparece na listagem e na consulta; outro usuário não o vê | Teste de integração + E2E com respostas registradas |
| RF-03 | Arquivo XLSX válido; arquivo malformado; arquivo acima do limite; extensão falsa | Submeter cada arquivo | Válido aceito; demais rejeitados com motivo explícito e sem gravação | Resultado por fixture comparado ao expected result versionado |
| RF-04 | XLSX com colunas fora do padrão | Executar o wizard até a prévia, sem confirmar | Prévia e alertas exibidos; nenhuma versão gravada antes da confirmação | Teste de UI + consulta mostrando zero versões novas antes da confirmação |
| RF-05 | Projeto com versão N confirmada | Confirmar nova importação do mesmo projeto | Versão N+1 criada; N inalterada; SHA-256 do arquivo de origem registrado e reproduzível | Consulta às duas versões + recálculo independente do hash |
| RF-06 | Golden dataset com erros conhecidos (duplicidade, ciclo, referência inexistente, data inválida) | Executar a auditoria duas vezes sobre a mesma versão e mesmo conjunto de regras | Achados esperados gerados; resultados idênticos (mesmos fingerprints) nas duas execuções | Comparação automatizada obtido x esperado |
| RF-07 | Achado existente | Consultar detalhe via API e UI | RuleId, versão da regra, entradas, evidência e atividades relacionadas presentes | Teste de contrato + E2E |
| RF-08 | Achado em estado aberto; transições permitidas definidas | Classificar, atribuir, comentar, decidir; tentar uma transição inválida | Transições válidas registradas com ator/justificativa/timestamp; inválida bloqueada no backend | Trilha AuditEvent + teste da transição negada |
| RF-09 | Duas versões com diferenças conhecidas e documentadas | Executar comparação | Adicionados/removidos/alterados e achados novos/resolvidos classificados conforme o esperado | Teste obtido x esperado |
| RF-10 | Auditoria concluída; usuário com e sem permissão | Exportar CSV e PDF com filtros; tentar sem permissão | Conteúdo coincide com a consulta autorizada e traz metadados; sem permissão é negado; valores perigosos escapados no CSV | Comparação conteúdo x consulta + teste negativo |
| RF-11 | Conjunto conhecido de ações por diferentes atores | Consultar histórico por ator, período e entidade | Retorno completo e exclusivo do filtro | Teste com contagem esperada x obtida |

## 9. Requisitos não funcionais — critérios de aceite operacionais

| ID | Condição inicial | Ação/procedimento de verificação | Resultado esperado | Evidência necessária | Natureza da meta |
|---|---|---|---|---|---|
| RNF-01 | Fluxo principal em condição normal e com falhas simuladas | E2E com erro, espera e repetição; teste com usuários | Interface comunica cada estado sem bloquear o fluxo | Registro de teste de usabilidade + E2E | Comportamental; critério de sucesso de tarefa a calibrar em F02-E05 |
| RNF-02 | Telas dos fluxos essenciais | Varredura automatizada + revisão manual (teclado, foco, leitor de tela) | Conformidade WCAG 2.2 AA nos fluxos essenciais | Relatório automatizado + checklist manual | Compromisso |
| RNF-03 | Cenário de referência documentado (volume, hardware), sem importação concorrente | Teste de carga das consultas usuais | p95 < 500 ms | Relatório de benchmark reprodutível | Provisória — requer calibração: definir cenário de referência em F08-E02 antes de validar o número |
| RNF-04 | XLSX de referência com 5.000 atividades; ambiente de referência | Importação completa cronometrada, repetida | Até 60 s | Relatório de benchmark reprodutível | Provisória — requer calibração: primeira medição em F05-E07, ajuste em F08-E02 |
| RNF-05 | Importação/auditoria repetida com mesma idempotency key e em concorrência | Reenviar a operação e executar em paralelo | Nenhuma versão ou achado duplicado | Teste com contagem antes/depois | Compromisso |
| RNF-06 | Release candidata | SAST/SCA + checklist OWASP ASVS | Nenhuma vulnerabilidade crítica/alta conhecida não mitigada | Relatórios de varredura e checklist | Compromisso |
| RNF-07 | Lista documentada de mutações críticas | Executar cada mutação; simular falha da transação | 100% com AuditEvent na mesma transação; falha não deixa evento órfão nem mutação sem evento | Teste de integração por mutação | Compromisso; lista de mutações críticas a definir em F03-E04 |
| RNF-08 | Backup diário configurado | Ensaio de restauração em ambiente isolado | Restauração dentro de RPO 24 h / RTO 4 h | Runbook executado com tempos medidos | Provisória — alvos, não SLA; calibração após primeiro ensaio (F08-E03) |
| RNF-09 | Requisição atravessando importação, auditoria e API, inclusive com erro | Rastrear de ponta a ponta | Mesmo correlation ID em logs/traces e na resposta de erro | Captura de trace | Compromisso |
| RNF-10 | PR com mudança incompatível de contrato | Executar validação OpenAPI em CI | Mudança identificada e PR bloqueado | Log do pipeline | Compromisso |

Nenhuma meta provisória foi convertida em compromisso definitivo.

## 10. Dependências entre requisitos
RF-01 → RF-02 → RF-03 → RF-04 → RF-05 → RF-06 → RF-07 → (RF-08 | RF-09 → RF-10); RF-11 depende de
RF-01 e RF-06. RNF-07 compartilha a base transacional de RF-08/RF-11. RNF-03/04/08 só podem ser
calibrados após RF-05/RF-06 implementados e nas etapas F05-E07/F08-E02/F08-E03.

## 11. Métricas de sucesso propostas
Taxa de importações concluídas sem erro impeditivo na primeira tentativa; tempo entre importação e
primeira decisão de achado; percentual de achados com justificativa registrada antes da resolução.
Sem linha de base — nenhum dado de uso existe; denominadores a definir em F07-E01.

## 12. Registro operacional de riscos
Classificações originais (probabilidade/impacto) do blueprint preservadas sem alteração.

| ID | Descrição | Prob. | Impacto | Causa | Consequência | Mitigação | Responsável proposto | Fase de tratamento | Indicador de acompanhamento |
|---|---|---|---|---|---|---|---|---|---|
| R-01 | Excel heterogêneo e colunas não padronizadas | Alta | Alto | Diversidade de formatos de planilha entre clientes/obras | Importação falha ou mapeia dados incorretamente, gerando achados falsos | Contrato de importação v0, wizard de mapeamento, fixtures | Produto/Importação | F00-E04, F04 | Nº de importações que exigem correção manual de mapeamento |
| R-02 | Erros de lógica por calendários e defasagens | Alta | Alto | Regras de calendário de trabalho e defasagens mais complexas que o suportado | Falsos positivos/negativos em regras temporais | Escopo FS simples; limitações documentadas | Domínio | F05-E04 | Nº de achados temporais contestados como incorretos |
| R-03 | Excesso de arquitetura antes de validar produto | Média | Alto | Tendência a over-engineering inicial | Atraso no MVP sem ganho validado | Monólito modular, ADRs, revisão por métricas | Arquitetura | F01, contínuo | Componentes adicionados sem necessidade mensurável registrada |
| R-04 | UI sofisticada sem fluxo utilizável | Média | Alto | Priorizar estética antes da tarefa | Baixa adoção, retrabalho | Protótipos e testes de tarefa desde F02 | UX | F02 | Taxa de sucesso de tarefa nos testes |
| R-05 | Auditoria insuficiente ou editável | Média | Alto | Falha de desenho do AuditEvent/transação | Perda de confiança na trilha | Evento transacional, retenção, integridade e restore | Dados/Segurança | F03-E04, F08-E03 | Resultado de testes de integridade e do ensaio de restauração |
| R-06 | Upload de arquivos adversariais | Média | Alto | Conteúdo malicioso/zip bomb em XLSX | Indisponibilidade ou exposição | Limites, parsing seguro, storage privado, testes | Segurança | F04-E06 | Casos maliciosos de teste bloqueados x total |
| R-07 | Escopo cresce por integração com Project | Alta | Médio | Pressão por integração nativa | Atraso do MVP | `.mpp` fora do MVP; backlog separado (F09) | Produto | F09 | Solicitações registradas x aceitas no MVP |
| R-08 | Falhas de CI/dívida de testes | Média | Alto | Pressão de prazo reduzindo testes | Regressões não detectadas | Gates obrigatórios, DoD, builds reproduzíveis | Engenharia | F01-E04, contínuo | PRs bloqueados por gate e regressões pós-merge |
| R-09 | Ausência de usuários reais para validação | Média | Alto | Falta de acesso a usuários-alvo | Hipóteses erradas chegando à implementação | Entrevistas e testes antes de F03/F07 (OQ-01) | Produto | F00-E01, F02-E05, F07-E05 | Hipóteses confirmadas x refutadas |
