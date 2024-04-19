// let money = 15000

// const lunchMenu = [
//     { name: '김치찌개', price: 8000 },
//     { name: '돼지국밥', price: 9000 },
//     { name: '카레', price: 7500 },
//     { name: '햄버거', price: 8500 },
//     { name: '초밥', price: 12000 },
//     { name: '김밥', price: 5000 }
// ];
// const names = lunchMenu.map(lunch => {
//     // return {name : lunch.name, price : lunch.price, remainMoney : money-lunch.price}
//     return {
//         ...lunch,
//         remainMoney : money-lunch.price
//     }
// })

// console.log(names)

// const lunchMenu = [
//     { name: '김치찌개', price: 8000 },
//     { name: '돼지국밥', price: 9000 },
//     { name: '카레', price: 7500 },
//     { name: '햄버거', price: 8500 },
//     { name: '초밥', price: 12000 },
//     { name: '김밥', price: 5000 }
// ];

// const filterMenu = lunchMenu.filter(menu=>{
//     return menu.price <= 8000
// })

// console.log(filterMenu)


// money = 10000
// const lunchMenu = [
//     { name: '김치찌개', price: 8000 },
//     { name: '돼지국밥', price: 9000 },
//     { name: '카레', price: 7500 },
//     { name: '햄버거', price: 8500 },
//     { name: '초밥', price: 12000 },
//     { name: '김밥', price: 5000 }
// ];

// const pass = lunchMenu.every(menu=>
// {
//     return menu.price <= money
// })

// // if (pass === true){
// //     console.log('더 비싼 메뉴 없음!')
// // }
// // else{
// //     console.log('더 비싼 메뉴 있음!')
// // }

// pass ?console.log('더 비싼 메뉴 없음!') : console.log('더 비싼 메뉴 있음!')


// const func = function(){
//     console.log(this)
// }
// func()

// const obj = {
//     name : 'test',
//     func : function(){
//         console.log(this)
//     }
// }
// obj.func()

// const obj3 = {

//     // 메서드 정의는 애로우가 아니라 function으로
//     arr : [1,2,3],
//     // 콜백
//     func : function(){
//         this.arr.forEach((el) =>{
//             //내부 콜백 함수는 arrow function으로!
//             console.log(this) // 화살표 함수 -> obj3를 가리킨다. 
//         })
//     }
// }

// obj3.func()
const students = [
  { name: 'Alice', scores: [85, 90, 95] },
  { name: 'Bella', scores: [50, 80, 80] },
  { name: 'Caley', scores: [90, 55, 35] },
  { name: 'Dave', scores: [100, 100, 100] },
  { name: 'Eve', scores: [88, 90, 92] }
]
// 아래에 코드 작성

// function makeAvgScores1(arr){
//   const result = {}
//   for(i=0;i<students.length;i+=1){
//     let total = 0
//     let cnt = 0
//     for(j=0;j<students[i].scores.length;j+=1){
//       total += students[i].scores[j]
//       cnt ++
//     }
//     let avg = total/cnt
//     // console.log(avg)
//     result[students[i].name]  = avg
//   } 

//   return result
// }
function makeAvgScores2(students){
  let result = {}  
  for (let student of students) {
      let total = 0

      for (let score of student.scores) {
          total += score
      }
      let avg = total / student.scores.length
      result[`${student.name}`] = avg
    }
    return result
}
// 함수 호출
const result1 = makeAvgScores2(students)
console.log(result1)
