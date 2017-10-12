# Research match
Filters a list of names by research interest. This is helpful for finding those with similar interests at a conference, or, say, finding a PhD advisor given a list of faculty and a list of your research interests.

Works by:
- Downloading N recent abstracts from each author in a list of names
- Searching the abstracts for keywords/regular expressions

# Required packages
- [ads](https://github.com/andycasey/ads)
    - Note: install from source, not from pip. The pip version gave me issues for lazy-loading attributes (similar to [here](https://github.com/andycasey/ads/issues/77)).
    - You also need the access token for the ADS API. Good instructions/examples are on the ads repo.
- [Nameparser](http://nameparser.readthedocs.io/en/latest/)
    - Used to parse the list of names
    - Install with, e.g., `pip install nameparser`


# Usage
`0`. Put your ADS access token into the environment variable `ADS_DEV_KEY`, for example:

`export ADS_DEV_KEY=JFJJ38fJ02VZ09JFD...`

`1`. Put all names in a text file, say `names.txt`, one name per line, first name before last, space separated. For example:
```
Carl Sagan
Donald Knuth
Ada Lovelace
...
```
`2`. Download some author abstracts using `download.py`. The first argument is the location of the names file, the second is the folder to store the abstracts, and the third arguments is the number of abstracts to download per author (most recent). For example, the following command downloads 10 abstracts per author into `./abstracts`.
```bash
python download.py names.txt ./abstracts 10
```
`3`. Search the abstracts by keyword. You can use `match.py` to do this. The first argument is the folder of the abstracts, and the next arguments are keywords (AND). They keywords are put into a regex, so can be regex themselves. For example:
```bash
python match.py ./abstracts GPU
```
This searches for participants who have done research with GPUs.

or, for example,
```bash
python match.py ./abstracts GPU "(pulsar|FRB)"
```
This will print out a list of people who have done research with GPUs AND (have done research with pulsars OR FRBs). 

You can make up more regex combinations [here](https://regex101.com/). Don't forget to include the quotation marks on regex arguments when running `match.py`.
