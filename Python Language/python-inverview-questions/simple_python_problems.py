### **1. Palindrome Check**
**Problem**: Determine if a string/number reads the same backward as forward (e.g., "madam", 121).

#### **Solution**:
```python
# Method 1: String slicing
def is_palindrome(s):
    s = str(s).lower().replace(" ", "")  # Handle numbers/spaces
    return s == s[::-1]

# Method 2: Two-pointer approach (efficient for large strings)
def is_palindrome_two_pointers(s):
    s = str(s).lower().replace(" ", "")
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("A man a plan a canal Panama"))  # True
```

---

### **2. Fibonacci Sequence**
**Problem**: Generate the Fibonacci sequence up to `n` terms (e.g., 0, 1, 1, 2, 3, 5...).

#### **Solution**:
```python
# Method 1: Iterative (efficient)
def fibonacci_iterative(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# Method 2: Recursive (inefficient for large n)
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_iterative(5))  # [0, 1, 1, 2, 3]
```

---

### **3. Reverse Items**
**Problem**: Reverse a string, list, or array.

#### **Solutions**:
```python
# Reverse a string
s = "hello"
reversed_str = s[::-1]  # "olleh"

# Reverse a list in-place
lst = [1, 2, 3]
lst.reverse()  # [3, 2, 1]

# Reverse using slicing
reversed_lst = lst[::-1]

# Reverse a number
num = 123
reversed_num = int(str(num)[::-1])  # 321
```

---

### **4. Odd Numbers**
**Problem**: Extract odd numbers from a list or range.

#### **Solution**:
```python
# Using list comprehension
numbers = [1, 2, 3, 4, 5]
odds = [x for x in numbers if x % 2 != 0]  # [1, 3, 5]

# Using filter
odds = list(filter(lambda x: x % 2 != 0, numbers))
```

---

### **5. Prime Numbers**
**Prime Number**: A number >1 divisible only by 1 and itself (e.g., 2, 3, 5, 7).

#### **Check if a number is prime**:
```python
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:  # 2 is the only even prime
        return True
    if n % 2 == 0:  # Eliminate even numbers
        return False
    for i in range(3, int(n**0.5) + 1, 2):  # Check up to sqrt(n)
        if n % i == 0:
            return False
    return True

print(is_prime(17))  # True
```

#### **Generate primes up to N**:
```python
# Sieve of Eratosthenes (efficient)
def primes_up_to(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i : n+1 : i] = [False] * len(sieve[i*i : n+1 : i])
    return [i for i, is_prime in enumerate(sieve) if is_prime]

print(primes_up_to(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
```

---

### **6. Additional Common Problems**
#### **FizzBuzz**:
```python
def fizzbuzz(n):
    result = []
    for i in range(1, n+1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        result.append(s if s else i)
    return result

print(fizzbuzz(5))  # [1, 2, 'Fizz', 4, 'Buzz']
```

#### **Find Missing Number**:
```python
def missing_number(arr):
    n = len(arr)
    total = n * (n + 1) // 2  # Sum of first n integers
    return total - sum(arr)

print(missing_number([3, 0, 1]))  # 2
```

---

### **Key Takeaways**
1. **Palindrome**: Use slicing or two-pointers for efficiency.
2. **Fibonacci**: Prefer iterative over recursive to avoid O(2^n) time.
3. **Reverse**: Use slicing (`[::-1]`) for simplicity.
4. **Odd Numbers**: Filter using `% 2 != 0`.
5. **Prime Numbers**: Optimize with the Sieve of Eratosthenes or check up to `sqrt(n)`.

Practice these patterns and understand the underlying logic. For interviews, always **test edge cases** (empty input, zero, negative numbers). 🚀
