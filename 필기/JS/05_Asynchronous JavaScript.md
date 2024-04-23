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

