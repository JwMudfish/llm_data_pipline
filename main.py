import json


def read_file(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            data = json.load(file)
    elif file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            data = file.read()
    else:
        raise ValueError("Unsupported file format")
    return data



if __name__ == '__main__':
    data_folder = './data/'

    novel_name = 'apple'
    result_dic = read_file(data_folder + f'{novel_name}_result.json')
    
    for chapter in result_dic:
        print(chapter)
        