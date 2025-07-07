def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def get_num_words():
    text = get_book_text("/home/iceeoverlord/workspace/github.com/ianchisholm24/bookbot/books/frankenstein.txt")
    word_count = len(text.split())
    print(word_count, "words found in the document")

