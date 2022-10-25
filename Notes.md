# Notes

## Java Syntax

```java
// String operations
str.length();
str.charAt(index);
str.append("ab");
str.substring(begin, end);
StringBuilder ans = new StringBuilder();
ans.toString();
```

```java
// int[][]
int[][] dirs = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
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

## Python Syntax

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

## Priority Queue

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
