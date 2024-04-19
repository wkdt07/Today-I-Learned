# JS03 - Reference Type

참조 자료형

## 함수

- 참조 자료형에 속하면 모든 함수는 function object
- 참조 자료형은 객체 배열 함수
- 참조 자료형은 주소가 저장되는 가변적 변수

![Alt text](image-60.png)

### 함수 정의 방법
- 선언식 
- 표현식

![Alt text](image-61.png)


![Alt text](image-62.png)


- 사용할 땐 차이가 없음
- 하지만 동작원리는 다름


![Alt text](image-63.png)


![Alt text](image-64.png)

> 표현식으로 정의한다.(변수 지정하는거)



## 매개변수

1. 기본 함수 매개변수
2. 나머지 매개 변수

### 1. 기본 함수 매개변수

![Alt text](image-65.png)

디폴트 인자 같은거

### 2. 나머지 매개변수

![Alt text](image-66.png)

파이썬의 가변인자 func(*arg)와 비슷한 것.


> 매개변수와 인자 개수가 불일치하면?

![Alt text](image-67.png)

![Alt text](image-68.png)

### Spread syntax '...' 

- 전개 구문
- 배열이나 문자열과 같이 반복 가능한 항목을 펼치는 것(확장,전개)
- 전개 대상에 따라 역할이 다름
  - 1. 함수와의 사용
    - 1. 함수 호출 시 인자 풀어낸다(확장)
    - 2. 나머지 매개변수(압축)
  - 2. 객체와의 사용(객체 파트에서 진행)
  - 3. 배열과의 활용(배열 파트에서 진행)




![Alt text](image-69.png)

- 호출시 풀어냄

![Alt text](image-70.png)

- 선언 시 압축함


### 화살표 함수

- 화살표 함수 표현식 : 함수 표현식의 간결한 표현법

![Alt text](image-71.png)

> shb : 인자를 => 형태로 바꾼다


### 화살표 함수 작성 과정

![Alt text](image-72.png)


![Alt text](image-73.png)


![Alt text](image-74.png)


```js
  <script>
    const arrow1 = function (name) {
      return `hello, ${name}`
    }
    
    // 1. function 키워드 삭제 후 화살표 작성
    const arrow2 = (name) => {return `hello, ${name}`}
    // 2. 인자의 소괄호 삭제 (인자가 1개일 경우에만 가능)
    const arrow3 = name => {return `hello, ${name}`}
    // 3. {}와 return 삭제 (함수 본문이 return을 포함한 표현식 1개일 경우에만 가능)
    const arrow4 = name => `hello, ${name}`
  </script>
```

### 참고

### 화살표 함수 심화

![Alt text](image-75.png)


## 객체

- 키로 구분된 데이터 집합을 저장하는 자료형 -> 파이썬의 딕셔너리

### 구조 및 속성

![Alt text](image-76.png)

- 키가 한 단어라면 '' 생략할 수 있음
- 키는 무조건 문자열
- 키 = 속성 

### 속성 참조

- 2가지 방법, .을 이용하는 방법과 []로 접근하는 방법
- 
![Alt text](image-77.png)

- 구분자가 키에 끼어있으면 []로만 가능

![Alt text](image-78.png)

- 수정과 삭제

### in 연산자

- 속성이 객체에 존재하는지 여부 확인

### 객체와 함수

### METHOD

- 객체 속성에 정의된 함수
- object.method() 방식으로 호출
- 객체를 '행동' 할 수 있도록

**this** 키워드??

> 'this' 키워드로 함수나 메서드를 호출한 객체를 카리킬 수 있다


![Alt text](image-79.png)

self 인자와는 전혀 다르다

> why? 본인을 가리키는게 아닐 수도 있다

![Alt text](image-80.png)

![Alt text](image-81.png)

![Alt text](image-82.png)

> 호출하는 방법이 가장 중요

![Alt text](image-83.png)

> 화살표 함수가 중요한 이유

- 화살표 함수는 본인의 this를 갖지 않기 때문에 외부 함수(한 단계 위,myObj3)에서 this를 가져온다

### this 정리

![Alt text](image-84.png)

![Alt text](image-85.png)

## 추가 객체 문법

1. 단축 속성

![Alt text](image-86.png)

2. 단축 메서드

![Alt text](image-87.png)


3. 계산된 속성

![Alt text](image-88.png)


### 4. 구조 부분할당 -> 중요한 부분

구조를 분해해서 변수에 할당한다

![Alt text](image-90.png)

```js
    // 4. 구조 분해 할당
    const userInfo = {
      firstName: 'Alice',
      userId: 'alice123',
      email: 'alice123@gmail.com'
    }

    const firstName = userInfo.firstName
    const userId = userInfo.userId
    const email = userInfo.email

    const{firstName} = userInfo
    const { firstName,userId,email} = userInfo

```


![Alt text](image-89.png)

> import 할 때도 자주 사용한다.

5. 전개 구문

- 객체 내부에서 객체 전개

![Alt text](image-91.png)

6. 유용한 객체 메서드

![Alt text](image-92.png)


> 파이썬에 있는것과 똑같음

7. Optional chaining ('?.')

- 선택적 연결

![Alt text](image-93.png)

- 에러 방지용으로 사용

![Alt text](image-94.png)

- 장점 : 누락될 가능성이 있는 속성으로 접근 가능

> 단점

![Alt text](image-95.png)


![Alt text](image-96.png)


## JSON

- 자바스크립트 객체 표기법
- JSON 자체는 문자열 -> 파이썬은 dict로 바꿨고, JS는 OBJECT로 바꿔야 한다.
  
![Alt text](image-97.png)

![Alt text](image-98.png)

## 참고 - new 연산자

41m


# offline

## 얕은 복사/ 깊은 복사

- 주소값을 복사 == 복사한 값을 변경하면 원본 값도 변경
- 깊은 복사 == 복사한 값을 변경해도 원본 값은 그대로

```js

// 깊은 복사 -> 원시 자료형
let a = 10
let b = a
b = 20

console.log(a) // 10
console.log(b) // 20

// 복사한 값을 바꿔도 원본 값은 유지된다

// 얕은 복사

let c = [1,2,3]
let d = c // 얕은 복사 : c의 주소값이 d에 저장

d[1] = 4 // d의 주소값에서 1칸만큼 이동한 곳의 값을 4로 변경

console.log(c) // [1,4,3] // 이것도 바뀜
console.log(d) // [1,4,3]

const arr = [1,2,3,4,5]
function func(arr) {
    arr[0] = 10
}

const arr = [1,2,3,4,5]
// const 인데 변경이 된다?
// arr은 실제로 주소값을 저장
// 아래 코드

arr[2] = 30 // 주소값+2칸인 곳의 값을 바꿔라 -> 실제 주소값을 변경하는게 아니다

// => const에 위배가 되지는 않는다.


func(arr)
console.log(arr)


// 1차원 배열 깊은 복사

{
    let numbers = [1,2,3]
    let newNumbers = [...numbers]
    // ... (스프레드 연산자) : 객체를 전개하여 각 요소를 개별적인 값으로 분리
    // 사실상 주소에 있는 값을 갖고와서 새로 만드는 주소에 갖다 넣는다고 생각
    
    newNumbers[1] = 1
    console.log(newNumbers) // 1,2,3
    console.log(numbers) // 1,10,3

}

// 2차원 배열 깊은 복사
{
    let numbers = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    let newNumbers = [...numbers]
    newNumbers[0][1] = 1
    // ... (스프레드 연산자) : 객체를 전개하여 각 요소를 개별적인 값으로 분리
    // 1차원은 가능하지만, 더 깊은 depth은 얕은 복사가 발생
    // 당연한 얘기임. 2차원 배열은 배열 안에 여러개의 주소가 있다고 생각해야함
    console.log(newNumbers) // 1,2,3
    console.log(numbers) // 1,10,3

    // 
    let newNumbers2 = numbers.map(v=>[...v]) // 깊은 복사 완료
    newNumbers2[0][1] = 100

}

const obj = {b:2, c:3 , d:4}
const newObj = {a:1,...obj,e:5}

obj.b = 10

console.log(obj) // { b: 10, c: 3, d: 4 }
console.log(newObj) // {a: 1, b: 2, c: 3, d: 4, e: 5}



```


## 콜백 함수

- 다른 함수의 인자로 전달되는 함수

```js
// 콜백 함수
// 다른 함수의 인자로 전달되는 함수
const calculator = function(a, b, mathFunction){
    return mathFunction(a, b)
  }
  
const add = function(a, b){
return a + b
}

const sub = function(a, b){
return a - b
}

// add, sub 를 콜백 함수라고 부름
console.log(calculator(3, 5, add))
console.log(calculator(3, 5, sub))

// JS는 이렇게 잘 안 씀. 그럼 어떻게 쓰는데? '익명함수'를 주로 콜백 함수로 넣음.
const add = function func(a, b){
return a + b
}
// 원래 이렇게 함수 이름을 정하는게 정석임
// 익명 함수는 이름이 없는 함수

console.log(calculator(3,5,function(a,b){
    return a+b
}))

console.log(calculator(3,5,function(a,b){
    return a-b
}))

// 화살표 함수로?



console.log(calculator(3,5,(a,b) =>
     a+b
))
```


## array helper method


'https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach'


```js
// Array Helper Method 란?
// - 배열 조작을 쉽게 만들어 주는 JS 내장 메서드
// - 얼마나 잘 쓰느냐에 따라 개발 속도가 엄청나게 차이난다

const lunchMenu = [
    { name: '김치찌개', price: 8000 },
    { name: '돼지국밥', price: 9000 },
    { name: '카레', price: 7500 },
    { name: '햄버거', price: 8500 },
    { name: '초밥', price: 12000 },
    { name: '김밥', price: 5000 }
];

// ----------------------------------------------------------------------------
// 문제1. 메뉴 맛있겠다 외치기
// 출력
// 김치찌개 맛있겠다!
// 돼지국밥 맛있겠다!
// 카레 맛있겠다!
// 햄버거 맛있겠다!
// 초밥 맛있겠다!
// 김밥 맛있겠다!
```

1. foreach
   - 주어진 배열의 각 요소에 대해 함수를 실행
   - 새로운 배열 생성 x
   - Array.forEach(element,index,array) => {}
```js
lunchMenu.foreach((menu,index,array) => {
    console.log(`${menu.name} 맛있겠다!`)
    console.log('array='`${menu.index}`)
}) // index와 array는 안 써도 된다 -> JS는 인자 갯수에 전혀 관계 없음

```


2. map
   - foreach와 똑같음 
   - 주어진 배열을 갖고와서 함수를 실행함
   - 하지만 반환 값으로 새로운 배열을 만든다
   - Array.map(element,index,array) => {}
```js
// ----------------------------------------------------------------------------
// 문제2. 내가 가진 돈은 15,000원 이다. 각 메뉴를 먹고 나서 남은 가격을 배열로 출력하시오.
// 출력
// [ 7000, 6000, 7500, 6500, 3000, 10000 ]
let money = 15000
const remains = lunchMenu.map(lunch => {
    return money - lunch.price // 배열 값들이 모두 이걸 가져가는것
})


// ----------------------------------------------------------------------------
// 문제3. 내가 가진 돈은 15,000원 이다. 각 메뉴에 먹고 나서 남은 가격을 추가한 새로운 배열을 출력하시오.
// 출력
// [
//   { name: '김치찌개', price: 8000, remainMoney: 7000 },
//   { name: '돼지국밥', price: 9000, remainMoney: 6000 },
//   { name: '카레', price: 7500, remainMoney: 7500 },
//   { name: '햄버거', price: 8500, remainMoney: 6500 },
//   { name: '초밥', price: 12000, remainMoney: 3000 },
//   { name: '김밥', price: 5000, remainMoney: 10000 }
// ]
const lunchMenu = [
    { name: '김치찌개', price: 8000 },
    { name: '돼지국밥', price: 9000 },
    { name: '카레', price: 7500 },
    { name: '햄버거', price: 8500 },
    { name: '초밥', price: 12000 },
    { name: '김밥', price: 5000 }
];
const names = lunchMenu.map(lunch => {
    // return {name : lunch.name, price : lunch.price, remainMoney : money-lunch.price}
    const remainMoney = money-lunch.price
    return {
        ...lunch,
        remainMoney
        // remainMoney : money-lunch.price
    }
})

console.log(names)







// ----------------------------------------------------------------------------
// 문제7. 모든 메뉴 가격 총합 구하기
// 출력
// 총 가격 : 50000
```

3. filter

```js
// ----------------------------------------------------------------------------
// 문제4. 가격이 8000원 이하인 메뉴만 걸러내시오.
// 출력
// [
//     { name: '김치찌개', price: 8000 },
//     { name: '카레', price: 7500 },
//     { name: '김밥', price: 5000 }
//   ]
const lunchMenu = [
    { name: '김치찌개', price: 8000 },
    { name: '돼지국밥', price: 9000 },
    { name: '카레', price: 7500 },
    { name: '햄버거', price: 8500 },
    { name: '초밥', price: 12000 },
    { name: '김밥', price: 5000 }
];

const filterMenu = lunchMenu.filter(menu=>{
    return menu.price <= 8000
})

console.log(filterMenu)
```

4. find
    - 조건에 만족하는 '첫 번째 값'을 찾고 싶어
    - 값이 없다면 undefined가 반환된다.

```js
// ----------------------------------------------------------------------------
// 문제5. '초밥'을 파는 지 찾으시오.
// 출력
// 있다면 { name: '초밥', price: 12000 } 출력
// 없다면 undefined 출력

```

5. every
```js
// ----------------------------------------------------------------------------
// 문제6. 내가 가진 돈으로 사먹지 못하는 메뉴가 있는 지 확인하시오.
// 있다면 "더 비싼 메뉴 있음!" 출력
// 없다면 "더 비싼 메뉴 없음!" 출력

money = 10000
const lunchMenu = [
    { name: '김치찌개', price: 8000 },
    { name: '돼지국밥', price: 9000 },
    { name: '카레', price: 7500 },
    { name: '햄버거', price: 8500 },
    { name: '초밥', price: 12000 },
    { name: '김밥', price: 5000 }
];

const pass = lunchMenu.every(menu=>
{
    return menu.price <= money
})

// if (pass === true){
//     console.log('더 비싼 메뉴 없음!')
// }
// else{
//     console.log('더 비싼 메뉴 있음!')
// }


// 삼항연산자
pass ?console.log('더 비싼 메뉴 없음!') : console.log('더 비싼 메뉴 있음!')
```

6. some


7. reduce
   - 각 요소에 주어진 함수를 실행하고, 하나의 결과값을 누적해서 반환
   ```js
    Array.reduce((acc,element,index,array)=>{
    //acc:누적된 값
    //start:시작값
    },start)
   ```
    ```js

    const totalPrice = lunchMenu.reduce((acc,menu)=>{
        return acc+menu.price
    },0)

    console.log(`총 가격 : ${totalPrice}원`)
    ```

## this

- 특정 object를 가리키는 키워드
- python(self) 에서는 인스턴스(클래스 변수) 자기자신을 가리킴
- JS의 this는 정해지지 않음. 호출 방법에 따라 this가 가리키는 Object가 다름

```js
//브라우저 : window, node.js : global
console.log(global) // 전역 개체(Node.js의 표준 전역개체)
cosole.log(globalThis) // 전역개체
// 모든 JS 환경에서 표준화된 전역 객체에 접근하기 위한 표준 방법

console.log(this) //{}
//nodejs 환경에서 js 파일은 하나의 모듈로 판단
// 즉, this는 하나의 파일을 가리킴
// 모듈에서 아무것도 내보내고 있지 않기 때문에 {}로 출력된다.

exports.add = function() { 
    console,log('test')
}
console.log(this) // {add:[Function (anonymous)]} // 이제 모듈이 내보내는게 생겼으니 그게 나온다
```

1. 일반적인 함수에서 this : 전역 개체를 꺼내온다.
```js
const func = function(){
    console.log(this) // global
}
func()
```

2. 객체 내부 메서드에서의 this : 해당 객체를 가리키게 된다. 

```js
const obj = {
    name : 'test',
    func : function(){
        console.log(this) // this : 메서드가 정의된 객체
    }
}
obj.func() // { name: 'test', func: [Function: func] }
```

```js
// 객체 내부의 화살표 함수와 this


const obj = {
    name : 'test',
    func : function(){
        console.log(this) // this : 메서드가 정의된 객체
    },

    // 화살표 함수 : 한 단계 상위 스코프의 this를 참조 -> 렉시컬 스코프 this 참조
    arrowFunc: ()=>{
        console.log(this) // {}
    },
    tmp:this // {}
    // tmp == arrowFunc

    // 웬만하면 이 안에서는 화살표 함수로 this 하지 마라
    

}

obj.func() // { name: 'test', func: [Function: func] }

// 그럼 언제는 괜찮냐? 콜백 함수 쓸 떄
const obj2 = {
    name : 'shb',
    greeting : function() {
        console.log(this) //obj2

        const normalFunc = function(){
            console.log(this) // global # 일반함수에서의 this니깐
        }

        const arrowFunc = () => {
            console.log(this) //
        }

        arrowFunc() // 
    }
}

```

### 정리 

1. 일반 함수의 this는 무조건 전역변수
2. 메서드의 function의 this는 메서드가 정의된 객체
3. 화살표 함수의 this는 렉시컬 스코프(바로 한 단계 위 객체가 가진 this)

```js

const obj3 = {

    // 메서드 정의는 애로우가 아니라 function으로
    arr : [1,2,3],
    // 콜백
    func : function(){
        this.arr.forEach((el) =>{
            //내부 콜백 함수는 arrow function으로!
            console.log(this) // 화살표 함수 -> obj3를 가리킨다. 
        })
    }
}

obj.func()
```