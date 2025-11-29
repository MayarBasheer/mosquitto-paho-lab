# 🛰️ Mosquitto + Paho MQTT Lab  
This repository contains the implementation of the MQTT Lab using Mosquitto Broker and Paho MQTT (Python).

---

## 🚀 Technologies Used
- **Mosquitto MQTT Broker**
- **Python 3**
- **Paho MQTT Client Library**

---

## 📡 MQTT Topics Used
The system uses multiple MQTT topics:

- `sensors/temperature`
- `sensors/humidity`
- `sensors/people`

---

## 📝 Description
This project demonstrates:
- Multiple **Publishers** (Temperature, Humidity, People Counter)
- Multiple **Subscribers** (Each reads one topic)
- Each publisher sends randomly generated values simulating sensor data.
- Each message **includes the Student ID** as requested in the lab instructions.

---

## 🔥 Publishers Implemented
### 1️⃣ Temperature Publisher  
File: `pub_temp.py`  
Publishes random temperature values + Student ID to:  
`topic: sensors/temperature`

### 2️⃣ Humidity Publisher  
File: `pub_humidity.py`  
Publishes random humidity values + Student ID to:  
`topic: sensors/humidity`

### 3️⃣ People Counter Publisher  
File: `pub_people.py`  
Publishes random people-count values + Student ID to:  
`topic: sensors/people`

---

## 📥 Subscribers Implemented
### Temperature Subscriber  
File: `sub_temp.py`  
Receives messages from: `sensors/temperature`

### Humidity Subscriber  
File: `sub_humidity.py`  
Receives messages from: `sensors/humidity`

### People Subscriber  
File: `sub_people.py`  
Receives messages from: `sensors/people`

---

## 📂 Files Included
pub_temp.py
pub_humidity.py
pub_people.py
sub_temp.py
sub_humidity.py
sub_people.py


