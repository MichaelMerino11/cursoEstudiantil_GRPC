import grpc
import learning_platform_pb2
import learning_platform_pb2_grpc

def run():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = learning_platform_pb2_grpc.LearningPlatformStub(channel)
        
        # Crear Curso
        print("Creando curso...")
        curso_response = stub.CrearCurso(learning_platform_pb2.Curso(
            nombre="Curso de Python",
            descripcion="Aprender Python desde cero",
            fecha_inicio="2024-11-01",
            fecha_fin="2024-12-01"
        ))
        print(curso_response.message)
        
        # Obtener Curso
        print("Obteniendo curso...")
        curso = stub.ObtenerCurso(learning_platform_pb2.ID(id=1))
        print(f"Curso: {curso.nombre}, Descripción: {curso.descripcion}")

        # Crear Estudiante
        print("Creando estudiante...")
        estudiante_response = stub.CrearEstudiante(learning_platform_pb2.Estudiante(
            nombre="Juan Perez",
            correo="juan.perez@example.com",
            cursos_inscritos=[1]
        ))
        print(estudiante_response.message)
        
        # Obtener Estudiante
        print("Obteniendo estudiante...")
        estudiante = stub.ObtenerEstudiante(learning_platform_pb2.ID(id=1))
        print(f"Estudiante: {estudiante.nombre}, Correo: {estudiante.correo}, Cursos Inscritos: {estudiante.cursos_inscritos}")
        
        # Actualizar Estudiante
        print("Actualizando estudiante...")
        update_response = stub.ActualizarEstudiante(learning_platform_pb2.Estudiante(
            id=1,
            nombre="Juan Pérez Actualizado",
            correo="juan.perez@actualizado.com",
            cursos_inscritos=[1, 2]
        ))
        print(update_response.message)
        
        # Eliminar Estudiante
        print("Eliminando estudiante...")
        delete_response = stub.EliminarEstudiante(learning_platform_pb2.ID(id=1))
        print(delete_response.message)

if __name__ == "__main__":
    run()
