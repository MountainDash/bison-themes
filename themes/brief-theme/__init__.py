from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_bison")
from nonebot_bison.theme import theme_manager

from .parse import BriefTheme
from .config import ThemeConfig

__plugin_meta__ = PluginMetadata(
    "bison-themes-brief",
    description="Brief theme for bison",
    usage="pip install nonebot-bison-theme-brief",
    type="library",
    homepage="https://github.com/MountainDash/bison-themes/brief-theme",
    config=ThemeConfig,
    supported_adapters=inherit_supported_adapters("nonebot_bison"),
)

# Register your theme here
theme_manager.register(BriefTheme())
