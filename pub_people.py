import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
TOPIC = "sensors/people"
STUDENT_ID = "12112956"  

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    ppl = random.randint(0, 20)
    msg = f"People Count: {ppl} | ID: {STUDENT_ID}"
    result = client.publish(TOPIC, msg)
    print("Published:", msg)
    time.sleep(2)
