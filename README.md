# oneMore_testing_work
One_more_test_free_work
Инструкции для запуска

1 скачать репозиторий
2 в  папке с файлом app.py открыть консоль и выполнить 2 команды:
sudo docker build -t cbc7 .
sudo docker run -p 5000:5000 cbc7

3
после сборки и запуска контейнера сделать загрузку файла через постман
или импортирвоат готовый файл с именем New Collection1.postman_collection.json
POST
http://localhost:5000/upload
далеe GET запросами постман можно:
- узнать имя и заголовки всех файлов которые есть на данный момент на сервере (http://localhost:5000/all_files_show_me)
- реализованы фильры по параметрам (http://localhost:5000/data/file1.csv?filter=m) где m значение столбца в строке
- реализована сортировка по возрасту (http://localhost:5000/data/file1.csv?sort=age)
- реализована сортировка с фильтрацией (http://localhost:5000/data/file1.csv?filter=m&sort=age)
- реализована функция просмотра содержимого файла по его имени (http://localhost:5000/data/file1.csv)
