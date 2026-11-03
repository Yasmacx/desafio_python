# SmartClinic

Sistema de gerenciamento de consultas médicas desenvolvido em **Python** e **SQLite**.

O projeto tem como objetivo aplicar conceitos de **programação, banco de dados relacionais, SQL, CRUD e regras de negócio** em um sistema de agendamento de consultas.

# Sistema

## 1. Descrição

O SmartClinic é um sistema de agendamento e gerenciamento de consultas médicas desenvolvido para facilitar a comunicação entre pacientes e médicos de clínicas de pequeno porte.

O sistema tem como objetivo simplificar o agendamento de consultas para os pacientes e oferecer aos médicos uma visão clara e organizada de seus compromissos, pacientes e disponibilidade de atendimento.

A aplicação contará com uma interface para pacientes, uma interface para médicos e um sistema de autenticação que permitirá o acesso às funcionalidades de acordo com o perfil de cada usuário.

## 2. Problema

O gerenciamento de consultas médicas pode se tornar desorganizado quando depende de processos manuais, dificultando o acompanhamento dos agendamentos, das confirmações, dos cancelamentos e da disponibilidade dos médicos.

Além disso, os pacientes precisam de uma maneira simples de consultar seus compromissos e solicitar novos horários.

O SmartClinic pretende centralizar essas informações em um único sistema, tornando o processo mais organizado, acessível e eficiente.

## 3. Objetivo geral

Desenvolver uma aplicação web full stack para agendamento e gerenciamento de consultas médicas, com funcionalidades específicas para pacientes e médicos.

## 4. Objetivos específicos

- Permitir o cadastro e a autenticação de pacientes e médicos.
- Oferecer um painel individual para cada perfil.
- Permitir que pacientes consultem seus agendamentos e solicitem novas consultas.
- Permitir que pacientes acompanhem o status de suas consultas.
- Permitir que médicos visualizem sua agenda de atendimentos.
- Organizar consultas por dia, semana e mês.
- Permitir o gerenciamento de confirmações e cancelamentos.
- Permitir que médicos gerenciem sua disponibilidade e reorganizem agendamentos.
- Armazenar os dados de maneira persistente em um banco de dados.
- Garantir que cada usuário tenha acesso somente às informações autorizadas para seu perfil.
- Disponibilizar uma interface simples, objetiva e intuitiva.

## 5. Público-alvo

### Pacientes

Pessoas que desejam agendar consultas com médicos específicos, acompanhar seus compromissos e consultar o histórico de atendimentos.

### Médicos

Profissionais que atendem em clínicas de pequeno porte e precisam organizar seus horários, visualizar seus pacientes e gerenciar a agenda de consultas.

## 6. Proposta de valor

O SmartClinic busca unir simplicidade para o paciente e organização para o médico, centralizando o agendamento e o acompanhamento de consultas em uma única aplicação.

## 7. Escopo inicial

A primeira versão do sistema deverá contemplar:

- Cadastro e autenticação de usuários.  &#x20;
- Separação entre os perfis de paciente e médico.
- Persistência dos dados em banco de dados.
- Agendamento e consulta de horários disponíveis.
- Visualização e gerenciamento de consultas.
- Controle de status das consultas.
- Painéis específicos para pacientes e médicos.
- Validação das regras de negócio no backend.

Funcionalidades adicionais serão avaliadas conforme o desenvolvimento evoluir.

## 8. Tecnologias previstas

- Python: desenvolvimento do backend.
- SQL: consultas e manipulação de dados.
- SQLite: banco de dados inicial.
- API: comunicação entre frontend e backend.
- HTML: estrutura das páginas.
- CSS: apresentação visual.
- JavaScript: interatividade e comunicação com a API.
- Docker: preparação de um ambiente de execução reproduzível.

O framework de backend, as bibliotecas auxiliares e as ferramentas de teste serão definidos durante o planejamento técnico.

## 9. Metodologia de desenvolvimento

O projeto será desenvolvido incrementalmente, com documentação das decisões técnicas, definição de requisitos, implementação por funcionalidades, testes e versionamento com Git e GitHub.

A inteligência artificial será utilizada como ferramenta de apoio para planejamento, programação, explicação de conceitos, revisão de código e investigação de erros.

As soluções sugeridas serão avaliadas e testadas antes de serem incorporadas ao projeto.

---

# Banco de Dados

## Entidades

O sistema é composto por três entidades principais:

- **Paciente**
- **Médico**
- **Consulta**

---

## Paciente

### Funcionalidades

- [ ] Cadastrar paciente
- [ ] Agendar consulta
- [ ] Cancelar consulta

### Atributos

| Atributo | Tipo | Regra |
|---|---|---|
| `id` | INTEGER | Chave primária |
| `nome` | TEXT | Obrigatório |
| `cpf` | TEXT | Obrigatório e único |
| `data_nascimento` | TEXT/DATE | Obrigatório |

### Regras de negócio

- O CPF deve ser único.
- Um CPF não pode estar associado a mais de um paciente.
- Todos os dados necessários para o cadastro devem ser informados.

---

## Médico

### Funcionalidades

- [ ] Cadastrar médico
- [ ] Visualizar consultas marcadas
- [ ] Cancelar consulta

### Atributos

| Atributo | Tipo | Regra |
|---|---|---|
| `id` | INTEGER | Chave primária |
| `nome` | TEXT | Obrigatório |
| `especialidade` | TEXT | Obrigatório |
| `crm` | TEXT | Obrigatório e único |

### Regras de negócio

- Cada médico possui um CRM único.
- O médico é identificado por sua especialidade.
- Um médico não pode atender dois pacientes no mesmo horário.

---

## Consulta

### Funcionalidades

- [ ] Agendar consulta
- [ ] Cancelar consulta
- [ ] Alterar horário
- [ ] Consultar status da consulta

### Atributos

| Atributo | Tipo | Regra |
|---|---|---|
| `id` | INTEGER | Chave primária |
| `paciente_id` | INTEGER | Chave estrangeira |
| `medico_id` | INTEGER | Chave estrangeira |
| `data` | TEXT/DATE | Obrigatório |
| `hora` | TEXT/TIME | Obrigatório |
| `status` | TEXT | Obrigatório + CHECK |

### Status disponíveis

O status da consulta pode assumir apenas um dos seguintes valores:

```sql
CHECK(status IN ('confirmada', 'cancelada', 'realizada'))
```

---

## Regras de negócio do agendamento

### Conflito de horário do paciente

Um paciente não pode possuir duas consultas no mesmo horário.

### Conflito de horário do médico

Um médico não pode possuir dois pacientes agendados para o mesmo horário.

### Horário indisponível

Caso o horário solicitado esteja ocupado, o sistema deverá informar a indisponibilidade e indicar outro horário disponível.

### Cancelamento

Quando uma consulta for cancelada, o horário deverá ser liberado para um novo agendamento.

### Realocação

O médico poderá realocar uma consulta para outro horário disponível.

---

## Banco de Dados

O projeto utiliza **SQLite** como banco de dados.

### Estrutura e relacionamentos

```text
PACIENTES
   |
   | 1:N
   |
   v
CONSULTAS
   ^
   |
   | N:1
   |
MÉDICOS
```

### Relacionamentos

- Um paciente pode possuir várias consultas.
- Um médico pode possuir várias consultas.
- Cada consulta pertence a um paciente.
- Cada consulta pertence a um médico.

As relações são estabelecidas através de chaves estrangeiras:

```sql
FOREIGN KEY(medico_id) REFERENCES medicos(id),
FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
```

---

## Integridade dos dados

O banco utiliza restrições para garantir a consistência das informações:

| Restrição | Utilização |
|---|---|
| `PRIMARY KEY` | Identificação única dos registros |
| `NOT NULL` | Campos obrigatórios |
| `UNIQUE` | CPF e CRM |
| `FOREIGN KEY` | Relacionamento entre tabelas |
| `CHECK` | Controle dos status da consulta |

---

## Tecnologias

- Python
- SQLite
- SQL
- Git
- GitHub

---

## Objetivo do projeto

O **SmartClinic** está sendo desenvolvido como um projeto de estudo e portfólio para colocar em prática conhecimentos de:

- Python
- SQL
- SQLite
- Banco de dados relacionais
- Modelagem de dados
- CRUD
- Chaves primárias e estrangeiras
- Validação de dados
- Regras de negócio
- Lógica de programação

<<<<<<< HEAD
O projeto será desenvolvido de forma incremental, adicionando novas funcionalidades conforme o avanço do desenvolvimento.
=======
O projeto será desenvolvido de forma incremental, adicionando novas funcionalidades conforme o avanço do desenvolvimento.
>>>>>>> e1e953f (fazendo funcionalidades em cadastrar paciente)
