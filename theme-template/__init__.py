from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_bison")
from nonebot_bison.theme import theme_manager

from .parse import NewTheme
from .config import ThemeConfig

__plugin_meta__ = PluginMetadata(
    "<theme_name>",
    description="<theme_description>",
    usage="<theme_usage>",
    type="library",
    homepage="https://github.com/MountainDash/bison-themes/<theme_name>",
    config=ThemeConfig,
    supported_adapters=inherit_supported_adapters("nonebot_bison"),
)

# Register your theme here
theme_manager.register(NewTheme())  # type: ignore
