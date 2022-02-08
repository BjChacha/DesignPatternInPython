from Builder import Builder

class HTMLBuilder(Builder):

    def __init__(self) -> None:
        self._filename = ""
        self._writer = None

    def make_title(self, title):
        self._filename = f"{title}.html"
        try:
            self._writer = open(self._filename, 'w', encoding='utf8')
        except IOError as e:
            print(f"Cant crate file: {self._filename}")

        self._writer.writelines(f"<html><head><title>{title}</title></head><body>")
        self._writer.writelines(f"<h1>{title}</h1>")
        
    def make_string(self, string):
        self._writer.writelines(f"<p>{string}</p>")

    def make_items(self, items):
        self._writer.writelines("<ul>")
        for item in items:
            self._writer.writelines(f"<li>{item}</li>")
        self._writer.writelines("</ul>")

    def close(self):
        self._writer.writelines("</body></html>")
        self._writer.close()

    def get_result(self):
        return self._filename
