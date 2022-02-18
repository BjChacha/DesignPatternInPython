from FileTreatMentException import FileTreatMentException
from File import File
from Directory import Directory


def main():
    try:
        print("Making root entries...")
        rootdir = Directory("root")
        bindir = Directory("bin")
        tmpdir = Directory("tmp")
        usrdir = Directory("usr")
        rootdir.add(bindir)
        rootdir.add(tmpdir)
        rootdir.add(usrdir)
        
        bindir.add(File("vi", 10000))
        bindir.add(File("latex", 20000))
        rootdir.print_list()

        print("")
        print("Making user entries...")
        yuki = Directory("yuki")
        hanako = Directory("hanako")
        tomura = Directory("tomura")
        usrdir.add(yuki)
        usrdir.add(hanako)
        usrdir.add(tomura)
        yuki.add(File("diary.html", 100))
        yuki.add(File("Composite.java", 200))
        hanako.add(File("memo.tex", 300))
        tomura.add(File("game.doc", 400))
        tomura.add(File("junk.html", 500))
        rootdir.print_list()
    except FileTreatMentException as e:
        print(e)

if __name__ == "__main__":
    main()