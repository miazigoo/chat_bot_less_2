# Bot для ...

Бот позволяет ...


### Как установить

* Скачать [этот script](https://github.com/miazigoo/chat_bot_less_2.git)

**Python3 уже должен быть установлен**. 
Используйте `pip` (или `pip3`, если возникает конфликт с Python2) для установки зависимостей:
```sh
pip install -r requirements.txt
```


### Как запустить:

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в каталоге проекта и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.
Доступно 5 переменных:
- `TELEGRAM_BOT_API_KEY` — Получите токен у [@BotFather](https://t.me/BotFather), вставте в `.env` например: `TELEGRAM_BOT_API_KEY=588535421721:AAFYtrO5YJhpU...`.
- `VK_GROUP_TOKEN` — [token группы VK](https://vk.com/groups?tab=admin), незабудьте в настройках группы включить сообщения.
- `API_KEY` — [включите API cloud](https://cloud.google.com/dialogflow/es/docs/quick/setup#api).
- `PROJECT_ID` — [создать проект в cloud](https://cloud.google.com/dialogflow/docs/quick/setup) и [агента в DialogFlow](https://cloud.google.com/dialogflow/docs/quick/build-agent).
- `GOOGLE_APPLICATION_CREDENTIALS` — путь к файлу с ключами от google cloud аккаунта [создать токен](https://cloud.google.com/docs/authentication/api-keys).

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