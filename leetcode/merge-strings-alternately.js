/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    ans = []
    for (let i = 0; i < Math.min(word1.length, word2.length); i++) {
        ans.push(word1[i])
        ans.push(word2[i])
    }
    if (word1.length <= word2.length) {
        r = word1.length
        while (r < word2.length) {
            ans.push(word2[r])
            r++;
        }
    } else { 
        r = word2.length
        while (r < word1.length) {
            ans.push(word1[r])
            r++;
        }

    }
  return ans.join('')  
};