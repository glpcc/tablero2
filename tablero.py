import time
import keyboard
def crear_tablero():
	for i in range(lado**2):
		if i == 0:
			tablero.append(1)
		else:
			tablero.append(0)

def crear_bloqueo():
	global posicion_x
	global posicion_y
	posicion = posicion_x + (posicion_y * lado)
	tablero[posicion] = "$"

def mover_derecha():
	global posicion_x
	global posicion_y
	posicion = posicion_x + (posicion_y * lado)
	if tablero[posicion] != "$":
		tablero[posicion] = 0
	posicion_x += 1
	posicion = posicion_x + (posicion_y * lado)
	if tablero[posicion] != "$":
		tablero[posicion] = 1
		dibujar_tablero()
	else:
		posicion_x -= 1


def mover_izquierda():
	global posicion_x
	global posicion_y
	posicion = posicion_x + (posicion_y * lado)
	if tablero[posicion] != "$":
		tablero[posicion] = 0
	posicion_x -= 1
	posicion = posicion_x + (posicion_y * lado)
	if tablero[posicion] != "$":
		tablero[posicion] = 1
		dibujar_tablero()
	else:
		posicion_x += 1

def mover_abajo():
	global posicion_x
	global posicion_y
	posicion = posicion_x + (posicion_y * lado)
	if tablero[posicion] != "$":
		tablero[posicion] = 0
	posicion_y += 1
	posicion = posicion_x + (posicion_y * lado)
	if tablero[posicion] != "$":
		tablero[posicion] = 1
		dibujar_tablero()
	else:
		posicion_y -= 1

def mover_arriba():
	global posicion_x
	global posicion_y
	posicion = posicion_x + (posicion_y * lado)
	if tablero[posicion] != "$":
		tablero[posicion] = 0
	posicion_y -= 1
	posicion = posicion_x + (posicion_y * lado)
	if tablero[posicion] != "$":
		tablero[posicion] = 1
		dibujar_tablero()
	else:
		posicion_y += 1

def dibujar_tablero():
	for i in range(len(tablero)):
		if (i +1)% lado != 0:
			print (tablero[i],end=" ")
		elif (i+1) == 0:
			print (tablero[i],end=" ")
		else:
			print(tablero[i])
	for i in range(5):
		print()



tablero  = []
lado = 10
posicion_x = 0

posicion_y= 0


crear_tablero()
dibujar_tablero()

while True:
	if keyboard.is_pressed('w'):
		mover_arriba()
		time.sleep(0.5)
	elif keyboard.is_pressed('s'):
		mover_abajo()
		time.sleep(0.5)
	elif keyboard.is_pressed('a'):
		mover_izquierda()
		time.sleep(0.5)
	elif keyboard.is_pressed('d'):
		mover_derecha()
		time.sleep(0.5)
	elif keyboard.is_pressed('b'):
		crear_bloqueo()