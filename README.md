# Yandex Cloud Assistants

В этом репозитории содержится пример создания интеллектуального ассистента по продаже вин в Yandex Cloud, а также создания многоагентной системы для подбора ужина из основного блюда и вина на основе пожеланий пользователя. Мы по шагам рассматриваем следующие понятия:

* [Yandex Cloud ML SDK](https://github.com/yandex-cloud/yandex-cloud-ml-sdk), и как работать с языковыми моделями
* Простейшие ассистенты [AI Assistant API](https://yandex.cloud/ru/docs/foundation-models/concepts/assistant/) для поддержания контекста диалога
* Подключение текстовой базы знаний (индекса) к модели для реализации RAG
* Умное чанкование и индексирование таблиц Markdown
* Понятие [Function Calling](https://yandex.cloud/ru/docs/foundation-models/concepts/yandexgpt/function-call) в генеративных моделях и его использование с ассистентами
* Реализация агента с документным индексом и поддержкой нескольких функций: поиск в базе данных, вызов оператора, добавление покупок в корзину
* Многоагентное тестирование модели с помощью диалога двух агентов
* Реализация телеграм-бота на основе ассистента, с поддержкой нескольких пользователей
* Создание Agentic Workflow с помощью LangGraph поверх AI Assistant API
* Тестирование Agentic Workflow с помощью фреймворка RAGAS
* Создание ReAct-агента, использующего MCP-протокол

## Запуск примера

Для работы с примером рекомендуется:
* Клонировать репозиторий в проекте Yandex Datasphere
* Установить в проекте секреты `folder_id`, `api_key` для сервисного аккаунта, имеющего права на работу с языковыми моделями и ассистентами.
* Установить секрет `tg_token`, если вы планируете тестировать телеграм-бота
* Открыть ноутбук [advanced-assistant.ipynb](advanced-assistant.ipynb) (Создание ассистента), [langgraph-agent.ipynb](langgraph-agent.ipynb) (построение Agentic Workflow) и [code-agent.ipynb](code-agent.ipynb) (ReAct-агент на основе кодогенерации)

## В выступлениях
* 3 апреля 2025 г., вебинар "[Создание Telegram-бота на базе LLM с RAG и Function Calling](https://yandex.cloud/ru/events/1117)" [![GitHub Release](https://img.shields.io/github/v/release/yandex-datasphere/advanced-assistant?filter=v1)](https://github.com/yandex-datasphere/advanced-assistant/tree/v1) [![](https://img.shields.io/badge/смотреть-запись-blue)](https://yandex.cloud/ru/events/1117)
* 16 мая 2025 г., доклад [Введение в агенты с YandexGPT и Yandex Cloud](https://imlconf.com/talks/2dd289be1ff54eeab2c2cce578668c23/) на конференции [IML 2025](https://imlconf.com/) [![GitHub Release](https://img.shields.io/github/v/release/yandex-datasphere/advanced-assistant?filter=v2)](https://github.com/yandex-datasphere/advanced-assistant/tree/v2) [![](https://img.shields.io/badge/смотреть-запись-blue)](https://imlconf.com/talks/2dd289be1ff54eeab2c2cce578668c23/)
* 25 июня 2025 г., доклад [Многоагентные системы в облаке Yandex Cloud](https://gigaconf.ru/program) на конференции [GigaConf 2025](https://gigaconf.ru/) [![GitHub Release](https://img.shields.io/github/v/release/yandex-datasphere/advanced-assistant?filter=v3)](https://github.com/yandex-datasphere/advanced-assistant/tree/v3)
* 26 июня 2025 г., вебинар [От AI-ассистента к многоагентным системам](https://yandex.cloud/ru/events/1282) [![GitHub Release](https://img.shields.io/github/v/release/yandex-datasphere/advanced-assistant?filter=v3)](https://github.com/yandex-datasphere/advanced-assistant/tree/v3)
* 17 июля 2025 г., семинар на летней школе [SMILES-2025](https://smiles.skoltech.ru/) от Skoltech и [Харбинского политехнического университета](https://en.hit.edu.cn/) [![GitHub Release]](https://img.shields.io/github/v/release/yandex-datasphere/advanced-assistant?filter=v3e)](https://github.com/yandex-datasphere/advanced-assistant/tree/v3e)

## Благодарности

Пример подготовлен [Дмитрием Сошниковым](https://soshnikov.com/ru), телеграм-канал "[Облачный адвокат](http://t.me/shwarsico)"