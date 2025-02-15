# 베이스 이미지
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /app

# 필수 패키지 설치
RUN pip install --upgrade pip

# 필요한 파일들 복사
COPY requirements.txt .
RUN pip install -r requirements.txt

# 프로젝트 코드 복사
COPY . .

# 포트 설정
EXPOSE 8000

# 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
