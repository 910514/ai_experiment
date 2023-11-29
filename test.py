from gradio_client import Client

client = Client("http://127.0.0.1:7860/")
result = client.predict(
		[["Hello!",None]],	# Tuple[str | Dict(file: filepath, alt_text: str | None) | None, str | Dict(file: filepath, alt_text: str | None) | None]  in 'parameter_2' Chatbot component
		0.7,	# float (numeric value between 0 and 1) in 'temperature' Slider component
		0.5,	# float (numeric value between 0.5 and 1) in 'top_p' Slider component
		2,	# float (numeric value between 0 and 5) in '上文轮次' Slider component
							api_name="/bot_1"
)
print(result)