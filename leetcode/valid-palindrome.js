/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let checker = "";
    for (i of s.toLowerCase()) {
        if (/^[a-zA-Z0-9]+$/.test(i) && (i != " ")) {
            checker += i;
        }
    }
    for (let i = 0; i < checker.length; i++) {
        if (checker[i] != checker[checker.length - (i + 1)]){ 
            return false 
        }
    }
    return true
};