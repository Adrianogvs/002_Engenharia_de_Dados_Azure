from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore
from azure.storage.blob.aio import ContainerClient
from dotenv import load_dotenv
import os
import asyncio
from datetime import datetime

# Carregar variáveis do .env
load_dotenv()

# Configurações de conexão
EVENT_HUB_CONNECTION_STRING = os.getenv("CONNECTION_STR")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")
STORAGE_CONNECTION_STRING = os.getenv("STORAGE_CONNECTION_STR")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")
CONSUMER_GROUP = "$Default"

# Função para salvar eventos no Data Lake Bronze
async def save_to_datalake(event_data, partition_id):
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
    file_name = f"bronze/partition_{partition_id}/{timestamp}.json"
    container_client = ContainerClient.from_connection_string(STORAGE_CONNECTION_STRING, BLOB_CONTAINER_NAME)
    async with container_client:
        blob_client = container_client.get_blob_client(file_name)
        await blob_client.upload_blob(event_data, overwrite=True)
    print(f"Evento salvo no Data Lake: {file_name}")

# Handler para processar eventos
async def process_event(partition_context, event):
    print(f"Received event: {event.body_as_str()} from partition {partition_context.partition_id}")
    await save_to_datalake(event.body_as_str(), partition_context.partition_id)
    await partition_context.update_checkpoint(event)

# Handler para processar erros
def process_error(partition_context, error):
    if partition_context:
        print(f"Error in partition {partition_context.partition_id}: {error}")
    else:
        print(f"General error: {error}")

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

    try:
        print("Iniciando processamento de eventos...")
        await consumer_client.receive(
            on_event=process_event,
            on_error=process_error,
            starting_position="-1",  # Consome desde o início do Event Hub
        )
    except KeyboardInterrupt:
        print("\nInterrupção detectada. Encerrando...")
    finally:
        await consumer_client.close()

# Execução do script
if __name__ == "__main__":
    asyncio.run(consume_events())
