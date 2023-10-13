# Bot для ...

Бот позволяет автоматически отвечать на сообщения юзеров
![Снимок экрана от 2023-10-12 20-29-32](https://github.com/miazigoo/chat_bot_less_2/assets/55626306/44d98253-df15-4254-b89c-df0f34849af9)

### Как установить


* Скачать [этот script](https://github.com/miazigoo/chat_bot_less_2.git)

**Python3 уже должен быть установлен**. 
Используйте `pip` (или `pip3`, если возникает конфликт с Python2) для установки зависимостей:
```sh
pip install -r requirements.txt
```


### Как запустить:

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в каталоге проекта и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.
Доступно 6 переменных:
- `TELEGRAM_BOT_API_KEY` — Получите токен у [@BotFather](https://t.me/BotFather), вставте в `.env` например: `TELEGRAM_BOT_API_KEY=588535421721:AAFYtrO5YJhpU...`.
- `VK_GROUP_TOKEN` — [token группы VK](https://vk.com/groups?tab=admin), незабудьте в настройках группы включить сообщения.
- `API_KEY` — [включите API cloud](https://cloud.google.com/dialogflow/es/docs/quick/setup#api).
- `PROJECT_ID` — [создать проект в cloud](https://cloud.google.com/dialogflow/docs/quick/setup) и [агента в DialogFlow](https://cloud.google.com/dialogflow/docs/quick/build-agent).
- `GOOGLE_APPLICATION_CREDENTIALS` — путь к файлу с ключами от google cloud аккаунта [создать токен](https://cloud.google.com/docs/authentication/api-keys).
- `TELEGRAM_ADMIN_ID` — ваш телеграм id. получить его можно у [@userinfobot ](https://t.me/userinfobot), отправив любое сообщение.
- 
Запуск производится командой: 
- Телеграм
```sh
python  tgbot.py
```
- Вконтакте
```sh
python  vkchat.py
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
