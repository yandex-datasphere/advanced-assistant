from agents import (
    Agent,
    Model,
    ModelProvider,
    OpenAIResponsesModel,
    RunConfig,
    Runner,
    function_tool,
    set_tracing_disabled,
)

class CustomModelProvider(ModelProvider):
    def __init__(self,model,client):
        self.model = model
        self.client = client

    def get_model(self, model_name: str | None) -> Model:
        return OpenAIResponsesModel(model=self.model, openai_client=self.client)
