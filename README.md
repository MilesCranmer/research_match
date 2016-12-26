# research_match
Sorts a list of names by research interest. Good for conferences.

# Required packages
- [ads](https://github.com/andycasey/ads)
    - Note: install from source, not from pip. The pip version gave me issues for lazy-loading attributes (see [here](https://github.com/andycasey/ads/issues/77)).
    - You also need the access token for the ADS API. Good instructions/examples are on the linked repo.
    
# Usage

- Put all names in a text file, say `names.txt`, one name per line, first name before last, space separated. For example:
```
Carl Sagan
Donald Knuth
Ada Lovelace
...
```
- Download the abstracts using `download.py`. The first argument is the location of the names file, the second is the folder to store the abstracts, and the third arguments is the number of abstracts to download per author (most recent). For example:
```bash
python download.py names.txt ./abstracts 10
```
- Search the abstracts by keyword. You can use `match.py` to do this. The first argument is the folder of the abstracts, and the next arguments are keywords (AND). They keywords are put into a regex, so can be regex themselves. For example:
```bash
python match.py ./abstracts GPU
```
This searches for participants who have done research with GPUs.

or, for example,
```bash
python match.py ./abstracts "(GPU|pulsar)"
```
This will print out a list of people who have done research with GPUs OR have done research with pulsars. 

You can make up more combinations [here](https://regex101.com/). Don't forget to include the quotation marks on regex arguments when running `match.py`.
