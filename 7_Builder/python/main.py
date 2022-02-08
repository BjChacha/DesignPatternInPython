import sys
from typing import Text
from TextBuilder import TextBuilder
from HTMLBuilder import HTMLBuilder
from Director import Director

def main():
    if len(sys.argv) != 2:
        usage()
        exit(0)
    if sys.argv[1].lower() == 'plain':
        textbuilder = TextBuilder()
        director = Director(textbuilder)
        director.construct()
        result = textbuilder.get_result()
        print(result)
    elif sys.argv[1].lower() == 'html':
        htmlbuilder = HTMLBuilder()
        director = Director(htmlbuilder)
        director.construct()
        filename = htmlbuilder.get_result()
        print(f"{filename} 文件编写完成。")
    else:
        usage()
        exit(0)


def usage():
    print("Usage: python Main plain".ljust(25) + "编写纯文本文档")
    print("Usage: python Main html".ljust(25) + "编写HTML文档")

if __name__ == "__main__":
    main()