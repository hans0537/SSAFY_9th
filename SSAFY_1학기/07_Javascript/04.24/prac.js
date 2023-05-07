console.log(name)
var name = "홍길동"

const dic = {
    'a':123,
    'b':321
}

// for(a in dic){
//     console.log(a)
// }
// for(a of dic){
//     console.log(a)
// }

const as = [1,2,3]
const bs = [1,...as,2]
console.log(bs)

sum(2,5)
function sum(a,b){
    console.log(a + b)
}

returnObject = () => {key:'velue'}
console.log(returnObject())

const myObj = {
    data: 1,
    myFunc() {
        console.log(this)
        console.log(this.data)
    }
}

myObj.myFunc()

arr = []
const sum1 = arr.reduce(function(acc, cur) {
    return acc + cur
},0)
console.log(sum1)
