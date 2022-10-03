# web_services_course

python -m grpc_tools.protoc --proto_path="protos/" --python_out="protos/builds/"  --grpc_python_out="protos/builds/" protos/services.proto

python server.py
python client.py images/main_image.jpg images/cv_logo.png 50 .
