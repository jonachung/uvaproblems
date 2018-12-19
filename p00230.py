class Book:
    title = " "
    author = " "

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __lt__(self, other):
        if self.author != other.author:
            return self.author < other.author

        return self.title < other.title


def make_book(title, author):
    book = Book(title, author)
    return book


def shelveOneBook(book, shelf):
    insert = False
    if len(shelf) == 0:
        shelf.insert(0, book)
        insert = True
        print("Put " + book.title + " first")
    elif len(shelf) > 0:
        for i in range(len(shelf)):
            if book < shelf[i]:
                shelf.insert(i, book)
                insert = True
                if i == 0:
                    print("Put " + book.title + " first")
                else:
                    print("Put " + book.title + " after " + shelf[i - 1].title)
                break
        if not insert:
            shelf.append(book)
            print("Put " + book.title + " after " + shelf[len(shelf) - 2].title)


def findSecondQuote(line):
    for i in range(1, len(line)):
        if line[i] == '"':
            return i


def getTitleAuthor(line):
    firstIndex = 0
    lastIndex = findSecondQuote(line)
    title = line[firstIndex:lastIndex + 1]
    author = line[lastIndex + 5:len(line)]
    return title, author


def main():
    book = input()
    bookListObjs = []
    while book != "END":
        title, author = getTitleAuthor(book)
        #print(title)
        #print(author)
        bookObject = make_book(title, author)
        bookListObjs.append(bookObject)
        book = input()
    sortedList = sorted(bookListObjs) # main list to use
    #print(sortedList)
    # for i in range(len(sortedList)):
    #     print("Title " + sortedList[i].title)
    #     print("Author " + sortedList[i].author)
    shelf = sortedList.copy()
    #print(shelf)
    command = input()
    returnedBooks = []
    while command != "END":
        commandSteps = command.split(" ", 1)
        step = commandSteps[0]
        if step == "BORROW":
            #do remove stuff
            for i in range(0, len(shelf)):
                if shelf[i].title == commandSteps[1]:
                    #print("I happen")
                    shelf.remove(shelf[i])
                    break
        elif step == "RETURN":
            #do return stuff
            for i in range(0, len(sortedList)):
                if sortedList[i].title == commandSteps[1]:
                    #copyOfList.append(sortedList[i])
                    returnedBooks.append(sortedList[i])
                    break
        else:
            sortedReturnedBooks = sorted(returnedBooks)
            for i in range(len(sortedReturnedBooks)):
                shelveOneBook(sortedReturnedBooks[i], shelf)
            #do shelve stuff
            returnedBooks = []
            print("END")
        command = input()
    #print("END")


main()