# Yandex Cloud Assistants

В этом репозитории содержится пример создания интеллектуального ассистента по продаже вин в Yandex Cloud. Мы по шагам рассматриваем следующие понятия:

* [Yandex Cloud ML SDK](https://github.com/yandex-cloud/yandex-cloud-ml-sdk), и как работать с языковыми моделями
* Простейшие ассистенты [AI Assistant API](https://yandex.cloud/ru/docs/foundation-models/concepts/assistant/) для поддержания контекста диалога
* Подключение текстовой базы знаний (индекса) к модели для реализации RAG
* Умное чанкование и индексирование таблиц Markdown
* Понятие [Function Calling](https://yandex.cloud/ru/docs/foundation-models/concepts/yandexgpt/function-call) в генеративных моделях и его использование с ассистентами
* Реализация агента с документным индексом и поддержкой нескольких функций: поиск в базе данных, вызов оператора, добавление покупок в корзину
* Многоагентное тестирование модели с помощью диалога двух агентов
* Реализация телеграм-бота на основе ассистента, с поддержкой нескольких пользователей

## Запуск примера

Для работы с примером рекомендуется:
* Клонировать репозиторий в проекте Yandex Datasphere
* Установить в проекте секреты `folder_id`, `api_key` для сервисного аккаунта, имеющего права на работу с языковыми моделями и ассистентами.
* Установить секрет `tg_token`, если вы планируете тестировать телеграм-бота
* Открыть ноутбук [advanced-assistant.ipynb](advanced-assistant.ipynb)

## В выступлениях
* 3 апреля 2025 г., Вебинар "[Создание Telegram-бота на базе LLM с RAG и Function Calling](https://yandex.cloud/ru/events/1117)" ![GitHub Release](https://img.shields.io/github/v/release/yandex-datasphere/advanced-assistant?filter=v1) ![](https://img.shields.io/badge/смотреть-запись-blue)

## Благодарности

Пример подготовлен [Дмитрием Сошниковым](https://soshnikov.com/ru), телеграм-канал "[Облачный адвокат](http://t.me/shwarsico)"