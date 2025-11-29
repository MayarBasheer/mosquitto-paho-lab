import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
TOPIC = "sensors/temperature"
STUDENT_ID = "12112956"   

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    temp = random.randint(20, 35)
    msg = f"Temp: {temp} C | ID: {STUDENT_ID}"
    result = client.publish(TOPIC, msg)
    print("Published:", msg)
    time.sleep(2)
