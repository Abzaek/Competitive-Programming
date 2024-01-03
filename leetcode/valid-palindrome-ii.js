/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function(s) {
    let l = 0;
    let r = s.length - 1;

    while (r > l) {
         if (s[l] != s[r]) {
        if (s.substring(l, r) === s.substring(l, r).split('').reverse().join('')) {
            return true
        } else if (s.substring(l + 1, r + 1) === s.substring(l + 1, r + 1).split('').reverse().join('')) {
            return true
        } else {
            return false
        }
    }

    r--;
    l++;

    }
    return true  
};