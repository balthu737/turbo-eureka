⚙️ Instalación
1️⃣ Clonar el repositorio
git clone https://github.com/balthu737/turbo-eureka
cd turbo-eureka

2️⃣ Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Configurar variables de entorno

Crear un archivo .env o configurar en config.py:

TELEGRAM_BOT_TOKEN=tu_token
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_password
DB_NAME=gastos

5️⃣ Ejecutar el proyecto
python main.py