import sqlite3
import grpc
from concurrent import futures
import learning_platform_pb2
import learning_platform_pb2_grpc

class LearningPlatformServicer(learning_platform_pb2_grpc.LearningPlatformServicer):
    def __init__(self):
        self.conn = sqlite3.connect('learning_platform.db', check_same_thread=False)
        self.init_db()

    def init_db(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Cursos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                fecha_inicio TEXT,
                fecha_fin TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Estudiantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL,
                cursos_inscritos TEXT
            )
        ''')
        self.conn.commit()

    # Métodos CRUD para Cursos
    def CrearCurso(self, request, context):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Cursos (nombre, descripcion, fecha_inicio, fecha_fin) VALUES (?, ?, ?, ?)",
                       (request.nombre, request.descripcion, request.fecha_inicio, request.fecha_fin))
        self.conn.commit()
        return learning_platform_pb2.Respuesta(success=True, message="Curso creado exitosamente")

    def ObtenerCurso(self, request, context):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nombre, descripcion, fecha_inicio, fecha_fin FROM Cursos WHERE id = ?", (request.id,))
        row = cursor.fetchone()
        if row:
            return learning_platform_pb2.Curso(id=row[0], nombre=row[1], descripcion=row[2],
                                               fecha_inicio=row[3], fecha_fin=row[4])
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Curso no encontrado")
            return learning_platform_pb2.Curso()

    def ActualizarCurso(self, request, context):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Cursos SET nombre = ?, descripcion = ?, fecha_inicio = ?, fecha_fin = ? WHERE id = ?",
                       (request.nombre, request.descripcion, request.fecha_inicio, request.fecha_fin, request.id))
        self.conn.commit()
        if cursor.rowcount == 0:
            return learning_platform_pb2.Respuesta(success=False, message="Curso no encontrado")
        return learning_platform_pb2.Respuesta(success=True, message="Curso actualizado exitosamente")

    def EliminarCurso(self, request, context):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Cursos WHERE id = ?", (request.id,))
        self.conn.commit()
        if cursor.rowcount == 0:
            return learning_platform_pb2.Respuesta(success=False, message="Curso no encontrado")
        return learning_platform_pb2.Respuesta(success=True, message="Curso eliminado exitosamente")

    # Métodos CRUD para Estudiantes
    def CrearEstudiante(self, request, context):
        cursor = self.conn.cursor()
        cursos_inscritos = ",".join(map(str, request.cursos_inscritos))
        cursor.execute("INSERT INTO Estudiantes (nombre, correo, cursos_inscritos) VALUES (?, ?, ?)",
                       (request.nombre, request.correo, cursos_inscritos))
        self.conn.commit()
        return learning_platform_pb2.Respuesta(success=True, message="Estudiante creado exitosamente")

    def ObtenerEstudiante(self, request, context):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nombre, correo, cursos_inscritos FROM Estudiantes WHERE id = ?", (request.id,))
        row = cursor.fetchone()
        if row:
            cursos_inscritos = list(map(int, row[3].split(','))) if row[3] else []
            return learning_platform_pb2.Estudiante(id=row[0], nombre=row[1], correo=row[2], cursos_inscritos=cursos_inscritos)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Estudiante no encontrado")
            return learning_platform_pb2.Estudiante()

    def ActualizarEstudiante(self, request, context):
        cursor = self.conn.cursor()
        cursos_inscritos = ",".join(map(str, request.cursos_inscritos))
        cursor.execute("UPDATE Estudiantes SET nombre = ?, correo = ?, cursos_inscritos = ? WHERE id = ?",
                       (request.nombre, request.correo, cursos_inscritos, request.id))
        self.conn.commit()
        if cursor.rowcount == 0:
            return learning_platform_pb2.Respuesta(success=False, message="Estudiante no encontrado")
        return learning_platform_pb2.Respuesta(success=True, message="Estudiante actualizado exitosamente")

    def EliminarEstudiante(self, request, context):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Estudiantes WHERE id = ?", (request.id,))
        self.conn.commit()
        if cursor.rowcount == 0:
            return learning_platform_pb2.Respuesta(success=False, message="Estudiante no encontrado")
        return learning_platform_pb2.Respuesta(success=True, message="Estudiante eliminado exitosamente")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    learning_platform_pb2_grpc.add_LearningPlatformServicer_to_server(LearningPlatformServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor iniciado en el puerto 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
