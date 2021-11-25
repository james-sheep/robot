import time
from robot import *
import bluetooth
import board
import adafruit_hcsr04
from adafruit_servokit import ServoKit

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D11, echo_pin=board.D12)
kit = ServoKit(channels=16)
kit.servo[5].actuation_range = 160
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)
 
port = server_sock.getsockname()[1]
 
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
 
bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid,
service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
profiles=[bluetooth.SERIAL_PORT_PROFILE])

print("iniciando")
print("Waiting for connection on RFCOMM channel", port)
 
client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)
 
try:
 while True:
     data = client_sock.recv(1024)
     if str(data) == "b'N0#'":
         print("frente")
         kit.continuous_servo[3].throttle = -0.5
         kit.continuous_servo[1].throttle = 0.5
         sleep(0.3)
         kit.continuous_servo [3] .throttle = 0
         kit.continuous_servo[1].throttle = 0
         
     if str(data) == "b'S0#'":
         print("ré")
         kit.continuous_servo[3].throttle = 0.5
         kit.continuous_servo[1].throttle = -0.5
         sleep(0.3)
         kit.continuous_servo [3] .throttle = 0
         kit.continuous_servo[1].throttle = 0
     
     if str(data) == "b'W0#'":
         print("esquerda")
         kit.continuous_servo[3].throttle = -0.5
         sleep(0.3)
         kit.continuous_servo [3] .throttle = 0
        
     if str(data) == "b'E0#'":
         print("direita")
         kit.continuous_servo[1].throttle = 0.5
         sleep(0.3)
         kit.continuous_servo [1] .throttle = 0   
     
     if str(data) == "b'04#'":
         print("bibibibibiiiiii")     
     if str(data) == "b'01#'":
         print("nao,nao,nao")
         kit.servo[5].angle = 0
         sleep(0.1)
         kit.servo[5].angle = 160
         sleep(0.1)
         kit.servo[0].angle = 0
         sleep(0.1)
         kit.servo[5].angle = 160
         sleep(0.1)
         kit.servo[5].angle = 0
         sleep(0.1)
         kit.servo[5].angle = 160
         sleep(0.1)
         kit.servo[5].angle = 0
         sleep(0.1)
         kit.servo[5].angle = 60
     
     if str(data) == "b'03#'":
        try:
            print(sonar.distance)
        except:
            print("não foi possível obter a distância")
     
     if not data:
         break
     print(str(data))
except OSError:
 pass
 
print("Disconnected.")
 
client_sock.close()
server_sock.close()
print("All done.")

 




    

