import telebot

bot = telebot.TeleBot('5151642864:AAGTdxf5DMfxW4ouwECd6WujfM7UmRW_6RQ')


def extract_arg(arg):
    return arg.split()[1]


def extract_arg2(arg2):
    return arg2.split()[2]


@bot.message_handler(commands=['start'])
def start(message):
    start = 'To start SMS Bomber type /bomb number msg count' \
            '\nFor example /bomb +911234567890 60'
    bot.send_message(message.chat.id, start)


@bot.message_handler(commands=['bomb'])
def bomb(message):
    status = extract_arg(message.text)
    status2 = extract_arg2(message.text)
    time_integer = int(status2)
    time = time_integer
    target = status
    from main import sms
    sms(target,time)
    bot.reply_to(message,f'Bomb completed on {target},count of {time}')


bot.polling()
