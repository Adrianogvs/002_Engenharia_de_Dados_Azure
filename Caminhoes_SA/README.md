# 1. Caminhões SA

### **Descrição**  
Projeto voltado para o monitoramento e controle em tempo real da temperatura de cargas de caminhões de uma empresa fictícia de transporte de alimentos congelados. A proposta é melhorar a eficiência e a segurança operacional por meio de tecnologias modernas de coleta e análise de dados.

---

### **Arquitetura do Sistema**  

![Arquitetura](https://github.com/Adrianogvs/002_Engenharia_de_Dados_Azure/blob/main/Caminhoes_SA/picture/01.png)

A arquitetura foi projetada para capturar, processar e analisar dados em tempo real provenientes de sensores instalados em caminhões e nas instalações da fábrica. Utiliza serviços da **Microsoft Azure** para gerenciar todas as etapas: desde a ingestão dos dados até a visualização por meio de dashboards interativos.  

#### Componentes Principais:  
1. **Sensores Físicos**  
   - Instalados nos caminhões para medir a temperatura das cargas.
   
2. **Event Producer**  
   - O componente que envia os dados capturados para o **Azure Event Hub**.

3. **Event Hub**  
   - Centraliza a ingestão dos dados dos sensores e os envia para processamento.

4. **Azure Stream Analytics**  
   - Processa os dados em tempo real e os encaminha para armazenamento e análise.

5. **Storage Account**  
   - Armazena os dados recebidos para análises históricas e relatórios.

6. **Power BI Streaming**  
   - Oferece dashboards em tempo real para visualização e monitoramento.

---

### **Detalhes dos Scripts**  
Cada componente possui scripts específicos para execução das funções.  
- [Envio de Eventos (Send)](https://github.com/Adrianogvs/002_Engenharia_de_Dados_Azure/blob/main/Caminhoes_SA/scripts/01-Send/README.md): Coleta os dados dos sensores e os envia para o Event Hub.  
- [Recebimento de Eventos (Receive)](https://github.com/Adrianogvs/002_Engenharia_de_Dados_Azure/blob/main/Caminhoes_SA/scripts/02-Receive/README.md): Recebe os dados no Event Hub e os prepara para processamento.  
- [Produção, Processamento e Consumo de Eventos (StreamAnalyzer)](https://github.com/Adrianogvs/002_Engenharia_de_Dados_Azure/blob/main/Caminhoes_SA/scripts/03-StreamAnalyzer/README.md): Processa os dados recebidos para identificar padrões e gerar insights.  

---

### **Tecnologias Utilizadas**  
- **Python**: Linguagem principal para desenvolvimento dos scripts.  
- **Event Hub**: Para ingestão e centralização dos eventos.  
- **Synapse Analytics**: Para análises avançadas e relatórios detalhados.  
- **Data Lake**: Armazena dados em larga escala.  
- **Azure Stream Analytics**: Processamento em tempo real.  
- **Power BI Streaming**: Visualização de dados em tempo real.  

---

### **Principais Entregas do Projeto**  
1. **Monitoramento de Temperatura em Tempo Real**  
   - Permite que equipes de logística tomem decisões rápidas com base nos dados.  
   
2. **Alertas em Caso de Variação de Temperatura**  
   - Notifica automaticamente as equipes de manutenção e operações.  

3. **Relatórios Detalhados**  
   - Geração de relatórios sobre variações de temperatura ao longo das rotas e nas instalações da fábrica.  

---

### **Benefícios do Projeto**  
- **Escalabilidade**:  
  - Suporte para grandes volumes de dados com a possibilidade de expansão conforme o crescimento da empresa.  
- **Análise em Tempo Real**:  
  - Identificação rápida de problemas, minimizando riscos e perdas.  
- **Visualização Dinâmica**:  
  - Dashboards interativos para facilitar a tomada de decisões estratégicas.  

---

### **Conclusão**  
Este projeto é essencial para empresas do setor logístico que lidam com transporte de produtos sensíveis à temperatura, como alimentos congelados. Ele garante maior controle, eficiência operacional e segurança, além de reduzir custos com perdas de mercadorias devido a falhas no monitoramento.

