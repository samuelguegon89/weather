#!/usr/bin/python
 # -*- coding: utf-8 -*-
 
import requests
import json


provincias = {"1":"Almeria","2":"Cadiz","3":"Cordoba","4":"Granada","5":"Huelva","6":"Jaen","7":"Malaga","8":"Sevilla"}
print "Lista de provincias""\n""----------------------""\n""1. Almería""\n""2. Cádiz""\n""3. Córdoba""\n""4. Granada""\n""5. Huelva""\n""6. Jaén""\n""7. Málaga""\n""8. Sevilla""\n""---------------"

cadena=raw_input('¿De que ciudad quieres saber la temperatura actual?: ')
respuesta=requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,Spain' % provincias[cadena]})
rest=provincias[cadena]
dicc=json.loads(respuesta.text)
temperatura=dicc["main"]["temp"]
	
print "La temperatura actual de",rest,"es",temperatura-273,"grados centígrados."
