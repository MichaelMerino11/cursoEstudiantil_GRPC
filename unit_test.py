import unittest
from server import LearningPlatformServicer
import learning_platform_pb2

class TestLearningPlatform(unittest.TestCase):
    
    def setUp(self):
        self.service = LearningPlatformServicer()

    
    def test_crear_curso(self):
        request = learning_platform_pb2.Curso(
            nombre="Curso de Test",
            descripcion="Este es un curso de prueba",
            fecha_inicio="2024-01-01",
            fecha_fin="2024-06-01"
        )
        response = self.service.CrearCurso(request, None)
        self.assertTrue(response.success)
        self.assertEqual(response.message, "Curso creado exitosamente")
        
    def test_obtener_curso(self):
        # Crear un curso antes de obtenerlo
        crear_request = learning_platform_pb2.Curso(
            nombre="Curso de Test",
            descripcion="Este es un curso de prueba",
            fecha_inicio="2024-01-01",
            fecha_fin="2024-06-01"
        )
        self.service.CrearCurso(crear_request, None)
        
        # Obtener el curso creado
        obtener_request = learning_platform_pb2.ID(id=1)
        response = self.service.ObtenerCurso(obtener_request, None)
        self.assertEqual(response.id, 1)
        self.assertEqual(response.nombre, "Curso de Test")
        self.assertEqual(response.descripcion, "Este es un curso de prueba")
        
    def test_actualizar_curso(self):
        # Crear un curso antes de actualizarlo
        crear_request = learning_platform_pb2.Curso(
            nombre="Curso de Test",
            descripcion="Este es un curso de prueba",
            fecha_inicio="2024-01-01",
            fecha_fin="2024-06-01"
        )
        self.service.CrearCurso(crear_request, None)
        
        # Actualizar el curso
        actualizar_request = learning_platform_pb2.Curso(
            id=1,
            nombre="Curso de Python",
            descripcion="Curso avanzado de Python",
            fecha_inicio="2024-02-01",
            fecha_fin="2024-07-01"
        )
        response = self.service.ActualizarCurso(actualizar_request, None)
        self.assertTrue(response.success)
        self.assertEqual(response.message, "Curso actualizado exitosamente")
        
    def test_eliminar_curso(self):
        # Crear un curso antes de eliminarlo
        crear_request = learning_platform_pb2.Curso(
            nombre="Curso de Test",
            descripcion="Este es un curso de prueba",
            fecha_inicio="2024-01-01",
            fecha_fin="2024-06-01"
        )
        self.service.CrearCurso(crear_request, None)
        
        # Eliminar el curso
        eliminar_request = learning_platform_pb2.ID(id=1)
        response = self.service.EliminarCurso(eliminar_request, None)
        self.assertTrue(response.success)
        self.assertEqual(response.message, "Curso eliminado exitosamente")
        
    def test_crear_estudiante(self):
        request = learning_platform_pb2.Estudiante(
            nombre="Juan Perez",
            correo="juan.perez@example.com",
            cursos_inscritos=[1]
        )
        response = self.service.CrearEstudiante(request, None)
        self.assertTrue(response.success)
        self.assertEqual(response.message, "Estudiante creado exitosamente")
        
    def test_obtener_estudiante(self):
        # Crear un estudiante antes de obtenerlo
        crear_request = learning_platform_pb2.Estudiante(
            nombre="Juan Perez",
            correo="juan.perez@example.com",
            cursos_inscritos=[1]
        )
        self.service.CrearEstudiante(crear_request, None)
        
        # Obtener el estudiante creado
        obtener_request = learning_platform_pb2.ID(id=1)
        response = self.service.ObtenerEstudiante(obtener_request, None)
        self.assertEqual(response.id, 1)
        self.assertEqual(response.nombre, "Juan Perez")
        self.assertEqual(response.correo, "juan.perez@example.com")
        
    def test_actualizar_estudiante(self):
        # Crear un estudiante antes de actualizarlo
        crear_request = learning_platform_pb2.Estudiante(
            nombre="Juan Perez",
            correo="juan.perez@example.com",
            cursos_inscritos=[1]
        )
        self.service.CrearEstudiante(crear_request, None)
        
        # Actualizar el estudiante
        actualizar_request = learning_platform_pb2.Estudiante(
            id=1,
            nombre="Juan Pérez Actualizado",
            correo="juan.perez@actualizado.com",
            cursos_inscritos=[1, 2]
        )
        response = self.service.ActualizarEstudiante(actualizar_request, None)
        self.assertTrue(response.success)
        self.assertEqual(response.message, "Estudiante actualizado exitosamente")
        
    def test_eliminar_estudiante(self):
        # Crear un estudiante antes de eliminarlo
        crear_request = learning_platform_pb2.Estudiante(
            nombre="Juan Perez",
            correo="juan.perez@example.com",
            cursos_inscritos=[1]
        )
        self.service.CrearEstudiante(crear_request, None)
        
        # Eliminar el estudiante
        eliminar_request = learning_platform_pb2.ID(id=1)
        response = self.service.EliminarEstudiante(eliminar_request, None)
        self.assertTrue(response.success)
        self.assertEqual(response.message, "Estudiante eliminado exitosamente")

if __name__ == '__main__':
    unittest.main()
