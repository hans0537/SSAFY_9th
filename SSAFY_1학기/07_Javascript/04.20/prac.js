// 매개변수보다 인자의 개수가 적을 경우 (매개변수와 인자의 불일치 허용)
const threeArgs = function(arg1, arg2, arg3) {
    return [arg1, arg2, arg3]
}

console.log(threeArgs())

// Spread syntax (Rest parameters)
const restArgs = function (arg1, arg2, ...restArgs) {
    return [arg1, arg2, ...restArgs]
}

console.log(restArgs(1,2,[1,2,3]))

// Arrow function
const arrow1 = function(name){
    return `hello ${name}`
}

// function 키워드 생략 가능
const arrow2 = (name) =>{
    return `hello ${name}`
}

// 인자가 1개인 경우에만 () 생략 가능
const arrow3 = name => {
    return `hello ${name}`
}

// 함수 바디가 retur을 포함한 표현식 1개일 경우에 {} & return 삭제 가능
const arrow4 = name => `hello ${name}`

console.log(arrow1('woong'))
console.log(arrow2('woong'))
console.log(arrow3('woong'))
console.log(arrow4('woong'))

