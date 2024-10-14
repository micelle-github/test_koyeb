import os
from dotenv import load_dotenv

print("Hello!")
load_dotenv()  # .envファイルを読み込む
token = os.getenv('DISCORD_TOKEN')

print(f"token:{token}")
print(token)
print(f"token_type:{type(token)}")