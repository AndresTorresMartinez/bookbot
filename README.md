# BookBot
> **Note:** This is my first project for boot.dev.

BookBot is a simple Python project that analyzes text files (books) to provide word and character statistics.

## Features

- Counts the total number of words in a book.
- Counts the frequency of each character (case-insensitive).
- Displays character counts sorted by frequency.

## Usage

Run the following command in your terminal:

```sh
python main.py <path_to_book>
```

Replace `<path_to_book>` with the path to your text file.

## Example Output

```
============ BOOKBOT ============
Analyzing book found at books/sample.txt...
----------- Word Count ----------
Found 12345 total words
--------- Character Count -------
e: 1500
t: 1200
a: 1100
...
```

## Files

- `main.py`: Main script to run the analysis.
- `stats.py`: Contains functions for word and character statistics.