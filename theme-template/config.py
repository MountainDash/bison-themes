from nonebot import get_driver
from pydantic import BaseModel


class ThemeConfig(BaseModel):
    pass


class Config(BaseModel):
    bison_theme: ThemeConfig

    class Config:
        extra = "ignore"


global_config = get_driver().config
theme_config = Config.parse_obj(global_config).bison_theme
