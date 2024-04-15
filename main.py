import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data


if __name__ == '__main__':
    data_folder = './data/'

    novel_name = 'apple'
    result_dic = read_json_file(data_folder + f'{novel_name}_result.json')
    
    for chapter in result_dic:
        print(chapter)
        # print(result_dic[chapter])