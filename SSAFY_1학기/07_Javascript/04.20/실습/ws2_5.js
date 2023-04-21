
function check(v, idx) {
    for (let i = 0; i < idx; i++) {
        if (v[i] == v[idx] || Math.abs(v[i] - v[idx]) == Math.abs(idx - i)) return false
    }
    return true
}

function nQueen(idx, n, v) {

    if (idx == n) {
        answer += 1
        return
    }

    for (let i = 0; i < n; i++) {
        v[idx] = i
        if (check(v, idx)){
            nQueen(idx + 1, n, v)
        }
    }
}

function findQueens(n) {
    answer = 0

    nQueen(0, n, [...Array(n)].map((_,i) => 0))    

    return answer
}

console.log(findQueens(2)) // 0
console.log(findQueens(4)) // 2
console.log(findQueens(8)) // 92
console.log(findQueens(9)) // 352
