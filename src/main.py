import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VkBot
import key


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,'random_id': random.randint(0, 2048)})


token = key._token  #здесь должен быть ваш токен от вк сообщества, добавьте его в файле key.py

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)

print("Server started")

game = False

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by: {event.user_id} ', end='')
            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))
            if event.text == 'игра':
                game = True
            print('Text: ', event.text)


