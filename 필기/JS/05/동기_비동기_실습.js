// 비동기

// 가장 간단한 비동기 코드

console.log('a')

setTimeout(() => {
    console.log('b')   
}, 1000)

console.log('c')


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