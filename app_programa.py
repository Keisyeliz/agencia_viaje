list_viajeros = []
import os 

def fnt_limpiar():
    os.system('cls')
    print('Autor: Keisy Murillo')

def fnt_agente(op):
    fnt_limpiar()
    if op == '1':
        print('---Agregar viajero---\n')
        viajero = ''
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        edad = input('Edad: ')
        if (int(edad) > 0 and int(edad) <= 25):
            viajero = nombre+ '  '+ apellido+ '  ' + edad
            list_viajeros.append(viajero)
            print('Viajero agregado con exito\n')
            enter = input('Presione <Enter> para continuar...')
        else:
            print('No cuentas con la edad necesaria\n')
            enter = input('Presione <Enter> para continuar...')
    elif op == '2':
        print('---Mostrar lista de viajeros---\n')
        if len(list_viajeros) == 0:
            print('No hay viajeros registrados\n')
            enter = input('Presione <Enter> para continuar...')
        else:
            for viajero in list_viajeros:
                print(viajero)
            enter = input('Presione <Enter> para continuar...')
    elif op == '3':
        print('---Salir---\n')
        
sw = True
while sw == True:
    fnt_limpiar()
    opcion = input('---MENÚ---\n1. Agregar\n2. Mostrar\n3. Salir\n->')
    fnt_agente(opcion)