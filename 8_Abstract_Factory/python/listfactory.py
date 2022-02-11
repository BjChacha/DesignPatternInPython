from factory import Factory, Link, Tray, Page


class ListFactory(Factory):
    
    def create_link(self, caption, url):
        return ListLink(caption, url)

    def create_tray(self, caption):
        return ListTray(caption)

    def create_page(self, title, author):
        return ListPage(title, author)


class ListLink(Link):

    def make_HTML(self):
        return f'  <li><a href="{self._link}">{self._caption}</a></li>\n'


class ListTray(Tray):

    def make_HTML(self):
        buffer = ""
        buffer += "<li>\n"
        buffer += f"{self._caption}\n"
        buffer += "<ul>\n"
        for item in self._tray:
            buffer += item.make_HTML()
        buffer += "</ul>\n"
        buffer += "</li>\n"
        return buffer


class ListPage(Page):

    def make_HTML(self):
        buffer = ""
        buffer += f"<html><head><title>{self._title}</title></head>\n"
        buffer += "<body>\n"
        buffer += f"<h1>{self._title}</h1>\n"
        buffer += "<ul>\n"
        for item in self._content:
            buffer += f"{item.make_HTML()}\n"
        buffer += "</ul>\n"
        buffer += f"<hr><address>{self._author}</address>"
        buffer += "</body></html>\n"
        return buffer


