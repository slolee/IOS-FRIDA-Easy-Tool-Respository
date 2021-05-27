# 프로젝트 소개
IOS FRIDA Easy Tool ([링크](https://github.com/slolee/IOS-FRIDA-Easy-Tool)) 에서 제공하는 파일 탐색기를 이용해 사용자는 작성한 FRIDA Script를 저장하고 관리할 수 있다. 하지만 이는 로컬환경에서만 사용이 가능하고 여러 컴퓨터에서 공유할 수 없다. 따라서 아래 두 가지 목표를 이루고자 IOS Frida Script Center를 제공한다.

- 여러 사용자가 FRIDA Script를 공유할 수 있다.
- 여러 환경에서 작업할 때 FRIDA Script를 백업 및 가져와 사용할 수 있다.
<br></br>

# 사용기술
- <b>Programming Language</b> : Django(Python)
- <b>Database</b> : PostgreSQL
- <b>Etc</b> : Docker, Docker Compose, Bootstrap
<br></br>

![4](https://user-images.githubusercontent.com/38906956/119841719-02760300-bf41-11eb-8724-00188b99b575.png)
<br></br>

# 사용법
> 제공하는 웹 서버는 Script를 백업하거나, 내부에서 협업을 위해 Script를 공유하기 위해 사용할 수 있고, Repository 단위로 Script를 저장한다.

1. Web-server를 실행시킬 PC에 Docker를 설치한다.
2. Web-server.zip 파일을 압축해제하고 cmd창을 이용해 해당 폴더로 이동한다.
3. docker-compose up 명령어를 실행한다.
4. 127.0.0.1:8000 혹은 IP주소:8000 으로 연결해 Web-server에 접속한다.
<br></br>

# 기능소개
사용자는 자신만의 Repository를 추가해 FRIDA Script를 관리할 수 있다. 기본적으로 Admin Repository를 제공해 IOS FRIDA Easy Tool에서 사용되는 Script를 제공한다.

![1](https://user-images.githubusercontent.com/38906956/119841706-0144d600-bf41-11eb-83ee-97be3be1d2b5.png)
![2](https://user-images.githubusercontent.com/38906956/119841712-01dd6c80-bf41-11eb-833a-40af321cdd8a.png)
<br></br>

`Create Post` 버튼을 통해서 FRIDA Script를 추가할 수 있는데, 직접 Modal창에 입력할 수도 있고 이미 작성된 파일을 Drag-and-Drop 형식으로 끌어서 옮길 수도 있다.

![3](https://user-images.githubusercontent.com/38906956/119841715-02760300-bf41-11eb-8e60-a804576152f8.png)

