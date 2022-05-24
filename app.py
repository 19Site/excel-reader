import json as Json;

import pandas as Pandas;

import re as Regex;

###
# main
#
def main():

    # all files
    files = ['a', 'b', 'c', 'd'];

    # each file
    for i in files:

        # read excel
        excel = Pandas.read_excel('./files/' + i + '.xlsx', sheet_name=None);

        # each excel sheet
        for sheetName in excel:

            # regex
            regex = Regex.compile('^.*(\d)樓$');

            # result
            r = regex.match(sheetName);

            # match
            if r != None:

                # dataframe
                df = excel[sheetName];

                # row count
                rowCount = len(df.index);

                # get floor
                floor = r.group(1);

                # print name
                # print('{} -- {}'.format(sheetName, rowCount));

                # each row
                for j in range(rowCount):

                    # update floor name
                    df.iat[j, 6] = '{}F'.format(floor);

                    # column count
                    columnCount = len(df.columns);

                    # column count error
                    if columnCount != 16:

                        # throw exception
                        raise Exception('column count error');

                    # each columns
                    for k in range(columnCount):

                        # cell value
                        cellValue = df.iat[j, k];

                        # check is string type
                        if type(cellValue) is str:

                            # replace all
                            df.iat[j, k] = Regex.sub('(^\s+|\s+)$', '', Regex.sub('[\r\n\t]', '', cellValue));
                
                # extract floor from sheet name
                fileName = 'x-{}-{}f.csv'.format(i, floor);

                # to excel
                df.to_csv('./files/' + fileName, header=False, index=False);

# execute main
main();