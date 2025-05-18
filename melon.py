# 필요한 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup

# 브라우저인 척 위장해서 요청을 보낼 때 사용할 헤더 정보 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# 멜론 차트 페이지에 HTTP GET 요청을 보냄
data = requests.get('https://www.melon.com/chart/', headers=headers)

# 받은 HTML을 BeautifulSoup으로 파싱 (HTML 문서 구조를 분석함)
soup = BeautifulSoup(data.text, 'html.parser')

# 파싱된 전체 HTML 문서를 출력해 봄 (디버깅용)
# print(soup)

# 멜론 차트 1위 곡 제목 요소 하나를 선택
# title = soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')

# 선택된 요소 출력 (HTML 태그 자체가 출력됨)
# print(title)

# 해당 곡의 제목 텍스트만 출력
# print(title.text)

# 1~50위 곡 정보 중, 각 곡의 div 부분을 모두 선택 (단, 여기선 100위까지는 안 가져옴)
top_100 = soup.select('#lst50 > td > div')

# 선택된 곡 div들을 하나씩 반복 처리
for tr in top_100:
    # 순위 정보가 담긴 span.rank 요소 선택
    rank = tr.select_one('span.rank')

    # 순위 정보가 있다면 출력 (줄 바꿈 없이 . 붙여서 출력)
    if rank is not None:
        print(rank.text, end=". ")

    # 곡 제목 요소 선택
    title = tr.select_one('div > div.ellipsis.rank01 > span > a')

    # 곡 제목이 있을 경우에만 아래 코드 실행
    if title is not None:
        # 아티스트 정보 추출
        artist = tr.select_one('div.ellipsis.rank02 > a').text

        # "아티스트 - 곡 제목" 형식으로 출력
        print(artist, '-', title.text)