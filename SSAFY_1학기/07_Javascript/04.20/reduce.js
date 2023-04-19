const tests = [90, 90, 80, 77]

const sum = tests.reduce((total, x) => {
    return total + x
})

console.log(sum)