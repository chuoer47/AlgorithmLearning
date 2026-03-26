# 基本语法和常用的库

## 入门语法

```c++
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n; // 录入
    cout << n; // 输出
    return 0;
}
```

## 系统自带库

### STL库

（有python基础可以快速上手）

> [C++ STL 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/cplusplus/cpp-stl-tutorial.html)

1. vector
- push_back()

- pop_back()

- size()

- clear() ： 复杂度为O(N) 

- insert() ：v.insert(v.begin()+2,-1); //将-1插入v[2]的位置

- erase() 
  
  > //删除v[3
  >
  > v.erase(v.begin()+3);
  >
  > //删除v[1]到v[4]的元素
  >
  > v.erase(v.begin()+1,v.begin()+4);

2. deque（双端队列，一个顶俩）

常用函数
- push_back() / push_front()

- pop_back() / pop_front()
- size()
- clear()
- empty()
- front() / back()

3. priority_queue  堆

- `empty()`: 检查队列是否为空。
- `size()`: 返回队列中的元素数量。
- `top()`: 返回队列顶部的元素（不删除它）。
- `push()`: 向队列添加一个元素。
- `pop()`: 移除队列顶部的元素。

```c++
priority_queue<int> pq; // 大顶堆
std::priority_queue<int, std::vector<int>, greater<int>() > pq_min; // 小顶堆
```

4. `set`

- `insert(元素)`: 插入一个元素。
- `erase(元素)`: 删除一个元素。
- `find(元素)`: 查找一个元素。
- `size()`: 返回容器中元素的数量。
- `empty()`: 检查容器是否为空。

```c++
    // 查找元素
    if (mySet.find(20) != mySet.end()) {
        std::cout << "20 is in the set." << std::endl;
    } else {
        std::cout << "20 is not in the set." << std::endl;
    }

    // 删除元素
    mySet.erase(20);
```

5. `unordered_set`

与`set`类似

6. `unordered_map`

与set类似的语法使用

7. `bitset` 

```
#include <iostream>
#include <bitset>

int main() {
    std::bitset<8> b1("10101010");
    std::bitset<8> b2("11110000");

    // 位与操作
    std::bitset<8> b_and = b1 & b2;
    std::cout << "Bitwise AND: " << b_and << std::endl;

    // 位或操作
    std::bitset<8> b_or = b1 | b2;
    std::cout << "Bitwise OR: " << b_or << std::endl;

    // 位异或操作
    std::bitset<8> b_xor = b1 ^ b2;
    std::cout << "Bitwise XOR: " << b_xor << std::endl;

    // 位非操作
    std::bitset<8> b_not = ~b1;
    std::cout << "Bitwise NOT: " << b_not << std::endl;

    return 0;
}
```

### `algorithm`库

```c++
sort(container.begin(), container.end(), compare_function); // 排序
auto it = find(container.begin(), container.end(), value); // 查找
copy(source_begin, source_end, destination_begin); // 复制，相当于python切片
bool result = equal(first1, last1, first2, compare_function); // 比较两个容器是否相等
```

### String库

```c++
#include <iostream>
#include <string>

int main() {
    std::string str = "Hello, World!";
    
    // size()
    std::cout << "Length: " << str.size() << std::endl;

    // empty()
    std::cout << "Is empty? " << (str.empty() ? "Yes" : "No") << std::endl;

    // operator[]
    std::cout << "First character: " << str[0] << std::endl;

    // at()
    std::cout << "Character at position 7: " << str.at(7) << std::endl;

    // substr()
    std::string sub = str.substr(7, 5);
    std::cout << "Substring from position 7 with length 5: " << sub << std::endl;

    // find()
    size_t pos = str.find("World");
    std::cout << "Position of 'World': " << pos << std::endl;

    // replace()
    str.replace(pos, 5, "C++");
    std::cout << "Modified string: " << str << std::endl;

    // append()
    str.append(" How are you?");
    std::cout << "Appended string: " << str << std::endl;

    // insert()
    str.insert(7, " Beautiful");
    std::cout << "String after insert: " << str << std::endl;

    // erase()
    str.erase(7, 10);
    std::cout << "String after erase: " << str << std::endl;

    // clear()
    str.clear();
    std::cout << "String after clear: " << (str.empty() ? "Empty" : "Not empty") << std::endl;

    // c_str()
    str = "Hello, C++!";
    const char* cstr = str.c_str();
    std::cout << "C-style string: " << cstr << std::endl;

    // compare()
    int cmp = str.compare("Hello, C++!");
    std::cout << "Comparison result: " << cmp << std::endl;

    // find_first_of()
    size_t pos_first_vowel = str.find_first_of("aeiou");
    std::cout << "First vowel at position: " << pos_first_vowel << std::endl;

    // find_last_of()
    size_t pos_last_vowel = str.find_last_of("aeiou");
    std::cout << "Last vowel at position: " << pos_last_vowel << std::endl;

    // find_first_not_of()
    size_t pos_first_non_vowel = str.find_first_not_of("aeiou");
    std::cout << "First non-vowel at position: " << pos_first_non_vowel << std::endl;

    // find_last_not_of()
    size_t pos_last_non_vowel = str.find_last_not_of("aeiou");
    std::cout << "Last non-vowel at position: " << pos_last_non_vowel << std::endl;

    return 0;
}
```

### cmath库

- `abs(x)`：计算 `x` 的绝对值。
- `pow(x, y)`：计算 `x` 的 `y` 次幂。
- `sqrt(x)`：计算 `x` 的平方根。
- `sin(x)`：计算 `x` 的正弦值（`x` 以弧度为单位）。
- `cos(x)`：计算 `x` 的余弦值（`x` 以弧度为单位）。
- `tan(x)`：计算 `x` 的正切值（`x` 以弧度为单位）。
- `log(x)`：计算 `x` 的自然对数。
- `exp(x)`：计算 `e` 的 `x` 次幂。
- `fabs(x)`
- `__gcd(2,4)`
