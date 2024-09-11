import json
import os
import ollama

# LLaMA 모델을 호출하는 함수
def run(prompt):
    client = ollama.Client()
    response = client.generate(model="llama3.1:8b", prompt=prompt)
    return response

# 파일에서 키 값 읽기
def read_keys_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        keys = json.load(file)
    return keys

# 파일 경로 설정 및 키 읽기
current_dir = os.path.dirname(os.path.abspath(__file__))
keys_file_path = os.path.join(current_dir, "keys_output.json")
keys = read_keys_from_file(keys_file_path)

# Ollama에 가중치를 판별할 프롬프트 생성
key_weight_prompts = []
for key in keys:
    prompt = f"Assign a weight to the following key based on importance: {key}"
    key_weight_prompts.append(prompt)

# 각 키에 대해 Ollama 모델로 가중치 판별
weights = {}
for prompt in key_weight_prompts:
    response = run(prompt)
    weights[prompt] = response['response']  # Ollama 응답에서 가중치 추출

# 결과를 파일로 저장할 경로 설정 (UTF-8 인코딩 지정)
output_file_path = os.path.join(current_dir, "key_weights.json")

# 가중치를 파일로 저장
with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(weights, output_file, ensure_ascii=False)

print(f"키에 대한 가중치가 '{output_file_path}' 파일에 저장되었습니다.")
