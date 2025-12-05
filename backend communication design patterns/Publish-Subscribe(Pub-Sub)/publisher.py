import pika
import sys
import json

# Replace with your CloudAMQP connection string
amqp_url = "amqps://user:passowrd@shrimp.rmq.cloudamqp.com/ryyaytil"

# Setup connection and channel
params = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Declare queue (idempotent)
channel.queue_declare(queue="jobs")

# Message payload
msg = {"number": sys.argv[1] if len(sys.argv) > 1 else "0"}

# Publish message
channel.basic_publish(
    exchange="",
    routing_key="jobs",
    body=json.dumps(msg)
)

print(f"Job sent successfully {msg['number']}")

connection.close()