import requests
from google.transit import gtfs_realtime_pb2

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get('https://svc.metrotransit.org/mtgtfs/vehiclepositions.pb', timeout=10) # without a timeout, program could hang indefinitely
response.raise_for_status() # Checks the http request succeeded
feed.ParseFromString(response.content)
for entity in feed.entity[:5]:
    if not entity.HasField('vehicle'):
        continue
    print("Vehicle ID:", entity.vehicle.vehicle.id)
    print("Route ID:", entity.vehicle.trip.route_id)
    print("Trip ID:", entity.vehicle.trip.trip_id)
    print("Latitude:", entity.vehicle.position.latitude)
    print("Longitude:", entity.vehicle.position.longitude)
    print("Timestamp:", entity.vehicle.timestamp)
    print("#########################\n")