
# script: formatter.py
# class: DataframeFormatter, methods:  text_to_df(content):DataFrame, df_to_html(DataFrame):text/html
# this script uses pandas dataframe to format the query output
# content for formatting may come from various sources as JSON, XML, Text/HTML, DataFrame, QuerySet, etc 



# imports for DataframeFormatter
# pandas 
import pandas as pd

# regular expressions
#import re


# this is the main class
class DataframeFormatter:

# takes text as argument and returns a dataframe
# TODO: tweak for all types of content
    def text_to_df(self,content):
        # split the text into list of lines
        lines = content.splitlines()
        # remove lines starting with #, as they are not neededs
        clean_lines = []
        for l in lines:
            if not l.startswith('#'):
                clean_lines.append(l)

        # extract column names from the text
        fields = []
        for l in clean_lines[0].split('\t'):
            fields.append(l)        
        
        rows = []
        for l in clean_lines:
            row = l.split('\t')
            rows.append(row)
        # all rows except first two as they are headers
        rows = rows[2:]
        # create a dictionary from fields and rows being keys and values respectively
        data = dict()
        for row in rows:
            for i in range(len(row)):
                if fields[i] in data.keys():
                    (data[fields[i]]).append(row[i])
                else:
                    data[fields[i]] = [row[i]]
        # convert dict to pandas dataframe
        df = pd.DataFrame.from_dict(data)
        return df


    # takes a dataframe and returns the data formatted in html
    def df_to_html(self, df):
        data_in_html = df.to_html()
        #TODO: format html code for table and add css
        return data_in_html