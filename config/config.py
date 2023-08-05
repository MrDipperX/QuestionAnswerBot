from environs import Env

env = Env()
env.read_env()

TOKEN = env.str('TOKEN')
CHAT_ID = env.str('CHAT_ID')
