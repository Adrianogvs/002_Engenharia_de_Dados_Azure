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
- [Envio de Eventos (Send)](https://github.com/Adrianogvs/002_Engenharia_de_Dados_Azure/blob/main/Caminhoes_SA/scripts/01-Send/README.md)  
- [Recebimento de Eventos (Receive)](https://github.com/Adrianogvs/002_Engenharia_de_Dados_Azure/blob/main/Caminhoes_SA/scripts/02-Receive/README.md)
- [Produção, Processamento e Consumo de Eventos (StreamAnalyzer)](https://github.com/Adrianogvs/002_Engenharia_de_Dados_Azure/blob/main/Caminhoes_SA/scripts/03-StreamAnalyzer/README.md)

**Tecnologias utilizadas:**  
- Event Hub  
- Synapse Analytics  
- Azure Stream Analytics
- Power BI Streaming

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
002_Engenharia_de_Dados_Azure/
├── .venv
├── Caminhoes_SA/
│   ├── dados/
│   ├── dashboards/
|   |   └── EventHubsProducer.pbix
│   ├── files/
|   |   └── CertificadoProjetoEventHubASA.pdf
│   ├── picture/
|   |   ├── Receive
|   |   ├── Send
|   |   └── StreamAnalyzer
│   ├── scripts/
│   │   ├── 01-Send/
│   │   │   ├── EventHubsSend.py
│   │   │   └── README.md
│   │   ├── 02-Receive/
│   │   │   ├── EventHubsReceive.py
│   │   │   └── README.md
│   │   ├── 03-StreamAnalyzer/
│   │   │   │── EventHubsProducer.py
│   │   │   └── README.md
│   └── README.md
├── Market_Star/
│   ├── dados/
│   ├── dashboards/
│   ├── picture/
│   ├── scripts/
│   └── README.md
├── NeoBank/
│   ├── dados/
│   ├── dashboards/
│   ├── picture/
│   ├── scripts/
│   └── README.md
├── .env
├── .gitignore
├── README.md 
└── requirements.txt
```

## Como Clonar o Repositório

Siga as etapas abaixo para clonar este repositório e explorá-lo localmente:

1. Certifique-se de ter o [Git](https://git-scm.com/) instalado.
2. Abra o terminal ou prompt de comando e execute o comando abaixo para clonar o repositório:

```bash
git clone https://github.com/Adrianogvs/002_Engenharia_de_Dados_Azure.git
```

3. Navegue até o diretório clonado:
```bash
cd 002_Engenharia_de_Dados_Azure
```

4. Abra os arquivos utilizando o editor de código de sua preferência, como o [VS Code](https://code.visualstudio.com/).

5. Configurar o Ambiente Virtual (Opcional, mas Recomendado)
Crie e ative um ambiente virtual para isolar as dependências do projeto:
* No Wondows
```bash
python -m venv venv
.\venv\Scripts\activate
```
* No Mac
```bash
python -m venv venv
source venv/bin/activate
```
<i><mark>Dica: Para desativar o ambiente virtual, use o comando deactivate.</mark></i>

<p></p>

6. Instalar as Dependências
Certifique-se de que todas as bibliotecas necessárias estão instaladas. Use o arquivo requirements.txt para instalar as dependências:
```bash
pip install -r requirements.txt
```

7. Configurar o Arquivo de Credenciais .env
Este projeto requer um arquivo .env para armazenar credenciais e variáveis sensíveis.

Crie um arquivo chamado .env na raiz do repositório.
Adicione as informações necessárias no formato abaixo:
```bash
API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
DATABASE_URL=your_database_url_here
```
<i><mark>Importante:</mark>

<b>Nunca compartilhe seu arquivo .env publicamente.
Adicione o arquivo .env ao .gitignore para evitar que ele seja incluído no controle de versão</b>.
</i>

8. Executar o Projeto
Após configurar o ambiente e instalar as dependências, você pode iniciar o projeto ou executar os scripts disponíveis conforme necessário.

9. Abrir o Projeto no Editor de Código
Abra o diretório do projeto no editor de código de sua preferência. Por exemplo, no VS Code, você pode usar o comando abaixo para abrir o projeto diretamente do terminal:
```bash
code .
```
Com esses passos concluídos, seu ambiente estará configurado e pronto para explorar e trabalhar no repositório.
```perl
Agora, você pode salvar este texto como um arquivo `.md`, como por exemplo `README.md`, sem precisar ajustar manualmente no VS Code. Basta copiar e colar! 😊
```
