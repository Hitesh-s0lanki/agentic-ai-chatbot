from configparser import ConfigParser

class Config:
    def __init__(self, config_file="./src/components/config/constant.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def _get_list(self, key: str) -> list[str]:
        """
        Internal helper to fetch a comma-separated list from the DEFAULT section.
        """
        raw = self.config.get("DEFAULT", key, fallback="")
        return [item.strip() for item in raw.split(",") if item.strip()]

    def get_llm_options(self) -> list[str]:
        """
        Returns the available LLM options as a list of strings.
        """
        return self._get_list("LLM_OPTIONS")

    def get_usecase_options(self) -> list[str]:
        """
        Returns the available use-case options as a list of strings.
        """
        return self._get_list("USECASE_OPTIONS")

    def get_groq_model_options(self) -> list[str]:
        """
        Returns the available Groq model options as a list of strings.
        """
        return self._get_list("GROQ_MODEL_OPTIONS")

    def get_openai_model_options(self) -> list[str]:
        """
        Returns the available OpenAI model options as a list of strings.
        """
        return self._get_list("OPENAI_MODEL_OPTIONS")

    def get(self, section: str, key: str, fallback=None) -> str:
        """
        Generic getter for any key in any section.
        """
        return self.config.get(section, key, fallback=fallback)
    

