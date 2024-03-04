from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self,grupo="Grupo de estudiantes: grupo predeterminado", asignaturas=[], estudiantes = []):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))


    def agregarAlumno(self, alumno, lista=[]):
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista
        lista.remove(alumno)

    # def __str__(self):
    #     pass

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

