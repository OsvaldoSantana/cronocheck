# CronoCheck — Roteiro de revisão de UX (CRONO-005)

**Estado:** plano de avaliação **não executado**, sem entrevistas, observação ou métricas empíricas.  
**Versão:** 0.1 · **Data:** 2026-10-14  
**Entradas:** [fluxos](flows.md), [wireframes](wireframes.md), [cenários CU-01..05](../product/personas-jtbd.md), blueprint D.4 e RNF-01/RNF-02.

## 1. Objetivo

Avaliar, com pessoas reais quando disponíveis, se os fluxos de **importar,
compreender achados, justificar decisão, comparar versões e exportar** são
compreensíveis sem instrução passo a passo. Registrar limitações e evidências;
não transformar a preferência do designer ou a simples conclusão do documento
em aprovação de usabilidade.

## 2. Participantes (hipóteses, não amostra recrutada)

- P-01 — profissional que recebe e valida cronogramas.
- P-02 — pessoa que prioriza pendências entre obras/projetos (CU-05 só se OQ-07 for validada).
- P-03 — responsável por revisar achados e justificar decisões.

O número e o perfil reais de participantes serão definidos e documentados
em F02-E05. Nenhuma pesquisa ou contato foi realizado nesta entrega.
Não utilizar informações confidenciais da empresa, clientes ou obras.

## 3. Cenários e tarefas observáveis (a executar futuramente)

| ID | Cenário | Tarefa formulada ao participante | Evidência a coletar | Resultado verificável proposto |
|---|---|---|---|---|
| UXT-01 | CU-01 | “Você recebeu um XLSX. Crie uma versão nova sem alterar o arquivo anterior.” | caminho percorrido, erros, tempo, confirmação de versão | usuário identifica a nova versão e explica que a prévia não grava |
| UXT-02 | CU-01 | “O arquivo apresenta uma data inválida. Localize o problema e retorne ao mapeamento.” | origem/linha/célula e ação escolhida | usuário identifica o erro impeditivo, sem gerar versão |
| UXT-03 | CU-01 | “O cronograma tem um ID duplicado. Localize o achado e sua origem.” | descrição verbal da regra e linhas afetadas | diferencia achado posterior de erro impeditivo de importação |
| UXT-04 | CU-03 | “Analise um achado e registre uma justificativa para a decisão permitida.” | tempo, permissão, resultado e compreensão do histórico | consegue recuperar ator, data, motivo e evidência original |
| UXT-05 | CU-03 | “Outro revisor mudou o achado antes de sua confirmação. O que você faria?” | comportamento diante do conflito e recuperação | não sobrescreve decisão anterior silenciosamente |
| UXT-06 | CU-02 | “Compare V1 e V2 e identifique atividade adicionada, removida e alterada.” | classificação obtida e origem | resultados coerentes com fixtures sintéticas e ambiguidade sinalizada |
| UXT-07 | CU-04 | “Exporte um relatório filtrado para terceiro e confira a versão do cronograma.” | filtros, autorização e metadados | usuário identifica versão, RuleSet e escopo autorizado |
| UXT-08 | CU-05* | “Entre nos projetos permitidos e encontre a pendência mais urgente.” | navegação, seleção do projeto e retorno | resultado interpretável sem exibir projetos sem acesso |
| UXT-09 | transversal | “Volte do detalhe de um achado à fila na mesma página e filtros.” | estado antes/depois | contexto preservado sem redirecionamento externo |
| UXT-10 | RNF-02 | “Execute tarefas por teclado ou tecnologias assistivas relevantes.” | foco, ordem de leitura, labels, anúncios | nenhuma etapa essencial exige exclusivamente mouse |

*CU-05 depende de OQ-07 e acesso a mais de um projeto autorizado; não presume cenário real validado.*

## 4. Ficha de observação (template vazio)

| Campo | Valor a registrar depois do teste |
|---|---|
| Sessão | Identificador pseudônimo; **não** nome ou dado pessoal no repositório público |
| Persona/CU | Identificador do perfil e cenário |
| Ambiente | Dispositivo, viewport, navegador, recursos assistivos quando aplicável |
| Tarefa | UXT-01...10 |
| Conclusão | Sim / Parcial / Não / Não testável |
| Caminho e desvios | Sequência de telas reais observada |
| Tempo de tarefa | Medição real, nunca inferida |
| Erros e obstáculos | Descrição do que aconteceu, sem culpar participante |
| Comentários diretos | Registrar somente com consentimento e remover identificadores |
| Ajuste proposto | Mudança na UI ou documentação, com responsável |
| Severidade | Bloqueante / Alta / Média / Baixa, justificada |
| Evidências de reprodução | Capturas sintéticas autorizadas ou passos descritos |
| Revisão/aceite | Responsável + data + restrições |

## 5. Heurísticas de inspeção (não realizadas nesta etapa)

- [ ] O usuário identifica projeto, versão e RuleSet antes de decidir.
- [ ] A ação principal da tela é identificável sem disputar atenção com gráficos.
- [ ] O wizard distingue erro impeditivo de warning e achado posterior.
- [ ] Tela de prévia permite voltar e remapear sem criar versão silenciosa.
- [ ] Estados assíncronos vêm do backend e são recuperáveis após refresh.
- [ ] A mesma operação retomada não duplica versão/auditoria.
- [ ] Filtros, ordenação e paginação permanecem quando navega para trás.
- [ ] Achado informa regra, versão, origem e atividade afetada.
- [ ] Decisão humana exige autorização, confirmação e trilha recuperável.
- [ ] Conflitos de concorrência são explicados e não sobrescrevem o trabalho alheio.
- [ ] A ausência de achados não é rotulada como “cronograma correto”.
- [ ] Tela responsiva não perde contexto ou controles essenciais.
- [ ] Mensagens de validação têm texto e não dependem só de cor/ícone.
- [ ] Fluxos essenciais têm foco visível, acesso por teclado e semântica para leitor de tela.
- [ ] Exportações mostram a origem da informação e não permitem leitura indevida.

## 6. Critérios de revisão técnica e gate

| Avaliação | Como comprovar | Estado |
|---|---|---|
| Cobertura de navegação | Seis seções e nove telas mínimas do blueprint D.1–D.2 | Documentado, não homologado |
| Cobertura de casos | CU-01..CU-05 ligados a FL-01..FL-05 | Documentado, não validado empiricamente |
| Wireframes | W-01..W-11 e estados de erro/permissão/conflito | Documentado, não testado em interface real |
| Acessibilidade | Checklist técnico e tarefas UXT-10 | Planejado, sem testes executados |
| UX com participantes | Sessões e evidências reais conforme F02-E05 | Não iniciado |
| Protótipo clicável | Navegação real sem backend para revisão de tarefas F02-E02 | Não implementado |
| Aprovação CRONO-005 | Registro nominal, datado e decisões abertas | Pendente |
| Gate G0 e Gate G2 | Critérios gerais de fase, além desta entrega | Não aprovados |

## 7. Perguntas que não devem ser respondidas silenciosamente

1. O planejador importa cronogramas ou essa atribuição cabe a outro papel?
2. A hierarquia de atividades deve aparecer na fila de achados ou no detalhe?
3. A revisão necessita estados, níveis de aprovação e justificativa obrigatória? Qual regra?
4. Como o usuário identifica a diferença entre dois `AuditRun` para a mesma versão?
5. Deve haver visão multiprojeto ou apenas home por projeto (OQ-07)?
6. Como o calendário profissional afetará o formulário de datas e prazos (OQ-03/08)?
7. A relação de dois registros com mesmo ID de origem exige um passo adicional de conciliação (OQ-09)?

**Nenhuma resposta foi obtida por entrevista nesta etapa.** Essas questões devem alimentar F00
e os workshops/testes F02, não ser convertidas silenciosamente em requisitos definitivos.
