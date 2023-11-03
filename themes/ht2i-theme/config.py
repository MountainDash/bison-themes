from nonebot import get_driver
from pydantic import Field, BaseModel, validator


class ThemeConfig(BaseModel):
    max_cut_length: int | None = Field(None, description="最大截断长度, None为不截断")

    @validator("max_cut_length")
    def validate_max_cut_length(cls, v):
        if v is None:
            return None
        if v <= 0:
            raise ValueError("max_cut_length必须大于0")
        return v


class Config(BaseModel):
    bison_theme: ThemeConfig

    class Config:
        extra = "ignore"


global_config = get_driver().config
theme_config = Config.parse_obj(global_config).bison_theme
