import pika
import json

# Replace with your CloudAMQP connection string
amqp_url = "amqps://user:passowrd@shrimp.rmq.cloudamqp.com/ryyaytil"

params = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Declare queue
channel.queue_declare(queue="jobs")

# Callback function
def callback(ch, method, properties, body):
    input_data = json.loads(body.decode())
    print(f"Received job with input {input_data['number']}")

    # Acknowledge only if number == 7
    if int(input_data["number"]) == 7:
        ch.basic_ack(delivery_tag=method.delivery_tag)

# Consume messages
channel.basic_consume(queue="jobs", on_message_callback=callback)

print("Waiting for messages...")
channel.start_consuming()