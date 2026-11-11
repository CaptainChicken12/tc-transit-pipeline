from confluent_kafka import Consumer
import json
import sys

group_id = sys.argv[1] if len(sys.argv) > 1 else "vehicle-consumer-group"

conf = {
    "bootstrap.servers": "localhost:9092",
    "group.id": group_id,
    "auto.offset.reset": "earliest"
}

consumer = Consumer(conf)

consumer.subscribe(['test-vehicles'])

try:
    while True:
        message = consumer.poll(1.0)
        if message is None:
            continue
        if message.error():
            print(f"Error: {message.error()}")
            continue
        vehicle = json.loads(message.value().decode('utf-8'))
        print(f"Received vehicle {vehicle["vehicle_id"]} on route {vehicle["route_id"]}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()