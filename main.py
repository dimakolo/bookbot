def count_symbols(string):
    symbol_count={}
    # initialize the alphaber - we will use only alphabet for this statistics
    for char in list(map(chr, range(97, 123))):
        symbol_count[char]=0
    
    for char in string.lower():
        if char in symbol_count:
            symbol_count[char]+=1
    return symbol_count

def sort_on(dict):
    return dict[""]

def main():
    book_path = 'books/frankenstein.txt'
    with open(book_path) as file:
        file_contents = file.read()
        words = file_contents.split()
        print("--- Begin report of "+book_path+" ---")
        print(str(len(words))+" words are in the document")
        print("Here are the symbols in their descending popularity ranking:")
        symbol_counts = count_symbols(file_contents)
        sorted_counts = dict(sorted(symbol_counts.items(), key=lambda x:x[1],reverse=True))
        for symbol in sorted_counts:
            print("Symbol \""+symbol+"\" apeared "+str(sorted_counts[symbol])+" times")

main()