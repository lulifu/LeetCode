# Notes

## Java Syntax

```java
// sort of complexity object
Arrays.sort(jobs, (a,b)->a[1]-b[1]); // ascending order
```

## Binary Search

```java
public int binarySearch(int[][] jobs, int right, int target) {
    // return the largest index of the element that is less than or equal to target
    // if not existing, return -1
    if (jobs[0][1] > target) return -1;
    int left = 0;
    while (left < right) {
        int mid = (right + left + 1) / 2; // ceiling as left = mid
        if (jobs[mid][1] > target) right = mid - 1;
        else left = mid;
        // make sure that left fits the constraint of less than or equal to, and return left
        // to avoid non-ternimal situation, there must are one = mid, one = +(-) 1
        // if left = mid, right = mid - 1, so mid should be ceiling(right + left) / 2
        // if right = mid, left = mid + 1, mid should be floor(right + left) / 2
    }
    return left; 
}
```
