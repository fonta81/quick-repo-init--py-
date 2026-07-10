import os
import subprocess


class BasemodClass:
    def __init__(self):
        self.path = ""  # Crea variable vacia

    def CrearCarpeta(self, NombreCc):
        try:
            os.makedirs(NombreCc, exist_ok=True)  # crea carpeta
            self.path = os.path.join("", NombreCc)  # asigna path -> variable
        except Exception as e:  # en caso de error:
            print(f"Error: {e}")

    def CrearArchivo(self, Nombre, Extencion):
        try:
            ExtencionArchivo = Nombre + Extencion  # agrega extencion (.py,ect)
            Crear = os.path.join(self.path, ExtencionArchivo)  # crea path del archivo
            with open(Crear, "w", encoding="utf=8"):  # crea archivo
                pass
        except Exception as e:  # en caso de error:
            print(f"Error: {e}")

    def CrearRead(self):
        try:
            ReadCrear = os.path.join(self.path, "Readme.md")  # crea path readme
            with open(ReadCrear, "w", encoding="utf-8"):  # crea el readme
                pass
        except Exception as e:  # en caso de error:
            print(f"Error: {e}")

    def CrearRepo(self):
        try:  # crea repo en carpeta creada:
            subprocess.run(["git", "-C", self.path, "init"], capture_output=True)
        except Exception as e:  # en caso de error:
            print(f"Error: {e}")

    def Usuario(self):
        print("\n")  # Se le pide nombre de carpeta:
        self.CrearCarpeta(input("Digite el nombre de la carpeta a crear: "))
        print("\n")
        self.CrearArchivo(  # se le pide el nombre del archivo y su extencion:
            input("Ecriba el nombre del archivo a crear: "),
            input("Escriba la extencion del archivo a crear .py/.sh/.js/.html/ect: "),
        )
        self.CrearRead()  # crea readme
        self.CrearRepo()  # crea repo
        print("\n")  # mensaje de exito:
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


if __name__ == "__main__":  # inicia el main
    main()
