from nonebot import get_driver
from pydantic import Field, BaseModel


class ThemeConfig(BaseModel):
    max_cut_length: int = Field(500, description="最大截断长度")


class Config(BaseModel):
    bison_theme: ThemeConfig

    class Config:
        extra = "ignore"


global_config = get_driver().config
theme_config = Config.parse_obj(global_config).bison_theme
