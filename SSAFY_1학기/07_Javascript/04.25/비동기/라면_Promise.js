/* Promise 객체 사용법
    
    new Promise((resolve, reject) => {

        if(성공조건){
            return resolve(value) => 비동기 작업이 성공했을때 리턴하고 싶은 값을 value로
        } else if (실패조건) {
            return reject(value) => 비동기 작업이 실패했을때 리턴하고 싶은 값을 value로
        }
    })

    axios.get() 이 함수도 return 값이 Promise 객체 였기 때문에 .then, .catch 사용 가능

*/

const water = function() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("A: 물을 넣는다!!")
            return resolve(["물"])
            // 에러 발생시 에러 메세지 반환
            // return reject("물을 너무 많이 넣었다")
        },Math.random() * 2000 + 1000)
    })
}

const soup = function(ramen) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(ramen)
            console.log("B: 스프를 넣는다!!")
            ramen.push("스프")
            return resolve(ramen)
        },Math.random() * 2000 + 1000)
    })
}

const noodle = function(ramen) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(ramen)
            console.log("C: 면을 넣는다!!")
            ramen.push("면")
            return resolve(ramen)
        },Math.random() * 2000 + 1000)
    })
}

// water()
// .then((ramen) => {
//     return soup(ramen)
// })
// .then((ramen) => {
//     return noodle(ramen)
// })
// .then((ramen) => {
//     // 위의 모든 작업이 끝나고 나서 하고 싶은 일
//     console.log("라면 끓이기 시작:", ramen)
// })
// .catch((error) => {
//     console.log('라면 만드는 도중에 문제 발생: ', error)
// })

// async, await
// await 는 해당 비동기 작업이 끝나면 사용할 수 있도록 해주는 키워드
// await 키워드는 async 함수 안에서만 사용 가능

const makeRamen = async function() {
    const ramen = await water()
        .then((ramen) => {
            return soup(ramen)
        })
        .then((ramen) => {
            return noodle(ramen)
        })
        .then((ramen) => {
            // 위의 모든 작업이 끝나고 나서 하고 싶은 일
            console.log("라면 끓이기 시작:", ramen)
            return ramen
        })
        .catch((error) => {
            console.log('라면 만드는 도중에 문제 발생: ', error)
        })

    console.log("결과: ", ramen)
};

makeRamen()