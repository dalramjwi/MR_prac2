import subprocess

def run_node_script(script_name):
    try:
        # node 명령어를 사용하여 Node.js 스크립트를 실행
        result = subprocess.run(['node', script_name], capture_output=True, text=True, encoding='utf-8')
        print(result.stdout)  # Node.js 스크립트의 출력 내용을 보여줌
        if result.stderr:  # 에러가 발생했을 경우 출력
            print("오류:", result.stderr)
    except FileNotFoundError:
        print("Node.js가 설치되어 있지 않거나 'node' 명령어를 찾을 수 없습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

# 사용자로부터 실행할 Node.js 파일명을 입력받음
script_name = input("실행할 Node.js 파일명을 입력하세요 (예: app.js): ")

# 입력된 파일을 실행
run_node_script(script_name)
