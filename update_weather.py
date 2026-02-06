import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# 지니뮤직 트로트 장르 차트 URL
TROT_URL = "https://www.genie.co.kr/chart/genre?ditc=D&ymd=20240522&genrecode=L0107"
# 크롤링 차단 방지를 위한 헤더 설정
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

README_PATH = "README.md"

def get_trot_ranking():
    """지니뮤직에서 실시간 트로트 순위 TOP 5를 가져옴"""
    try:
        response = requests.get(TROT_URL, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 곡명과 가수 가져오기
        titles = soup.select('a.title.ellipsis')[:5] # 상위 5개
        artists = soup.select('a.artist.ellipsis')[:5]

        ranking_list = []
        for i in range(len(titles)):
            title = titles[i].text.strip()
            artist = artists[i].text.strip()
            ranking_list.append(f"{i+1}위: **{title}** - {artist}")
        
        return "\n".join(ranking_list)
    except Exception as e:
        return f"순위 정보를 가져오는 데 실패했습니다: {e}"

def update_readme():
    """README.md 파일을 업데이트"""
    trot_info = get_trot_ranking()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    readme_content = f"""
# 🎤 Real-time Trot Ranking

이 리포지토리는 지니뮤직 데이터를 활용하여 실시간 트로트 순위를 자동으로 업데이트합니다.

## 🏆 실시간 트로트 TOP 5
{trot_info}

⏳ 업데이트 시간: {now} (KST)

---
자동 업데이트 봇에 의해 관리됩니다.
"""

    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()