# web-crawler
1. Create virtual env on your windows/MacOS machine using command
        `python -m venv env`
2. Activate virtual environment
    - WINDOWS `env/Scripts/activate`
    - MAC `source env/bin/activate`        
3. Install python packages
        `pip install python`
        `pip install scrapy`
        `pip install pypiwin32`
    you will find all other dependent packages required for the application in the file `requirements.txt`
4. On the activated virtual environment run the below commands to run the program
    `cd Debenhams_Links_Spider`
    `scrapy crawl Debenhams_Links_Spider`
5. The output goes to a file by name `output.txt` where you will find all the links being crawled from the website

Note:
     -- python vesion used 3.6.3
     -- IDE used 'VSCode'
     -- Django version 2.2

'''
    1) we can use `css' selector` to directly go to a particular html tag
    2) we can use `xpath expressions` to transverse inside an html tag to fetch the information
    3) we can use `items.py` to store our data we get from crawling url's
    4) Once you have our crawled data in `items.py` that is step-3, we can enable pipeline to store the data that we get from crawling the url's into a database 
       by enabling `ITEM_PIPELINES` in the `settings.py`
    5) include `logging` for better exception handling
    6) go further inside the links by crawling the links given by scrapying the URL.
