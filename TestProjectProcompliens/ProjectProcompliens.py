from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import pandas as pd
#import subprocess

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secretkey'  #секретный ключ
jwt = JWTManager(app)
files = {}

# Аутентификация и выдача JWT-токена
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Проверка имени пользователя и пароля (здесь используйте свою реализацию)
    if username == 'admin' and password == 'password':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"message": "Неверное имя пользователя или пароль"}), 401

# Загрузка файла
@app.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    file = request.files['file']
    df = pd.read_csv(file)
    files[file.filename] = df.columns.tolist()
    return 'Файл успешно загружен.'

# Получение списка файлов и информации о колонках
@app.route('/files', methods=['GET'])
@jwt_required()
def get_files():
    return {'files': list(files.keys())}

# Получение данных из файла фильтрацией и сортировкой
@app.route('/data/<filename>', methods=['GET'])
@jwt_required()
def get_data(filename):
    if filename not in files:
        return 'Файл не найден.', 404

    df = pd.read_csv(filename)
    for column, value in request.args.items():
        if column in df.columns:
            df = df[df[column] == value]

    sort_by = request.args.get('sort_by')
    if sort_by and sort_by in df.columns:
        df = df.sort_values(by=sort_by)

    return df.to_dict(orient='records')

if __name__ == '__main__':
    #subprocess.run(['python', 'C:\\Users\\Никита\\source\\repos\\TestProjectProcompliens\\TestProjectProcompliens\\PyTestMod.py'])
    app.run()
