from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_bison")
from nonebot_bison.theme import theme_manager

from .config import Config
from .parse import ArknightsTheme

__plugin_meta__ = PluginMetadata(
    "bison-themes-arknights",
    description="Arknights theme for bison",
    usage="pip install nonebot-bison-theme-arknights",
    type="library",
    homepage="https://github.com/MountainDash/bison-themes/arknights-theme",
    config=Config,
    supported_adapters=inherit_supported_adapters("nonebot_bison"),
)

theme_manager.register(ArknightsTheme())
