#salam ostad man task 1 va 2 ro kamel anjam dadam
#ye ghesmatayi az task3 k3 baraye status gereftam bod motovaje nashodam chejoriye
#lotffan rahnamayi mikonid?
#_____TASK1_______
#*******************************************
#*************REAL WORLD********************

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO 

class device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):
        
        self.topic=topic
        
        self.topic_list=self.topic.split('/')
        
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        
        self.mqtt_broker=mqtt_broker
        self.port=port
        
        #self.connect_mqtt()
        #self.setup_gpio()
        
        
    def connect_mqtt(self):
        self.mqtt_client=mqtt.client()
        
        self.mqtt_client.connect(self.mqtt_broker,self.port)
        
    
    def setup_gpio(self):
        
        #GPIO.setup(adad,GPIO.OUT)
        #age lamp --> 17
        #ag dar --> 27
        #ag fan --> 22
        
        #---->
        if self.device_type=='lamps':
            GPIO.setup(17,GPIO.OUT)
        
        elif self.device_type=='doors':
            GPIO.setup(27,GPIO.OUT)
            
        elif self.device_type=='fans':
            GPIO.setup(22,GPIO.OUT)
        
        elif self.device_type=='camera':
            GPIO.setup(100,GPIO.OUT)
            
        #elif self.device_type..
            
        
    def turn_on(self):
        
        #niaz daram b yek code inja k vasl she va
        #b device aslie man bege agha kahmois sho lotfan
        self.mqtt_client.publish(self.topic,'TURN_ON')
        #AGHA INJA BAYADF YEK ALGORITHEM BASZHE VASL SHE
        
        print('turn on successfully')
        
        
        
    def turn_off(self):
        
        self.mqtt_client.publish(self.topic,'TURN_OFF')


        print('turn off successfully')
    
    
    
    
a1=device(topic='home/parking/lamps/lamps100',mqtt_broker='189.11.39.114',port=1883)


a1.location #home
a1.group #parking
a1.device_type #lamps
a1.name #lamps1000


a1.turn_on() #turn on successfully


#topic= home/parking/thermosets/thermo100 , pin=2398373987198739173217


import Adafruiy_DHT

class Sensor:
    
    def __init__(self,topic,pin=100):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.sensor_type=self.topic_list[2]
        self.name=self.topic_list[3]
        
    #def tunr_on
    def read_sensor(self):
        
        humidity, temperature=Adafruiy_DHT.read_retry(Adafruiy_DHT.DHT22,self.pin)
        
        if self.sensor_type=='thermosets':
            return temperature
        else:
            return humidity



a1=Sensor('home/paking/thermosets/thermo100',pin=431723689473674626392267349727)







#___TASK2 & TASK3
#*******************************************
#**********FINAL STRUCTURE***************** 
class Device:
    def __init__(self,topic):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        
        self.status='off'
        
 
    def turn_on(self):
        self.status='on'
        print('turn on successfully')
        

    def turn_off(self):
        self.status='off'
        print('turn off successfully')


class Sensor:
    def __init__(self,topic,pin=100):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.sensor_type=self.topic_list[2]
        self.name=self.topic_list[3]
    def read_sensor(self):
        return 25



class admin_panel:
    
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        
        if group_name not in self.groups:

            self.groups[group_name]=[]
            
            print(f'group {group_name} is created')
        
        else:
            
            print('your group name is existed already')
        
        
    def add_device_to_group(self,group_name,new_device):
        
        if group_name in self.groups:
            
            self.groups[group_name].append(new_device)
            
            #print(f'{device.name} is added to {group_name})
            
        else:
            
            print(f'group {group_name} is not exist')
        
        
        
    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            
            self.add_device_to_group(group_name,new_device)
            print(f'device{new_device}is added to group{group_name}')
            
        else:
            
            print(f'group {group_name} is not exist')
            
            
            
            
            
    def create_multiple_devices(self,group_name,device_type,number_of_devices):
        
        if group_name in self.groups:
            for i in range(1,number_of_devices+1):
                topic=f'home/{group_name}/{device_type}/{device_type}{i}'
                new_device=Device(topic)
                
                self.add_device_to_group(group_name, new_device)
                
            print(f'{number_of_devices}number of {device_type}is added to {group_name}')
                    

        else:
            print(f'group {group_name} is not exist')
           
        
        
    def turn_on_devices_in_group(self,group_name):
        
        if group_name in self.groups:
            
            devices_list=self.groups[group_name]
            
            for device in devices_list:   
                device.turn_on()
            
            print(f'devices in group {group_name} are on') 
            
        else:
            print(f'group {group_name} is not exist')
    
    
    def turn_off_devices_in_group(self,group_name):
        '''
        khamoosh kone
        '''
        if group_name in self.groups:
            
            devices_list=self.groups[group_name]
            
            for device in devices_list:   
                device.turn_off()
            print(f'devices in group {group_name} are off') 
        else:
            print(f'group {group_name} is not exist')
        
        
        
    def trun_on_all(self):
        '''hameye device haro roshan kone
        tooo hame group ha 
        '''
        for i in self.groups:
            
            devices_list=self.groups[i]
         
            for device in devices_list:   
                device.turn_on()
        print('all devices  are on')    
        
        
    def turn_off_all(self):
        '''hameye devcie haro khamosh kone'''
        for i in self.groups:
            
            devices_list=self.groups[i]
         
            for device in devices_list:   
                device.turn_off()
        print('all devices  are off')    
        
    
        

    def get_status_in_group(self,group_name):
        
        '''living_room y matn print mikone mige lamp1 on , klamp2 off , lamp3 ,..'''
        pass
    
    
    
    
    def get_status_in_device_type(self,device_type):
        
        ''' device=lamps --> tamame lamp haro status mohem nabashe tooye living rome kojas'''
        pass
    
    
    #create_device
    
    #create_sensor.......................
    
    #inja add semsor ham ezafe kardam mesle le betonim mesle device creat ham bokonim 
    def add_sensor_to_group(self,group_name,new_sensor):
        
        if group_name in self.groups:
            
            self.groups[group_name].append(new_sensor)
            
        else:
            
            print(f'group {group_name} is not exist')

                
    def create_sensor(self,group_name,sensor_type,name) :
            if group_name in self.groups:
                
                topic=f'home/{group_name}/{sensor_type}/{name}'
                new_sensor=Sensor(topic)
                
                self.add_sensor_to_group(group_name,new_sensor)
                print(f'device{new_sensor}is added to group{group_name}')
                
            else:
                
                print(f'group {group_name} is not exist')
    #bar asase clASS SENSOR argument bzarid
        

    
    
    #read_sensor()
    def get_status_sensor_in_group(self,group_name):
        
        
        '''
        
        sensor haye yek goroh ro biad doone dooen status ro pas bde
        
        '''
        pass
