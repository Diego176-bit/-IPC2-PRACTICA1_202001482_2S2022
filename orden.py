class Orden:
    def __init__(self, nombre, ingrediente, tiempo) -> None:
        self.nombre = nombre
        self.ingrediente = ingrediente
        self.tiempo = tiempo
        self.tiempo_espera = 0
        self.siguiente= None