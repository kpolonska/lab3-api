# This is an assignment on lab 3 (grpc part)

Sample code based on following sources:
based on https://github.com/ramananbalakrishnan/basic-grpc-python
https://realpython.com/python-microservices-grpc/

To run sample code:

```bash
pip install -r requirements.txt # installs deps
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protobufs/question.proto # to generate stubs. u can skip as one is already committed
python server.py # to start server
python client.py # to start client
```

## Assignment

**Задача** Реалізувати gRPC-шар для тієї самої предметної області, що й у ЛР 1 (REST) та ЛР 2 (event-sourcing). Persistence шар може бути stub/in-memory

Завдання

1. Рівень 1. Взяти декілька сутностей і описати їх в  .proto. Описати сервіси для отримання сутності по ID та її створенню та редагуванню. Зрегенерувати стаби та скелетони і підключити існуючі сервіси.(3) \
Рівень 2.Налаштувати deadline чи timeout для клієнта (1)
1. Рівень 1. Реалізувати стрімінг даних з клієнта або сервера. Переконатися у відсутності n+1 та cartesian join проблем (2) \
Рівень 2. Реалізувати фільтрацію стріма по полях сутності (щонайменше 3 поля).  Додати limit-offset пагінацію (2) \
Рівень 3. Зробити bidirectional stream або client stream та гарантувати ідемпотентність обробки повідомлень у ньому (2)
1. Рівень 1: Додати валідацію на методи сервісів (непорожні обов’язкові рядкові поля; числові поля у допустимому діапазоні і тд). При порушенні валідації повертати INVALID_ARGUMENT з деталями google.rpc.BadRequest (список FieldViolation). Якщо сутність не знайдена — NOT_FOUND. Якщо дублюється унікальне поле — ALREADY_EXISTS (2 бали)  [https://grpc.io/docs/guides/status-codes/](https://grpc.io/docs/guides/status-codes/)
