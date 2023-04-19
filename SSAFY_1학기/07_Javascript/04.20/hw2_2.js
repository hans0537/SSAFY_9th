// 값 하나 입력받기
const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function stars(n) {
    tmp = 1
    for (let i = 0; i < n; i++) {
        for (let j = n - i; j >= 0; j--) {
            process.stdout.write(' ')
        }
        for (let k = 0; k < tmp; k++) {
            process.stdout.write('*')
        }
        for (let j = n - i; j >= 0; j--) {
            process.stdout.write(' ')
        }
        tmp += 2
        console.log()
    }
}

let input = undefined;
process.stdout.write('값을 입력하세요: ')
// 입력시 줄바꿈이 입력될때 마다 수행되는 코드 등록
rl.on('line', function(line){ // 사용자가 입력한 line (string)
    input = line.trim()
    rl.close(); // 입력완료시 close!
})

// 입력완료 close시 수행할 코드 등록
rl.on("close", function(){
    stars(input)
})