# Этот репозиторий содержит пример Discord бота, созданного для обучения и тестирования

Этот репозиторий представляет собой пример Discord бота с базовыми командами и функциональностью

Он предназначен для новичков, чтобы они могли познакомиться с принципами работы Discord ботов и начать разрабатывать свои собственные проекты

## Установка

Для того, чтобы запустить бота, выполните следующие шаги:

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/Malix-Floof/easy-discord-bot.git
    cd easy-discord-bot
    ```

2. Установите зависимости с помощью pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Создание бота на портале разработчиков Discord:

    - Заходим на [Discord Developer Portal](https://discord.com/developers/applications) во вкладку Application и нажимаем New Application
      ![image](https://github.com/user-attachments/assets/ff716c81-e57d-429a-8447-10dfcbec1a4f)
    - После этого указываем назание нашего бота (его можно будет изменить в будущем)
      ![image](https://github.com/user-attachments/assets/74c10a67-196c-44e5-8bb2-ecd80e6eeeba)
    - Переходим в созданное приложение и во вкладке Bot копируем токен

      ![image](https://github.com/user-attachments/assets/d6d0772b-17dc-4a41-9d85-cdc784705ebf)


5. Создайте `.env` файл в корне проекта и заполните его исходя из [`.env.example`](./.env.example).

6. Запустите бота:

    ```bash
    python bot.py
    ```

Теперь ваш бот будет работать, и вы сможете добавить его на сервер и начать взаимодействовать с ним!
