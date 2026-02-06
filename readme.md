# 🎤 실시간 트로트 랭킹 (Real-time Trot Ranking)

이 리포지토리는 Python과 GitHub Actions를 사용하여 **지니뮤직의 실시간 트로트 차트**를 자동으로 크롤링하고 업데이트합니다.

## 🏆 현재 트로트 TOP 5
> 데이터를 불러오는 중입니다...

## ⚙️ 주요 기능
- **Web Scraping**: `BeautifulSoup`를 활용한 지니뮤직 차트 데이터 추출
- **Automation**: `GitHub Actions`를 통한 정기적 자동 업데이트 (매일 오전 9시 KST)
- **CI/CD**: 코드 수정 시 즉시 반영 및 README 자동 커밋

## 🛠 사용된 기술
- **Language**: Python 3.9+
- **Library**: `requests`, `BeautifulSoup4`, `python-dotenv`
- **Platform**: GitHub Actions

## 🚀 로컬 실행 방법
1. 저장소 클론:
   ```bash
   git clone [https://github.com/dankim9215-debug/weather-api.git](https://github.com/dankim9215-debug/weather-api.git)