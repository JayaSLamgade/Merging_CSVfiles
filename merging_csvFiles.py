import os
import glob
import pandas as pd
os.chdir("/Users/jsl/Desktop/CSVData")

extention = "csv"
all_filenames = [i for i in glob.glob('*.{}'.format(extention))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

'''
you need to activate enviroment to run this file and make sure you have pandas 
in you active enviroment.
'''