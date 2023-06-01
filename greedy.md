## The Greedy Approach

- 탐욕 알고리즘은 각 순간마다 **'최적의'** 선택을 한다.
- (locally optimal): 선택할 당시에는 최적
- (globally optimal): 그러나, 전체에서 최적인 해를 보장하진 않는다.
- => 해당 알고리즘이 항상 최적 해를 얻는지 점검해 줘야 한다.

<br>

**탐욕법의 반례**

Coins = [12, 10, 5, 1, 1, 1, 1]

Amount owed = 16 cents

- 탐욕법: [12, 1, 1, 1, 1]
- optimal change: [10, 5, 1]

<br>

**탐욕법의 방식**

- **Selection Procedure**: 최적을 선택하는 기준에 따라
- **Feasibility Check**: 집합이 반환해야 하는 값을 넘지 않는다면, 최적 해를 해당 집합에 추가
- **Solution Check**: 집합이 반환해야 하는 값과 같거나 더이상 해를 선택할 수 없다면, 해당 과정을 종료. 그렇지 않다면 다시 반복