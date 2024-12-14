# Portfólio - Engenharia de Dados Azure

Este repositório reúne os projetos desenvolvidos durante a minha formação em Engenharia de Dados Azure. Cada projeto aborda um caso prático que simula cenários do mundo real, utilizando ferramentas e serviços da plataforma Azure.

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/) (se necessário para os scripts)
- Conta no [Microsoft Azure](https://azure.microsoft.com/) (para replicar os projetos)
- Editor de código, como o [VS Code](https://code.visualstudio.com/)

## Projetos

### 1. Caminhões SA
**Descrição:**  
Projeto voltado para o monitoramento e controle em tempo real da temperatura de cargas de caminhões de uma empresa fictícia de transporte de alimentos congelados.

**Detalhes dos Scripts:**
- [Envio de Eventos (Send)](Caminhoes_SA/scripts/Send/README.md)  
- [Recebimento de Eventos (Receive)](Caminhoes_SA/scripts/Receive/README.md)

**Tecnologias utilizadas:**  
- Event Hub  
- Synapse Analytics  

**Principais entregas:**  
- Monitoramento de temperatura em tempo real.  
- Criação de alertas para equipes de logística.  
- Geração de relatórios com variações de temperatura.  

---

### 2. Market Star
**Descrição:**  
Desenvolvimento de uma infraestrutura centralizada na nuvem para controle de receitas e despesas de uma empresa fictícia que vende cursos online. O objetivo foi integrar dados de diferentes fontes, como internet, arquivos CSV e Excel.

**Tecnologias utilizadas:**  
- Data Factory  
- Data Lake  

**Principais entregas:**  
- Infraestrutura de dados centralizada.  
- Relatório visual estilo OnePage.  
- Integração de diferentes fontes de dados.  

[Confira mais detalhes](Market_Star/README.md)

---

### 3. NeoBank
**Descrição:**  
Estruturação de suporte para dados massivos e implementação de inteligência artificial em um banco digital fictício. O projeto abordou a criação de uma infraestrutura para analisar e escalar o volume de dados gerado pelo banco.

**Tecnologias utilizadas:**  
- Synapse Analytics  
- DataBricks  
- Python  

**Principais entregas:**  
- Estruturação de dados utilizando Synapse e DataBricks.  
- Criação de notebooks para análise e transformação de dados.  
- Modelagem de dados para inteligência artificial.  

[Confira mais detalhes](NeoBank/README.md)

---

## Estrutura do Repositório

```plaintext
002-AZURE/
├── Caminhoes_SA/
│   ├── dados/
│   ├── dashboards/
│   ├── documentos/
│   ├── picture/
│   ├── scripts/
│   │   ├── Send/
│   │   │   ├── EventHubsSend.py
│   │   │   └── README.md
│   │   ├── Receive/
│   │       ├── EventHubsReceive.py
│   │       └── README.md
│   └── README.md
├── Market_Star/
│   ├── dados/
│   ├── dashboards/
│   ├── documentos/
│   ├── picture/
│   ├── scripts/
│   └── README.md
├── NeoBank/
│   ├── dados/
│   ├── dashboards/
│   ├── documentos/
│   ├── picture/
│   ├── scripts/
│   └── README.md
└── README.md
```

## Como Clonar o Repositório

Siga as etapas abaixo para clonar este repositório e explorá-lo localmente:

1. Certifique-se de ter o [Git](https://git-scm.com/) instalado.
2. Abra o terminal ou prompt de comando e execute o comando abaixo para clonar o repositório:

```bash
git clone https://github.com/Adrianogvs/002-AZURE.git
```

3. Navegue até o diretório clonado:
```bash
cd 002_AZURE
```

4. Abra os arquivos utilizando o editor de código de sua preferência, como o [VS Code](https://code.visualstudio.com/).
