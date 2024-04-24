# 05_Asynchronous JavaScript

- 비동기


## 비동기

![Alt text](image-125.png)

- 순차적? 앞에 있던 애들이 처리되어야 처리 가능. 동시 진행 불가능

![Alt text](image-126.png)

![Alt text](image-127.png)

![Alt text](image-128.png)

![Alt text](image-129.png)

![Alt text](image-130.png)

![Alt text](image-131.png)


![Alt text](image-132.png)


- 병렬적 수행이 가장 큰 특징


### JS와 비동기

![Alt text](image-133.png)

![Alt text](image-134.png)

- 스레드가 하나기 때문에 실제론 병렬 구조를 사용 못 함
- 그럼 어떻게 비동기?
- > 런타임

![Alt text](image-135.png)

### 브라우저 환경에서 비동기 처리

![Alt text](image-136.png)

> 과정은 강의록 보멵서 다시 확인

- 자바스크립트의 자체 스레드는 콜스택 하나


![Alt text](image-137.png)

![Alt text](image-138.png)

![Alt text](image-139.png)

콜백 함수? 콜 스택으로 돌아와서 이름이 콜백 함수임

![Alt text](image-141.png)


![Alt text](image-142.png)

### ajax

![Alt text](image-143.png)


![Alt text](image-144.png)

> 목적 : 웹페이지를 새로고침 하지 않고도 일부 DOM만 업데이트
>
> 웹 페이지 일부가 다시 로드되는 동안에도 코드가 계속 실행되어, 비동기식으로 작업 할 수 있음

![Alt text](image-145.png)

![Alt text](image-146.png)

![Alt text](image-147.png)

![Alt text](image-148.png)

![Alt text](image-149.png)


### AXIOS

- XHR을 만드는걸 도와주고, 요청도 손쉽게 해주는 라이브러리
- 파이썬의 request와 같은 역할
- 요청 객체를 만들어준다

![Alt text](image-150.png)

![Alt text](image-151.png)

![Alt text](image-152.png)

- 부트스트랩처럼 cdn으로 가져와서 쓴다. 

![Alt text](image-153.png)


```html
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const URL = 'https://api.thecatapi.com/v1/images/search' 

    // 1.
    const promiseObj = axios({
      method : 'get',
      url : URL, // 요청을 어디 서버로 보낼건데
    })
    // response = request.get(URL)를 JS에서 쓴거라 생각
    // 다만 비동기 응답

    console.log(promiseObj)

    promiseObj = then((response) => {
        console.log(response)
    })
    
    // 2.
  </script>
```

![Alt text](image-154.png)
































# offline

- 오늘꺼 엄청 중요
- 오늘꺼 놓치면 최종 pjt 못한다. 

- 오늘 할 것
  1. 동기 비동기
       - 설명 + 예시코드 실행
  2. 이론
     - 브라우저 렌더링 원리
     - 자바스크립트 엔진 및 런타임 동작 원리
  3. 게시판 만들어보기
     - with json-server
     - json-server?
     - 아주 짧은 시간에 REST API를 구축해주는 개발용 라이브러리


## 1. 동기적(synchronous) vs 비동기적(asynchronous)

- 순서대로 일이 마치는가?에 대한 여부
  - a->b->c 순서로 일이 시작되었을 때, 순서대로 끝나면 동기적
  - 즉, 실행 순서와 끝나는 순서가 동일한가에 대한 구분
  - 동시에 작업을 하는가? 는 다른 문제 (Blocking과 Non-Blocking 생각)
- Blocking, Non-Blocking -> 동시 작업에 대한 부분
  - 블로킹? 무언가를 막는다.  -> 프로그래밍에서는 A함수가 실행되고 있을 때 다른 함수는 실행하지 못하도록 막는것 
  - 블로킹은 동시에 작업을 할 수 있는가-> 호출한 함수가 제어권을 계속 가지고 있는가?
    - 가지고 있다면: 다른 함수 호출이 불가.
  - 예시
    - A함수 내에서 B함수 호출
    - B함수가 돌 동안 A 함수가 아무것도 못하면 Blocking
    - A 함수가 자기 일을 동시에 한다면 Non-Blocking
  - 동기인데 Non Blocking일 수도 있고, 비동기인데 Blocking일 수도 있다
-  예시
   -  강사 금기륜이 효준에게 일을 시키고 밥을 먹으러 가고 싶음
      -  강사 입장 : 일을 시킨다, 밥을 먹는다 (두 가지 작업이 존재함)
      -  효준 : 일이 끝나면 강사에게 전화함
        1. 일을 시키고 바로 밥을 먹으러 감
            - 일의 진행과 동시에 밥을 먹는것(Non-Blocking)
            - 1.1 밥을 먹는 중에 일이 끝났다고 전화가 옴 : 실행 순서와 끝나는 순서가 같음 : 동기적 => NonBlocking-Synchronous
            - 1.2 밥을 먹고 와서 일에 대한 결과를 들음  : 실행순서와 끝나는 순서가 다름 : 비동기적 (순서 비보장) => NonBlocking-Asynchronous
        2. 일의 결과를 듣고 밥을 먹으러 가기로 함 
            - 일의 진행과 밥을 먹는게 동시에 일어나지 않음(Blocking)
            - 동시에 처리를 못하니 무조건 끝나는 순서가 보장된다. : 동기적
            - Blocking-Synchronous
 - Blocking Asynchronous는 설계를 일부로 하는 일은 없음-> 개발자의 실수
   -  NonBlocking-Asynchrounous 방식을 쓰다가 그 과정에 하나라도 Blocking 요소가 존재하면 의도치 않게 Blocking-Asynchrounous 가 발생 가능!
-  


```js
// 비동기

// 가장 간단한 비동기 코드

console.log('a')

setTimeout(() => {
    console.log('b')   
}, 1000)

console.log('c')

// a c b


// 동기식으로 만드는 방법
// Promise 객체
// 1. resolve : 성공적인 로직 이행 시 결과값을 전달
// 2. reject : 로직 이행 실패 시 결과값을 전달
// 3. then: 로직 이행 성공 시(resolve() 호출 시) then 으로 넘어감
// 4. catch: 로직 이행 실패 시(reject() 호출 시) catch 로 넘어감

const myPromise = new Promise(function (resolve, reject) {
    console.log('Promise 생성!')
    // 간단한 예시
    let num = 1
    if (num === 0) {
        resolve("num 은 0이다")
    } else {
        reject("num 은 0이 아니다")
    }
})

// Promise 로직 이행 성공 시 then / 실패 시 catch
// Promise 객체에서 resolve() 호출 시 then 으로 넘어온다.
// Promise 객체에서 reject() 호출 시 catch 으로 넘어온다.
myPromise.then((result) => {
    console.log("로직 성공 ! - ", result)
}).catch((error) => {
    console.log("로직 실패 ! - ", error)
})

// ---------------------------------------------
// promise 를 이용해서 a b c 순서대로 호출하기
console.log('a')

// 비동기 코드를 promise 객체 안에 
const myPromise2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log('b')   
        resolve()
    }, 1000)
    // 이렇게하면 a c b 가 호출됨
    // resolve 도 정확한 위치에 넣어주어야 한다!
    // resolve()
})

myPromise2.then(() => {
    console.log('c')
})

// a b c
```

- 웹서비스의 퍼포먼스 탭에서 내 화면이 어떤 과정으로 그려지는지 확인이 가능한다. 

### +) 브라우저 구성 요소


# 이론

## 1. 브라우저의 구성요소
## 2. 브라우저 렌더링 과정


- "https://d2.naver.com/helloworld/59361"

렌더링 엔진
렌더링 엔진의 역할은 요청 받은 내용을 브라우저 화면에 표시하는 일이다.

렌더링 엔진은 HTML 및 XML 문서와 이미지를 표시할 수 있다. 물론 플러그인이나 브라우저 확장 기능을 이용해 PDF와 같은 다른 유형도 표시할 수 있다. 그러나 이 장에서는 HTML과 이미지를 CSS로 표시하는 주된 사용 패턴에 초점을 맞출 것이다.

![Alt text](image-155.png)


1. 사용자가 웹 사이트 접속
   - 해당 페이지(html,css)를 서버로부터 받은
2. 파싱(parsing)
   - HTML Parser
     - 문서 내 모든 요소(element)를 나타내는 **DOM 트리**를 만든다. -> 이게 목적
     - '< link>'태그와 '< style>'태그를 CSS 파서로 전달한다.
     - 자바스크립트 부분을 호출하는 요소나 '< script>'태그는 "자바스크립트 해석기" 로 전달한다. 
     - 해석기가 결과를 반환하는걸 기다리지 않는다.(비동기)
   - CSS Parser
     - 문서 내 모든 스타일(style) 규칙을 나타내는 CSSOM(CSS Object Model) 트리를 만든다.
   - 이 두 파서를 거쳐서 html과 css 파일이 트리 구조로 변환
   - +) 자바스크립트 코드가 조작할 수 있는 상태(DOM)가 된다. 
3. 둘을 합쳐서 렌더 트리 (Render Tree) 생성
   - 렌더링 엔진이 파싱 과정에서 생성된 두 트리를 결합하여 렌더 트리를 생성
   - 렌더 트리는 브라우저에서 실제로 표시되는 요소들을 포함
     - 요소의 크기, 위치, 색상 등을 계산
   - *자바스크립트 코드가 요소나 스타일을 변경되면, 변경된 부분에 대해서 렌더 트리를 다시 만든다*
4. 화면에 그리기(렌더링)
   - 렌더링 과정은 크게 layout(배치), paint(그리기) 단계로 나뉜다.
     - layout : 각 요소의 크기와 위치 등을 계산
     - paint : 계산된 값을 이용해서 각 요소를 화면상의 *픽셀*로 변환. 필요 시 layer를 만듦.
     - layer : 그려지는 층. 독립적인 여러 레이어를 합쳐서 최종 화면을 만든다.
5. 마지막 합성(composite) 단계
   - 배치와 그리기 단계에서 생성된 레이어들을 결합하여 브라우저 화면에 표시


> 이걸 왜 알아야 할까?
>
> 화면이 느리게 뜨면 위 내용을 토대로 잘못된 부분을 추적,
>
> 크롬 개발자 도구 performance 탭

# 자바스크립트 해석기

## 엔진

- 주요 구성 요소
  - 힙 메모리(Heap Memory)
    - 메모리 할당이 일어나는 곳
    - 변수나 함수가 어딘가에는 저장되어 있어야 참조나 호출을 할텐데, 그 영역이 힙 메모리다.
  - 콜 스택(Call Stack)
    - 호출 스택이 쌓이는 곳
    - 코드를 읽어내려가면서 수행할 작업들을 밑에서부터 쌓는다.
      - 힙 메모리에서 작업 수행에 필요한 것들을 찾아서 작업을 수행하는 공간
  - 실행 컨텍스트(Execution Context)
    - 함수를 실행하기 위해서 필요한 정보
      - 변수, 매개변수, 렉시컬 스코프 등
    - 실행 컨텍스트가 콜 스택에 쌓였다가, 실행되고 나서 콜 스택에서 삭제
  - 눈으로 보는 사이트
    - https://ui.dev/javascript-visualizer
    - 참고로 ES5 까지밖에 지원 안한다. (var 로 써야함 / 세미콜론 필수 등)

- 예제 코드

```
var x = 10;

function outer() {
   var y = 20;
  
   function inner(z) {
      console.log(x + y + z);
   }
  
  return inner;
}

var innerFunc = outer();
innerFunc(30);


```

## 런타임
```js
function first() {
    console.log("first")
    second()
}

function second() {
    setTimeout(function() {
        console.log("second")
    }, 1000)
    third()
}

function third() {
    console.log("third")
}

first()
```

# 런타임은 왜 저렇게 만들어졌을까?

- 자바스크립트 Single Thread 기반 언어기 때문에, 런타임이 저런 식으로 만들어져있다.

Single Thread 기반 언어??


### 프로세스와 쓰레드

- 간단하게 할거임. OS 공부 하면서 다시 학습하시기 바랍니다.

#### 프로세스(Process)
- 실행 중에 있는 프로그램
- 프로그램
  - 명령어와 정적인 데이터 묶음
  - 프로그램 저장 위치: 보조기억장치
    - 실행되기 위해서 보조기억장치에서 대기
    - 프로그램을 실행하면, 주기억장치(RAM)에 메모리 할당
- 프로세스는 적어도 하나 이상의 쓰레드를 가진다.

#### 쓰레드(Thread)
- 프로세스 내부에서 실제로 작업을 하는 주체
  - 작업의 단위, 흐름 이라고도 표현함
  - 프로그램을 돌리기 위해서 프로세스에 할당된 자원(cpu, 메모리 용량)이 존재
    - 이러한 자원들을 실제로 이용하는 단위
- 하나의 프로세스가 하나 이상의 쓰레드로 동작

#### 멀티 프로세스
- 실제로 우리는 동시에 여러 프로그램을 실행
  - 라이브 + vscode + 야구 + op.gg 등등
- CPU 는 한 번에 하나의 연산만 수행 가능
  - 연산이 너무 빨라서 동시처럼 보이는 것
- 프로세스(프로그램)끼리는 독립된 자원(영역)을 가짐

#### 멀티 쓰레드
- 하나의 프로세스 내에서 동시에 여러 쓰레드로 작업을 실행
- 쓰레드끼리는 프로세스 내의 자원을 공유함
  - 동시성 문제
    - 공유된 자원에 동시에 여러 쓰레드가 접근하는 경우
    - 개발자가 주의해서 작업
    - 문제를 막는 기법: 뮤텍스(Mutex), 세마포어(Semaphore)


# 중요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

## html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/1.6.8/axios.min.js" integrity="sha512-PJa3oQSLWRB7wHZ7GQ/g+qyv6r4mbuhmiDb8BjSFZ8NZ2a42oTtAq5n0ucWAwcQDlikAtkub+tPVCw4np27WCg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <title>Document</title>
</head>
<!-- onload: 렌더링 후에 바로 실행할 함수를 등록 -->
<body onload="getData()">
    <form id="articleForm">
        <label for="title">제목: </label>
        <input type="text" id="title" name="title">
        <br><br>
        <label for="content">내용: </label>
        <input type="text" id="content" name="content">
        <br><br>
        <button type="submit">작성하기</button>
    </form>

    <hr>
    <section id="articleSection"></section>

    <script>
        const url = "http://localhost:3001/articles"
        // 전체 조회
        const getData = function() {
            axios.get(url)
            .then((response) => {
                console.log(response)
                renderData(response.data)
            }).catch((error) => {
                console.log("에러남!", error)
            })
        }

        // 화면 렌더링(게시글 출력)
        function renderData(data) {
            const section = document.querySelector('#articleSection')
            section.innerHTML = '' // 기존 내용 비우기

            data.forEach((item) => {
                const articleElement = document.createElement('article')
                articleElement.innerHTML = `
                    <p>글번호: ${item.id}</p>
                    <h2>${item.title}</h2>
                    <p>${item.content}</p>
                    <button onclick="deleteArticle('${item.id}')">삭제</button>
                    <hr/>
                `
                section.appendChild(articleElement)
            })
        }

        // 생성
        const form = document.querySelector('#articleForm')
        form.addEventListener('submit', function(event) {
            event.preventDefault()

            const title = document.querySelector('#title')
            const content = document.querySelector('#content')

            const postData = {
                title: title.value,
                content: content.value
            }

            axios.post(url, postData)
                .then((response) => {
                    console.log('create 완료: ', response.data)
                    title.value = ''
                    content.value = ''
                    getData()
                }).catch((error) => {
                    console.log("에러남!", error)
                })
        })
        
        // 삭제
        function deleteArticle(id) {
            axios.delete(`${url}/${id}`)
                .then((response) => {
                    console.log("삭제 완료: ", response.data)
                    getData()
                }).catch((error) => {
                    console.log("에러남!", error)
                })
        }
    </script>
</body>
</html>
```