# OfficeAutomation

# 개요
- 지인의 요청으로 2023.06.03 ~ 활용한 업무 반자동화 CLI 프로그램
- Selenium을 이용한 검색 결과 분석, pyautogui를 이용한 반복 작업 자동화
- 국내 브랜드를 알리바바 클라우드에 상표로써 등록을 요청하는 작업
- 동적으로 생성되는 경우가 많아 BS4보다 Selenium 선택

# 목표
1. 대상 브랜드가 알리바바에 등록되지 않은 경우 신규 브랜드로 양식 작성 후 신청
2. 대상 브랜드가 알리바바에 등록되어 있는 경우 기존 브랜드로 양식 작성 후 신청

# 해결 아이디어 - 목표 1
1. Selenium으로 https://tm.aliyun.com/ 에 접속하고 html을 분석하여 검색창 찾기
2. input()을 통해 입력 받은 브랜드명을 검색창에 입력하고 검색
3. 검색 결과가 표시된 후 https://www.naver.com/ 에 접속하여 같은 키워드로 검색
4. 검색 결과중 대상 브랜드가 존재하지 않거나 검색 결과가 없는 경우 대상 브랜드의 상품 판매 페이지를 로고와 함께 캡쳐
5. 홍크 브랜드 운영 플랫폼으로 이동하여 신규 브랜드 탭으로 이동 후 브랜드 명 입력, 국가(대한 민국) 선택, 이미지 등록

# 해결 아이디어 - 목표 2
1. 1~3 동일
2. 검색 결과 화면은 20개까지 표시되므로, 20개 중 몇 번째에 위치하는지 콘솔에 입력하여 해당 요소의 상표 세부 정보로 이동하여 캡쳐 (1페이지에 없는 경우 없다고 가정)
4. 홍크 브랜드 운영 플랫폼으로 이동하여 기존 브랜드 탭에서 브랜드 명, 등록 번호, 상표 소유자명, 상표 세부 정보 캡쳐 이미지 등록

# 제한사항
1. 상표 세부정보 페이지의 봇 탐지 (BS4 접근 불가능)
2. 동일 브랜드인지 비교는 간단한 알고리즘으로는 구현 불가능
3. 웹사이트의 로딩 속도로 인해 예상치 못한 오류 발생 가능성 높음

# 사전 작업
1. 1920*1080 해상도 모니터를 주 모니터로 설정, 화면 왼쪽 절반은 크롬 브라우저 탭 1개 이상 오픈, 오른쪽은 홍크 브랜드 운영 플랫폼 로그인
2. 본 소스코드는 크롬 북마크 탭이 열린 상태로 진행되었음. 환경에 따라 pyautogui.moveTo() 파라미터 값이 다를 수 있음.
