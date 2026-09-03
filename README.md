# Explanation

## 1. `range(8)`

```python
range(8)
```

Generates numbers from **0 to 7**:

```text
0, 1, 2, 3, 4, 5, 6, 7
```

---

## 2. Applying `filter()`

```python
filter(lambda n: n % 2, range(8))
```

The lambda function checks:

```python
n % 2
```

For each number:

| Number | Calculation | Result | Keep? |
| -----: | ----------: | -----: | :---: |
|      0 |     `0 % 2` |    `0` |   ❌   |
|      1 |     `1 % 2` |    `1` |   ✅   |
|      2 |     `2 % 2` |    `0` |   ❌   |
|      3 |     `3 % 2` |    `1` |   ✅   |
|      4 |     `4 % 2` |    `0` |   ❌   |
|      5 |     `5 % 2` |    `1` |   ✅   |
|      6 |     `6 % 2` |    `0` |   ❌   |
|      7 |     `7 % 2` |    `1` |   ✅   |

In Python, `0` is treated as **False**, while `1` is treated as **True**.

Therefore, `filter()` keeps only the **odd numbers**:

```text
1, 3, 5, 7
```

---

## 3. Applying `map()`

```python
map(lambda n: n // 2, ...)
```

Each filtered number is passed to:

```python
n // 2
```

The `//` operator performs **floor division**.

### Calculations

```text
1 // 2 = 0
3 // 2 = 1
5 // 2 = 2
7 // 2 = 3
```

So `map()` produces:

```text
0, 1, 2, 3
```

---

## 4. Applying `sum()`

The code then uses:

```python
sum(x)
```

This adds all the values produced by `map()`:

```text
0 + 1 + 2 + 3 = 6
```

---

## 5. Final Output

Therefore:

```python
x = map(lambda n: n // 2,
        filter(lambda n: n % 2, range(8)))

print(sum(x))
```

produces:

```text
6
```

### Final Answer

**Output:**

```text
6
```
