// 1번
const nums = [1,2,3,4,5,6,7,8]

// for문 안에 있는 변수 i는 증가하는 변수인데 const로 지정하면 값이 바뀔 수 가 없다.
// 따라서 i는 let으로 변수를 선언해야 한다.
for (let i = 0; i < nums.length; i++) {
    console.log('nums[' + i + ']: ' + nums[i])
}

// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.



// 2번

// for in 구문은 속성 이름을 통해서 반복 하고 속성명은 문자열(string) 형태로 반환되기 때문에, 결과값이 문자열이다.
// 따라서 배열의 요소값을 가져오기 위해선 for of 구문을 사용하여야 한다.
for (num of nums) {
  console.log(num, typeof num)
}

// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string
