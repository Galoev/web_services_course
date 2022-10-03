# web_services_course

Клиент передаёт серверу 2 изображения, главное и лого (водяной знак). Сервер добавляет этот водяной знак на изображение.

python -m grpc_tools.protoc --proto_path="protos/" --python_out="protos/builds/"  --grpc_python_out="protos/builds/" protos/services.proto

python server.py
python client.py images/main_image.jpg images/cv_logo.png 50 .


![Alt text](images/cv_logo.png "LOGO")
![Alt text](images/main_image.jpg "MAIN")
![Alt text](new_image.jpg "MAIN")
