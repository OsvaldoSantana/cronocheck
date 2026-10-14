# CronoCheck — F00-E02: Jornadas AS-IS / TO-BE (rascunho v0.1)

**Estado:** em elaboração; **não validado por usuários**.  
**Data:** 2026-10-14  
**Fontes:** blueprint v1.0 (A.7, D.1–D.4, E/F00-E02), PRD v1.2, cenários CU-01 a CU-05, decisões OQ-01/OQ-02 de 2026-10-14.

## 1. Objetivo da etapa e limitações

Mapear a jornada de análise e revisão de cronogramas, comparando um fluxo operacional **AS-IS hipotético** com o **TO-BE proposto pelo CronoCheck**, descrevendo fricções, evidências, exceções e requisitos rastreáveis.

**Atenção:** não houve entrevista, observação de processo real ou medição de tempo. Nenhuma etapa do AS-IS abaixo é afirmada como procedimento efetivo de empresas ou usuários específicos. OQ-01 permite avançar com essas hipóteses, não validá-las. OQ-02 permite apenas dados de cronogramas sintéticos para a descoberta e as futuras fixtures.

**Critério de saída F00-E02 (blueprint):** jornada primária completa com hipóteses explícitas e limitações registradas; revisão humana do mapa e lista das hipóteses que exigem confirmação.

## 2. Atores propostos (a validar)

| Ator (hipótese) | Participação na jornada | Questão a validar |
|---|---|---|
| P-01 Planejador | recebe versões, verifica e propõe correção/aprovação | realmente importa e compara versões? |
| P-02 Coordenador | prioriza pendências e distribui responsáveis | possui poderes de decisão e acesso entre projetos? |
| P-03 Auditor técnico | revisa achados e registra decisões justificadas | função separada ou acumulada pelo planejador? |
| Cliente/fornecedor do cronograma | fornece dados de origem (externo ao MVP) | formato e canal de entrega reais? |

## 3. AS-IS hipotético — processo de referência a validar

| Seq. | Passo hipotético | Fricção / risco hipotético | Evidência necessária |
|---|---|---|---|
| A01 | Receber cronograma XLSX por e-mail/pasta compartilhada | origens e versões dispersas | entrevistas e exemplos autorizados |
| A02 | Conferir estrutura e colunas manualmente | layouts heterogêneos e mapeamento incorreto (R-01) | layouts sintéticos primeiro; depois observação consentida |
| A03 | Verificar IDs, datas e predecessoras em planilhas | inconsistências difíceis de detectar | observação de tarefa e erros frequentes |
| A04 | Comparar arquivo novo com versão anterior | trabalho manual; ambiguidade de identificadores | exemplo concreto do procedimento |
| A05 | Registrar pendências e solicitar esclarecimentos | achados sem evidência padronizada | instrumento real de registro |
| A06 | Discutir aceite/correção entre envolvidos | decisões ficam fora do histórico | fluxo real de aprovação |
| A07 | Comunicar status e emitir relatório | relatórios inconsistentes ou demorados | relatório e tempo de produção reais |

Hipóteses prioritárias: H-01 (A02/A03 causam retrabalho); H-02 (A04 é demorado); H-03 (A06 não deixa trilha recuperável); H-04 (A07 demanda exportação); H-05 (coordenador acompanha múltiplos projetos).

## 4. TO-BE proposto — jornada principal (CU-01 → CU-03 → CU-02 → CU-04)

| Passo | Ator | Interface / ação proposta | Resposta esperada e estados | RF / RNF |
|---|---|---|---|---|
| T01 | P-01 | Autenticar e selecionar projeto | apenas projetos autorizados; erros de acesso claros | RF-01, RF-02, RNF-06 |
| T02 | P-01 | Enviar XLSX no wizard | validação de tipo, limites e permissões; erro recuperável | RF-03, RNF-05 |
| T03 | P-01 | Mapear colunas | sugestão editável; mapeamento explícito e controlável | RF-04, RNF-01 |
| T04 | P-01 | Conferir prévia | separa erros bloqueantes de avisos; sem gravação antes de confirmar | RF-04, RNF-01 |
| T05 | P-01 | Confirmar importação | preserva original, hash e nova versão; feedback do servidor | RF-05, RNF-05 |
| T06 | P-01 | Executar auditoria | progresso real; retries idempotentes; resultados versionados | RF-06, RNF-04/05/09 |
| T07 | P-01/P-03 | Consultar fila e detalhe | regra, evidências, atividade e origem visíveis | RF-07, RNF-01/02 |
| T08 | P-03 | Justificar e decidir achado | autorização, estado válido, ator e histórico transacional | RF-08, RF-11, RNF-07 |
| T09 | P-01/P-02 | Comparar versões | novos/removidos/alterados e ambiguidades sinalizadas | RF-09 |
| T10 | P-03/P-02 | Exportar CSV/PDF | metadados de auditoria, filtros, escopo de acesso | RF-10, RNF-06 |

**Handoff:** importar não é aprovar o cronograma; achado automatizado não é decisão humana; decisão humana não reescreve os resultados originais.

### Estados, exceções e recuperação a cobrir no UX

- Sem projetos: ação para criar ou solicitar permissão; nunca exibir dados de outro projeto.
- Sem importações: estado vazio com próximo passo explícito.
- XLSX inválido / colunas insuficientes: erro explicativo no estágio da validação, sem gerar versão.
- Upload e auditoria demorados: estado persistente recuperável após atualização da página.
- Arquivo já importado / repetição: idempotência e mensagem contextual, sem duplicação indevida.
- Resultado sem achados: distinguir “sem problemas detectados pelas regras vigentes” de “cronograma correto”.
- Acesso negado: mensagem genérica sem revelar existência de dados.
- Duas decisões simultâneas sobre achado: evitar perda silenciosa da decisão anterior.
- Exportação falhou: permitir repetição segura; não expor dados fora das permissões.
- Alteração da versão durante navegação: contexto explícito e aviso para evitar interpretação da versão errada.

## 5. Mapeamento dos cinco cenários de uso

| Cenário | Entrada | Resultado TO-BE esperado | Incerteza prioritária |
|---|---|---|---|
| CU-01 | novo XLSX | versão preservada + auditoria explicável | layout real de XLSX / papel do importador |
| CU-02 | duas versões do mesmo projeto | mudanças classificadas sem pareamento silencioso | identificadores de atividades entre versões |
| CU-03 | achado aberto | decisão justificada e recuperável | estados de decisão e autoridade |
| CU-04 | solicitação de relatório | CSV/PDF autorizado e rastreável | formatos exigidos e destinatários |
| CU-05 (OQ-07 pendente) | conjunto de projetos acessíveis | próxima pendência crítica e aprofundamento até a origem | se o coordenador gerencia múltiplos projetos |

CU-05 permanece **proposta de cenário prioritário**, não aprovação da OQ-07.

## 6. Artefatos de descoberta e validação a produzir

1. Roteiro de entrevistas: como o usuário recebe versões, encontra inconsistências, registra decisões e comunica resultados; perguntar por casos reais, não induzir respostas.
2. Registro de hipóteses H-01 a H-05: situação, evidência favorável/contrária, decisão de manter/alterar e responsável.
3. Diagrama visual AS-IS/TO-BE após confirmação de atores e pontos de transferência.
4. Roteiro de teste de tarefa para F02-E05: importar → corrigir mapeamento → localizar achado → justificar → comparar → exportar.
5. Revisão de segurança/privacidade para qualquer dado de campo: nesta fase, utilizar **somente fixtures sintéticas** até outra aprovação explícita.

## 7. Checklist de saída F00-E02 (ainda não concluída)

- [x] Jornada TO-BE primária descrita conforme blueprint A.7.
- [x] Etapas AS-IS explicitamente identificadas como hipóteses.
- [x] Cinco CU mapeados, com CU-05 sinalizado como pendente.
- [x] Estados negativos, handoffs e recuperação inicial registrados.
- [ ] Validar o AS-IS com usuários ou registrar formalmente a limitação aceita pelo responsável.
- [ ] Revisão humana do mapa e dos requisitos vinculados.
- [ ] Confirmar ou ajustar papéis, exceções e critérios de sucesso.
- [ ] Registrar aprovação da etapa (responsável, data e evidências).

**Não confundir rascunho útil com F00-E02 aprovada.** O Gate G0 continua não aprovado.
