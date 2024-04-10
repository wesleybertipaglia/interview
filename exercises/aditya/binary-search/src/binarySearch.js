function binarySearch(arr, target) {
    const sortedArr = arr.sort();
    let step = 1
    const high = sortedArr.length - 1
    let current = high / 2

    while (sortedArr[current] != target) {
        console.log(`Setp ${step} - target: ${target} | current: ${sortedArr[current]}`);

        if (sortedArr[current] > target) {
            current = current / 2
        } else {
            current = current * 2
        }

        step++;
    }

    return console.log(`Found ${target} at: ${current}`);
}

export default binarySearch;
