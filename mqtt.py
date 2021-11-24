import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):

    
    client.subscribe("robot_garraH")
    client.subscribe("robot_seguir")
    client.subscribe("robot_re")
    client.subscribe("robot_L")
    client.subscribe("robot_R")
    

def on_message(client, userdata, msg):
    
    texto1 = str(msg.payload)
    texto_tratado = texto1.strip("b")
    return texto_tratado
       
    
client = mqtt.Client()
client.connect("192.168.0.42", 1883)
client.on_connect = on_connect
client.on_message = on_message

