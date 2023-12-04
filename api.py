from gradio_client import Client

file_path = 'output_api.txt'
client = Client("http://127.0.0.1:7860/")

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

result_string = "請以根据提供的数据，我们可以得出以下结论開頭總結出這幾天的天氣狀況:" + "這是降雨機率" + pop12h + "這是平均溫度" + average_temp + "這是最大體感溫度" + MaxAT

result = client.predict(
    [[result_string, None]],  # Tuple[str | Dict(file: filepath, alt_text: str | None) | None, str | Dict(file: filepath, alt_text: str | None) | None] in 'parameter_2' Chatbot component
    0.95,  # float (numeric value between 0 and 1) in 'temperature' Slider component
    0.5,  # float (numeric value between 0.5 and 1) in 'top_p' Slider component
    3,  # float (numeric value between 0 and 5) in '上文轮次' Slider component
    api_name="/bot"
)
result_str = str(result)
#save the result to output_api.txt
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(result_str)

