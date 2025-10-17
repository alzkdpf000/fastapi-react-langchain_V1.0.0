# 주제
> LangChain을 이용해서 지피티에게 물어보면 정보를 출력하게 하는 접근으로 가보자
사용 화면 react로 제작
![](https://velog.velcdn.com/images/alzkdpf000/post/cc7cdf9e-3cb6-44c9-8234-ad93e21dc78d/image.png)

# 사용할 Rag용 데이터

이 프로젝트는 PDF로 사용하겠다
![](https://velog.velcdn.com/images/alzkdpf000/post/e4129d72-5d8b-46b6-a85a-d13ddfcc5fa8/image.png)
![](https://velog.velcdn.com/images/alzkdpf000/post/48b894a4-7839-497a-8210-dce1f3c74d34/image.png)



# 로컬 모델
>먼저 우리가 LLM을 선택해야하는데 이 프로젝트는 Ollama를 다음과 같은 이유로 선택했다.
- 로컬 실행: 대규모 언어 모델의 로컬 실행 가능, 사용자에게 빠르고 효율적인 AI 처리 기능 제공
- 다양한 모델 지원: (Meta)Llama3 , (Mcrosoft)Phi-3 , (Google)Gemma , mixtral, mistral ... 
- 모델 커스터마이징: 자신만의 모델을 자유롭게 커스터마이징하고 제작 가능
- 사용자 친화적인 인터페이스: 도구의 디자인은 사용 편의성을 보장하여 빠르고 번거롭지 않은 설정 가능
- 다양한 시스템 환경 호환성: macOS, Windows, Linux 지원


## 설치하기
해당 [사이트](https://ollama.com/download/mac)에 들어가서 맥 버전으로 다운로드
![](https://velog.velcdn.com/images/alzkdpf000/post/8099a228-921d-4c22-83ae-855b30efa1ba/image.png)
설치가 완료된 후 터미널에서 <code>ollama --version</code>를 입력해서 ![](https://velog.velcdn.com/images/alzkdpf000/post/ed3ba10f-9d57-4b5b-915f-a5fd5507e693/image.png)
위에 처럼 나오면 설치 완료 

[모델 종류 모음](https://ollama.com/search)에 들어가서 본인이 원하는 모델을 선택 이 프로젝트는 **llama3.1:8b**을 선택했습니다.
![](https://velog.velcdn.com/images/alzkdpf000/post/ebaeb803-3ea1-46c8-b236-339094ee54f4/image.png)

모델 선택 후 <code>ollama pull llama3.1:8b</code>을 입력하면 이제 모델을 다운로드 받는다. 만약 바로 실행하고 싶으면 pull 대신 run을 입력해주세요.
모델을 다운로드 받고 나서 <code>ollama list</code>를 입력하면 ![](https://velog.velcdn.com/images/alzkdpf000/post/95d2fd53-304c-487c-bacb-d2f6ce80d3a7/image.png) 지금까지 다운로드 받은 모델들이 다 나옵니다. 이제 이걸 파이썬으로 사용해보자.





# 실행 결과들


![](https://velog.velcdn.com/images/alzkdpf000/post/f04158c4-adfb-43f8-be0a-ff730b1f0616/image.png)
![](https://velog.velcdn.com/images/alzkdpf000/post/e9471c11-2543-421a-bf25-38dae9662ab5/image.png)


## 콘솔 출력 
![](https://velog.velcdn.com/images/alzkdpf000/post/5892c326-db22-4d4a-9e93-8949742b9ddc/image.png)
이런 식으로 어떤 내용을 참고했는지 어디 페이지인지 어떤 pdf를 참고했는지 알려준다.


# 에러 상황들

1. 유튜브와 블로그, 공식 문서를 돌아가면서 작업을 하니 버전이 다르거나 라이브러리가 이동되거나 하는 문제들이 너무 많아 공식 문서에서 찾아가면서 수정해야했다.

2. 마찬가지로 버전이 바뀌면서 메소드가 사라지거나 대체되는 함수들을 찾는 어려움이 존재했다.

3. 전에 파이썬을 공부하면서 너무 많은 설치를 하면서 라이브러리가 꼬여서 삭제하고 다시 깔아도 실행이 안되고 하는 문제가 발생해 가상환경을 새로파서 다시 시작해서 해결했다.
