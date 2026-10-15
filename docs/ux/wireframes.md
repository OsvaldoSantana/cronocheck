# CronoCheck — Wireframes de baixa fidelidade (CRONO-005 / v0.1)

> **Atualização de 15/10/2026:** CU-05 priorizado pela OQ-07, ainda sem validação empírica; wizard de sete colunas e predecessor FS são apenas ilustrações sintéticas v0, não o escopo do domínio robusto aprovado na OQ-03. Ver `../product/decisions-2026-10-15.md`.

**Status:** proposta de UX para revisão; sem frontend implementado e sem entrevistas.  
**Escopo:** representações textuais e de navegação, legíveis no GitHub, destinadas a posterior protótipo clicável em F02-E02. **Não** são maquetes de alta fidelidade.  
**Fontes:** [fluxos](flows.md), blueprint D.1–D.4, PRD, jornada F00-E02 e dados XLSX **sintéticos** da F00-E04.

## 1. Padrão de composição e navegação

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ CronoCheck  | Projeto: [Projeto sintético ▾]  |  Versão: [V2 ▾]   [Usuário]   │
├──────────────┬───────────────────────────────────────────────────────────────┤
│ Projetos     │ Breadcrumb > Projeto > Tela                                    │
│ Importações  │ Título da tela                           [Ação principal]      │
│ Auditorias   │ Contexto: projeto • versão • última execução • regra           │
│ Pendências   ├───────────────────────────────────────────────────────────────┤
│ Relatórios   │ Conteúdo / tabelas / filtros / estados                          │
│ Configurações│                                                               │
└──────────────┴───────────────────────────────────────────────────────────────┘
```

- Largura, espaçamento, densidade e tema são propostas de F02-E03, ainda não tokens finais.
- Projeto, versão e execução aparecem de modo explícito; nunca trocar apenas porque outro
  item ficou “mais recente”.
- Navegação lateral preserva **seis rótulos do blueprint**. Em dispositivos menores,
  usar menu recolhível com foco gerenciado e identificação do projeto.
- As telas mostram informações autorizadas e caminhos de retorno; o backend verificará
  permissão em toda requisição.
- Componentes e botões representados são **conceituais**; nenhum é funcional neste documento.

## W-01 — Acesso e seleção de projeto

```text
┌───────────────────────────────┐  ┌────────────────────────────────────────────┐
│ CRONOCHECK                    │  │ Selecionar projeto                          │
│ Acesso                        │  │                                            │
│ [ Entrar com identidade ]     │  │ [Buscar projeto                    ]        │
│                               │  │ Projeto sintético A    [Abrir →]           │
│ Sessão expirada? Entre de     │  │ Projeto sintético B    [Abrir →]           │
│ novo e retome com segurança.  │  │                                            │
└───────────────────────────────┘  │ [Criar projeto] (se autorizado)             │
                                   └────────────────────────────────────────────┘
```

**Ações:** autenticar, buscar projeto permitido, selecionar.  
**Estados:** nenhum projeto autorizado → texto explicativo + solicitar acesso/criar se permitido; sessão expirada → reautenticar; acesso negado → mensagem neutra.  
**Acessibilidade:** labels de formulário, título único, foco preservado após redirecionamento autorizado.

## W-02 — Home operacional do projeto

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Projetos / Projeto sintético A                                                │
│ Projeto sintético A                    [Importar cronograma XLSX]             │
│ Versão em análise: V2 • Auditoria R2 • 6 achados* (exemplo ilustrativo)       │
├──────────────────────────────────────────────────────────────────────────────┤
│ PRÓXIMA AÇÃO                                                                 │
│ [Revisar achados críticos →]  [Comparar V1 e V2 →]                            │
├──────────────────────────────────────────────────────────────────────────────┤
│ Pendências críticas                  │ Últimas importações                    │
│ [Abrir achado D001 duplicado →]      │ V2 • execução pendente [Acompanhar]     │
│ [Abrir ciclo de predecessoras →]     │ V1 • importação confirmada [Abrir]      │
├──────────────────────────────────────┴───────────────────────────────────────┤
│ Projetos com acesso autorizado: [Trocar projeto]                               │
└──────────────────────────────────────────────────────────────────────────────┘
```

_*Contagens da figura não são resultados do motor e não representam dados reais._
**Estados:** projeto sem versão → “Nenhum cronograma importado” + CTA; versão sem
auditoria → CTA executar; auditoria em execução → status do servidor; zero achados →
“Nenhum achado detectado pelas regras executadas”, nunca “cronograma correto”.
**CU-05:** visão multiprojeto é hipótese de navegação condicionada a OQ-07.

## W-03 — Wizard / etapa 1: selecionar arquivo

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Projeto A / Importações / Nova                                                │
│ Importar cronograma • Etapa 1 de 4 — Arquivo                                  │
│ ● Arquivo   ○ Mapeamento   ○ Prévia   ○ Confirmação                             │
├──────────────────────────────────────────────────────────────────────────────┤
│ Arquivo XLSX                                                                  │
│ [Selecionar arquivo]    ou arraste um arquivo (opcional)                       │
│ Exemplo: basic-valid.xlsx                                                     │
│                                                                              │
│ Validação: aguardando seleção. Tipos/limites serão verificados pelo servidor.│
│ [Cancelar]                                              [Continuar →]         │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Erros:** extensão falsa / OOXML inválido / tamanho excessivo / sem permissão →
mensagem explicativa sem afirmar que a versão foi criada. **Operações longas:**
upload informa etapa real do servidor e pode ser retomado de modo seguro.
**Acessibilidade:** não depender exclusivamente de drag-and-drop.

## W-04 — Wizard / etapa 2: mapear colunas

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Importar cronograma • Etapa 2 de 4 — Mapeamento                               │
│ ● Arquivo   ● Mapeamento   ○ Prévia   ○ Confirmação                             │
├──────────────────────────────────────────────────────────────────────────────┤
│ Aba de origem: [Activities ▾]                                                │
│                                                                              │
│ Campo de destino            Coluna de origem         Status                    │
│ ID da atividade*            [activity_id      ▾]     ✓ Mapeada                 │
│ Nome da atividade*          [name             ▾]     ✓ Mapeada                 │
│ Início*                     [start_date       ▾]     ✓ Mapeada                 │
│ Término*                    [finish_date      ▾]     ✓ Mapeada                 │
│ Duração*                    [duration_calendar_days ▾] ✓ Mapeada             │
│ Predecessoras               [predecessors_fs  ▾]     Opcional                  │
│ Atividade-pai               [parent_activity_id ▾]  Opcional                  │
│                                                                              │
│ [Voltar]                                    [Ver prévia e validar →]           │
└──────────────────────────────────────────────────────────────────────────────┘
```

_*Obrigatoriedade somente do perfil sintético v0; semântica OQ-08 pendente._
**Erros:** coluna obrigatória não mapeada → resumo e foco na linha com problema;
duplicidade de mapeamento → explicar conflito em vez de escolher silenciosamente.
**Operação:** wizard oferece sugestão editável; não tratar inferência de coluna como
decisão irrevogável.

## W-05 — Wizard / etapa 3: prévia e validação

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Importar cronograma • Etapa 3 de 4 — Prévia                                   │
│ ● Arquivo   ● Mapeamento   ● Prévia   ○ Confirmação                             │
├──────────────────────────────────────────────────────────────────────────────┤
│ Origem: Activities • 4 atividades | Erros impeditivos: 0 | Avisos: 0           │
│ [Erros] [Avisos] [Linhas]                                                      │
│                                                                              │
│ Linha   ID      Nome                    Início      Fim          Predecessora  │
│ 2       A001    Planejamento sintético  2026-11-02  2026-11-03   —            │
│ 3       A002    Preparação sintética    2026-11-04  2026-11-05   A001         │
│ ...                                                                          │
├──────────────────────────────────────────────────────────────────────────────┤
│ Um aviso não equivale a bloqueio. A auditoria verificará regras após confirmar.│
│ [Voltar ao mapeamento]                           [Revisar confirmação →]     │
└──────────────────────────────────────────────────────────────────────────────┘
```

_Os valores da figura são exemplos de apresentação, não saídas reais de uma API. Para o fixture `basic-valid.xlsx`, a especificação prevê zero avisos estruturais nesta fase._
**Erros impeditivos:** por exemplo “Activities!C2: data `2026-02-30` não é válida”;
ação primária desabilitada até resolução. **Achados de auditoria (posteriores):**
duplicatas, predecessoras ausentes ou ciclos não devem ser falsamente rotulados como
erro do parser. **Regra:** evidenciar origem e valor bruto/normalizado.

## W-06 — Wizard / etapa 4: confirmar criação da versão

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Importar cronograma • Etapa 4 de 4 — Confirmar                                │
│ ● Arquivo   ● Mapeamento   ● Prévia   ● Confirmação                             │
├──────────────────────────────────────────────────────────────────────────────┤
│ Projeto            Projeto sintético A                                        │
│ Arquivo            basic-valid.xlsx                                          │
│ Aba                Activities                                                │
│ Linhas válidas     4                                                         │
│ Erros impeditivos  0                                                         │
│ SHA-256            gerado pelo servidor após receber os bytes do arquivo      │
│                                                                              │
│ A confirmação cria uma nova versão, preserva o original e o mapeamento.      │
│ Não aprova o cronograma e não corrige automaticamente as inconsistências.     │
│                                                                              │
│ [Voltar]                                        [Confirmar nova versão]       │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Estados após ação:** aguardando servidor → versão Vn confirmada; falhou →
erro e opção de tentar novamente com idempotência; operação já confirmada →
abrir mesma Vn, sem duplicação. Nunca exibir “Versão criada” antes da resposta
do servidor. A forma exata de hash e política de confirmação dependem de F04.

## W-07 — Auditorias e fila de achados

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Projeto A / Auditorias / Execução #R2 • V2 • RuleSet v1                       │
│ Status: Concluída                       [Executar auditoria novamente]        │
├──────────────────────────────────────────────────────────────────────────────┤
│ Pendências: [Buscar                         ] [Severidade ▾] [Estado ▾]       │
│             [Responsável ▾] [Ordenação ▾]                     [Limpar filtros] │
│                                                                              │
│ Achado           Regra            Evidência          Estado          Abrir    │
│ D001 duplicado   duplicate_id     Activities!A2:A3   Aberto          [→]      │
│ Predecessora?    missing_pred     Activities!F3      Aberto          [→]      │
│                                                                              │
│ Exibindo 1–2 de 2  [Anterior] [Próxima]                                       │
│ [Retornar ao projeto]  [Comparar versões]  [Exportar relatório]               │
└──────────────────────────────────────────────────────────────────────────────┘
```

Exemplos de linhas pertencem a **fixtures diferentes** e servem somente para mostrar
layout. Uma execução real exibirá exclusivamente achados associados à versão e regra
declaradas. Filtros e paginação devem permanecer na URL/estado ao abrir detalhes e voltar.
Não confundir `RuleSetVersion` com a `ScheduleVersion`.

## W-08 — Detalhe de achado e revisão humana

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Pendências (filtros preservados) / Achado • duplicidade de ID                 │
│ Projeto A • Versão V2 • Auditoria #R2 • Regra duplicate_activity_id/v1       │
├───────────────────────────────────┬──────────────────────────────────────────┤
│ EVIDÊNCIA DA REGRA                │ REVISÃO HUMANA                            │
│ ID origem: D001                   │ Estado atual: Aberto                      │
│ Activities!A2 → D001              │ Responsável: [Selecionar ▾]             │
│ Activities!A3 → D001              │ Ação: [Decisão permitida ▾]             │
│ Critério: mesmo ID em duas linhas │ Justificativa: [                    ]   │
│ Dados preservados na V2           │               [                    ]   │
│ Regra/versão • entradas • saída   │ [Rever decisão e confirmar]             │
├───────────────────────────────────┴──────────────────────────────────────────┤
│ HISTÓRICO                                                                    │
│ [Instante UTC/local] [Ator] [Ação] [Justificativa disponível]                │
│ A decisão não altera a evidência original.                                    │
│ [← Voltar às pendências]                                                       │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Estados essenciais:** usuário sem permissão → somente leitura; achado alterado
por outro revisor → conflito com recarregar/comparar, sem overwrite; tentativa
de transição inválida → rejeição clara. Os estados e a forma de justificar
são hipóteses (F06); `AuditEvent` deverá ter ator, instante e contexto.

**Mobile (W-08-M):** evidência primeiro, revisão em aba/painel seguinte, histórico
acessível por navegação de foco; nunca ocultar identificação de projeto/versão.

## W-09 — Versões e comparação

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Projeto A / Versões                                                          │
│ [Versão base: V1 ▾]   [Versão alvo: V2 ▾]           [Comparar versões]        │
│ Mesmo projeto • duas versões confirmadas • regras/versões identificadas       │
├──────────────────────────────────────────────────────────────────────────────┤
│ [Adicionadas] [Removidas] [Modificadas] [Sem alteração] [Ambiguidades]         │
│                                                                              │
│ ID      Mudança       Campo          Origem         Destino                   │
│ M004    Adicionada    —              —              V2                      │
│ M002    Removida      —              V1             —                       │
│ M003    Modificada    name           Atividade antiga  Atividade modificada │
│ M001    Igual         —              V1             V2                      │
│                                                                              │
│ [Inspecionar evidência]         [Retornar às versões]                         │
└──────────────────────────────────────────────────────────────────────────────┘
```

As linhas reproduzem o cenário sintético `multi-version-v1/v2` como
**expectativa**, não resultado de API. Não parear duas atividades com ID repetido
sem sinalizar ambiguidade (OQ-09).

## W-10 — Relatórios, exportação e configurações

```text
┌────────────────────────────────────────┐ ┌────────────────────────────────────┐
│ Relatórios • Projeto A                 │ │ Configurações • Projeto A          │
│ Versão [V2 ▾] Execução [R2 ▾]          │ │ Membros e papéis                   │
│ Filtros [Severidade ▾] [Estado ▾]      │ │ Usuário autorizado [Papel ▾]      │
│                                        │ │ [Gerenciar] (se permitido)         │
│ Prévia: período e conjunto de regras  │ │                                    │
│ Metadados: versão • RuleSet • data     │ │ Usuário sem permissão:             │
│ [Exportar CSV]   [Exportar PDF]        │ │ "Você não pode alterar membros"    │
└────────────────────────────────────────┘ └────────────────────────────────────┘
```

**Segurança de exportação:** verificar permissão no backend, incluir metadados do
escopo autorizado e proteger contra fórmula maliciosa em células CSV.
**Administração:** não exibir os membros de projetos sem acesso; funções de membro
reais serão definidas em F03.

## W-11 — Mobile: wizard e achado em sequência linear

```text
┌─────────────────────────────┐   ┌──────────────────────────────┐
│ ☰  CronoCheck               │   │ ← Achado D001 • V2           │
│ Projeto sintético A ▾       │   │ Regra / versão              │
│ Nova importação             │   ├──────────────────────────────┤
│ 2 de 4 • Mapeamento         │   │ Evidência                   │
├─────────────────────────────┤   │ Origem Activities!A2/A3     │
│ Campo: ID atividade         │   │ Valores e contexto          │
│ [activity_id ▾]             │   ├──────────────────────────────┤
│ Campo: Nome                 │   │ Revisar (se permitido)      │
│ [name ▾]                    │   │ [Decisão permitida ▾]       │
│ …                           │   │ [Justificativa             ] │
│ [← Voltar] [Prévia →]        │   │ [Rever antes de confirmar]  │
└─────────────────────────────┘   │ [Voltar à lista filtrada]    │
                                  └──────────────────────────────┘
```

Nada depende exclusivamente de hover. Preservar foco, título, contexto e
mensagens. Não prometer paridade em layout pixel-a-pixel: testar tarefas em
larguras reais na F02.

## 2. Matriz de estados por tela

| Tela | Empty | Loading/long job | Erro | Acesso negado | Sucesso | Conflito/retorno |
|---|---|---|---|---|---|---|
| W-01 | sem projetos | autenticação | falha de login | seleção negada | projeto aberto | sessão expirada |
| W-02 | sem importações | status do projeto | dados indisponíveis | projeto não autorizado | próximo passo | versão alterada |
| W-03..06 | sem arquivo | upload/prévia/confirmar | inválido/mapeamento | upload negado | versão confirmada | retry sem duplicar |
| W-07 | sem auditorias/achados | job em fila/executando | job falhou | auditoria negada | resultados exibidos | página/filtros preservados |
| W-08 | sem histórico | salvando decisão | transição inválida | modo leitura | evento confirmado | conflito de concorrência |
| W-09 | menos de duas versões | comparando | versões incompatíveis | projeto negado | diff rastreável | ambiguidade exposta |
| W-10 | sem relatório/membro | gerando exportação | exportação falhou | exportação/edição negada | arquivo gerado | repetir sem expor dados |
| W-11 | etapa inicial | espera anunciada | erro vinculado ao campo | acesso limitado | continuidade | retorno ao mesmo contexto |

## 3. Componentes a desenhar em F02-E03 (não implementados)

- Seletor de projeto com navegação acessível e sinalização de contexto.
- Stepper do wizard com progresso textual (não só mudança de cor).
- Card de estado de importação/job assíncrono com recuperação após refresh.
- Tabela de prévia com valores brutos/normalizados e origem.
- Painel de erros impeditivos separado da lista de avisos.
- Tabela de achados com filtros persistentes e paginação.
- Visor de evidências `RuleId/Version/SourceLocator`.
- Formulário de revisão com validações e confirmação contextual.
- Histórico cronológico com ator/instante em UTC e apresentação local.
- Diff entre versões com categoria de ambiguidade explícita.
- Exportação com metadados de escopo.
- Dialog, toast e banners apropriados: ações irreversíveis não dependem só de toast.

## 4. Hipóteses, decisões e aceite

| Tema | Hipótese ilustrada | Pendente |
|---|---|---|
| Predecessoras FS | Exibição/alerta para vínculos suportados | OQ-03 |
| CU-05 multiprojeto | Entrada na home para pendências | OQ-07 |
| Datas e duração | Campos v0 com texto ISO e dias corridos | OQ-08 |
| IDs duplicados | Evidência de duas linhas distintas | OQ-09 |
| Estado de achado | Formulário de decisão com transições permitidas | F06 e validação com usuários |
| Meta de UX | Concluir tarefa sem bloqueios críticos | Testes de F02-E05; não inventar taxa |

**Condições de saída desta entrega:** wireframes cobrindo as telas D.2,
importação e revisão com cenários negativos, desktop/mobile e rastreabilidade
para CU-01..05; **ainda falta** revisão humana, teste com usuários e construção
de protótipo clicável (F02-E02). O Gate G0 permanece não aprovado.
