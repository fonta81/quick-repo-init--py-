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

    def CrearPy(self, NombrePy):
        ExtencionArchivoPy = NombrePy + ".py"
        PyCrear = os.path.join(self.path, ExtencionArchivoPy)
        with open(PyCrear, "w", encoding="utf=8"):
            pass

    def CrearRead(self):
        ReadCrear = os.path.join(self.path, "Readme.md")
        with open(ReadCrear, "w", encoding="utf-8"):
            pass


# cc = BasemodClass()
# cc.CrearCarpeta("pepe")
# cc.CrearPy("albion")
# cc.CrearRead()
