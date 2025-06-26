# This is an assignment on lab 3 (grpc part)

Sample code based on following sources:
based on https://github.com/ramananbalakrishnan/basic-grpc-python
https://realpython.com/python-microservices-grpc/

To run sample code:

```bash
pip install -r requirements.txt # installs deps
fastapi dev server.py # start server
open http://127.0.0.1:8000/graphql - view graphiql ui
```

## Assignment GraphQL Schema & Implementation

**Задача** Спроєктувати й реалізувати GraphQL-API для предметної області, вибраної у ЛР 1. *Persistence* шар необов’язковий — припускаються stub-дані або in-memory-сховище

Завдання

1. Рівень 1: Для ЛР 1 взяти 2-3 повʼязані сутності, опитати їх як types в graphQL schema і продублювати API зчитування по ID та створення до них з допомогою graphQL server (додати виклики готових сервісів в резолвери).(3) \
Рівень 2: Показати вкладеність сутностей з рівнем більше 2 (можете додати додаткові сутності-поля до існуючої моделі) (1) \
Рівень 3: Для івент-сорсингу з ЛР2, додати можливіть для клієнта отримувати graphQL subscription на одну з подій в системі (1)
2. Реалізувати мутації для оновлення даних основних сутностей (2)
3. Доступ до сутностей: \
Рівень 1: Запит на пагінований список високорівневих сутностей (2) \
Рівень 2-3: Для 1-n залежності використати шаблон DataLoader для уникнення n+1 на рівні резолвера(1)
4. Рівень 3: Винесіть сутність з окремого контексту в окремий підграф і відповідно окремий сервіс. Реалізувати єдиний граф з допомогою GraphQL federation (2)
