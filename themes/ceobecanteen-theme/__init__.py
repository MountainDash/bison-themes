from nonebot import require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_bison")
from nonebot_bison.theme import theme_manager

from .config import ThemeConfig
from .parse import CeobeCanteenTheme

__plugin_meta__ = PluginMetadata(
    "ceobecanteen-theme",
    description="ceobecanteen theme for bison",
    usage="pip install nonebot-bison-theme-ceobecanteen",
    type="library",
    homepage="https://github.com/MountainDash/bison-themes/ceobecanteen-theme",
    config=ThemeConfig,
    supported_adapters=inherit_supported_adapters("nonebot_bison"),
)

# Register your theme here
theme_manager.register(CeobeCanteenTheme())
