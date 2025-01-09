### 1. Caminhões SA
**Descrição:**  
Projeto voltado para o monitoramento e controle em tempo real da temperatura de cargas de caminhões de uma empresa fictícia de transporte de alimentos congelados.

### Arquitetura

![Arquitetura](https://github.com/Adrianogvs/002_Engenharia_de_Dados_Azure/blob/main/Caminhoes_SA/picture/01.png)

Esta arquitetura é projetada para capturar, processar e analisar dados provenientes de sensores instalados em caminhões e em uma fábrica. Ela utiliza tecnologias da **Azure** para ingestão, processamento em tempo real e visualização dos dados.



**Detalhes dos Scripts:**
- [Envio de Eventos (Send)](https://github.com/Adrianogvs/002_Engenharia_de_Dados_Azure/blob/main/Caminhoes_SA/scripts/01-Send/README.md)  
- [Recebimento de Eventos (Receive)](https://github.com/Adrianogvs/002_Engenharia_de_Dados_Azure/blob/main/Caminhoes_SA/scripts/02-Receive/README.md)
- [Produção, Processamento e Consumo de Eventos (StreamAnalyzer)](https://github.com/Adrianogvs/002_Engenharia_de_Dados_Azure/blob/main/Caminhoes_SA/scripts/03-StreamAnalyzer/README.md)

**Tecnologias utilizadas:**  
- Python
- Event Hub  
- Synapse Analytics  
- Data lake
- Azure Stream Analytics
- Power BI Streaming

**Principais entregas:**  
- Monitoramento de temperatura em tempo real.  
- Criação de alertas para equipes de logística.  
- Geração de relatórios com variações de temperatura.  

**Benefícios**
- **Escalabilidade**: Capacidade de processar grandes volumes de dados de forma eficiente.
- **Análise em Tempo Real**: Detecção de problemas e geração de insights rapidamente.
- **Visualização Dinâmica**: Dashboards interativos que suportam a tomada de decisão.

Essa arquitetura é ideal para monitorar operações logísticas e industriais, garantindo maior eficiência e segurança operacional.
