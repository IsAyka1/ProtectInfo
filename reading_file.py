import json

def read_from_json():
    dict_users = {}
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        for user in data["users"]:
            login = user['login']
            dict_users[login] = user
        return dict_users


def write_to_json(users):
    with open('data.json', 'w') as json_file:
        dict_users = {'users': []}
        for user in users.values():
            dict_users["users"].append(user)

        json.dump(dict_users, json_file)



if __name__ == '__main__':
    write_to_json({'ADMIN': {"login": "ADMIN", "password": "1234", "is_password_limited": "False", "is_blocked": "False"}})
