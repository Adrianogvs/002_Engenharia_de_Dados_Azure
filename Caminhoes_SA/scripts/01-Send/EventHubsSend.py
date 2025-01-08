from azure.eventhub import EventHubProducerClient, EventData
from dotenv import load_dotenv
import os

# Carregar as variáveis do arquivo .env
load_dotenv()

# Informações de conexão (obtidas do .env)
CONNECTION_STR = os.getenv('CONNECTION_STR')
EVENT_HUB_NAME = os.getenv('EVENT_HUB_NAME')

def send_event_to_event_hub():
    try:
        # Criar um cliente do Event Hub
        producer = EventHubProducerClient.from_connection_string(
            conn_str=CONNECTION_STR,
            eventhub_name=EVENT_HUB_NAME
        )

        # Criar um lote de eventos
        event_data_batch = producer.create_batch()

        # Adicionar eventos ao lote
        event_data_batch.add(EventData("Mensagem 1 para o Event Hub"))
        event_data_batch.add(EventData("Mensagem 2 para o Event Hub"))
        event_data_batch.add(EventData("Mensagem 3 para o Event Hub"))

        # Enviar o lote para o Event Hub
        producer.send_batch(event_data_batch)

        print("Eventos enviados com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar eventos: {e}")
    finally:
        # Fechar a conexão
        producer.close()

if __name__ == "__main__":
    send_event_to_event_hub()
