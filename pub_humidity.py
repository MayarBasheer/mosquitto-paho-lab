import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
TOPIC = "sensors/humidity"
STUDENT_ID = "12112956"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    hum = random.randint(40, 80)
    msg = f"Humidity: {hum}% | ID: {STUDENT_ID}"
    print("Published:", msg)
    client.publish(TOPIC, msg)
    time.sleep(2)
