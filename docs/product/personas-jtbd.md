# CronoCheck — Personas, JTBD e cenários prioritários (Fase 00) — v1.2
Status: Redigido, aguardando validação técnica. Não aprovado.
Persistência: baseline v1.2 versionada na `main` pelo PR #1 em 14/10/2026. Personas e cenários continuam hipotéticos e não validados.

Nenhuma entrevista, pesquisa ou dado quantitativo foi realizado ou inventado. Todo conteúdo abaixo é
hipótese derivada de CRONOCHECK_BLUEPRINT_V1.md, salvo indicação explícita.

## 1. Personas (preservadas da v1.1)

### P-01 — Planejador de obras
- Objetivos: aprovar ou corrigir uma versão de cronograma rapidamente, sem retrabalho manual.
- Responsabilidades: manter a versão vigente íntegra; comunicar inconsistências à equipe de obra.
- Necessidades: saber objetivamente, antes de aprovar, se uma versão nova tem erro estrutural.
- Tarefas principais: importar XLSX; revisar prévia de mapeamento; confirmar versão.
- Fricções hipotéticas: verificação manual sujeita a erro; ausência de registro de por que uma
  versão foi aceita.
- Critério de sucesso hipotético: erros estruturais não passam para a obra sem revisão.
- Desconhecido: se este papel realiza de fato a importação ou se é outro perfil.

### P-02 — Coordenador de planejamento
- Objetivos: priorizar atenção entre vários projetos sem abrir cada cronograma.
- Responsabilidades: acompanhar pendências críticas; reportar status a terceiros.
- Necessidades: painel de pendências e próxima ação, não só gráficos.
- Tarefas principais: consultar dashboard operacional; redistribuir achados.
- Fricções hipotéticas: dificuldade de identificar qual projeto exige atenção imediata.
- Critério de sucesso hipotético: identificar o achado mais crítico sem varredura manual.
- Desconhecido: nº típico de projetos por coordenador; hierarquia formal de escalonamento.

### P-03 — Auditor técnico
- Objetivos: emitir decisão defensável sobre cada achado, com evidência auditável.
- Responsabilidades: justificar decisões; eventualmente responder por elas externamente.
- Necessidades: evidência legível ligada à regra que gerou o achado.
- Tarefas principais: revisar fila de achados; registrar decisão; exportar relatório.
- Fricções hipotéticas: justificativas hoje ficam fora de sistema (e-mail, conversa).
- Critério de sucesso hipotético: toda decisão tem trilha recuperável.
- Desconhecido: se é papel interno ou externo; exigências legais/contratuais de retenção.

## 2. Cenários prioritários (recuperados da iteração 1 e consolidados)
CU-01 a CU-04 são os quatro cenários apresentados no Prompt 001. CU-05 foi derivado da persona P-02
e da tela "Home operacional" do blueprint (D.2), e está marcado como ADIÇÃO PROPOSTA.

### CU-01 — Verificar integridade de uma nova versão antes de aprovar
- Persona: P-01 (Planejador).
- Objetivo: identificar erros estruturais (IDs duplicados, predecessoras circulares, referências
  inexistentes, datas inválidas) antes de aceitar a versão.
- Evento iniciador: recebimento de um cronograma XLSX atualizado (ex.: enviado por terceiro).
- Pré-condições: usuário autenticado com papel de edição no projeto; projeto já cadastrado.
- Fluxo principal: 1) selecionar projeto; 2) enviar XLSX; 3) mapear colunas; 4) conferir prévia e
  alertas; 5) confirmar versão; 6) executar auditoria; 7) consultar achados.
- Resultados esperados: nova versão criada sem sobrescrever a anterior; achados listados com regra
  e evidência.
- Exceções: arquivo malformado ou acima do limite (rejeitado com motivo); colunas obrigatórias não
  mapeadas (bloqueia confirmação); tipo de dependência não suportado (aviso explícito).
- Critérios de sucesso propostos: usuário consegue concluir o fluxo sem ajuda externa e explicar ao
  menos um achado com base na evidência mostrada.
- Evidências disponíveis: nenhuma empírica; apenas a jornada primária e as regras MVP do blueprint.
- Hipóteses pendentes: que o planejador é quem importa; que XLSX é o formato realmente recebido.

### CU-02 — Comparar a versão aprovada com a versão recebida
- Persona: P-01 (Planejador); secundária P-02.
- Objetivo: entender exatamente o que mudou entre duas versões.
- Evento iniciador: existência de nova versão confirmada para um projeto com versão anterior.
- Pré-condições: pelo menos duas versões confirmadas no mesmo projeto.
- Fluxo principal: 1) abrir lista de versões; 2) selecionar duas versões; 3) executar comparação;
  4) revisar atividades adicionadas/removidas/alteradas e achados novos/resolvidos.
- Resultados esperados: diferenças classificadas, com vínculo às atividades de origem.
- Exceções: identificadores de origem alterados entre versões (pareamento ambíguo deve ser sinalizado,
  não decidido silenciosamente); versões de projetos distintos (bloqueado).
- Critérios de sucesso propostos: diferenças conhecidas em dataset de teste são todas identificadas.
- Evidências disponíveis: nenhuma empírica.
- Hipóteses pendentes: que "comparação básica" (blueprint A.5) atende à necessidade real; critério
  de pareamento de atividades entre versões.

### CU-03 — Justificar formalmente o descarte ou aceite de um achado
- Persona: P-03 (Auditor).
- Objetivo: registrar decisão (ex.: falso positivo aceito como exceção) com justificativa recuperável.
- Evento iniciador: achado em estado aberto atribuído ao auditor.
- Pré-condições: auditoria executada; usuário com permissão de revisão no projeto.
- Fluxo principal: 1) abrir fila de pendências; 2) abrir detalhe do achado; 3) analisar regra e
  evidência; 4) registrar decisão e justificativa; 5) confirmar transição de estado.
- Resultados esperados: decisão registrada com ator, data, justificativa e histórico, sem apagar o
  achado original.
- Exceções: transição de estado inválida (bloqueada no backend); duas pessoas decidindo o mesmo
  achado simultaneamente (sem dupla conclusão).
- Critérios de sucesso propostos: um terceiro consegue reconstruir, só pelo histórico, quem decidiu,
  quando e por quê.
- Evidências disponíveis: nenhuma empírica.
- Hipóteses pendentes: conjunto real de estados de revisão; se justificativa é obrigatória em todos
  os estados.

### CU-04 — Exportar relatório de auditoria para terceiros
- Persona: P-03 (Auditor); secundária P-02.
- Objetivo: entregar resultado de auditoria a cliente/fiscalização em formato legível e estruturado.
- Evento iniciador: solicitação externa de relatório ou fechamento de ciclo de revisão.
- Pré-condições: auditoria concluída; usuário com permissão de exportação.
- Fluxo principal: 1) abrir relatórios; 2) aplicar filtros; 3) exportar CSV e/ou PDF; 4) conferir
  metadados (versão, conjunto de regras, data).
- Resultados esperados: arquivo contém apenas dados autorizados e identifica versão e regras usadas.
- Exceções: usuário sem permissão (negado); valores potencialmente perigosos em CSV (escapados).
- Critérios de sucesso propostos: conteúdo exportado coincide com a consulta de origem.
- Evidências disponíveis: nenhuma empírica.
- Hipóteses pendentes: se a exportação externa é de fato prioritária para os usuários reais; formato
  exigido por clientes/fiscalização.

### CU-05 — Priorizar pendências críticas entre projetos (ADIÇÃO PROPOSTA)
- Persona: P-02 (Coordenador).
- Objetivo: identificar o próximo achado ou projeto que exige ação.
- Evento iniciador: início da rotina de acompanhamento do coordenador.
- Pré-condições: usuário com acesso a um ou mais projetos com auditorias executadas.
- Fluxo principal: 1) abrir home operacional; 2) visualizar pendências críticas e importações
  recentes; 3) filtrar por severidade/responsável; 4) atribuir ou redistribuir achados.
- Resultados esperados: pendências priorizadas com drill-down até a origem.
- Exceções: projeto sem auditoria (estado vazio explícito); permissão parcial (só vê projetos
  autorizados).
- Critérios de sucesso propostos: coordenador identifica o achado mais crítico sem abrir cada
  cronograma.
- Evidências disponíveis: nenhuma empírica.
- Hipóteses pendentes: se o coordenador atua sobre vários projetos ao mesmo tempo; inclusão deste
  cenário depende de aprovação (OQ-07).

## 3. Classificação explícita
- Hipóteses baseadas no blueprint: todas as personas e todos os cenários acima.
- Informações desconhecidas: nº de usuários por papel; hierarquia de aprovação; exigências de
  retenção; formatos de arquivo reais; sobreposição de papéis.
- Evidências disponíveis: nenhuma (sem entrevistas, pesquisas ou métricas de uso).
- Questões para validação com usuários: todos os itens "Hipóteses pendentes" e "Desconhecido".

## 4. Uso futuro
Estes cenários são entrada para F00-E02 (mapa AS-IS/TO-BE), F02-E05/F07-E05 (testes de usabilidade)
e F08-E04 (homologação). F00-E02 NÃO foi iniciada.
