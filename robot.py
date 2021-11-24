
from time import sleep
import  RPi.GPIO  as  GPIO 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#Ajuste estes valores para obter o intervalo completo do movimento do servo
deg_0_pulse   = 0.5 
deg_180_pulse = 2.5
f = 50.0

# Faca alguns calculos dos parametros da largura do pulso
period = 1000/f
k      = 100/period
deg_0_duty = deg_0_pulse*k
pulse_range = deg_180_pulse - deg_0_pulse
duty_range = pulse_range * k




class Robot:
    
    
    def __init__(self, gpio_esteira1):

     
        self.gpio_esteira1 = gpio_esteira1
        GPIO.setup(gpio_esteira1, GPIO.OUT)
        self.pwm_e1 = GPIO.PWM(self.gpio_esteira1,f)
        
        
       

    def movimenta_frente(self):
        self.pwm_e1.start(0)
        angle=0
        duty = deg_0_duty + (angle/180.0)* duty_range
        self.pwm_e1.ChangeDutyCycle(duty)
        sleep(2)
        
        

    def movimenta_tras(self):
        self.pwm_e1.start(0)
        angle=180
        duty = deg_0_duty + (angle/180.0)* duty_range
        self.pwm_e1.ChangeDutyCycle(duty)
        sleep(2)
       

    def movimenta_esquerda(self):

        pass


    def movimenta_direita(self):
       
        pass


    def garra_abre(self):

        pass


    def garra_fecha(self):
        
       pass


