import json

f = open('test.json', 'r')
json_dict = json.load(f)

for x in json_dict:
    #book_page = json_dict[x]['page']

    #if(book_page >= 500):
        print('{0}:{1}'.format(x, json_dict[x]['page']))