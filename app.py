from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import threading
import signal

# Configuration de la connexion à la base de données
db_host = os.environ.get('DB_HOST', 'localhost')
db_port = os.environ.get('DB_PORT', '3306')
db_user = os.environ.get('DB_USER', 'root')
db_password = os.environ.get('DB_PASSWORD', 'password')
db_name = os.environ.get('DB_NAME', 'mydatabase')
store_data_route = os.environ.get('STORE_DATA_ROUTE', '/store_data')
read_data_route = os.environ.get('READ_DATA_ROUTE', '/read_data')

# Connexion à la base de données
engine = create_engine(f'mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
Session = sessionmaker(bind=engine)
session = Session()

# Définition du modèle de données
Base = declarative_base()


class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    name = Column(String)


# Initialisation de l'application Flask
app = Flask(__name__)


# Route pour le POST qui stocke des données en base de données
@app.route('/store_data', methods=['POST'])
def store_data():
    data = request.json
    new_data = Data(name=data['name'])
    session.add(new_data)
    session.commit()
    return jsonify(status='success', message='Data stored successfully')


# Route pour le GET qui lit des données depuis la base de données
@app.route('/read_data', methods=['GET'])
def read_data():
    data = session.query(Data).all()
    result = [{'id': item.id, 'name': item.name} for item in data]
    return jsonify(result)


@app.route('/')
def home():
    return jsonify(status="success", message="200 OK")


def shutdown_server():
    os.kill(os.getpid(), signal.SIGINT)


@app.route('/exit')
def exit_server():
    shutdown_server()
    return jsonify(status="success", message="Server is shutting down...")


@app.route('/cpu')
def cpu_load():
    def cpu_stress():
        while True:
            pass

    thread = threading.Thread(target=cpu_stress)
    thread.start()
    return jsonify(status="success", message="CPU load started")


if __name__ == '__main__':
    app.run(debug=True)
