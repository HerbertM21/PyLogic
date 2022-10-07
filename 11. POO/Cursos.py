class MiEstudiante:
    def __init__(self, nombre, edad, registro_cursos):
        self.nombre = nombre
        self.edad = edad
        self.registro_cursos = registro_cursos
        self.cursos = [registro_cursos]

    def Agregar_curso(self):
        print("Agrega el curso: ")
        curso = input(">>> ")
        self.cursos.append(curso)

    def Quitar_curso(self):
        try:
            print("¿Deseas eliminar un curso?")
            print(self.cursos)
            print("¿Cual curso deseas eliminar?")
            CursoRemove = input(">>> ")
            print("¿Realmente deseas eliminar el curso?")
            OpcionRemove = int(input("1.- SI  2.- NO >>> "))

            if OpcionRemove == 1:
                self.cursos.remove(CursoRemove)
                print("El curso se ha eliminado con éxito")

            elif OpcionRemove == 2:
                print("Adios")
        except ValueError as err:
            print (err +"\nNo se pudo eliminar el curso")
        finally:
            print("\nPor favor vuelve a seleccionar otra opción")


estudiante1 = MiEstudiante("Herbert", 20, "Ingeniería")

try:
    while True:
        print("===============================================================")
        print("1.- AGREGAR CURSO  2.- QUITAR CURSO  3.- VER CURSOS  4.- SALIR")
        respuesta = int(input(">>> "))
        if respuesta == 1:
            estudiante1.Agregar_curso()

        elif respuesta == 2:
            estudiante1.Quitar_curso()

        elif respuesta == 3:
            print(estudiante1.cursos)

        elif respuesta == 4:
            print("HASTA LUEGO")
            print("===============================================================")
            break
        else:
            print("Selecciona una opción correcta, por favor")
except ValueError as err:
            print (err +"\nNo se pudo elegir una opción")
