# Sistema de Administración de Blogs

Este proyecto es una API para un sistema de administración de blogs que permite a cualquier usuario crear blogs, ver blogs de otros usuarios y gestionar categorías.

---

## Características

- **Creación de Blogs**: Los usuarios pueden crear nuevos blogs proporcionando detalles como título, palabras clave y categoría.
- **Visualización de Blogs**: Los usuarios pueden explorar blogs creados por otros usuarios.
- **Gestión de Categorías**: Administración de categorías para clasificar los blogs.
- **Información Adicional**: Almacena información extra relacionada con los usuarios.

---

## Estructura de la Base de Datos

El sistema utiliza una base de datos relacional con las siguientes tablas principales:

- **Users**: Almacena información de los usuarios, incluyendo nombre, apellido, correo electrónico, si es escritor y nombre de usuario.
- **ExtraInformation**: Contiene información adicional de los usuarios, como tipo e información específica.
- **Blogs**: Registra los blogs creados por los usuarios, incluyendo título, palabras clave y categoría.
- **Categories**: Define las categorías disponibles para clasificar los blogs.
- **Contents**: Detalles del contenido de los blogs, especificando número de contenido y tipo.

---

## Esquema de base de datos

### Tabla: Users

| **Campo**   | **Tipo**   | **Restricciones** |
|-------------|------------|-------------------|
| id          | INT        | PRIMARY KEY       |
| name        | VARCHAR(20)| NOT NULL          |
| lastname    | VARCHAR(20)| NOT NULL          |
| email       | VARCHAR(30)| NOT NULL          |
| writer      | BOOLEAN    | NOT NULL          |
| username    | VARCHAR(10)| NOT NULL          |

---

### Tabla: ExtraInformation

| **Campo**     | **Tipo**   | **Restricciones**                          |
|---------------|------------|--------------------------------------------|
| user_ID       | INT        | FOREIGN KEY (Users.id), PRIMARY KEY        |
| type          | VARCHAR(10)| NOT NULL, PRIMARY KEY                      |
| information   | VARCHAR(50)| NOT NULL                                   |

---

### Tabla: Blogs

| **Campo**     | **Tipo**    | **Restricciones**                          |
|---------------|-------------|--------------------------------------------|
| blog_ID       | VARCHAR(8)  | PRIMARY KEY                               |
| user_ID       | INT         | FOREIGN KEY (Users.id), NOT NULL          |
| category_ID   | INT         | FOREIGN KEY (Categories.category_ID), NOT NULL |
| title         | VARCHAR(50) | NOT NULL                                  |
| keywords      | VARCHAR(100)| NOT NULL                                  |

---

### Tabla: Categories

| **Campo**     | **Tipo**    | **Restricciones**      |
|---------------|-------------|------------------------|
| category_ID   | INT         | PRIMARY KEY           |
| name          | VARCHAR(30) | NOT NULL              |

---

### Tabla: Contents

| **Campo**     | **Tipo**    | **Restricciones**                          |
|---------------|-------------|--------------------------------------------|
| blog_ID       | VARCHAR(8)  | FOREIGN KEY (Blogs.blog_ID), PRIMARY KEY  |
| user_ID       | INT         | FOREIGN KEY (Users.id)                    |
| category_ID   | INT         | FOREIGN KEY (Categories.category_ID)      |
| content_num   | INT         | NOT NULL, PRIMARY KEY                     |
| type          | VARCHAR(10) | NOT NULL                                  |
| content       | VARCHAR(1000) | NOT NULL                                |

---

### Ejemplo adicional:
Si necesitas una tabla similar a la imagen proporcionada (por ejemplo, la tabla `Products`):

### Tabla: Products

| **Campo**           | **Tipo**       | **Restricciones**                          |
|----------------------|----------------|--------------------------------------------|
| Product_ID          | INT            | PRIMARY KEY                               |
| Name                | VARCHAR(255)   | NOT NULL                                  |
| Description         | TEXT           |                                           |
| Price               | DECIMAL(10, 2) | NOT NULL                                  |
| Available_Quantity  | INT            | NOT NULL                                  |
| Location            | VARCHAR(255)   |                                           |
| Supplier_ID         | INT            | FOREIGN KEY (Supplier.Supplier_ID)        |

---

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/arielpincayy/blogpage_admin_api.git
   ```

2. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar la base de datos**:
   - Asegúrate de tener una instancia de MySQL en funcionamiento.
   - Actualiza la configuración de la base de datos en el archivo `main.py` con tus credenciales de MySQL.

8. **Ejecutar la aplicación**:
   ```bash
   tu_directorio/app/main.py
   ```

---

## Uso

Una vez que la aplicación esté en funcionamiento, puedes interactuar con la API utilizando herramientas como [Postman](https://www.postman.com/) o [cURL](https://curl.se/).

### Endpoints Principales

#### Usuarios

- `GET /users`: Obtiene la lista de todos los usuarios.
- `POST /users`: Crea un nuevo usuario.
- `GET /user/<id>`: Obtiene información de un usuario específico.
- `PUT /user/<id>`: Actualiza información de un usuario.
- `DELETE /user/<id>`: Elimina un usuario.

#### Blogs

- `GET /blogs`: Obtiene la lista de todos los blogs.
- `POST /blogs`: Crea un nuevo blog.
- `GET /blog/<id>`: Obtiene información de un blog específico.
- `PUT /blog/<id>`: Actualiza información de un blog.
- `DELETE /blog/<id>`: Elimina un blog.

#### Categorías

- `GET /categories`: Obtiene la lista de todas las categorías.
- `POST /categories`: Crea una nueva categoría.
- `GET /category/<id>`: Obtiene información de una categoría específica.
- `PUT /category/<id>`: Actualiza información de una categoría.
- `DELETE /category/<id>`: Elimina una categoría.

---

## Contacto

Para más información, puedes contactarme:

- **Nombre**: [Ariel](https://github.com/arielpincayy)

- **Correo**: arielpincay812@gmail.com