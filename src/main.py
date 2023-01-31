import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VkBot


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,'random_id': random.randint(0, 2048)})


token = "vk1.a.-WJxdP82ws0bFoy1xEv4CY-8y5yOGSNM2OSGBAQVI2EQhuxOmcYys8Cta7Vfs2sNcKPFLLR3Q2hPG-bdXeS5gPNYZ6cX-5mEYMB7wDklqqP6uSLTBfqlGe8wsEEfd04K516xMbc27KthAo4ophjqhPbm8ZzYSPNUiBxO_X0YzwZ6QR5t1xUAaTSfyWfXhzsNPgM86NR5F8NFSCvnRgsTIQ"
vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)

print("Server started")



for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by: {event.user_id} ', end='')

            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))

            print('Text: ', event.text)
