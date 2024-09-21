// 1. Reverse a String
function reverseString(str) {
    let reversed = '';
    for (let i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }
    return reversed;
}
console.log(reverseString("welcome")); 

// 2. Check for Palindrome
function isPalindrome(str) {
    const reversed = reverseString(str);
    return str === reversed;
}
console.log(isPalindrome("racecar")); 

// 3. Find the Factorial of a Number
function factorial(n) {
    let result = 1;
    for (let i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}
console.log(factorial(5)); 

 // 4. Generate Fibonacci Sequence
 function fibonacci(n) {
   
    if (n <= 0) return [];
    if (n === 1) return [0];

    
    const sequence = [0, 1];

    
    for (let i = 2; i < n; i++) {
        const next = sequence[i - 1] + sequence[i - 2];
        sequence.push(next);
    }

    return sequence;
}


console.log(fibonacci(10));
 

// 5. Find the Largest Element in an Array
function findLargest(arr) {
    if (arr.length === 0) return undefined;

    let largest = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }
    return largest;
}

console.log(findLargest([3, 1, 4, 1, 5, 9])); 


// 6. Sum of Elements in an Array
function sumArray(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}

console.log(sumArray([1, 2, 3, 4, 5])); 

7. Count Occurrences of a Character in a String
function countOccurrences(str, char) {
    let count = 0;
    for (const c of str) {
        if (c === char) {
            count++;
        }
    }
    return count;
}
console.log(countOccurrences("hello world", "l")); 

// 8. Check if a Number is Even or Odd
function isEven(n) {
    return n % 2 === 0;
}
console.log(isEven(2)); 
console.log(isEven(9)); 

// 9. Find the Second Largest Element in an Array
function findSecondLargest(arr) {
    let largest = -Infinity;
    let secondLargest = -Infinity;
    for (const num of arr) {
        if (num > largest) {
            secondLargest = largest;
            largest = num;
        } else if (num > secondLargest && num < largest) {
            secondLargest = num;
        }
    }
    return secondLargest;
}
console.log(findSecondLargest([3, 1, 4, 1, 5, 9])); 

10. Remove Duplicates from an Array
function removeDuplicates(arr) {
    return [...new Set(arr)];
}
console.log(removeDuplicates([1, 2, 2, 3,3, 4, 4, 5])); 

// 11. Check if a String is a Substring of Another String
function isSubstring(str, sub) {
    return str.includes(sub);
}
console.log(isSubstring("hello world", "world")); 

// 12. Reverse an Array
function reverseArray(arr) {
    return arr.reverse();
}
console.log(reverseArray([1, 2, 3, 4, 5])); 

// 13. Find the Sum of Digits of a Number
function sumOfDigits(n) {
    let sum = 0;
    let number = Math.abs(n); // Handle negative numbers by using absolute value

    while (number > 0) {
        sum += number % 10; // Get the last digit
        number = Math.floor(number / 10); // Remove the last digit
    }

    return sum;
}

console.log(sumOfDigits(1234)); 


// 14. Convert Celsius to Fahrenheit
function celsiusToFahrenheit(celsius) {
    return (celsius * 9/5) + 32;
}
console.log(celsiusToFahrenheit(0)); 

// 15. Print the Multiplication Table of a Given Number
function printMultiplicationTable(num) {
    for (let i = 1; i <= 10; i++) {
        console.log(`${num} * ${i} = ${num * i}`);
    }
}
printMultiplicationTable(5);

// 16. Find the Length of a String Without Using Built-in Functions
function stringLength(str) {
    let length = 0;
    for (const char of str) {
        length++;
    }
    return length;
}
console.log(stringLength("hello")); 

// 17. Swap Two Numbers Without Using a Temporary Variable
function swapNumbers(a, b) {
    a = a + b;
    b = a - b;
    a = a - b;
    return [a, b];
}
console.log(swapNumbers(3, 5)); 

// 18. Find the GCD of Two Numbers
function gcd(a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
console.log(gcd(48, 18)); 

19. Find the LCM of Two Numbers
// Function to find the Greatest Common Divisor (GCD) using the Euclidean Algorithm
function gcd(a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Function to find the Least Common Multiple (LCM) using the GCD
function lcm(a, b) {
    return (a * b) / gcd(a, b);
}


console.log(lcm(4, 6));  
console.log(lcm(15, 25)); 
  


// 20. Check if a Number is Prime
function isPrime(n) {
    if (n <= 1) return false;

    let count = 0;

    for (let i = 1; i <= n; i++) {
        if (n % i === 0) {
            count++;
        }
    }

    return count === 2;
}

console.log(isPrime(7));  


// 21. Print the First 10 Prime Numbers
function isPrime(n) {
    if (n <= 1) return false;

    let count = 0;

    for (let i = 1; i <= n; i++) {
        if (n % i === 0) {
            count++;
        }
    }

    return count === 2;
}

function firstNPrimes(n) {
    const primes = [];
    let i = 2;
    while (primes.length < n) {
        if (isPrime(i)) {
            primes.push(i);
        }
        i++;
    }
    return primes;
}

console.log(firstNPrimes(10));


// 22. Find the Average of Numbers in an Array
function averageArray(arr) {
    return sumArray(arr) / arr.length;
}
console.log(averageArray([1, 2, 3, 4, 5]));

// 23. Print the Pattern:
// *
// **
// ***
// ****
// *****
function printStarPattern1() {
    for (let i = 1; i <= 5; i++) {
        console.log('*'.repeat(i));
    }
}
printStarPattern1();

// 24. Print the Pattern:
// 1
// 22
// 333
// 4444
// 55555
function printNumberPattern1() {
    for (let i = 1; i <= 5; i++) {
        console.log(i.toString().repeat(i));
    }
}
printNumberPattern1();

// 25. Calculate the Power of a Number
function power(base, exponent) {
    let result = 1;
    for (let i = 0; i < exponent; i++) {
        result *= base;
    }
    return result;
}
console.log(power(2, 3)); 

// 26. Count Vowels in a String
function countVowels(str) {
    const vowels = 'aeiouAEIOU';
    let count = 0;
    for (const char of str) {
        if (vowels.includes(char)) {
            count++;
        }
    }
    return count;
}
console.log(countVowels("Antartica")); 

// 27. Check if a Year is a Leap Year
function isLeapYear(year) {
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}
console.log(isLeapYear(2020)); 

// 28. Find the Minimum Element in an Array
function findMinimum(arr) {
    let min = arr[0];
    for (const num of arr) {
        if (num < min) {
            min = num;
        }
    }
    return min;
}
console.log(findMinimum([3, 1, 4, 1, 5, 9])); 

// 29. Find the Maximum Element in an Array
function max(arr){
   console.log(arr.length)
}
max([3, 1, 4, 1, 5, 9]); 


// // 30. Check if a String Contains Only Digits
function isOnlyDigits(str) {
    for (let i = 0; i < str.length; i++) {
        const char = str[i];
        if (char < '0' || char > '9') {
            return false;
        }
    }
    return true;
}

console.log(isOnlyDigits("12345")); 
console.log(isOnlyDigits("123a5"));  


// 31. Convert a String to Uppercase Without Using Built-in Functions
function toUpperCase(str) {
    let upperStr = '';
    for (const char of str) {
        const code = char.charCodeAt(0);
        if (code >= 97 && code <= 122) {
            upperStr += String.fromCharCode(code - 32);
        } else {
            upperStr += char;
        }
    }
    return upperStr;
}
console.log(toUpperCase("hello world")); 

// 32. Merge Two Sorted Arrays
function mergeSortedArrays(arr1, arr2) {
    const merged = [];
    let i = 0, j = 0;
    while (i < arr1.length && j < arr2.length) {
        if (arr1[i] < arr2[j]) {
            merged.push(arr1[i++]);
        } else {
            merged.push(arr2[j++]);
        }
    }
    return merged.concat(arr1.slice(i)).concat(arr2.slice(j));
}
console.log(mergeSortedArrays([1, 3, 5], [2, 4, 6])); 

// 33. Find the Intersection of Two Arrays
function intersectArrays(arr1, arr2) {
    return [...new Set(arr1)].filter(item => arr2.includes(item));
}
console.log(intersectArrays([1, 2, 3, 4], [3, 4, 5, 6])); 

// 34. Count the Number of Words in a String
function countWords(str) {
    return str.trim().split(/\s+/).length;
}
console.log(countWords("Hello world, this is a test.")); 

// 35. Check if Two Strings are Anagrams
function areAnagrams(str1, str2) {
    const sortString = s => s.split('').sort().join('');
    return sortString(str1) === sortString(str2);
}
console.log(areAnagrams("listen", "silent")); 
console.log(areAnagrams("hello", "world")); 

// 36. Print the Pattern:
// 1
// 12
// 123
// 1234
// 12345
function printNumberPattern2() {
    for (let i = 1; i <= 5; i++) {
        console.log([...Array(i).keys()].map(n => n + 1).join(''));
    }
}
printNumberPattern2();

// 37. Print the Pattern:
// 54321
// 4321
// 321
// 21
// 1
function printNumberPattern3() {
    for (let i = 5; i >= 1; i--) {
        console.log([...Array(i).keys()].map(n => i - n).join(''));
    }
}
printNumberPattern3();

// 38. Find the Sum of Two Matrices
function addMatrices(matrix1, matrix2) {
    return matrix1.map((row, i) => row.map((value, j) => value + matrix2[i][j]));
}
console.log(addMatrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]));

// 39. Transpose a Matrix
function transposeMatrix(matrix) {
    return matrix[0].map((_, colIndex) => matrix.map(row => row[colIndex]));
}
console.log(transposeMatrix([[1, 2, 3], [4, 5, 6]])); 

// 40. Check if a Number is Armstrong
function isArmstrong(n) {
    const digits = n.toString().split('');
    const sum = digits.reduce((acc, digit) => acc + Math.pow(parseInt(digit), 3), 0);
    return sum === n;
}
console.log(isArmstrong(153));

// 41. Print the Pattern:
// *
// * *
// * * *
// * * * *
// * * * * *
function printStarPattern2() {
    for (let i = 1; i <= 5; i++) {
        console.log('* '.repeat(i).trim());
    }
}
printStarPattern2();

// 42. Convert a Decimal Number to Binary
function decimalToBinary(n) {
    return n.toString(2);
}
console.log(decimalToBinary(12)); 

// 43. Find the Sum of Elements in the Main Diagonal of a Matrix
function sumMainDiagonal(matrix) {
    return matrix.reduce((sum, row, i) => sum + row[i], 0);
}
console.log(sumMainDiagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])); 

// 44. Remove All Whitespaces from a String
function removeWhitespaces(str) {
    return str.replace(/\s+/g, '');
}
console.log(removeWhitespaces("  Dip   Dut  ")); 

// 45. Find the Common Elements in Three Arrays
function commonElements(arr1, arr2, arr3) {
    return intersectArrays(intersectArrays(arr1, arr2), arr3);
}
console.log(commonElements([1, 2, 3], [2, 3, 4], [3, 4, 5]));

// 46. Find the Median of an Array
function median(arr) {
    arr.sort((a, b) => a - b);
    const mid = Math.floor(arr.length / 2);
    return arr.length % 2 === 0 ? (arr[mid - 1] + arr[mid]) / 2 : arr[mid];
}
console.log(median([1, 3, 3, 6, 7, 8, 9])); 

// 47. Print All Prime Numbers in a Given Range
function primesInRange(start, end) {
    const primes = [];
    for (let num = start; num <= end; num++) {
        if (isPrime(num)) {
            primes.push(num);
        }
    }
    return primes;
}
console.log(primesInRange(10, 20)); 

// 48. Reverse the Words in a Sentence
function reverseWords(sentence) {
    return sentence.split(' ').reverse().join(' ');
}
console.log(reverseWords("Hello world, this is a test.")); 

// 49. Find the First Non-Repeated Character in a String
function firstNonRepeatedCharacter(str) {
    const counts = {};
    for (const char of str) {
        counts[char] = (counts[char] || 0) + 1;
    }
    for (const char of str) {
        if (counts[char] === 1) return char;
    }
    return null;
}
console.log(firstNonRepeatedCharacter("swiss")); 
// 50. Check if an Array is Sorted
function isSorted(arr) {
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < arr[i - 1]) return false;
    }
    return true;
}
console.log(isSorted([1, 2, 3, 4, 5])); 
console.log(isSorted([1, 3, 2, 4, 5]));
