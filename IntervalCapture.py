from PIL import ImageGrab
import time,os



# 캡처 주기 (초 단위)
capture_interval = 600  # 10분 = 10 * 60 초


def create_folder_if_not_exists(folder_path):
    # 폴더가 존재하지 않으면 폴더 생성
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"폴더가 생성되었습니다: {folder_path}")
    else:
        print(f"폴더가 이미 존재합니다: {folder_path}")


while True:
    # 현재 시간을 파일 이름으로 사용하여 캡처 저장
    current_time = time.strftime("%Y-%m-%d___%H-%M-%S")
    current_date = time.strftime("%Y-%m-%d")
    create_folder_if_not_exists(f"./images/{current_date}")


    screenshot = ImageGrab.grab()
    screenshot.save(f"./images/{current_date}/{current_time}.png")  # 저장할 폴더 경로
    
    # 대기 시간 후 다음 캡처를 위해 반복
    time.sleep(capture_interval)