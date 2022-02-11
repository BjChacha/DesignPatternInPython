from factory import Factory, Link, Tray, Page

class TableFactory(Factory):

    def create_link(self, caption, url):
        return TableLink(caption, url)

    def create_tray(self, caption):
        return TableTray(caption)

    def create_page(self, title, author):
        return TablePage(title, author)


class TableLink(Link):
    
    def make_HTML(self):
        return f'<td><a href="{self._link}">{self._caption}</a></td>\n'


class TableTray(Tray):
    def make_HTML(self):
        buffer = ""
        buffer += "<td>"
        buffer += '<table width="100%" border="1"><tr>'
        buffer += f'<td bgcolor="#cccccc" align="center" colspan="{len(self._tray)}"><b>"{self._caption}"</b></td>'
        buffer += "</tr>\n"
        buffer += "<tr>\n"
        for item in self._tray:
            buffer += item.make_HTML()
        buffer += "</tr></table>"
        buffer += "</td>"
        return buffer


class TablePage(Page):
    def make_HTML(self):
        buffer = ""
        buffer += f"<html><head><title>{self._title}</title></head>\n"
        buffer += "<body>\n"
        buffer += f"<h1>{self._title}</h1>"
        buffer += '<table width="80%" border="3">\n'
        for item in self._content:
            buffer += f"<tr>{item.make_HTML()}</tf>"
        buffer += "</table>\n"
        buffer += f"<hr><address>{self._author}</address>"
        buffer += "</body></html>"
        return buffer

