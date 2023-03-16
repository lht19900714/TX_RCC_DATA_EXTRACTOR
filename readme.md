# EBCDIC Data Converter

## Description

A Python application is aimed to convert mainframe EBCDIC data into Unicode ASCII delimited text files.

The converter consists of two parts

1. Parser
2. File layouts  
   File layouts are a driver to parse EBCDIC data.  
   File layouts are defined in JSON format. They are created as per manual
   from [rcc website](https://www.rrc.texas.gov/resource-center/research/data-sets-available-for-download/#gas-masters)

## Quick start

1. Install Python 3.6 or higher
2. Install required packages
   ```bash
   pip install -r requirements.txt
   ```
3. Download EBCDIC data
   from [rcc website](https://www.rrc.texas.gov/resource-center/research/data-sets-available-for-download/#gas-masters)
4. Go to `parser` folder and execute specific file(you will find main entry in each file)

some parsed files are located in `out` folder


## Todo
1. Add more layouts
2. Add error handling
3. Add more documentation and comments
4. modify code to be executed from command line


# Reference
* [Reading COBOL Layouts](http://www.3480-3590-data-conversion.com/article-reading-cobol-layouts-1.html)
* [TXRRC_data_harvest](https://github.com/mlbelobraydi/TXRRC_data_harvest)
* [ebcdic-parser](https://github.com/larandvit/ebcdic-parser)
