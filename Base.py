# como ptas hago para crear algo dentro de otra mrd
import os


class BasemodClass:
    def __init__(self):
        self.path = ""

    def CrearCarpeta(self, NombreCc):
        try:
            os.makedirs(NombreCc, exist_ok=True)
            print("Creada correctamente")
            self.path = os.path.join("", NombreCc)
        except Exception as e:
            print(f"Error: {e}")

    def CrearPy(self, nombrepy):
        nombre = nombrepy + ".py"
        py = os.path.join(self.path, nombre)
        with open(py, "w", encoding="utf=8") as archivo:
            pass


# cc = BasemodClass()
# cc.CrearCarpeta("pepe")
# cc.CrearPy("albion")
