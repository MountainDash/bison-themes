# bison-themes

[Nonebot-Bison](https://github.com/MountainDash/nonebot-bison) 的主题仓库。

## 使用方法

安装对应的主题插件

```shell
pip install nonebot-bison-theme-<theme-name>
```

> [!NOTE]
> 请将 `<theme-name>` 替换为你想要安装的主题名称。
> 例如 `basic-theme`, 则安装命令为 `pip install nonebot-bison-theme-basic`

在 `pyproject.toml` 中启用

```toml
[tool.nonebot]
plugin = [
    "nonebot_bison_theme_basic",
    # ...
]
```

> [!NOTE]
> bison 初始化携带 basic 主题，无需安装即可使用。

## 主题画廊

- arknights
- basic
- brief
- ceobecanteen
- ht2i
