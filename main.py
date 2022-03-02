import requests

def get_names():
    names = ['Hulk', 'Thanos', 'Captain America']
    powerstat_list = []
    for name in names:
        request_url = f'https://www.superheroapi.com/api.php/2619421814940190/search/{name}'
        response = requests.get(request_url)
        name_list = response.json()['results']
        for name_dict in name_list:
            if name_dict['name'] == name:
                powerstats_dict = name_dict['powerstats']
                powerstat = powerstats_dict['intelligence']
                powerstat_list.append(int(powerstat))
    new_zip = dict(zip(names, powerstat_list))
    max_val = max(new_zip.items(), key=lambda x: x[1])
    print(f'Самый умный супергерой - {max_val[0]} с интеллектом {max_val[1]}')

if __name__ == '__main__':
    get_names()
