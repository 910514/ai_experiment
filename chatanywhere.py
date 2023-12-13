import openai
from datetime import datetime

# openai.log = "debug"
openai.api_key = "sk-"
openai.api_base = "https://api.chatanywhere.com.cn/v1"

file_path = 'output_api.txt'

#read timestamps.txt
with open('timestamps.txt', 'r') as file:
    # Step 3: Read the content of the file into a variable
    timestamps = file.read()

#read pop12h.txt
with open('pop12h.txt', 'r') as file:
    # Step 3: Read the content of the file into a variable
    pop12h = file.read()

#read average_temp.txt
with open('average_temp.txt', 'r') as file:
    # Step 3: Read the content of the file into a variable
    average_temp = file.read()

#read MaxAT.txt
with open('MaxAT.txt', 'r') as file:
    # Step 3: Read the content of the file into a variable
    MaxAT = file.read()

with open('timestamps.txt', 'r') as file:
    # Step 3: Read the content of the file into a variable
    timestamps = file.read()

# 獲取當前時間
current_time = datetime.now()

# 以字符串形式打印當前時間
print("當前時間:", current_time)

# 如果你想要特定格式的時間字符串，可以使用strftime函數
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

prompt = "現在你是氣象主播，請根據現在時間說明當前的天氣狀況並報導明後兩天的天氣情況，" + "現在時間為" + formatted_time + "，這是時間戳，" + timestamps + "，這是降雨機率，" + pop12h + "，這是平均溫度，" + average_temp + "，這是最大體感溫度，" + MaxAT + "最後，請畫一張表格顯示天氣狀況"

def gpt_35_api_stream(messages: list):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
        api_key (str): OpenAI API 密钥

    Returns:
        tuple: (results, error_desc)
    """
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            stream=True,
        )
        completion = {'role': '', 'content': ''}
        for event in response:
            if event['choices'][0]['finish_reason'] == 'stop':
                print(f'收到的完成数据: {completion}')
                break
            for delta_k, delta_v in event['choices'][0]['delta'].items():
                #print(f'流响应数据: {delta_k} = {delta_v}')
                completion[delta_k] += delta_v
        messages.append(completion)  # 直接在传入参数 messages 中追加消息
        return (True, '')
    except Exception as err:
        return (False, f'OpenAI API 异常: {err}')

if __name__ == '__main__':
    messages = [{'role': 'user','content': prompt},]
    print(gpt_35_api_stream(messages))
    print(messages)

messages_str = str(messages)
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(messages_str)