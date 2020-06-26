def sort_list_of_dict(input_list):
  return sorted(input_list, key=lambda x: x['id'])

print(sort_list_of_dict([{'id': 345, 'name':'ABC'}, {'id':432, 'name':'asd'}, {'id':98, 'name':'qwe'}]))
