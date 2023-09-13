import threading
import time
import random
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client['bancoiot']

temperaturas = db.sensores


def sensor1(nome, intervalo):
    res = 0
    while True:
        
        if (res >38):
            filter_query = {"nomeSensor" : 'TEMP1'}  
            temperaturas.update_one(filter_query, {"$set": {'sensorAlarmado': True}})
            print('TEMPERATURA MUITO ALTA! VERIFICAR SENSOR 1')
        else:
            res = random.uniform(0.3, 0.4)*100
            print(nome, res)
            filter_query = {"nomeSensor" : 'TEMP1'}  
            temperaturas.update_one(filter_query, {"$set": {'valorSensor': res}})
            time.sleep(intervalo)

def sensor2(nome, intervalo):
    res = 0
    while True:
        
        if (res >38):
            filter_query = {"nomeSensor" : 'TEMP2'}  
            temperaturas.update_one(filter_query, {"$set": {'sensorAlarmado': True}})
            print('TEMPERATURA MUITO ALTA! VERIFICAR SENSOR 2')
        else:
            res = random.uniform(0.3, 0.4)*100
            print(nome, res)
            filter_query = {"nomeSensor" : 'TEMP2'}  
            temperaturas.update_one(filter_query, {"$set": {'valorSensor': res}})
            time.sleep(intervalo)

def sensor3(nome, intervalo):
    res = 0
    while True:
        
        if (res >38):
            filter_query = {"nomeSensor" : 'TEMP3'}  
            temperaturas.update_one(filter_query, {"$set": {'sensorAlarmado': True}})
            print('TEMPERATURA MUITO ALTA! VERIFICAR SENSOR 3')
        else:
            res = random.uniform(0.3, 0.4)*100
            print(nome, res)
            filter_query = {"nomeSensor" : 'TEMP3'}  
            temperaturas.update_one(filter_query, {"$set": {'valorSensor': res}})
            time.sleep(intervalo)







x = threading.Thread(target=sensor1, args=('sensor1', 3))
x.start()

y = threading.Thread(target=sensor1, args=('sensor2', 3))
y.start()

z = threading.Thread(target=sensor1, args=('sensor3', 3))
z.start()





