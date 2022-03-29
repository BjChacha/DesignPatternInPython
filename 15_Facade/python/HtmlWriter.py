class HtmlWriter:

    def __init__(self, writer):
        self._writer = writer

    def title(self,title):
        self._writer.write('<html>')
        self._writer.write('<head>')
        self._writer.write(f'<title>{title}</title>')
        self._writer.write('</head>')
        self._writer.write('<body>\n')
        self._writer.write(f'<h1>{title}</h1>')
    
    def paragraph(self, msg):
        self._writer.write(f'<p>{msg}</p>\n')

    def link(self, href, caption):
        self.paragraph(f'<a href={href}>{caption}</a>')

    def mailto(self, mail, username):
        self.link(f"mailto:{mail}", username)

    def close(self):
        self._writer.write('</body>')
        self._writer.write('</html>\n')
        self._writer.close()
        