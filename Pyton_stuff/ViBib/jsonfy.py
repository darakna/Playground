import json
def get_filelines():
    filehandler = open("test_carti_all.log", "r")
    linereader = filehandler.readlines()
    print("Read %s lines" % len(linereader))
    return linereader
def create_json():
    elements = get_filelines()
    current_arch = ""
    id=0
    json_data_string = "{\"Books\": ["
    for elem in elements:
        if elem.startswith("./Cole"):
            current_arch=elem[2:-1]
        else:
            print(elem)
            if "–" in elem:
                first_split = elem.split("–", 1)
            elif "-" in elem:
                first_split = elem.split("-", 1)
            else:
                first_split = (elem.split("{", 1)[0] + "-" + elem).split("-", 1)
                print(first_split)
            author = first_split[0]
            second_split = first_split[1].split("{", 1)
            title = second_split[0][:-1]
            third_split = second_split[1].split("}", 1)
            genre = third_split[0]
            json_data_string += "{\"Name\": \"" \
            + author \
            + "\", \"Title\": \"" \
            +  title \
            + "\", \"Category\": \"" \
            + genre + "\",\"Path\": \"" \
            + elem.replace("\"", "\\\"")[:-1] + "\","\
            + "\"Archive\": \"" + current_arch + "\"},"
            #print("ID: %s\nNume: %s\nTitlu: %s\nCategorie: %s\nPath: %s" %(id, author, title, genre, elem))
            id+=1
    json_data_string = json_data_string[:-1] + "]}"
    #print(json_data_string)
    #print(json.dumps(json_data_string, indent=4, ensure_ascii=False))
    #json_object = json.loads(json_data_string)
    python_dictionary = json.loads(json_data_string)
    print("Converted %s values" % len(python_dictionary['Books']))
    with open('json_data.json', 'w') as outfile:
        json.dump(python_dictionary, outfile, indent=4, ensure_ascii=False)
            
        
create_json()