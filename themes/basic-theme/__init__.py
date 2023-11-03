from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_bison")
from nonebot_bison.theme import theme_manager

from .parse import BasicTheme
from .config import ThemeConfig

__plugin_meta__ = PluginMetadata(
    "bison-themes-basic",
    description="Basic theme for bison",
    usage="pip install nonebot-bison-theme-basic",
    type="library",
    homepage="https://github.com/MountainDash/bison-themes/basic-theme",
    config=ThemeConfig,
    supported_adapters=inherit_supported_adapters("nonebot_bison"),
)

theme_manager.register(BasicTheme())
