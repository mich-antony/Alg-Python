# Blind 75 Python Concepts for Coding Interviews

## Introduction
The **Blind 75** is a curated list of 75 LeetCode problems covering essential coding patterns for technical interviews. This document outlines key Python concepts, code examples, alternative solutions, a summary, cheat sheet, and flashcards to aid your preparation.

---

## Key Python Concepts in Blind 75

### 1. Arrays and Lists
- **Concept**: Ordered collections for indexing and manipulation.
- **Use Case**: *Two Sum* - Find two numbers in an array summing to a target.
- **Code Example**:
  ```python
  def twoSum(nums: List[int], target: int) -> List[int]:
      hash_map = {}
      for i, num in enumerate(nums):
          complement = target - num
          if complement in hash_map:
              return [hash_map[complement], i]
          hash_map[num] = i
      return []
  ```
- **Alternative**:
  ```python
  def twoSum_brute(nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
          for j in range(i + 1, len(nums)):
              if nums[i] + nums[j] == target:
                  return [i, j]
      return []
  ```
- **Notes**: Hash maps reduce time from O(n²) to O(n).

### 2. Hash Maps (Dictionaries)
- **Concept**: Key-value pairs for O(1) lookups.
- **Use Case**: *Group Anagrams* - Group strings that are anagrams.
- **Code Example**:
  ```python
  from collections import defaultdict
  def groupAnagrams(strs: List[str]) -> List[List[str]]:
      anagram_map = defaultdict(list)
      for s in strs:
          sorted_s = ''.join(sorted(s))
          anagram_map[sorted_s].append(s)
      return list(anagram_map.values())
  ```
- **Alternative**:
  ```python
  def groupAnagrams_counter(strs: List[str]) -> List[List[str]]:
      from collections import Counter
      anagram_map = defaultdict(list)
      for s in strs:
          count = tuple(Counter(s).items())
          anagram_map[count].append(s)
      return list(anagram_map.values())
  ```
- **Notes**: Useful for grouping and frequency counting.

### 3. Two Pointers
- **Concept**: Two indices to traverse arrays, optimizing paired searches.
- **Use Case**: *Container With Most Water* - Maximize area between two lines.
- **Code Example**:
  ```python
  def maxArea(height: List[int]) -> int:
      left, right = 0, len(height) - 1
      max_area = 0
      while left < right:
          area = min(height[left], height[right]) * (right - left)
          max_area = max(max_area, area)
          if height[left] < height[right]:
              left += 1
          else:
              right -= 1
      return max_area
  ```
- **Alternative**:
  ```python
  def maxArea_brute(height: List[int]) -> int:
      max_area = 0
      for i in range(len(height)):
          for j in range(i + 1, len(height)):
              area = min(height[i], height[j]) * (j - i)
              max_area = max(max_area, area)
      return max_area
  ```
- **Notes**: Reduces time from O(n²) to O(n).

### 4. Sliding Window
- **Concept**: Variable-size window for subarray/substring problems.
- **Use Case**: *Longest Substring Without Repeating Characters*.
- **Code Example**:
  ```python
  def lengthOfLongestSubstring(s: str) -> int:
      char_index = {}
      max_length = 0
      left = 0
      for right in range(len(s)):
          if s[right] in char_index and char_index[s[right]] >= left:
              left = char_index[s[right]] + 1
          else:
              max_length = max(max_length, right - left + 1)
          char_index[s[right]] = right
      return max_length
  ```
- **Alternative**:
  ```python
  def lengthOfLongestSubstring_set(s: str) -> int:
      char_set = set()
      max_length = 0
      left = 0
      for right in range(len(s)):
          while s[right] in char_set:
              char_set.remove(s[left])
              left += 1
          char_set.add(s[right])
          max_length = max(max_length, right - left + 1)
      return max_length
  ```
- **Notes**: Tracks boundaries with sets or maps.

### 5. Binary Search
- **Concept**: Divides sorted arrays for O(log n) searches.
- **Use Case**: *Search in Rotated Sorted Array*.
- **Code Example**:
  ```python
  def search(nums: List[int], target: int) -> int:
      left, right = 0, len(nums) - 1
      while left <= right:
          mid = (left + right) // 2
          if nums[mid] == target:
              return mid
          if nums[left] <= nums[mid]:
              if nums[left] <= target < nums[mid]:
                  right = mid - 1
              else:
                  left = mid + 1
          else:
              if nums[mid] < target <= nums[right]:
                  left = mid + 1
              else:
                  right = mid - 1
      return -1
  ```
- **Alternative**:
  ```python
  def search_linear(nums: List[int], target: int) -> int:
      for i, num in enumerate(nums):
          if num == target:
              return i
      return -1
  ```
- **Notes**: Check for sorted halves in rotated arrays.

### 6. Depth-First Search (DFS)
- **Concept**: Explores branches fully before backtracking.
- **Use Case**: *Number of Islands* - Count islands in a grid.
- **Code Example**:
  ```python
  def numIslands(grid: List[List[str]]) -> int:
      if not grid:
          return 0
      rows, cols = len(grid), len(grid[0])
      islands = 0
      
      def dfs(i: int, j: int):
          if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
              return
          grid[i][j] = "#"  # Mark as visited
          dfs(i+1, j)
          dfs(i-1, j)
          dfs(i, j+1)
          dfs(i, j-1)
      
      for i in range(rows):
          for j in range(cols):
              if grid[i][j] == "1":
                  dfs(i, j)
                  islands += 1
      return islands
  ```
- **Alternative**:
  ```python
  from collections import deque
  def numIslands_bfs(grid: List[List[str]]) -> int:
      if not grid:
          return 0
      rows, cols = len(grid), len(grid[0])
      islands = 0
      
      def bfs(i: int, j: int):
          queue = deque([(i, j)])
          grid[i][j] = "#"
          while queue:
              x, y = queue.popleft()
              for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                  nx, ny = x + dx, y + dy
                  if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                      queue.append((nx, ny))
                      grid[nx][ny] = "#"
      
      for i in range(rows):
          for j in range(cols):
              if grid[i][j] == "1":
                  bfs(i, j)
                  islands += 1
      return islands
  ```
- **Notes**: DFS marks connected components.

### 7. Breadth-First Search (BFS)
- **Concept**: Explores nodes level by level.
- **Use Case**: *Word Ladder* - Shortest transformation sequence.
- **Code Example**:
  ```python
  from collections import deque
  def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
      if endWord not in wordList:
          return 0
      word_set = set(wordList)
      queue = deque([(beginWord, 1)])
      while queue:
          word, length = queue.popleft()
          if word == endWord:
              return length
          for i in range(len(word)):
              for c in 'abcdefghijklmnopqrstuvwxyz':
                  new_word = word[:i] + c + word[i+1:]
                  if new_word in word_set:
                      queue.append((new_word, length + 1))
                      word_set.remove(new_word)
      return 0
  ```
- **Alternative**:
  ```python
  def ladderLength_dfs(beginWord: str, endWord: str, wordList: List[str]) -> int:
      if endWord not in wordList:
          return 0
      word_set = set(wordList)
      
      def can_transform(w1, w2):
          return sum(c1 != c2 for c1, c2 in zip(w1, w2)) == 1
      
      def dfs(word, visited, depth):
          if word == endWord:
              return depth
          min_length = float('inf')
          for next_word in list(word_set):
              if can_transform(word, next_word) and next_word not in visited:
                  visited.add(next_word)
                  length = dfs(next_word, visited, depth + 1)
                  if length:
                      min_length = min(min_length, length)
                  visited.remove(next_word)
          return min_length if min_length != float('inf') else 0
      
      return dfs(beginWord, {beginWord}, 1)
  ```
- **Notes**: BFS ensures shortest paths.

### 8. Dynamic Programming (DP)
- **Concept**: Solves problems by breaking into subproblems.
- **Use Case**: *Coin Change* - Fewest coins for an amount.
- **Code Example**:
  ```python
  def coinChange(coins: List[int], amount: int) -> int:
      dp = [float('inf')] * (amount + 1)
      dp[0] = 0
      for i in range(1, amount + 1):
          for coin in coins:
              if i >= coin:
                  dp[i] = min(dp[i], dp[i - coin] + 1)
      return dp[amount] if dp[amount] != float('inf') else -1
  ```
- **Alternative**:
  ```python
  def coinChange_memo(coins: List[int], amount: int) -> int:
      memo = {}
      def dfs(amt):
          if amt == 0:
              return 0
          if amt < 0:
              return float('inf')
          if amt in memo:
              return memo[amt]
          min_coins = float('inf')
          for coin in coins:
              min_coins = min(min_coins, dfs(amt - coin) + 1)
          memo[amt] = min_coins
          return min_coins
      
      result = dfs(amount)
      return result if result != float('inf') else -1
  ```
- **Notes**: Bottom-up DP is often faster.

### 9. Linked Lists
- **Concept**: Nodes with values and pointers.
- **Use Case**: *Reverse Linked List*.
- **Code Example**:
  ```python
  class ListNode:
      def __init__(self, val=0, next=None):
          self.val = val
          self.next = next
  
  def reverseList(head: ListNode) -> ListNode:
      prev, curr = None, head
      while curr:
          next_temp = curr.next
          curr.next = prev
          prev = curr
          curr = next_temp
      return prev
  ```
- **Alternative**:
  ```python
  def reverseList_recursive(head: ListNode) -> ListNode:
      if not head or not head.next:
          return head
      new_head = reverseList_recursive(head.next)
      head.next.next = head
      head.next = None
      return new_head
  ```
- **Notes**: Practice pointer manipulation.

### 10. Trees and Binary Trees
- **Concept**: Hierarchical node structures.
- **Use Case**: *Invert Binary Tree*.
- **Code Example**:
  ```python
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right
  
  def invertTree(root: TreeNode) -> TreeNode:
      if not root:
          return None
      root.left, root.right = root.right, root.left
      invertTree(root.left)
      invertTree(root.right)
      return root
  ```
- **Alternative**:
  ```python
  from collections import deque
  def invertTree_iterative(root: TreeNode) -> TreeNode:
      if not root:
          return None
      queue = deque([root])
      while queue:
          node = queue.popleft()
          node.left, node.right = node.right, node.left
          if node.left:
              queue.append(node.left)
          if node.right:
              queue.append(node.right)
      return root
  ```
- **Notes**: Master recursion and BFS.

### 11. Graphs
- **Concept**: Nodes and edges, often adjacency lists.
- **Use Case**: *Course Schedule* - Detect cycle in prerequisites.
- **Code Example**:
  ```python
  from collections import deque, defaultdict
  def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
      graph = defaultdict(list)
      indegree = [0] * numCourses
      for course, prereq in prerequisites:
          graph[prereq].append(course)
          indegree[course] += 1
      
      queue = deque([i for i in range(numCourses) if indegree[i] == 0])
      count = 0
      while queue:
          node = queue.popleft()
          count += 1
          for neighbor in graph[node]:
              indegree[neighbor] -= 1
              if indegree[neighbor] == 0:
                  queue.append(neighbor)
      return count == numCourses
  ```
- **Alternative**:
  ```python
  def canFinish_dfs(numCourses: int, prerequisites: List[List[int]]) -> bool:
      graph = defaultdict(list)
      for course, prereq in prerequisites:
          graph[prereq].append(course)
      
      visited = set()
      rec_stack = set()
      
      def dfs(node):
          visited.add(node)
          rec_stack.add(node)
          for neighbor in graph[node]:
              if neighbor not in visited:
                  if not dfs(neighbor):
                      return False
              elif neighbor in rec_stack:
                  return False
          rec_stack.remove(node)
          return True
      
      for i in range(numCourses):
          if i not in visited:
              if not dfs(i):
                  return False
      return True
  ```
- **Notes**: BFS for topological sort, DFS for cycle detection.

### 12. Heap/Priority Queue
- **Concept**: Maintains min/max elements.
- **Use Case**: *Kth Largest Element in an Array*.
- **Code Example**:
  ```python
  import heapq
  def findKthLargest(nums: List[int], k: int) -> int:
      heap = []
      for num in nums:
          heapq.heappush(heap, num)
          if len(heap) > k:
              heapq.heappop(heap)
      return heap[0]
  ```
- **Alternative**:
  ```python
  def findKthLargest_sort(nums: List[int], k: int) -> int:
      return sorted(nums, reverse=True)[k-1]
  ```
- **Notes**: Heaps for top-k problems.

---

## Summary
The Blind 75 covers arrays, hash maps, two pointers, sliding windows, binary search, DFS, BFS, DP, linked lists, trees, graphs, and heaps. These patterns address time/space trade-offs, edge cases, and coding fluency. Practice recognizing patterns and optimizing solutions.

---

## Cheat Sheet
| **Concept**              | **Key Problems**                              | **Time Complexity**                     | **Tips**                                                                 |
|--------------------------|----------------------------------------------|----------------------------------------|--------------------------------------------------------------------------|
| Arrays/Lists             | Two Sum, Maximum Subarray                   | O(n) to O(n²)                          | Use hash maps for O(n) lookups.                                          |
| Hash Maps                | Group Anagrams, Valid Anagram               | O(n)                                   | Defaultdict and Counter simplify grouping.                               |
| Two Pointers             | Container With Most Water, 3Sum             | O(n)                                   | Look for sorted arrays or paired elements.                               |
| Sliding Window           | Longest Substring Without Repeating Chars   | O(n)                                   | Track window with pointers or sets/maps.                                 |
| Binary Search            | Search in Rotated Sorted Array              | O(log n)                               | Ensure data is sorted; handle edge cases.                                |
| DFS                      | Number of Islands, Word Search              | O(V + E) or O(rows * cols)             | Mark visited nodes to avoid cycles.                                      |
| BFS                      | Word Ladder, Rotting Oranges                | O(V + E)                               | Use queue for shortest paths.                                            |
| Dynamic Programming      | Coin Change, Longest Palindromic Substring  | O(n) to O(n²)                          | Identify subproblems; use memoization.                                   |
| Linked Lists             | Reverse Linked List, Merge Two Sorted Lists | O(n)                                   | Master pointer manipulation.                                             |
| Trees/Binary Trees       | Invert Binary Tree, LCA                     | O(n)                                   | Practice traversals; use recursion or BFS.                               |
| Graphs                   | Course Schedule, Clone Graph                | O(V + E)                               | Use adjacency lists; detect cycles.                                      |
| Heap/Priority Queue      | Kth Largest Element, Merge K Sorted Lists   | O(n log k)                             | Use heapq for min-heaps.                                                 |

---

## Flashcards
1. **Arrays/Lists**
   - **Q**: Find two numbers summing to a target?
   - **A**: Hash map for O(n).
   - **Example**: `hash_map[num] = i`.

2. **Hash Maps**
   - **Q**: Group anagrams?
   - **A**: Sort strings or use counts as keys.
   - **Example**: `anagram_map[sorted_s].append(s)`.

3. **Two Pointers**
   - **Q**: Maximize area between lines?
   - **A**: Move shorter line inward.
   - **Example**: `area = min(height[left], height[right]) * (right - left)`.

4. **Sliding Window**
   - **Q**: Longest substring without repeats?
   - **A**: Track characters, adjust window.
   - **Example**: `left = char_index[s[right]] + 1`.

5. **Binary Search**
   - **Q**: Search rotated array?
   - **A**: Check sorted half.
   - **Example**: `if nums[left] <= nums[mid]`.

6. **DFS**
   - **Q**: Count islands?
   - **A**: Mark connected '1's.
   - **Example**: `grid[i][j] = "#"`.

7. **BFS**
   - **Q**: Shortest word ladder?
   - **A**: Explore transformations level by level.
   - **Example**: `queue.append((new_word, length + 1))`.

8. **Dynamic Programming**
   - **Q**: Fewest coins for amount?
   - **A**: Minimize coins for sub-amounts.
   - **Example**: `dp[i] = min(dp[i], dp[i - coin] + 1)`.

9. **Linked Lists**
   - **Q**: Reverse linked list?
   - **A**: Adjust pointers iteratively/recursively.
   - **Example**: `curr.next = prev`.

10. **Trees**
    - **Q**: Invert binary tree?
    - **A**: Swap children recursively.
    - **Example**: `root.left, root.right = root.right, root.left`.

11. **Graphs**
    - **Q**: Detect cycle in course schedule?
    - **A**: Topological sort or DFS.
    - **Example**: `indegree[course] += 1`.

12. **Heap**
    - **Q**: Kth largest element?
    - **A**: Min-heap of size k.
    - **Example**: `heapq.heappush(heap, num)`.

---

## Interview Prep Tips
- **Patterns**: Recognize two pointers, DP, etc.
- **Trade-offs**: Optimize with hash maps or sorting.
- **Edge Cases**: Test empty inputs, extremes.
- **Mock Interviews**: Practice under time constraints.
- **Review**: Analyze mistakes to improve.
