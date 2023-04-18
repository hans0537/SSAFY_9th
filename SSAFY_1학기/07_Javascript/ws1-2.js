words = ['level', 'noon', 'mom', 'happy', 'ssafy', 'life']

function palindrome(word) {
    let temp = ''

    for (let i = word.length - 1; i >= 0; i--) {
        temp += word[i]
    }

    if (word === temp){
        return true
    }
    return false
}
  
for (const word of words) {
  console.log(palindrome(word))
}

// 출력 예시
// true
// true
// true
// false
// false
// false
