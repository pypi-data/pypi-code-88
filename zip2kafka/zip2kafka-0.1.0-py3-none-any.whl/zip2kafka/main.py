import typer
import json
import socket

from confluent_kafka import Producer, Consumer
from loguru import logger
from pathlib import Path

app = typer.Typer()

@app.command()
def produce(
    server: str = typer.Argument(..., help="Server IP + Port, in the format <IP>:<PORT>; 1.23.456.789:9092"), 
    client_id: str = typer.Argument(..., help="ID Kafka Identifies you as; zip2kafka.producer"), 
    topic: str = typer.Argument(..., help="Kafka Topic; zipfiles"), 
    filename: str = typer.Argument(..., help="File to upload, also will act as your default 'key' in Kafka; ~/test.zip")
):
    kafka_conf = {
            'bootstrap.servers': server,
            'client.id': client_id,
            "message.max.bytes": 1000000000,
        }
    producer = Producer(kafka_conf)

    try:
        with open(filename, 'rb') as file_data:
            bytes_content = file_data.read()
            producer.produce(topic, key=filename, value=bytes_content)
            typer.echo(f"{filename} has been sent to {server} using ID {client_id}")

    except Exception as e:
        logger.error(e)
        logger.error("Failed to produce a message to server {} on topic {} with filename: {}", server, topic, filename)
        
    finally:
        producer.flush()    

@app.command()
def consume(
        server: str = typer.Argument(..., help="Server IP + Port, in the format <IP>:<PORT>; 1.23.456.789:9092"), 
        group_id: str = typer.Argument(..., help="ID Kafka Identifies you as; zip2kafka.consumer"), 
        topic: str = typer.Argument(..., help="Kafka Topic; zipfiles"), 
        foldername: str = typer.Argument(..., help="Folder to save to"),
        auto_offset_reset: str = typer.Argument('smallest', help=""),
        force: str = typer.Option(False, help="Force creation of output directory and file (overwrites!)")
    ):
    FOLDER_NAME = Path(foldername)

    if not force:
        assert FOLDER_NAME.is_dir()
    else:
        FOLDER_NAME.mkdir(parents=True, exist_ok=True)


    kafka_conf = {'bootstrap.servers': server,
            'group.id': group_id,
            'auto.offset.reset': auto_offset_reset}

    consumer = Consumer(kafka_conf)
    try:
        consumer.subscribe([topic])

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                logger.error(msg.error())
            else:
                typer.echo(f"Recieved Message with key: {msg.key()} in topic {msg.topic()}")
                with open(FOLDER_NAME / msg.key().decode(), 'wb') as file:
                    if not force:
                        assert (FOLDER_NAME / msg.key()).is_file() != True

                    file.write(msg.value())

    except Exception as e:
        logger.error(e)

    finally:
        # Close down consumer to commit final offsets.
        consumer.close()



if __name__ == "__main__":
    app()