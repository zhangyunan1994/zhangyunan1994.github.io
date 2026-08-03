#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将 docs 下的 md 笔记转换为静态 HTML（仅标准库，无外部依赖）。

用法：修改 docs/ 下的 md 后执行  python3 tools/md2html.py
"""

import html
import os
import re
import shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV = [
    ("首页", "/"),
    ("一千零一夜", "/jottings/"),
    ("Java 8", "/java8/"),
    ("Java 21", "/java21/"),
    ("Java 混合编程", "/java-mix/"),
    ("Go", "/go/"),
]

SIDEBARS = {
    "jottings": {
        "title": "一千零一夜",
        "items": [
            ("随便写的", "/jottings/"),
            ("第一夜 总纲", "/jottings/01.html"),
            ("第二夜 编程伊始", "/jottings/02.html"),
            ("第三夜 十三信徒", "/jottings/03.html"),
            ("第四夜 初入峰鸟", "/jottings/04.html"),
            ("第五夜 宿舍趣事", "/jottings/05.html"),
            ("第六夜 大学前夕", "/jottings/06.html"),
            ("第七夜 连标题都是谎言", "/jottings/07.html"),
            ("第八夜 第一桶金", "/jottings/08.html"),
            ("第九夜 我的信条", "/jottings/09.html"),
            ("第十夜 自律下的自由", "/jottings/10.html"),
            ("第十一夜 我梦见你离开", "/jottings/11.html"),
            ("第十二夜 我的故事一直有你们", "/jottings/12.html"),
        ],
    },
    "java8": {
        "title": "Java 8",
        "items": [
            ("概述", "/java8/"),
            ("时间相关", "/java8/date.html"),
            ("lambda", "/java8/lambda.html"),
            ("Stream", "/java8/stream.html"),
        ],
    },
    "java21": {
        "title": "Java 21",
        "items": [
            ("概述", "/java21/"),
            ("虚拟线程 Virtual Threads", "/java21/virtual-threads.html"),
        ],
    },
    "java-mix": {
        "title": "Java 混合编程",
        "items": [
            ("概述", "/java-mix/"),
            ("Groovy", "/java-mix/groovy.html"),
            ("Kotlin", "/java-mix/kotlin.html"),
        ],
    },
    "go": {
        "title": "Go",
        "items": [
            ("Gin 解决跨域问题跨域配置", "/go/"),
        ],
    },
}

# VitePress 路径 -> 静态 HTML 路径
LINK_MAP = {
    "/jottings/README": "/jottings/",
    "/jottings/01 第一夜 总纲": "/jottings/01.html",
    "/jottings/02 第二夜 编程伊始": "/jottings/02.html",
    "/jottings/03 第三夜 十三信徒": "/jottings/03.html",
    "/jottings/04 第四夜 初入峰鸟": "/jottings/04.html",
    "/jottings/05 第五夜 宿舍趣事": "/jottings/05.html",
    "/jottings/06 第六夜 大学前夕": "/jottings/06.html",
    "/jottings/07 第七夜 连标题都是谎言": "/jottings/07.html",
    "/jottings/08 第八夜 第一桶金": "/jottings/08.html",
    "/jottings/09 第九夜 我的信条": "/jottings/09.html",
    "/jottings/10 第十夜 自律下的自由 辞别 2020 计划 2021": "/jottings/10.html",
    "/jottings/11 第十一夜 我梦见你离开": "/jottings/11.html",
    "/jottings/12 第十二夜 我的故事一直有你们": "/jottings/12.html",
    "/java8/index": "/java8/",
    "/java8/Date": "/java8/date.html",
    "/java8/lambda": "/java8/lambda.html",
    "/java8/Stream": "/java8/stream.html",
    "/java21/index": "/java21/",
    "/java21/Virtual Threads": "/java21/virtual-threads.html",
    "/javaMix/README": "/java-mix/",
    "/javaMix/Groovy": "/java-mix/groovy.html",
    "/javaMix/Kotlin": "/java-mix/kotlin.html",
    "/go/Gin 解决跨域问题跨域配置": "/go/",
}


def rewrite_href(url):
    if url.startswith("http") or url.startswith("#") or url.startswith("mailto:"):
        return url
    if url.startswith("./"):
        url = url[1:]
    if url.startswith("/"):
        return LINK_MAP.get(url, url)
    return url


def inline(text):
    text = html.escape(text)

    def img(m):
        alt = html.escape(m.group(1))
        src = rewrite_href(html.escape(m.group(2)))
        return f'<img src="{src}" alt="{alt}" loading="lazy">'

    def link(m):
        text_ = m.group(1)
        href = rewrite_href(m.group(2))
        if href.startswith("/") or href.startswith("http"):
            return f'<a href="{href}">{text_}</a>'
        return text_

    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", img, text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def split_fence(lines):
    blocks, cur, in_fence = [], [], False
    for line in lines:
        if line.strip().startswith("```"):
            if in_fence:
                blocks.append((True, cur))
                cur, in_fence = [], False
            else:
                if cur:
                    blocks.append((False, cur))
                cur, in_fence = [], True
        else:
            cur.append(line)
    if cur:
        blocks.append((True if in_fence else False, cur))
    return blocks


def md_to_html(md):
    html_parts = []
    for is_code, lines in split_fence(md.splitlines()):
        if is_code:
            code = html.escape("\n".join(lines)).rstrip()
            html_parts.append(f"<pre><code>{code}\n</code></pre>")
            continue

        i, n = 0, len(lines)
        while i < n:
            line = lines[i]
            stripped = line.strip()

            if not stripped or stripped == "[TOC]":
                i += 1
                continue

            if stripped in ("---", "***"):
                html_parts.append("<hr>")
                i += 1
                continue

            m = re.match(r"^(#{1,6})\s+(.*)$", line)
            if m:
                level = len(m.group(1))
                html_parts.append(f"<h{level}>{inline(m.group(2).strip())}</h{level}>")
                i += 1
                continue

            if stripped.startswith(">"):
                quote, j = [], i
                while j < n and lines[j].strip().startswith(">"):
                    quote.append(lines[j].strip()[1:].strip())
                    j += 1
                content = "<br>".join(inline(q) for q in quote if q)
                html_parts.append(f"<blockquote><p>{content}</p></blockquote>")
                i = j
                continue

            if stripped.startswith("|") and stripped.endswith("|"):
                rows, j = [], i
                while j < n and lines[j].strip().startswith("|"):
                    rows.append(lines[j].strip())
                    j += 1
                cells = lambda r: [c.strip() for c in r.strip("|").split("|")]
                is_sep = lambda r: all(re.fullmatch(r":?-{2,}:?", c) for c in cells(r))
                header = cells(rows[0])
                body = [cells(r) for r in rows[1:] if not is_sep(r)]
                table = ["<table>", "<thead><tr>"]
                table += [f"<th>{inline(c)}</th>" for c in header]
                table += ["</tr></thead><tbody>"]
                for row in body:
                    table.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
                table.append("</tbody></table>")
                html_parts.append("".join(table))
                i = j
                continue

            if re.match(r"^\s*[-*+]\s+", line) or re.match(r"^\s*\d+[.、]\s+", line):
                ordered = bool(re.match(r"^\s*\d+[.、]\s+", line))
                tag = "ol" if ordered else "ul"
                items, j = [], i
                while j < n:
                    s = lines[j].strip()
                    if ordered and re.match(r"^\d+[.、]\s+", s):
                        items.append(inline(re.sub(r"^\d+[.、]\s+", "", s)))
                    elif not ordered and re.match(r"^[-*+]\s+", s):
                        items.append(inline(re.sub(r"^[-*+]\s+", "", s)))
                    else:
                        break
                    j += 1
                html_parts.append(f"<{tag}>" + "".join(f"<li>{it}</li>" for it in items) + f"</{tag}>")
                i = j
                continue

            para, j = [], i
            while j < n and lines[j].strip():
                if re.match(r"^```", lines[j].strip()):
                    break
                para.append(lines[j].strip())
                j += 1
            html_parts.append(f"<p>{inline(' '.join(para))}</p>")
            i = j

    return "\n".join(html_parts)


def page_template(title, section, content_html, active_link=""):
    if section:
        sb = SIDEBARS[section]
        items = "".join(
            f'        <li><a href="{link}"{" class=\"active\"" if link == active_link else ""}>{text}</a></li>\n'
            for text, link in sb["items"]
        )
        sidebar = f"""
    <aside class="sidebar">
      <div class="sidebar-title">{sb['title']}</div>
      <ul>
{items}      </ul>
    </aside>"""
    else:
        sidebar = ""

    nav_html = "\n".join(
        f'      <a href="{link}"{" class=\"active\"" if link == active_link else ""}>{text}</a>'
        for text, link in NAV
    )

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | 张瑀楠</title>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="nav">
  <div class="nav-inner">
    <a class="brand" href="/">张瑀楠</a>
    <nav class="nav-links">
{nav_html}
    </nav>
  </div>
</header>
<div class="layout">
{sidebar}
  <main class="content">
{content_html}
  </main>
</div>
<footer class="footer">
  <p>© 2023-present zhangyunan · 骑摩托不会堵车</p>
</footer>
</body>
</html>
"""


def convert(src, out, section):
    md_path = os.path.join(BASE, src)
    md = open(md_path, encoding="utf-8").read()
    m = re.search(r"^#\s+(.+)$", md, re.M)
    title = m.group(1).strip() if m else "笔记"
    active = out.replace("index.html", "")
    html_text = page_template(title, section, md_to_html(md), active_link="/" + active)
    target = os.path.join(BASE, out)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(html_text)
    print(f"  {src} -> {out}")


def main():
    pages = [
        ("docs/jottings/README.md", "jottings/index.html", "jottings"),
        ("docs/jottings/01 第一夜 总纲.md", "jottings/01.html", "jottings"),
        ("docs/jottings/02 第二夜 编程伊始.md", "jottings/02.html", "jottings"),
        ("docs/jottings/03 第三夜 十三信徒.md", "jottings/03.html", "jottings"),
        ("docs/jottings/04 第四夜 初入峰鸟.md", "jottings/04.html", "jottings"),
        ("docs/jottings/05 第五夜 宿舍趣事.md", "jottings/05.html", "jottings"),
        ("docs/jottings/06 第六夜 大学前夕.md", "jottings/06.html", "jottings"),
        ("docs/jottings/07 第七夜 连标题都是谎言.md", "jottings/07.html", "jottings"),
        ("docs/jottings/08 第八夜 第一桶金.md", "jottings/08.html", "jottings"),
        ("docs/jottings/09 第九夜 我的信条.md", "jottings/09.html", "jottings"),
        ("docs/jottings/10 第十夜 自律下的自由 辞别 2020 计划 2021.md", "jottings/10.html", "jottings"),
        ("docs/jottings/11 第十一夜 我梦见你离开.md", "jottings/11.html", "jottings"),
        ("docs/jottings/12 第十二夜 我的故事一直有你们.md", "jottings/12.html", "jottings"),
        ("docs/java8/Date.md", "java8/date.html", "java8"),
        ("docs/java8/lambda.md", "java8/lambda.html", "java8"),
        ("docs/java8/Stream.md", "java8/stream.html", "java8"),
        ("docs/java21/Virtual Threads.md", "java21/virtual-threads.html", "java21"),
        ("docs/javaMix/Groovy.md", "java-mix/groovy.html", "java-mix"),
        ("docs/javaMix/Kotlin.md", "java-mix/kotlin.html", "java-mix"),
        ("docs/go/Gin 解决跨域问题跨域配置.md", "go/index.html", "go"),
    ]
    for src, out, section in pages:
        convert(src, out, section)

    src_img = os.path.join(BASE, "docs/jottings/img")
    dst_img = os.path.join(BASE, "jottings/img")
    if os.path.isdir(src_img):
        shutil.rmtree(dst_img, ignore_errors=True)
        shutil.copytree(src_img, dst_img)
        print(f"  sync img: docs/jottings/img -> jottings/img")


if __name__ == "__main__":
    main()
