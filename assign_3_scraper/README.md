Hello.

This project is for scraping election data from portal https://volby.cz
For making csv information with information data, you will need to start election-scraper.py with 2 arguments
1st argument must be web link for district like "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101"
2nd argument must be name of csv file like "./benesow.csv" file name must contain name of file and path where it must be stored.
BOTH arguments must have "" doulbe qoutes signs at the start and at the end of argument.


For starting this script you will need some modules in your environment.
To use requirements.txt you can use command $ pip install -r requirements.txt 

Example of csv file is stored with election-scraper.py

Example how to start scraper:

python ./election-scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "./project_3.csv"

