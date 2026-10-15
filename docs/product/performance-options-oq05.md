# OQ-05 — Metas de desempenho, recuperação e critérios de aceite

**Status:** explicação de alternativas; **NÃO DECIDIDA** em 15/10/2026.  
**Fontes:** PRD v1.2 §9 (RNF-03, RNF-04, RNF-08), `risk-kpi-plan.md` e `requirements-prioritization.md`.  
**Atenção:** os números abaixo são **propostas de requisitos existentes**, não medições, SLAs firmados ou tempos já alcançados pelo CronoCheck.

## 1. O que significam RNF-03, RNF-04, RNF-08?

| ID | Meta da baseline documental | Significado prático |
|---|---|---|
| **RNF-03** | Resposta de consultas usuais com **p95 inferior a 500 ms** em cenário de referência | Ao medir 100 requisições comparáveis, pelo menos cerca de 95 devem terminar em menos de 0,5 s, no ambiente e carga definidos. Não inclui automaticamente upload/auditoria e não equivale à percepção total da página. |
| **RNF-04** | Processar um XLSX de **5.000 atividades em até 60 s**, no ambiente de referência | Tempo de processamento completo precisa ter ponto inicial/final explícitos; a verificação atual de OOXML não executa importador nem motor C#. |
| **RNF-08** | Backup/recuperação: **RPO de 24 h, RTO de 4 h** | RPO é o máximo de dados potencialmente perdidos em desastre (até 24 h); RTO é quanto tempo o sistema poderia levar para voltar a operar (até 4 h), na situação acordada. |

**Importante:** não é adequado comparar “p95 500 ms” sem definir volume de
dados, quantidade de usuários concorrentes, tipo de consulta e
infraestrutura. Também não se deve equiparar “5.000 atividades” a 5.000
relações: um cronograma pode ter muitas predecessoras por atividade,
calendários e defasagens complexas (OQ-03).

## 2. Quais são as alternativas de compromisso?

| Modelo | O que você aprova agora | Vantagem | Risco / consequência |
|---|---|---|---|
| **A — Metas contratuais fixas agora** | Exigir os valores documentados independentemente de benchmark inicial | Critério simples e objetivamente testável; previsibilidade aparente | Escolher números sem conhecer cenário pode bloquear lançamento ou incentivar otimização superficial e mudanças de escopo |
| **B — Metas provisórias com calibração e aprovação antes do release** | Preservar números como **hipóteses-alvo**; definir testes reproduzíveis e só fixar limites após benchmarks/restore | Evidência real, evita promessas infundadas; permite dimensionar infraestrutura | Exige governança para não terminar com metas vagas ou adiamentos indefinidos |
| **C — Objetivos graduais por classe de carga** | Definir faixas de capacidade (pequeno/médio/grande), com limites distintos e orçamento/infra acordados | Faz sentido para clientes/volumes diversos; facilita planejamento de escala | Mais testes e contratos, maior custo operacional e de manutenção |
| **D — Nenhum limite mensurável agora ou no MVP** | Aceitar desempenho “razoável” sem critério objetivo | Facilita começar rapidamente | **Não recomendada:** impede provar qualidade, capacidade e recuperação; contradiz robustez desejada |

**Recomendação para discussão:** **B como método de decisão**, com **C na
especificação de cenários de carga**. Preservar exigência de testes e
resultados objetivos no gate de release. Não adotar D; A só é defensável
se houver contexto e compromisso de infraestrutura suficientes.

## 3. Como medir corretamente (plano de engenharia proposto)

### RNF-03 — API e experiência percebida

Definir classes de operações: consulta de projetos; listagem de versões;
lista filtrada de achados; detalhe/evidências; comparativo. Relatar
p50/p95/p99 e taxas de erro com tamanho de dataset, cache e concorrência
documentados. Medir também **jornada percebida** (navegação/estado de job),
pois p95 da API não cobre renderização e espera de auditoria.

### RNF-04 — Importação e auditoria

Separar: tempo de upload, validação de segurança, leitura XLSX,
normalização/persistência, enfileiramento, auditoria e obtenção do resultado.
Medir a operação total **e** suas etapas, com definições inequívocas.
Usar cenários de 5.000 atividades com complexidade variada: quantidade
de predecessoras, relações FS/SS/FF/SF, lag/lead, múltiplos calendários,
restrições e hierarquia. Reportar memória máxima, CPU, falhas e retries,
e não apenas tempo de sucesso.

### RNF-08 — Continuidade e recuperação

Definir quais dados entram no RPO: PostgreSQL, histórico, AuditEvent,
snapshots normalizados **e arquivos originais em storage privado**. Exercitar
restauração em ambiente isolado, medir o tempo real e comprovar integridade
dos hashes. Backup configurado não equivale a restore testado.

### Condição de aceitação sugerida antes do release

- Definir ambiente de referência **antes** da medição (CPU, RAM, disco,
  rede, região, versão da aplicação/banco/storage).
- Definir cenário controlado de carga (projetos, atividades, dependências,
  usuários simultâneos, arquivos, cálculos de calendário).
- Executar repetidamente, com amostra suficiente, relatar distribuição
  e taxa de erros; não usar uma execução isolada como p95.
- Registrar limiar acordado, custos de infraestrutura correspondentes,
  exceções conhecidas e decisão de **go/no-go** com responsável e data.
- Retestar após mudanças importantes de parser, regras, domínio ou banco.

## 4. Robustez e escalabilidade não são números ilimitados

O objetivo técnico saudável é **crescimento controlado da capacidade**,
sem perda silenciosa de dados e com isolamento de workloads. Cada classe
de uso deve possuir limite conhecido, comportamento de degradação,
observabilidade e trajetória de evolução.

Uma promessa de "qualquer volume" não é verificável; sem faixas e medições
não podemos distinguir gargalo, custo e falha de produto.

## 5. Exemplo de aprovação possível (NÃO PREENCHIDO)

```text
OQ-05: [A / B / C / B+C / outra]
RNF-03: [valor e cenário / provisório com marco para aprovar]
RNF-04: [tamanho e tempo / provisório com marco para aprovar]
RNF-08: [RPO/RTO e cenário de desastre / provisório com marco para aprovar]
Data e aprovador: [PENDENTE]
Evidência da decisão: [PENDENTE]
```

**Nenhum modelo foi selecionado pelo responsável** nesta rodada. Até
nova autorização, RNF-03/04/08 continuam metas **propostas**, sem SLAs
ou medições comprovadas.
