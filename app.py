import glob
import settings


class ReadFiles:

    def read_words(self, path, index):
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                f_contents = f.read().split('\n')
                for lines in f_contents:
                    words = lines.split(' ')
                    for word in words:
                        if word in index:
                            value = str(files.index(name) +1)
                            if value not in index[word]:
                                index[word] = index[word] + "," + str(files.index(name) +1)
                        else:
                            index[word] = str(files.index(name) +1)
        return index


class ExcludeValues:

    def exclude_words(self, index):
        with open(settings.EXCLUDE_FILE_PATH, 'r') as data:
            exclude = data.read().split('\n')
            for word in exclude:
                if word in index:
                    index.pop(word)
            return index


class WriteIndexFile:

    def write_into_file(self, index):
        with open(settings.INDEX_FILE_PATH, 'w') as file:
            file.write("Word : Page Numbers\n" + "-------------------\n")
            for key in sorted(index):
                if ord(list(key)[0]) > 64:
                    file.write(key + " : " + index[key] + "\n")


class CreateIndex:

    def createIndex(self):
        index ={}
        read_file = ReadFiles()
        index = read_file.read_words(settings.BOOK_PATH, index)
        exclude_words = ExcludeValues()
        exclude_words.exclude_words(index)
        create_write_index_file = WriteIndexFile()
        create_write_index_file.write_into_file(index)
        print("check your index file")


obj = CreateIndex()
obj.createIndex()