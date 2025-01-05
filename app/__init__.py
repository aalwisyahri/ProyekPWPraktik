from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Memuat konfigurasi dari file .env
load_dotenv()

# Inisialisasi db dan migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Inisialisasi aplikasi Flask dengan pengaturan folder static dan template
    app = Flask(__name__, 
                static_folder="../static",  # Menentukan lokasi folder static
                template_folder="../templates")  # Menentukan lokasi folder templates

    # Mengambil konfigurasi DATABASE_URI dari file .env
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = os.urandom(24)  # Menambahkan secret key untuk session

    db.init_app(app)
    migrate.init_app(app, db)

    # Cek apakah koneksi ke database berhasil
    with app.app_context():
        try:
            db.create_all()  # Coba membuat tabel jika belum ada
            print("Database connected and tables created.")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    from .routes import main
    app.register_blueprint(main)

    return app
