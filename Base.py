# se nesecita el nombre de la carpeta, el nombre del py
# se crea el path con los datos pedidos anteriormente
# se crean los archivos
# se muesta mensaje de que salio correctamente
import os


class BasemodClass:
    def __init__(self):
        self.path = ""
        self.NombrePy = ""
        self.NombreDeCarpeta = ""

    def CrearCarpeta(self, NombreCc):
        try:
            os.makedirs(NombreCc, exist_ok=True)
            print("Creada correctamente")
        except Exception as e:
            print(f"Error: {e}")


cc = BasemodClass()

cc.CrearCarpeta("pepe")
