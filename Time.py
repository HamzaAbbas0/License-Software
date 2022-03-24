from firebase import firebase
from firebase_admin import db
from getmac import get_mac_address as gma
import datetime

address = gma()
print('address', address)
'''while True:
    print('address', address)'''
current_time = datetime.datetime.now()
#current_time = datetime.datetime.now()
#current_time = current_time.strftime("%d-%m-%Y %H-%M-%S")
firebase = firebase.FirebaseApplication('https://macexpires-default-rtdb.firebaseio.com/', None)
firebase.put('data/',address,str(current_time))

while True:
    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%d-%m-%Y %H-%M-%S")
    firebase.put('data/','Current time',str(current_time))