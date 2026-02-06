import random
import os
from datetime import datetime

def generate_fortune():
    # 1. 운세 메시지 리스트
    fortunes = [
        "오늘은 운수 대통! 하는 일마다 술술 풀릴 거예요. 🍀",
        "조금은 차분하게 주위를 둘러보는 하루가 좋겠네요. ☕",
        "예상치 못한 곳에서 소중한 인연을 만날지도 몰라요! ✨",
        "오늘은 맛있는 걸 먹으면 행운이 두 배가 됩니다. 🍕",
        "새로운 도전을 시작하기에 아주 완벽한 날이에요! 🚀",
        "말조심! 오늘은 듣는 것에 집중하면 화를 면합니다. 🤫",
        "그동안 고민하던 일이 드디어 해결될 기미가 보여요. ✔️"
    ]
    
    # 2. 행운의 아이템 리스트
    items = ["무선 이어폰", "따뜻한 아메리카노", "노란색 양말", "오래된 동전", "좋아하는 노래", "책 한 권"]

    # 3. 아바타 요소 (Dicebear 픽셀 스타일 - 슈게임 느낌)
    shapes = ["shaggy", "bob", "shortHair", "hat"]
    colors = ["b6e3f4", "c0aede", "d1d4f9", "ffd5dc"] # 파스텔톤 배경

    # 랜덤 뽑기
    my_fortune = random.choice(fortunes)
    my_item = random.choice(items)
    my_shape = random.choice(shapes)
    my_color = random.choice(colors)
    
    # 능력치 (0~100)
    luck_score = random.randint(1, 100)
    
    # Dicebear URL (픽셀 아트 스타일인 'pixel-art' 사용)
    seed = datetime.now().strftime("%Y%m%d") # 하루 동안은 같은 아바타 유지
    avatar_url = f"https://api.dicebear.com/7.x/pixel-art/svg?seed={seed}&backgroundColor={my_color}"

    return avatar_url, my_fortune, my_item, luck_score

def update_readme():
    url, fortune, item, score = generate_fortune()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    readme_content = f"""
# 🔮 오늘의 아바타 운세 보관함

> **매일 오전 9시, 새로운 아바타가 당신의 운세를 점쳐줍니다.**

---

### 👤 오늘의 행운 아바타
![Lucky Avatar]({url})

### 📜 오늘의 운세
**"{fortune}"**

### 🍀 오늘의 데이터
* **행운 지수**: `{score}%`
* **행운의 아이템**: `{item}`

---
⏳ 마지막 업데이트: {now} (KST)
"""
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()