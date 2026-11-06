from confluent_kafka import Producer
import json

# Configure the Kafka producer with the bootstrap server address
producer = Producer({"bootstrap.servers": "localhost:9092"})

# Sample data to be sent to Kafka
vehicle_data_1 = {"vehicle_id": "1001", "route_id": "21", "latitude": 44.97, "longitude": -93.26}
vehicle_data_2 = {"vehicle_id": "1002", "route_id": "5", "latitude": 44.98, "longitude": -93.27}
vehicle_data_3 = {"vehicle_id": "1003", "route_id": "12", "latitude": 44.99, "longitude": -93.28}
vehicle_data_4 = {"vehicle_id": "1004", "route_id": "7", "latitude": 45.00, "longitude": -93.29}
vehicle_data_5 = {"vehicle_id": "1005", "route_id": "3", "latitude": 45.01, "longitude": -93.30}
vehicles = [vehicle_data_1, vehicle_data_2, vehicle_data_3, vehicle_data_4, vehicle_data_5]

topic_name = 'test-vehicles'

for vehicle in vehicles:
    # Produce each vehicle data to the Kafka topic
    producer.produce(topic_name, key=vehicle["vehicle_id"], value=json.dumps(vehicle))
producer.flush()  # Ensure all messages are sent before exiting