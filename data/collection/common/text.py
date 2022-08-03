
import re


__g_colours: "set[str]" = set()

colour_tag_reg = re.compile(r'<color=#([0-9a-fA-F]{6}[0-9a-fA-F]{2}?)>')
def clearFormat(text: str) :
    res = text.replace('</color>', '').replace('\\n', '\n')
    search_colours = colour_tag_reg.findall(res)
    if len(search_colours) > 0 :
        for col in search_colours :
            __g_colours.add(col)
        res = colour_tag_reg.sub('', res)
    return res


def getAutoColours() -> "list[str]" :
    res = [
        x[:-2] if len(x) > 6 else x
        for x in __g_colours
    ]
    res.sort()
    return res
