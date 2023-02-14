from bs4 import BeautifulSoup
import requests
import json

def get_db():
    return json.load(open('data.json', encoding="utf-8"))

def change_pos(x):
    with open("pos.json", "rt", encoding="utf-8") as file:
        f = json.load(file)
    f["pos"] = x
    with open("pos.json", "wt", encoding="utf-8") as _file:
        json.dump(f, _file, indent=2)

def get_pos():
    with open("pos.json", "rt") as f:
        x = json.load(f)
        return x["pos"]
data = get_db()

class VkBot:
    @staticmethod
    def _clean_all_tag_from_str(string_line):
        res = string_line[7:]
        res = res.split(' ')
        return res[0] + ' ' + res[1]

    def __init__(self, user_id):
        print("Создан объект бота!")
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._COMMANDS = ["НАЧАТЬ","ИГРА","ПУТЬ","ПОМОЩЬ","РЕСТАРТ"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id" + str(user_id))
        bs = BeautifulSoup(request.text, "html.parser")
        user_name = self._clean_all_tag_from_str(str(bs.findAll("title")[0]))

        return user_name.split()[0]

    def new_message(self, message):
        can_i_go = False
        if message.upper() == self._COMMANDS[0]:
            return f"Привет-привет, {self._USERNAME}!\nДобро пажаловать в мою игру! Введи 'игра' если хочеть начать игру"
        elif message.upper() == self._COMMANDS[4]:
            change_pos(1)
            return f"Добро пожаловать, {self._USERNAME}!\nВы находитесь на центральной площади\nВведите 'путь' чтобы узнать куда вы можете пройти"
        elif message.upper() == self._COMMANDS[3]:
           return ('\n'.join(self._COMMANDS))
        elif str.isnumeric(message.upper()):
            peak_to_go = int(message.upper())
            if peak_to_go <= len(data):
                splitted = data[get_pos()][0]["peaks_i_can_reach"].split()
                for i in range(len(splitted)):
                    if peak_to_go == int(splitted[i]):
                        can_i_go = True
                if can_i_go:
                    change_pos(peak_to_go)
                    return data[get_pos()][1]["infoaboutplace"]
                else:
                    return "Вы не можете попасть на данный этап"
            else:
                return "Вы не можете попасть на данный этап"
        elif message.upper() == self._COMMANDS[1]:
            change_pos(1)
            return f"Добро пожаловать, {self._USERNAME}!\nВы находитесь на центральной площади\nВведите 'путь' чтобы узнать куда вы можете пройти"
        elif message.upper() == self._COMMANDS[2]:
            return f'Сейчас вы можете:\n{data[get_pos()][0]["info"]} \nвведите {data[get_pos()][0]["peaks_i_can_reach"]}'

        else:
            return "Не понимаю о чем вы...\nВведите 'помощь' чтобы узнать что умеет бот"
