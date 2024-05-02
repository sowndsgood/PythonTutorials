book={}

book['tom']={
    'name':'tom',
    'address':'1,X Street'
}

book['bob']={
    'name':'bob',
    'address':'2,Y Street'
}

import json
s=json.dumps(book)   #dump method dumps dictionary object to string.
print(s)
with open("d://PyProblems//CodeBasics//book.txt","w") as f:
    f.write(s)