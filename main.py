from cola_clientes import cola_clientes


def nueva_orden():
    print('Realiza una orden')
    nombre_cliente = input('¿Cuál es tu nombre para la orden?: ')
    print('¿De que ingrediente será tu Shuco?')
    print('1.Salchicha')
    print('2.Chorizo')
    print('3.Salami')
    print('4.Longaniza')
    print('5.Costilla')
    ingrediente_shuco = input('Escoge una opción: ')
    if ingrediente_shuco == '1':
       ingrediente_shuco == 'Salchicha'
       tiempo_preparacion = 2
    if ingrediente_shuco == '2':
       ingrediente_shuco == 'Chorizo'
       tiempo_preparacion = 3
    if ingrediente_shuco == '3':
       ingrediente_shuco == 'Salami'
       tiempo_preparacion = 1.5
    if ingrediente_shuco == '4':
       ingrediente_shuco == 'Longaniza'
       tiempo_preparacion = 4
    if ingrediente_shuco == '5':
       ingrediente_shuco == 'Costilla'
       tiempo_preparacion = 6
    
    
    cola_clientes.agregar(nombre_cliente, ingrediente_shuco,tiempo_preparacion)
    cola_clientes.buscar(nombre_cliente).tiempo_espera = cola_clientes.tiempo_en_cola()+tiempo_preparacion
    cola_clientes.graficar()
    print(f'Tu tiempo de espera en cola será de: {cola_clientes.buscar(nombre_cliente).tiempo_espera}')
    
    
    print('---------------------------------------------------------------------')
    
    
def menu_principal():
   opcion = 0
   while opcion != 4:
      print('¡Bienvenido a la venta de Shucos!')
      print('')
      print('Escoge una opción')
      print('')
      print('1. Nueva Orden')
      print('2. Enlistar ordenes')
      print('3. Quitar orden')
      print('4. Salir')
      opcion = int(input('Escoge una opción: '))
        
      if opcion == 1:
         nueva_orden()
      if opcion == 2:
         cola_clientes.recorrer()
      if opcion == 3:
         cola_clientes.extraer()
            
if __name__ == '__main__':
    menu_principal()