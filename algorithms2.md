## Algorithms: Efficiency, Analysis, and Order - part2

#### 📌Algorithm Analysis

알고리즘 분석에는 두가지 방법이 있습니다.

- The correctness of an algorithm

  - 알고리즘이 수행해야 하는 일을 수행한다는 proof를 develop하면서 분석
  - 문제의 모든 경우에 항상 옳은 해결책을 찾는지 분석

  <br>

- The efficiency of an algorithm

  - 시간이나 공간적 측면에서 알고리즘이 효율적으로 문제를 해결하는지 분석
  - 효율성을 측정하는 방법
    - **특정 컴퓨터와 무관해야 한다.**
    - **특정 프로그래밍 언어와 무관해야 한다.**
    - **알고리즘의 복잡한 디테일과 무관해야 한다.**
  - **"Complexity Analysis(복잡도 분석) = 입력의 크기(input size)에 따른 단위 연산(basic operation)의 수행 횟수"**

<br>

#### 📌Complexity Analysis

알고리즘의 효율성을 증명하기 위한 전형적인 기법으로, 입력의 크기(input size)에 따른 단위 연산(basic operation)의 수행 횟수를 계산한다.

이때, 단위 연산은 합리적이게 정해야 한다. **알고리즘에 의해 수행된 작업은, basic operation의 연산 횟수에 대략적으로 비례해야 한다.**

Ex) Exchange Sort의 Complexity

![exchange_sort](algorithms.assets/exchange_sort.jpeg)

- input size 는 n이다.

- 단위 연산의 후보로는 비교연산과 swap연산이 있는데, 이 중 더 합리적인 연산은 비교연산이다. swap 연산은 리스트에 따라 수행 횟수가 다른데, 비교연산은 n의 크기에 종속적으로 변하기 때문이다.
- 가장 바깥 for문의 i가 1~n까지 변하므로, 
  - i가 1일 때, 비교연산의 수행횟수는 n-1
  - i가 2일 때, 비교연산의 수행횟수는 n-2
  - ...
  - i가 n일 때, 배교연산의 수행횟수는 1 로,
- exchange sort의 complexity = (n-1) + (n-2) + ... + 1 = 1/2(n)(n-1) 이 된다.