# Convert a book from VitalSource Bookshelf into a PDF
Largely yoinked from here: https://github.com/manhtai/vitalsource-printer

This script simulates clicking through and screenshotting every page of the text, then putting together those images into a single PDF

# Usage:
Install pyautogui and img2pdf

`pip install -r requirements.txt`

Get the coordinates of the top left corner of the page, bottom right corner, and the next button using coord_getter.py:

`python coord_getter.py`

Type the coordinate pairs in the file `coordinfo.txt`, along with the total number of pages, as instructed in the file.

Then open up Bookshelf and the book you want to download, and run:

`python app.py`

Make sure you aren't covering up the screenshot area or next button. Works with multiple monitors. Book will be saved as book.pdf
