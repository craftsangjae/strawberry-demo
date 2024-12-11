# 딸기 병충해 DEMO

## GET STARTED

### 1. 환경 변수 설정하기

`.env` 파일을 아래와 같이 생성하거나, 환경변수를 설정해 주세요.

````bash
SERVING_HOST_URL='http://serving-gateway.example.com'
````

### 2. 프로젝트 실행하기

docker-compose를 이용해서 바로 띄울 수 있습니다. 'http://localhost:8501'로 접속하면 됩니다.


````shell 
docker-compose up
````

## 제안사항

- [ ] : OCR 회전감지 기능 추가
- [ ] : 금액 정보 관계를 파악하여, 잘못된 금액에 대해 보정하는 기능 추가
- [ ] : 단계 별로 OCR 결과를 확인할 수 있도록 기능 추가