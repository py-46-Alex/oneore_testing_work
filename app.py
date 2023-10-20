from flask import Flask, request, jsonify
import pandas as pd
import csv

# print("hi")
app = Flask(__name__)
ufv = {}
uploaded_files = {"file3.csv": [["sex", 'name'], ['m', 'Cimon'], ["m", "Alfred"], ['m', 'Ben']]}
uploaded_files = {}
#
@app.route('/')
def hello():
    return 'Hello, World!'
#
@app.route('/upload', methods=['POST'])
def upload_file():
    """функция для загрузки файлов в целом хранятся только в оперативке
    можно прикрутить дополнительно долговременную базу постгрес"""
    if 'file' not in request.files:
        return 'No file uploaded.', 400
    #
    file = request.files['file']
    if file.filename == '':
        return 'No file selected.', 200
    #
    df = pd.read_csv(file)
    dfname = file.filename
    dfcol = df.columns.tolist()
    uploaded_files[dfname] = dfcol
    ufv[file.filename] = df
    return 'File uploaded successfully.', 200
    #
@app.route("/all_files_show_me", methods=['GET'])
def all_files_show_me():
    """функция чтобы просмотреть все имена всех
    загруженных файлов и название их колонок"""
    return jsonify(uploaded_files)
    #
@app.route('/data/<filename>', methods=['GET'])
def get_data(filename):
    """функция отдает содержимое файла
    конкретно по имени файла."""
    if filename not in uploaded_files:
        return 'file not found.', 404
    df2 = ufv.get(filename)
    filter = request.args.get('filter')
    sort = request.args.get('sort')
    if filter and sort:
        df2 = df2[(df2['sex'] == filter)]
        df2 = df2.sort_values(sort, ascending=False)
        answer = df2.to_dict(orient='records')
        return answer
    if filter:
        df2 = df2[(df2['sex'] == filter)]
        answ = df2.to_dict(orient='records')
        return answ
    if sort:
        sorted_df = df2.sort_values(sort, ascending=False)
        answer = sorted_df.to_dict(orient='records')
        return answer
    if not sort and not filter:
        answer = df2.to_dict(orient='records')
        return answer

    #
if __name__ == '__main__':
    # создать файл ксв в папке далее для примера с запросами будет использваться он
    # with open("file1.csv", mode="w") as file:
    #     w = csv.writer(file)
    #     w.writerow(["name", "sex", "age"])
    #     w.writerow(["daria", "w", 17])
    #     w.writerow(["alex", "m", 14])
    #     w.writerow(["cimeon", "m", 15])
    #     w.writerow(["yameron", "m", 16])
    #     w.writerow(["zlata", "w", 13])
    #     w.writerow(["boris", "m", 16])
    #     w.writerow(["cat", "m", 18])
    app.run(host='0.0.0.0')