# research_match
Sorts a list of names by research interest. Good for conferences.

# Required packages
- [ads](https://github.com/andycasey/ads)
    - Note: install from source, not from pip. The pip version gave me issues for lazy-loading attributes (see [here](https://github.com/andycasey/ads/issues/77)).
    - You also need the access token for the ADS API. Good instructions/examples are on the linked repo.
    
# Usage

- Put all names in a text file, say `names.txt`, one name per line, first name before last, space separated.
- Download the abstracts. The first argument is the location of the names file, the second is the folder to store the abstracts, and the third arguments is the number of abstracts to download per author (most recent)
```bash
python download.py names.txt ./abstracts 10
```
- Search the abstracts by keyword
