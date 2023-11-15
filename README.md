# Test_04

## Installation

1. Клонируйте репозиторий:

```bash
git clone https://github.com/codingoleg/Test_04.git
```

2. Перейдите в папку проекта:

```bash
cd .\Test_04\
```

+ Если в Windows используется Hyper-V вместо WSL, для создания volumes нужно добавить путь проекта в Docker по
  инструкции: https://stackoverflow.com/questions/62215781/docker-compose-failed-to-build-filesharing-has-been-cancelled-eshoponcontain
+ Запускаем docker-compose:

```bash
docker-compose up -d
```
+ После запуска контейнера в MongoDB создается база данных и коллекция с набором данных из db/mongo.py.

## Usage
+ Тесты на все случаи жизни лежат в пакете tests. Запускаем:
```bash
docker exec app pytest -v tests/test_run.py
```
+ Некоторые опциональные запросы:
1. ```bash
   curl --location --request POST 'http://127.0.0.1:8000/get_form?phone_num=%2B70000000000&date=2023-10-10'
   ```
   ```bash
   [
    {
        "date": "2023-10-10",
        "phone_num": "70000000000",
        "email": "email000000@mail.ru",
        "text": "0 text"
    },
    {
        "date": "2023-10-10",
        "phone_num": "70000000000",
        "email": "email111111@mail.ru",
        "text": "1 text"
    }
   ]

2. ```bash
   curl --location --request POST 'http://127.0.0.1:8000/get_form?email=email%40mail.ru%40'
   ```
   ```bash
   {
     "detail": "Invalid email"
   }
   ```

3. ```bash
   curl --location --request POST 'http://127.0.0.1:8000/get_form?date=11.20.2023'
   ```
   ```bash
   {
     "detail": "Invalid date format. Please use 'DD.MM.YYYY' or 'YYYY-MM-DD'"
   }
   ```
   
4. ```bash
   curl --location --request POST 'http://127.0.0.1:8000/get_form?phone_num=%2B700'
   ```
   ```bash
   {
     "detail": "Phone number should contain 11 digits"
   }
   ```
   
5. ```bash
   curl --location --request POST 'http://127.0.0.1:8000/get_form?text=aaaaaaa'
   ```
   ```bash
   {
     "date": "typing.Optional[str]",
     "phone_num": "typing.Optional[str]",
     "email": "typing.Optional[str]",
     "text": "typing.Optional[str]"
   }
   ```