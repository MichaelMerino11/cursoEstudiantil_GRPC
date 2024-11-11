import sqlite3

def init_db():
    conn = sqlite3.connect('learning_platform.db')
    cursor = conn.cursor()
    
    # Crear tabla Cursos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        fecha_inicio TEXT,
        fecha_fin TEXT
    )
    ''')
    
    # Crear tabla Estudiantes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT UNIQUE,
        cursos_inscritos TEXT
    )
    ''')  # Lista de IDs como texto (puedes usar JSON para mejor manejo)
    
    conn.commit()
    conn.close()
    print("Base de datos inicializada correctamente.")

if __name__ == '__main__':
    init_db()
