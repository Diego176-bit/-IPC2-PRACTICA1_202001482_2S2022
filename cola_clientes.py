from orden import Orden
import os
class ColaClientes:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None
        
    
    def es_vacio(self):
        return self.primero == None
    
    def agregar(self, nombre, ingrediente,tiempo):
        orden = Orden(nombre, ingrediente, tiempo)
        orden.siguiente = None
        
        if self.es_vacio():
            self.primero = orden
            self.ultimo = orden
        else:
            self.ultimo.siguiente = orden
            self.ultimo = orden
        
    
    def buscar(self, nombre):
        aux = self.primero
        while aux != None:
            if aux.nombre == nombre:
                return aux
            aux = aux.siguiente
    
    def extraer(self):
        if self.es_vacio() == False:
            aux = self.primero.siguiente
            
            while aux != None:
                aux.tiempo_espera -= self.primero.tiempo_espera
                aux = aux.siguiente
 
            if self.primero == self.ultimo:
                self.primero = None
                self.ultimo = None
            else:
                self.primero = self.primero.siguiente
            #return (aux.nombre, aux.ingrediente, aux.tiempo)
    
    
    def recorrer(self):
        orden = self.primero
        contador_ordenes = 1
        while orden != None:
            print('********************************************')
            print(f'Orden # {contador_ordenes}')
            print(f'nombre: {orden.nombre}')
            print(f'Ingrediente: {orden.ingrediente}')   
            print(f'Tu tiempo de espera es: {orden.tiempo_espera}')
            print('***********************************************')
            print('')
            print('')
            contador_ordenes += 1
            orden = orden.siguiente
            
    def tiempo_en_cola(self):
        
        cola_ordenes = self.primero
        
        while cola_ordenes != self.ultimo:
            
            if self.primero == self.ultimo:
                
                return 0

            self.ultimo.tiempo_espera += cola_ordenes.tiempo
            cola_ordenes = cola_ordenes.siguiente
        return self.ultimo.tiempo_espera
    
    def graficar(self):
        aux = self.primero
        contador = 0
        archivo = open('grafica.dot', 'w')
        cadena = ''
        cadena = '''
            digraph G {
            rankdir="LR"
            subgraph cluster_0 {
            style=filled;
            fontsize=42;
            color= lightgray;
            node [style=filled,fontsize=32,color=skyblue, shape= box,width=2.5,height = 2.5];
            label = "cola";
            
        '''
        while aux != None:
            
            cadena = cadena + f' a{contador}[label = "{aux.nombre}  ingrediente: {aux.ingrediente}  tiempo de espera: {aux.tiempo_espera}", style=filled,fontsize=32,color=white, shape= box]\n'
            contador +=1
            aux = aux.siguiente
        
        
        while contador >= 0:
            cadena = cadena + f'a{contador} -> a{contador -1}->'
            contador -=2
            if contador <= 0:
                contador = 0
                cadena = cadena + f' a{contador}'
                break
        cadena = cadena + '\n } \n }'
        
        archivo.write(cadena)
        archivo.close()
        os.system('dot -Tpng grafica.dot -o grafica.png')
    
cola_clientes = ColaClientes()