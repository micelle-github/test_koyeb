import os
#from dotenv import load_dotenv

print("Hello!")
#load_dotenv()  # .envファイルを読み込む
token = os.environ.get('KOYEB_REGION')

print(f"token:{token}")
print(token)
print(f"token_type:{type(token)}")
