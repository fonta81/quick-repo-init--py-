import os
import subprocess


class BasemodClass:
    def __init__(self):
        self.path = ""

    def CrearCarpeta(self, NombreCc):
        try:
            os.makedirs(NombreCc, exist_ok=True)
            self.path = os.path.join("", NombreCc)
        except Exception as e:
            print(f"Error: {e}")

    def CrearPy(self, NombrePy):
        try:
            ExtencionArchivoPy = NombrePy + ".py"
            PyCrear = os.path.join(self.path, ExtencionArchivoPy)
            with open(PyCrear, "w", encoding="utf=8"):
                pass
        except Exception as e:
            print(f"Error: {e}")

    def CrearRead(self):
        try:
            ReadCrear = os.path.join(self.path, "Readme.md")
            with open(ReadCrear, "w", encoding="utf-8"):
                pass
        except Exception as e:
            print(f"Error: {e}")

    def CrearRepo(self):
        try:
            subprocess.run(["git", "-C", self.path, "init"], capture_output=True)
        except Exception as e:
            print(f"Error: {e}")

    def Usuario(self):
        print("\n")
        self.CrearCarpeta(input("Digite el nombre de la carpeta a crear: "))
        print("\n")
        self.CrearPy(input("Digite el nombre del archivo python a crear: "))
        self.CrearRead()
        self.CrearRepo()
        print("\n")
        print("El Proceso se ejecuto correctamente")
        return


def main():  # El menu principal
    Base = BasemodClass()

    while True:
        print("\n" + "=" * 60)
        print("1. Iniciar")
        print("2. Salir")
        elige = input("Elige: ")

        if elige == "2":
            print("Saliendo...")
            break
        elif elige == "1":
            Base.Usuario()
        else:
            print("Ingrese un valor válido")


if __name__ == "__main__":
    main()
