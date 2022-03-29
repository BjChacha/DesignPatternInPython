from sqlite3 import paramstyle
from Database import Database
from HtmlWriter import HtmlWriter

class PageMaker:

    @staticmethod
    def make_welcome_page(mailaddr, filename):
        try:
            mailprop = Database.get_properties('maildata')
            username = mailprop[mailaddr]
            writer = HtmlWriter(open(f'15_Facade\\python\\{filename}', 'w+', encoding='utf-8'))
            writer.title(f'Welcome to {username}\'s page!')
            writer.paragraph(f'{username} 欢迎来到 {username} 的主页。')
            writer.paragraph('等着你的邮件哦！')
            writer.mailto(mailaddr, username)
            writer.close()
            print(f'{filename} is created for {mailaddr} ({username})')
        except:
            print('Something wrong.')