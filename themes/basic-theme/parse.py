from typing import TYPE_CHECKING, Literal

from nonebot_bison.theme import Theme
from nonebot_bison.utils import pic_merge, is_pics_mergable
from nonebot_plugin_saa import Text, Image, MessageSegmentFactory

from .config import theme_config

if TYPE_CHECKING:
    from nonebot_bison.post import Post


class BasicTheme(Theme):
    """最基本的主题

    纯文本，应为每个Post必定支持的Theme
    """

    name: Literal["basic"] = "basic"

    async def render(self, post: "Post") -> list[MessageSegmentFactory]:
        text = ""

        if post.title:
            text += f"{post.title}\n\n"

        text += (
            post.content
            if len(post.content) < theme_config.basic_max_cut_length
            else f"{post.content[:theme_config.basic_max_cut_length]}..."
        )

        text += f"\n来源: {post.platform.name} {post.nickname or ''}\n"

        if post.url:
            text += f"详情: {post.url}"

        msgs: list[MessageSegmentFactory] = [Text(text)]
        if post.images:
            pics = post.images
            if is_pics_mergable(pics):
                pics = await pic_merge(list(pics), post.platform.client)
            msgs.extend(map(Image, pics))

        return msgs
