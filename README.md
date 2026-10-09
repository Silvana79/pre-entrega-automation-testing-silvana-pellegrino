# Pre-entrega - Automation & Testing QA

## Descripción del proyecto

Proyecto de automatización de pruebas web sobre [SauceDemo](https://www.saucedemo.com/), desarrollado con Python, Selenium WebDriver y Pytest.

El objetivo es verificar el funcionamiento del inicio de sesión, el catálogo de productos y el proceso de agregar un producto al carrito de compras.

## Actividades implementadas

* Login exitoso.
* Validación de la URL `/inventory.html`.
* Validación del título de la página `Swag Labs`.
* Validación de la sección `Products`.
* Verificación de que el inventario esté visible.
* Obtención dinámica del nombre y precio del primer producto.
* Validación de la visibilidad del menú y del filtro de productos.
* Agregado del primer producto al carrito.
* Validación del contador del carrito.
* Navegación al carrito.
* Verificación de que el producto agregado coincida con el producto listado en el carrito.

## Tecnologías utilizadas

* Python
* Pytest
* Selenium WebDriver
* webdriver-manager
* pytest-html
* Git
* GitHub

## Estructura del proyecto

```text
pre-entrega-automation-testing/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_saucedemo.py
├── utils/
│   ├── __init__.py
│   └── saucedemo.py
├── reports/
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

La carpeta `reports/` contiene los reportes y registros generados durante la ejecución. Las capturas de pantalla se guardan en `reports/screenshots/` cuando corresponde.

## Requisitos previos

* Python instalado.
* Google Chrome instalado.
* Conexión a Internet para acceder a SauceDemo e instalar las dependencias.

## Instalación

### 1. Clonar el repositorio

Una vez publicado el proyecto en GitHub:

```bash
git clone URL_DEL_REPOSITORIO
cd NOMBRE_DEL_REPOSITORIO
```

Reemplazar los valores de ejemplo por la URL y el nombre reales del repositorio.

### 2. Crear el entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual en Windows

```powershell
.\venv\Scripts\Activate.ps1
```

Si utilizás el Símbolo del sistema (CMD), ejecutá:

```bat
venv\Scripts\activate.bat
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Ejecución de las pruebas

Desde la carpeta principal del proyecto, ejecutar:

```bash
pytest
```

Pytest ejecuta las pruebas automatizadas y genera el reporte HTML y el archivo de registro.

## Reportes y evidencias

* **Reporte HTML:** `reports/reporte.html`
* **Registro de ejecución:** `reports/execution.log`
* **Capturas ante fallos:** `reports/screenshots/`

El reporte HTML permite consultar los resultados de las pruebas. El archivo de registro contiene los mensajes de ejecución configurados en el proyecto.

## Decisiones técnicas

* Se utilizan esperas explícitas mediante `WebDriverWait`.
* No se utiliza `time.sleep`.
* Cada prueba utiliza un navegador nuevo mediante el fixture de Pytest, favoreciendo la independencia entre pruebas.
* Se utiliza `webdriver-manager` para gestionar ChromeDriver.
* Se utilizan localizadores de Selenium como `By.ID` y `By.CLASS_NAME`.
* El nombre y el precio del primer producto se obtienen dinámicamente desde la página.
* No se implementa Page Object Model, ya que el proyecto se mantiene dentro del alcance de los contenidos trabajados en clase.

## Repositorio

**GitHub:** URL_DEL_REPOSITORIO

Completar este apartado con el enlace al repositorio una vez publicado.
