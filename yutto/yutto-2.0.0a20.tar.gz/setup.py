# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yutto',
 'yutto.api',
 'yutto.cli',
 'yutto.media',
 'yutto.processor',
 'yutto.utils',
 'yutto.utils.console',
 'yutto.utils.functiontools']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles==0.7.0',
 'aiohttp==3.7.4.post0',
 'biliass==1.3.4',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['yutto = yutto.__main__:main']}

setup_kwargs = {
    'name': 'yutto',
    'version': '2.0.0a20',
    'description': 'yutto 一个可爱且任性的 B 站视频下载器',
    'long_description': '# yutto [WIP]\n\n<p align="center">\n   <a href="https://python.org/" target="_blank"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/yutto?logo=python&style=flat-square"></a>\n   <a href="https://pypi.org/project/yutto/" target="_blank"><img src="https://img.shields.io/pypi/v/yutto?style=flat-square" alt="pypi"></a>\n   <a href="https://pypi.org/project/yutto/" target="_blank"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/yutto?style=flat-square"></a>\n   <a href="LICENSE"><img alt="LICENSE" src="https://img.shields.io/github/license/SigureMo/yutto?style=flat-square"></a>\n   <a href="https://gitmoji.dev"><img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67?style=flat-square" alt="Gitmoji"></a>\n</p>\n\nyutto，一个可爱且任性的 B 站下载器（CLI）\n\n## 版本号为什么是 2.0\n\n因为 yutto 是 bilili 的後輩呀～\n\n## 名字的由来\n\n终于在 B 站播放[《転スラ日記》](https://www.bilibili.com/bangumi/play/ep395211)这一天将 yutto 基本流程搭建完了，可以稍微休息一下了（\n\n至于名字嘛，开始只是觉得 yutto 很可爱，印象里是萌王说过的，但具体忘记出处是在哪里了，今天“重温”《転スラ日記》第一话时候，居然 00:25 就是～总之，リムル最可爱啦〜\n\n## 安装预览版\n\n在此之前请确保安装 Python3.9（不支持 3.8 及以下，3.10 尚处于 beta，没有测试）与 FFmpeg（参照 [bilili 文档](https://bilili.sigure.xyz/guide/getting-started.html)）\n\n由于是预览版，所以希望得到更多的建议～特别是命令的设计上（当前这种多级子命令是否合适？）\n\n### pip 安装\n\n```bash\npip install --pre yutto\n```\n\n### git clone\n\n```bash\ngit clone https://github.com/SigureMo/yutto.git\npython setup.py build\npython setup.py install\n```\n\n## 功能预览\n\n### 基本命令\n\n你可以通过 yutto 命令来下载**一个**视频。它支持 av/BV 号以及相应带 p=n 参数的投稿视频页面，也支持 ep 号（episode_id）的番剧页面。\n\n比如只需要这样你就可以下载《転スラ日記》第一话：\n\n```bash\nyutto https://www.bilibili.com/bangumi/play/ep395211\n```\n\n不过有时你可能想要批量下载很多剧集，因此 yutto 提供了用于批量下载的参数 `-b/--batch`，它不仅支持前面所说的单个视频所在页面地址（会解析该单个视频所在的系列视频），还支持一些明确用于表示系列视频的地址，比如 md 页面（media_id）、ss 页面（season_id）。\n\n比如像下面这样就可以下载《転スラ日記》所有已更新的剧集：\n\n```bash\nyutto --batch https://www.bilibili.com/bangumi/play/ep395211\n```\n\n### 基础参数\n\n> 大部分参数与 bilili 重合，可参考 [bilili 的 cli 文档](https://bilili.nyakku.moe/cli/)\n\nyutto 支持一些基础参数，无论是批量下载还是单视频下载都适用。\n\n<details>\n<summary>点击展开详细参数</summary>\n\n#### 最大并行 worker 数量\n\n-  参数 `-n` 或 `--num-workers`\n-  默认值 `8`\n\n与 bilili 不同的是，yutto 并不是使用多线程实现并行下载，而是使用协程实现的，本参数限制的是最大的并行 Worker 数量。\n\n#### 视频质量\n\n-  参数 `-q` 或 `--video-quality`\n-  可选值 `125 | 120 | 116 | 112 | 80 | 74 | 64 | 32 | 16`\n-  默认值 `125`\n\n用于调节视频清晰度（详情可参考 bilili 文档）。\n\n#### 音频质量\n\n-  参数 `-aq` 或 `--audio-quality`\n-  可选值 `30280 | 30232 | 30216`\n-  默认值 `30280`\n\n用于调节音频码率（详情可参考 bilili 文档）。\n\n#### 视频编码\n\n-  参数 `--vcodec`\n-  下载编码可选值 `hevc | avc`\n-  保存编码可选值 FFmpeg 所有可用的视频编码器\n-  默认值 `avc:copy`\n\n该参数略微复杂，前半部分表示在下载时**优先**选择哪一种编码的视频流，后半部分则表示在合并时如何编码视频流，两者使用 `:` 分隔。\n\n值得注意的是，前半的下载编码只是优先下载的编码而已，如果不存在该编码，则仍会像视频清晰度调节机制一样自动选择其余编码。\n\n而后半部分的参数如果设置成非 `copy` 的值则可以确保在下载完成后对其进行重新编码，而且不止支持 `hevc` 与 `avc`，只要你的 FFmpeg 支持的视频编码器，它都可以完成。\n\n#### 音频编码\n\n-  参数 `--acodec`\n-  下载编码可选值 `mp4a`\n-  保存编码可选值 FFmpeg 所有可用的音频编码器\n-  默认值 `mp4a:copy`\n\n详情同视频编码。\n\n#### 仅下载视频流\n\n-  参数 `--video-only`\n-  默认值 `False`\n\n#### 仅下载音频流\n\n-  参数 `--audio-only`\n-  默认值 `False`\n\n仅下载其中的音频流，保存为 `.aac` 文件。\n\n值得注意的是，在不选择视频流时，嵌入字幕、弹幕功能将无法工作。\n\n#### 弹幕格式选择\n\n-  参数 `-df` 或 `--danmaku-format`\n-  可选值 `ass | xml | protobuf`\n-  默认值 `ass`\n\n#### 下载块大小\n\n-  参数 `-bs` 或 `--block-size`\n-  默认值 `0.5`\n\n以 MiB 为单位，为分块下载时各块大小，不建议更改。\n\n#### 强制覆盖已下载文件\n\n-  参数 `-w` 或 `--overwrite`\n-  默认值 `False`\n\n#### 代理设置\n\n-  参数 `-x` 或 `--proxy`\n-  可选值 `auto | no | <https?://url/to/proxy/server>`\n-  默认值 `auto`\n\n设置代理服务器，默认是从环境变量读取，`no` 则为不设置代理，设置其它 http/https url 则将其作为代理服务器。\n\n#### 存放根目录\n\n-  参数 `-d` 或 `--dir`\n-  默认值 `./`\n\n#### 存放子路径模板\n\n-  参数 `-tp` 或 `--subpath-template`\n-  可选参数变量 `title | id | name` （以后可能会有更多）\n-  默认值 `{auto}`\n\n通过配置子路径模板可以灵活地控制视频存放位置。\n\n默认情况是由 yutto 自动控制存放位置的。比如下载单个视频时默认就是直接存放在设定的根目录，不会创建一层容器目录，此时自动选择了 `{name}` 作为模板；而批量下载时则会根据视频层级生成多级目录，比如番剧会是 `{title}/{name}`，首先会在设定根目录里生成一个番剧名的目录，其内才会存放各个番剧剧集视频，这样方便了多个不同番剧的管理。当然，如果你仍希望将番剧直接存放在设定根目录下的话，可以修改该参数值为 `{name}`即可。\n\n另外，该功能语法由 Python format 语法提供，所以也支持一些高级的用法，比如 `{id:0>3}{name}`。\n\n#### url 别名文件路径\n\n-  参数 `-af` 或 `--alias-file`\n-  默认值 `None`\n\n指定别名文件路径，别名文件中存放一个别名与其对应的 url，使用空格或者 `=` 分隔，示例如下：\n\n```\nrimuru1=https://www.bilibili.com/bangumi/play/ss25739/\nrimuru2=https://www.bilibili.com/bangumi/play/ss36170/\nrimuru-nikki=https://www.bilibili.com/bangumi/play/ss38221/\n```\n\n比如将上述文件存储到 `~/.yutto_alias`，则通过以下命令即可解析该文件：\n\n```bash\nyutto rimuru1 --batch --alias-file=\'~/.yutto_alias\'\n```\n\n当参数值为 `-` 时，会从标准输入中读取：\n\n```bash\ncat ~/.yutto_alias | yutto rimuru-nikki --batch --alias-file -\n```\n\n#### Cookies 设置\n\n-  参数 `-c` 或 `--sessdata`\n-  默认值 ``\n\n详情参考 bilili 文档。\n\n#### 不下载弹幕\n\n-  参数 `--no-danmaku`\n-  默认值 `False`\n\n#### 不下载字幕\n\n-  参数 `--no-subtitle`\n-  默认值 `False`\n\n#### 不显示颜色\n\n-  参数 `--no-color`\n-  默认值 `False`\n\n#### 启用 Debug 模式\n\n-  参数 `--debug`\n-  默认值 `False`\n\n</details>\n\n### 批量参数\n\n有些参数是只有批量下载时才可以使用的\n\n<details>\n<summary>点击展开详细参数</summary>\n\n#### 启用批量下载\n\n-  参数 `-b` 或 `--batch`\n-  默认值 `False`\n\n只需要 `yutto --batch <url>` 即可启用批量下载功能。\n\n#### 选集\n\n-  参数 `-p` 或 `--episodes`\n-  默认值 `^~$`\n\n详情参考 bilili 文档。\n\n#### 同时下载附加剧集\n\n-  参数 `-s` 或 `--with-section`\n-  默认值 `False`\n\n</details>\n\n## 从 bilili1.x 迁移\n\n### 取消的功能\n\n-  `- bilibili` 目录的生成\n-  播放列表生成\n-  源格式修改功能（不再支持 flv 源视频下载，如果仍有视频不支持 dash 源，请继续使用 bilili）\n\n### 默认行为的修改\n\n-  使用协程而非多线程进行下载，同时也不是批量解析批量下载，而是边解析边下载\n-  默认生成弹幕为 ASS\n-  默认启用从多镜像源下载的特性\n-  不仅可以控制是否使用系统代理，还能配置特定的代理服务器\n\n### 新增的特性\n\n-  单视频下载与批量下载命令分离（`bilili` 命令与 `yutto --batch` 相类似）\n-  音频/视频编码选择\n-  仅下载音频/视频\n-  存放子路径的自由定制\n-  支持 url alias\n-  支持 file scheme\n\n### 小技巧\n\n#### 使用 url alias\n\nyutto 新增的 url alias 可以让你下载正在追的番剧时不必每次都打开浏览器复制 url，只需要将追番列表存储在一个文件中，并为这些 url 起一个别名即可\n\n```\nrimuru-nikki=https://www.bilibili.com/bangumi/play/ss38221/\n```\n\n之后下载最新话只需要\n\n```\nyutto --batch rimuru-nikki --alias-file=/path/to/alias-file\n```\n\n#### 使用 file scheme 作为 url\n\n现在 url 不仅支持 http/https scheme，还支持使用 file scheme 来用于表示文件列表，文件列表以行分隔，每行写一次命令的参数，该参数会覆盖掉主程序中所使用的参数，示例如下：\n\n```\nrimuru-nikki --batch -p $\nhttps://www.bilibili.com/bangumi/play/ss38260/ --batch -p $\n```\n\n现在只需要\n\n```\nyutto file:///path/to/list\n```\n\n即可分别下载这两个番剧的最新一话\n\n当然，也许你不想每次输入这个路径，只需要将该路径存到 alias 文件中即可（alias 也支持 file scheme），比如\n\n```\nsubscription=file:///path/to/list\nrimuru-nikki=https://www.bilibili.com/bangumi/play/ss38221/\n```\n\n这样就可以直接使用\n\n```\nyutto subscription --alias-file=/path/to/alias-file\n```\n\n貌似没太大作用呢 2333\n\n值得注意的是，在文件列表各项里的参数优先级是高于命令里的优先级的，比如文件中使用：\n\n```\nrimuru-nikki --batch -p $ --no-danmaku --vcodec="hevc:copy"\nrimuru1 --batch -p $\n```\n\n而命令中则使用\n\n```\nyutto file:///path/to/list --vcodec="avc:copy"\n```\n\n最终下载的 rimuru-nikki 会是 "hevc:copy"，而 rimuru1 则会是 "avc:copy"\n\n最后，你当然可以在列表中嵌套列表～\n\n## TODO List\n\n-  [ ] 完善的信息提示\n-  [ ] 字幕、弹幕嵌入视频支持\n-  [ ] 以插件形式支持更多音视频处理方面的功能，比如 autosub\n-  [ ] 更多批下载支持（UP 主、收藏夹等）\n-  [ ] 编写测试\n-  [ ] 等等等等，以及\n-  [ ] 更加可爱～\n\n## 参考\n\n-  基本结构：<https://github.com/SigureMo/bilili>\n-  协程下载：<https://github.com/changmenseng/AsyncBilibiliDownloader>\n-  弹幕转换：<https://github.com/ShigureLab/biliass>\n-  样式设计：<https://github.com/willmcgugan/rich>\n\n## 参与贡献\n\n请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)\n',
    'author': 'Nyakku Shigure',
    'author_email': 'sigure.qaq@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SigureMo/yutto',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9.0,<4.0.0',
}


setup(**setup_kwargs)
