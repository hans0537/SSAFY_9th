// 물 => 스프 => 면 순서로 하고 싶다.

console.log("라면을 끓이자!! (각 재료가 준비되는데 1~3초 시간이 걸린다)")

// 라면 = 물, 스프, 면
let aFinished = false;  // 물
let bFinished = false;  // 스프
let cFinished = false;  // 면

setTimeout(() => {
    console.log("A: 물을 넣는다.")
    setTimeout(() => {
        console.log("B: 스프를 넣는다.")
        setTimeout(() => {
            console.log("C: 면을 넣는다")
            console.log("라면을 끓인다.")
        },Math.random() * 2000 + 1000);
    },Math.random() * 2000 + 1000);
},Math.random() * 2000 + 1000);