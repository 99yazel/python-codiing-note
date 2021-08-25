- tuple:
  - 한번 선언된 값을 변경할 수 없다.
  - 리스트는 대괄호, 튜플은 소괄호
  - 리스트에 비해 상대적으로 공간 효율적
  - 튜플 사용 시 좋은 경우, 서로 다른 성질의 데이터를 묶어서 관리해야 할 때 (최단 경로 알고리즘)
  - 데이터의 나열을 해싱의 키 값으로 사용해야 할 때
  - 리스트보다 메모리를 효율적으로 사용해야 할 때
- 사전 자료형
  - O(1) 의 자료형 
  - dict() 로 초기화
  - if key in data: 
- 집합 자료형
  - set([1,2,2,3,3,3,4]) = {1,2,4}
  - | & -

- 리스트나 튜플은 순서가 있다.
- 사전 자료형과 집합 자료형은 순서가 없어서 인덱싱으로 값을 얻을 수 없다.

---

##### 프로그램 동작의 첫 번재 단계는 데이터를 입력 받거나 생성하는 것입니다.

- input() : 한 줄의 문자열을 입력 받는 함수입니다.
- map() : 리스트의 모든 원소를 대상으로 함수를 적용한다.

- 빠르게 입력받기 : 
  - sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용한다.
  - 단 입력 후 엔터가 줄바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용합니다.
---
```python3


```

---
f-string 방법
- 수 데이터를 문자열로 안바꿔도 됨.
---
```
if codition:
파이썬에서는 코드의 블록을 들여쓰기로 지정한다.
space * 4 
if elif else
```
---

비교 연산자

논리 연산자
- and
- or
- not

기타연산자
- in 연산자
- not in 연산자

pass 키워드.

---
## 반복문
 
for x in array:  
for i in range(0,10):  
continue  
break;  
중첩된 반복문

---
## 함수와 람다표현식  

def name():  
global 키워드  
여러 개의 반환값  
람다표현식 : 어떠한 함수 자체를 입력으로 받는 또 다른 함수에서 사용.  
ex) lambda x: x[1]  
map(lambda a,b : a + b, list1, list2 )

---
표준 라이브러리 
- 내장함수
  - sum()
  - min()
  - max()
  - eval()
  - sorted()
  - sorted() with key -> lambda 함수 형태 사용
- itertools : 반복되는 형태의 데이터를 처리 하기 위한 유용한 기능들을 제공
  - 순열과 조합 라이브러리
  - nPr : 순서 고려
  - from itertools import
  - nCr : 순서 무상관
  - from itertools import
- heapq : 힙 자료구조 제공
  - 일반적으로 우선순위 큐 기능을 구현하기 위해 사용
- bisect : 이진 탐색 기능 제공
- collections : 덱, 카운터 등의 유용한 자료구조를 포함
  - from collections import Counter
- math :  
  - gcd :최대 공약수,  
  - lcm :최소 공배수  



---