from file_read import file_read
from Search.search import SimpleSearch, BM

def main():
    print(file_read.file_read("dog.txt"))
    simple = SimpleSearch("abcabcababcaba","abcaba")
    simple.search()
    bm = BM("abcabcababcaba","abcaba")
    bm.search()

if __name__ == "__main__":
    main()