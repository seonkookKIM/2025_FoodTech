import socket

# 소켓 설정
HOST = '192.168.137.101'  # 로봇 IP
PORT = 20000              # 포트 번호

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 접속
client_socket.connect((HOST, PORT))
print(f"[서버에 접속 성공!!] {HOST}:{PORT}")

valid_cmds = {
    "tos1", "tos2", "egg", "pen1", "pen2",
    "grip1", "grip2", "grip3", "open",
    "once", "home", "q", "exit", "full"
}

try:
    while True:
        # 입력 메시지
        print("========================================")
        print("tos1 = 토스트 1")
        print("tos2 = 토스트 2")
        print("egg = 계란물")
        print("pen1 = 프라이팬 1")
        print("pen2 = 프라이팬 2")
        print("cut = 커팅 도마")
        
        print("grip1 = 조리도구 잡기")
        print("grip2 = 식빵 잡기")
        print("grip3 = 최대 잡기")
        print("open = 그리퍼 오픈")
        print("full = 프로세스 한 사이클")
        print("home = 작업 위치 이동")
        print("q = 종료")
        print("========================================")
        msg = input("명령 입력 : ").strip()

        # 허용 명령어 체크
        if msg not in valid_cmds:
            print(f"[잘못된 명령] {msg} 은(는) 사용할 수 없습니다.")
            continue

        # 로컬 종료 (서버에 'exit'를 보내지 않음)
        if msg.lower() == 'exit':
            break

        # 서버로 명령 전송
        client_socket.send(msg.encode('utf-8'))
        print("[전송 완료] 작업 종료 신호(DONE) 대기 중...")

        # 서버 응답 수신
        data = client_socket.recv(1024)
        if not data:
            print("[서버가 종료되었습니다...]")
            break

        response = data.decode('utf-8')
        print(f"[서버로 부터 받은 메시지는] {response}")

except KeyboardInterrupt:
    print("\n강제로 종료되었습니다")
finally:
    client_socket.close()
    print("클라이언트 종료")
