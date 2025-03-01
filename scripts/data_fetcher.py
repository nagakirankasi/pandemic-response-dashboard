import boto3
import json
import time

kinesis_client = boto3.client('kinesis', region_name='us-east-1')
stream_name = 'pandemic-data-stream'

def get_public_health_data():
    # Simulate API call (replace with actual API fetching logic)
    return {"region": "NY", "cases": 100, "vaccinated": 50, "timestamp": time.time()}

while True:
    data = get_public_health_data()
    kinesis_client.put_record(
        StreamName=stream_name,
        Data=json.dumps(data),
        PartitionKey="region"
    )
    time.sleep(10)  # Send data every 10 seconds
