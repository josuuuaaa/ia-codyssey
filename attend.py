# attend.py
# 스터디 출석부 - 표준 라이브러리만 사용

import csv
import os
from datetime import datetime

# 출석 기록을 저장할 파일 이름
DATA_FILE = "attendance.csv"


def load_attendance():
    """CSV 파일에서 출석 기록을 읽어 리스트로 반환"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def save_attendance(date, name):
    """출석 한 건을 CSV 파일 끝에 추가"""
    # 파일이 없으면 헤더부터 쓴다
    file_exists = os.path.exists(DATA_FILE)
    with open(DATA_FILE, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "name"])   # 헤더
        writer.writerow([date, name])


def add_record():
    """사용자에게 날짜·이름을 받아 저장"""
    date = input("날짜 (YYYY-MM-DD, 비우면 오늘): ").strip()
    if date == "":
        date = datetime.today().strftime("%Y-%m-%d")
    else:
        # 날짜 형식 검증
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("⚠️  날짜 형식이 올바르지 않습니다. 예: 2025-01-15")
            return

    name = input("이름: ").strip()
    if name == "":
        print("⚠️  이름은 비울 수 없습니다.")
        return

    save_attendance(date, name)
    print(f"✅ 저장되었습니다: {date} / {name}")


def show_list():
    """저장된 출석 기록을 모두 출력"""
    records = load_attendance()
    if not records:
        print("아직 출석 기록이 없습니다.")
        return

    print("\n--- 출석 목록 ---")
    print(f"{'날짜':<12} {'이름'}")
    print("-" * 25)
    for r in records:
        print(f"{r['date']:<12} {r['name']}")
    print(f"총 {len(records)}건\n")


def main():
    while True:
        print("\n=== 스터디 출석부 ===")
        print("1. 출석 기록")
        print("2. 출석 목록 보기")
        print("3. 종료")
        choice = input("선택: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            show_list()
        elif choice == "3":
            print("종료합니다. 수고하셨습니다!")
            break
        else:
            print("1, 2, 3 중에서 골라 주세요.")


if __name__ == "__main__":
    main()
