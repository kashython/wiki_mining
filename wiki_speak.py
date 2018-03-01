'''
    Will take query from user and reply appropriate answer from wikipedia
'''

import sys
import wiki_mining as wm

query = sys.argv[1:]
query = "when is Anil Kapoor's b'day"
print('Query :', query)

wm_object = wm.WikiMining(query=query)

# wm_object.get_wiki_bday("Anil Kapoor")
# wm_object.get_wiki_def("neural networks")
