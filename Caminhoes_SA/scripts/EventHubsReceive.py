from azure.eventhub import EventHubConsumerClient
from azure.storage.blob import BlobCheckpointStore
from dotenv import load_dotenv
import os
import asyncio

# Carregar variáveis do .env
load_dotenv()

# Configurações de conexão
EVENT_HUB_CONNECTION_STRING = os.getenv("CONNECTION_STR")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")
STORAGE_CONNECTION_STRING = os.getenv("STORAGE_CONNECTION_STR")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")
CONSUMER_GROUP = "$Default"  # Nome padrão do grupo de consumidores

# Handler para processar eventos
async def process_event(event):
    print(f"Received event: {event.body_as_str()}")
    # Atualiza o checkpoint no blob storage
    await event.update_checkpoint()

# Handler para processar erros
def process_error(partition_context, error):
    print(f"Partition {partition_context.partition_id}: {error}")

# Função principal para consumir eventos
async def consume_events():
    checkpoint_store = BlobCheckpointStore.from_connection_string(
        STORAGE_CONNECTION_STRING, BLOB_CONTAINER_NAME
    )

    consumer_client = EventHubConsumerClient.from_connection_string(
        EVENT_HUB_CONNECTION_STRING,
        consumer_group=CONSUMER_GROUP,
        eventhub_name=EVENT_HUB_NAME,
        checkpoint_store=checkpoint_store,
    )

    async with consumer_client:
        print("Iniciando processamento de eventos...")
        await consumer_client.receive(
            on_event=process_event,
            on_error=process_error,
            starting_position="-1",  # Recebe desde o início
        )

if __name__ == "__main__":
    asyncio.run(consume_events())
