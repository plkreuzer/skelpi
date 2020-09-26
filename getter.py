import paho.mqtt.client as mqtt # Import the MQTT library

import time # The time library is useful for delays

def onMsgFunc(client, userdata, message):
    topic = str(message.topic)
    data = str(message.payload.decode("utf-8"))
    print ("Topic {0}, data {1}".format(topic, data))

mqttClient = mqtt.Client("seklpi")
mqttClient.connect("10.0.0.100", 1883)
mqttClient.subscribe("skeleton")
mqttClient.on_message = onMsgFunc
mqttClient.loop_start()

