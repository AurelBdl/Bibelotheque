from pydantic_settings import BaseSettings, SettingsConfigDict


class Theme(BaseSettings):
    light_primary: str = "#b7441c"
    light_accent: str = "#EEDDB2"
    light_secondary: str = "#893315"
    light_success: str = "#43A047"
    light_info: str = "#1976D2"
    light_warning: str = "#FF6D00"
    light_error: str = "#EF5350"

    dark_primary: str = "#b7441c"
    dark_accent: str = "#EEDDB2"
    dark_secondary: str = "#893315"
    dark_success: str = "#43A047"
    dark_info: str = "#1976D2"
    dark_warning: str = "#FF6D00"
    dark_error: str = "#EF5350"
    model_config = SettingsConfigDict(env_prefix="theme_", extra="allow")
