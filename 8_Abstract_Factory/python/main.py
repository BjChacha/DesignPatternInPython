import sys
from factory import Factory

def main():
    if len(sys.argv) != 3:
        print("Usage: python main class.name.of.ConcreteFactory")
        print("Example 1: python main.py listfactory ListFactory")
        print("Example 2: python main.py tablefactory TableFactory")
        sys.exit(0)
    
    factory = Factory.get_factory(sys.argv[1], sys.argv[2])

    people = factory.create_link("人民日报", "http://www.people.com.cn/")
    gmw = factory.create_link("光明日报", "http://gmw.cn/")

    us_yahoo = factory.create_link("Yahoo!", "http://www.yahoo.com/")
    jp_yahoo = factory.create_link("Yahoo!Japan", "http://yahoo.co.jp/")
    excite = factory.create_link("Excite", "http://excite.com/")
    google = factory.create_link("Google", "http://google.com/")

    tray_news = factory.create_tray("日报")
    tray_news.add(people)
    tray_news.add(gmw)

    tray_yahoo = factory.create_tray("Yahoo!")
    tray_yahoo.add(us_yahoo)
    tray_yahoo.add(jp_yahoo)

    tray_search = factory.create_tray("搜索引擎")
    tray_search.add(tray_yahoo)
    tray_search.add(excite)
    tray_search.add(google)

    page = factory.create_page("LinkPage", "杨文轩")
    page.add(tray_news)
    page.add(tray_search)
    page.output()

if __name__ == '__main__':
    main()