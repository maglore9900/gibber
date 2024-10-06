
class Adapter:
    def __init__(self, env):
        self.llm_text = env("LLM_TYPE")
        if self.llm_text.lower() == "openai":
            from langchain_openai import ChatOpenAI
            self.llm_chat = ChatOpenAI(
                temperature=0.3, model=env("OPENAI_MODEL"), openai_api_key=env("OPENAI_API_KEY")
            )
        elif self.llm_text.lower() == "local":
            from langchain_community.chat_models import ChatOllama
            llm_model = env("OLLAMA_MODEL")
            self.llm_chat = ChatOllama(
                base_url=env("OLLAMA_URL"), model=llm_model
            )
        else:
            print(f"Invalid LLM choice, can be openai or local, you selected: {self.llm_text}")
            raise ValueError("Invalid LLM")

