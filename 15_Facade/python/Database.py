class Database:

    @staticmethod
    def get_properties(dbname):
        filename = f'15_Facade\\python\\{dbname}.txt'
        content = {}
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    key, value = line.split('=')
                    content[key] = value[:-1]
            return content
        except:
            print(f'Warning: {filename} is not found.')