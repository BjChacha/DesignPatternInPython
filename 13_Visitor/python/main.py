from typing import List
from File import File
from Directory import Directory
from ListVisitor import ListVisitor
from MyVisitor import MyVisitor
from FileTreatMentException import FileTreatMentException

def main():
    try:
        print('Making root entries...')
        rootdir = Directory('root')
        bindir = Directory('bin')
        tmpdir = Directory('tmp')
        usrdir = Directory('usr')
        rootdir.add(bindir)
        rootdir.add(tmpdir)
        rootdir.add(usrdir)
        bindir.add(File("vi", 10000))
        bindir.add(File('latex', 20000))
        rootdir.accept(ListVisitor())

        print('')
        print('Making user entries...')
        yuki = Directory('yuki')
        hanako = Directory('hanako')
        tomura = Directory('tomura')
        usrdir.add(yuki)
        usrdir.add(hanako)
        usrdir.add(tomura)
        yuki.add(File('diary.html', 100))
        yuki.add(File('Compisite.java', 200))
        hanako.add(File('memo.tex', 300))
        tomura.add(File('game.doc', 400))
        tomura.add(File('junk.mail', 500))
        rootdir.accept(MyVisitor())

    except FileTreatMentException as e:
        print(e)

if __name__ == '__main__':
    main()