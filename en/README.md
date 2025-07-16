# Yandex Cloud Assistants

In this repository, there are sample of creating intelligent RAG assistants using Yandex AI Assistant API, and how to create multi-agent workflows and ReAct agents on top of that.

There are two files to look at:
* [langgraph-agent.ipynb](langgraph-agent.ipynb)
  - Starts with building single agent using [AI Assistant API](https://yandex.cloud/ru/docs/foundation-models/concepts/assistant/) and [Yandex Cloud ML SDK](https://github.com/yandex-cloud/yandex-cloud-ml-sdk)
  - Using [Function Calling](https://yandex.cloud/ru/docs/foundation-models/concepts/yandexgpt/function-call) to access tabular data and other functions
  - Multi-agent model testing by dialog of two agents
  - Orchestrating multiple agents using LangGraph
  - Testing LangGraph workflow using RAGAS
* [code-agent.ipynb](code-agent.ipynb)
  - How to implement coding agents that search internet and use MCP
  - Creating complex agent for food-wine matching

## Running the sample

To run the sample, you need  `folder_id` and `api_key` environment variables that refer to a service account with rights to use LLMs, AI Assistant API and Yandex Search API.

## Credits

This sample has been prepared by [Dmitry Soshnikov](https://soshnikov.com), author of "[Cloud Advocate](http://t.me/shwarsico)" telegram channel.