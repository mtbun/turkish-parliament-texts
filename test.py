import os
from urllib.request import *
import json


# path = 'TXTs'
# txts = []
# for root, d, files in os.walk(path):
#     for file in files:
#         if '.txt' in file:
#             txts.append(os.path.join(root, file))

collection = 'tbmm'
q          = 'istanbul'
url        = 'http://localhost:8983/solr/' + collection + '/select?q=' + q

connection = urlopen(url)
response = json.load(connection)

print ('number of repeat: ' + str(response['response']['numFound']))