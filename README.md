# WorkPlate-AI
WorkPlate AI 파트 입니다.

# 실행
1. 필요 모듈 설치
    ```shell
    pip install -r requirement.txt
    ```
2. 환경 변수 설정
    ```shell
    export OPENAI_API_KEY="<api_key>"
    ```
3. config/secret.py 파일 생성
    ```py
    DATABASE_URL="mysql+pymysql://<username>:<password>@<host>:<port>/<database>"
    ```
3. 서버 실행
    ```shell
    fastapi run
    ```
