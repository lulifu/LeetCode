## Notes

- [Notes](#notes)
- [Syntax](#syntax)
  - [JavaScript Syntax](#javascript-syntax)
  - [Java Syntax](#java-syntax)
  - [Python Syntax](#python-syntax)
- [Algorithms](#algorithms)
  - [Fast Power](#fast-power)
  - [Binary Search](#binary-search)
  - [Priority Queue](#priority-queue)
  - [Bepth-First Search](#bepth-first-search)
  - [Breadth-First Search](#breadth-first-search)
  - [QuickSort](#quicksort)
  - [MergeSort](#mergesort)
  - [HeapSort](#heapsort)

## Syntax

### JavaScript Syntax

```js
// Char Code
var s = new Array(n).fill('1');
let size = s[i].charCodeAt() - '0'.charCodeAt();
s[j] = String.fromCharCode('0'.charCodeAt() + diff);
```

### Java Syntax

```java
// Max Min
int maxn = Integer.MIN_VALUE;
int minn = Integer.MAX_VALUE;
```

```java
//bit manipulate
chars[pos] = (char) (chars[pos] ^ 32); // switch a letter between upper or lower case
// ^ means XOR: Bitwise XOR also takes two equal-length bit patterns. If both bits in the compared position of the bit patterns are 0 or 1, the bit in the resulting bit pattern is 0, otherwise 1.
```

```java
Map<Character, Integer> freq = new HashMap<>();
Set<Map.Entry<Character, Integer>> entrySet = freq.entrySet();
for (Map.Entry<Character, Integer> entry: entrySet) {
    int value = entry.getValue();
}
```

```java
// String operations
chars = str.toCharArray();
new String(chars);
str.length();
str.charAt(index);
str.append("ab");
str.equals("target");
str.substring(begin, end);
StringBuilder ans = new StringBuilder();
ans.toString();
// character
Character.isDigit(chars[pos]);
Character.isLetter(chars[pos]);
```

```java
// int[][]
int[][] dirs = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
// List
n = ls.size();
elem = ls.get(idx);
// queue
Queue<int[]> queue = new ArrayDeque<int[]>();
while (!queue.isEmpty())
int[] cell = queue.poll();
queue.offer(new int[]{nx, ny});
```

```java
// sort of complexity object
Arrays.sort(jobs, (a,b)->a[1]-b[1]); // ascending order
Arrays.sort(people, new Comparator<int[]>() {
    public int compare(int[] people1, int[] people2) {
        if (people1[0] != people2[0]) return people1[0] - people2[0]; // people[0] in ascending order
        else return people2[1] - people1[1]; // people[1] in descending order
        // empty before is higher than or equal to, occupied before is lower
    }
});
```

```java
HashMap <Integer, Integer> mp = new HashMap<>();
mp.put(0, 1);
if (mp.containsKey(pre - k)) {
    count += mp.get(pre - k);
}
mp.put(pre, mp.getOrDefault(pre, 0) + 1);
```

```java
// monotonic stack
Deque<Integer> stack = new LinkedList<>(); // define stack
for (int i = 0; i < len; i++) {
    while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
        int preIdx = stack.pop();
        ans[preIdx] = i - preIdx;
    }
    stack.push(i);
    // stack operations:
    // stack.isEmpty(), stack.peek(), stack.pop(), stack.push()
}
```

### Python Syntax

```python
# HashMap counter
freq = collections.Counter(tasks)
maxExec = max(freq.values())
```

```python
# stack
stack = []
# stack operations:
# while stack, stack[-1]. stack.pop(), stack.append()
while stack and temperature > temperatures[stack[-1]]:
    prev_index = stack.pop()
    ans[prev_index] = i - prev_index
stack.append(i)
```

## Algorithms

### Fast Power

```ts
// 70. climbing stairs
function climbStairs(n: number): number {
    // f(1) = f(0) = 1
    // f(n) = f(n-1) + f(n-2)
    // f(n+1) =  1 1   f(n)     = 1 1 (n)   f(1)
    // f(n)   =  1 0   f(n-1)   = 1 0       f(0)
    const p: number[][] = [[1,1],[1,0]];
    let res = pow(p, n);
    return res[1][0] + res[1][1];

    // fast power: Time Complexity O(logn)
    function pow(p: number[][], n: number): number[][] {
        let ret = [[1,0],[0,1]];
        while (n > 0) {
            if ((n & 1) === 1) {
                ret = multiple(ret, p);
            }
            n >>= 1;
            p = multiple(p, p);
        }
        return ret;
    }

    function multiple(p: number[][], q: number[][]): number[][] {
        let ret = new Array(2).fill(0).map(() => new Array(2).fill(0));
        for (let i = 0; i < 2; i++) {
            for (let j = 0; j < 2; j++) {
                ret[i][j] = p[i][0] * q[0][j] + p[i][1] * q[1][j];
            }
        }
        return ret;
    }
};
```

### Binary Search

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

```ts
// LeetCode 034 Find First and Last Position of Element in Sorted Array
function searchRange(nums: number[], target: number): number[] {
    let n: number = nums.length, ans: number[] = [-1, -1];
    if (n == 0) return ans;
    // find the first position of target
    let l: number = 0, r: number = n - 1;
    while (l < r) {
        let mid = l + ((r - l) >> 1);
        if (nums[mid] >= target) r = mid;
        else l = mid + 1;
    }
    if (nums[r] != target) return ans;
    else ans[0] = r;
    // finde the last position of target
    l = 0; r = n - 1;
    while (l < r) {
        let mid = l + ((r - l + 1) >> 1);
        // note (r - l + 1). Without  + 1, `r = mid` maybe cause infinite loop.
        if (nums[mid] <= target) l = mid;
        else r = mid - 1;
    }
    ans[1] = r;
    return ans;
};
```

### Priority Queue

```java
public int popMaxHeap(int[] a, int heapSize) {
    swap(a, 0, heapSize - 1);
    maxHeapify(a, 0, heapSize - 2);
    return a[heapSize - 1];
}

public void buildMaxHeap(int[] a, int heapSize) {
    for (int i = heapSize / 2; i >= 0; --i) {
        maxHeapify(a, i, heapSize);
    } 
}

public void maxHeapify(int[] a, int i, int heapSize) {
    // shift down at a[i]
    int l = i * 2 + 1, r = i * 2 + 2, largest = i;
    if (l < heapSize && a[l] > a[largest]) {
        largest = l;
    } 
    if (r < heapSize && a[r] > a[largest]) {
        largest = r;
    }
    if (largest != i) {
        swap(a, i, largest);
        maxHeapify(a, largest, heapSize);
    }
}

public void swap(int[] a, int i, int j) {
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}
```

### Bepth-First Search

```java
public void dfs(int x, int y, int[][] grid, Queue<int[]> queue) {
    if (x < 0 || y < 0 || x >= grid.length || y >= grid[0].length || grid[x][y] != 1) return;
    queue.offer(new int[]{x, y});
    grid[x][y] = -1; // explored
    dfs(x - 1, y, grid, queue);
    dfs(x + 1, y, grid, queue);
    dfs(x, y - 1, grid, queue);
    dfs(x, y + 1, grid, queue);
}
```

### Breadth-First Search

```java
while (!queue.isEmpty()) {
    int sz = queue.size();
    for (int k = 0; k < sz; k++) {
        int[] cell = queue.poll();
        int x = cell[0], y = cell[1];
        for (int d = 0; d < 4; d++) {
            int nx = x + dirs[d][0];
            int ny = y + dirs[d][1];
            if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
                if (grid[nx][ny] == 0) {
                    queue.offer(new int[]{nx, ny});
                    grid[nx][ny] = -1;
                } else if (grid[nx][ny] == 1) {
                    return step;
                }
            }
        }
    }
}
```

### QuickSort

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    
    def quickSort(self, nums, left, right):
        if left < right:
            # randomly select pivot (in case of ascending or descending ording testing sample)
            pivotIndex = random.randint(left, right)
            storeIndex = self.partition(nums, left, right, pivotIndex)
            self.quickSort(nums, left, storeIndex - 1)
            self.quickSort(nums, storeIndex + 1, right)

    def partition(self, nums, left, right, pivotIndex):
        pivotValue = nums[pivotIndex]
        nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
        storeIndex = left
        for i in range(left, right):
            # when nums[i] == pivotValue, randomly put nums[i] to left or right side of pivot (in case of [2,2,2,...,2,2] testing sample)
            if nums[i] < pivotValue or (nums[i] == pivotValue and random.random() < 0.5):
                nums[i], nums[storeIndex] = nums[storeIndex], nums[i]
                storeIndex += 1
        nums[storeIndex], nums[right] = nums[right], nums[storeIndex]
        return storeIndex
```

### MergeSort

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums
    def mergeSort(self, nums, l, r):
        if l >= r: return
        mid = (l + r) // 2
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)
        temp = []
        i, j = l, mid + 1
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= r:
            temp.append(nums[j])
            j += 1
        nums[l: r + 1] = temp
```

### HeapSort

```python
class Solution:
    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 < heap_len:
            l, r = p * 2 + 1, p * 2 + 2
            if heap_len <= r or heap[r] < heap[l]:
                nex = l
            else:
                nex = r
            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break
        
    def build_heap(self, heap):
        for i in range(len(heap) - 1, -1, -1):
            self.max_heapify(heap, i, len(heap))

    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)
            
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heap_sort(nums)
        return nums
```