/**
 * @param {number[][]} points
 * @return {number}
 */
var maxWidthOfVerticalArea = function(points) {
    maximum = -Infinity

    points.sort((a, b) => a[0] - b[0])

    for (let i = 0; i < points.length - 1; i++) 
    {
        maximum = Math.max(maximum, points[i + 1][0] - points[i][0])

    }
    return maximum
    
};