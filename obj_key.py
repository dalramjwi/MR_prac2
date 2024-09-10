import json

def extract_keys(data, keys=None):
    if keys is None:
        keys = []

    # 데이터 타입이 배열 또는 객체인지 판별
    if isinstance(data, dict):
        for key, value in data.items():
            keys.append(key)
            if isinstance(value, (dict, list)):
                extract_keys(value, keys)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                extract_keys(item, keys)

    return keys

# 데이터를 json으로 저장
def save_keys_to_file(keys, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(keys, file, ensure_ascii=False)

# 테스트 데이터
data = {
    "교통비": 5000,
    "생활비": {
        "교통비": 3000,
        "음식비": 2000
    },
    "기타비용": [1000, {"교통비": 1500}]
}

keys = extract_keys(data)
save_keys_to_file(keys, "keys_output.json")