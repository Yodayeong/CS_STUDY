## Greedy - 허프만 코드

데이터 파일을 효율적으로 encoding 하기 위한 방법을 찾아내는 문제

<br>

- 길이가 고정된 이진 코드

  : 길이가 고정된 이진 코드는 각각의 문자를 표현하는 비트의 개수가 일정함

  ``````
  ex) a: 00, b: 01, c: 10
  => abcabcbbb: 총 18개의 비트가 필요
  ``````

- 길이가 변하는 이진 코드

  : 길이가 변하는 이진 코드는 각각의 문자를 표현하는 비트의 개수가 가변적임

  => 더 효율적

  ``````
  ex) a: 10, b: 0, c: 11
  => abcabcbbb: 총 13개의 비트가 필요
  ``````

<br>

**허프만 알고리즘**: 탐욕법을 이용해서 최적 코드에 해당하는 이진트리를 만들어서 최적 이진 문자 코드를 만드는 것

=> min heap을 이용하여 priority queue를 만들고, 빈도수가 낮은 문자를 우선순위가 높은 순위로, 우선순위가 가장 높은 원소가 먼저 빠져나간다.

``````
1. 우선순위가 높은 두 개의 원소를 뺀다.
2. 두 개의 원소를 자식으로 가지는 원소를 만든다. 해당 원소의 빈도수는 자식 빈도 수의 합과 같다.
3. 새롭게 만든 원소를 다시 우선 순위 큐에 넣는다.
4. 원소의 개수가 n개라면 n-1번 반복한다.
``````

<br>

**허프만 코드와 허프만 알고리즘**

> **Description**
>
> 교재와 강의자료를 참고하여 허프만 코드 트리를 생성하는 허프만 알고리즘의 구현을 완성하시오.
>
> 허프만 트리의 리프 노드가 아닌 internal 노드들에는 심볼값으로 '+' 문자를 입력해 두도록 한다.
>
> 위 알고리즘을 통해 허프만 트리를 만들었다면, 문자열을 허프만 코드로 인코딩, 디코딩하는 알고리즘을 구현하시오.
>
> **Input**
>
> 첫째 줄에 문자의 개수 n이 주어진다.
>
> 둘째 줄에 n개의 문자가 주어진다.
>
> 문자는 알파벳 대문자, 또는 소문자로만 입력된다고 가정한다.
>
> 셋째 줄에 n개의 빈도값이 주어진다.
>
> 빈도값은 모두 양의 정수라고 가정한다.
>
> 다음 줄에 문자열의 개수 T1이 주어진다.
>
> 이후 T1개의 줄에 한 줄에 하나씩 텍스트 문자열이 주어진다.
>
> 다음 줄에 문자열의 개수 T2가 주어진다.
>
> 이후 T2개의 줄에 한 줄에 하나씩 허프만 코드 문자열이 주어진다.
>
> **Output**
>
> 첫째 줄에 허프만 트리의 preorder traversal 결과를 쓴다. (출력 포맷은 아래 출력 사례를 참조한다. 예외적으로 줄끝 공백이 있음에 주의한다.)
>
> 둘째 줄에 허프만 트리의 inorder traversal 결과를 쓴다.(출력 포맷은 아래 출력 사례를 참조한다.예외적으로 줄끝 공백이 있음에 주의한다.)
>
> 셋째 줄 이후로 T1개의 문자열을 인코딩한 허프만 코드를 한 줄에 하나씩 출력한다. (줄끝 공백이 없다.)
>
> 이후로 T2개의 허프만 코드를 디코딩한 텍스트 문자열을 한 줄에 하나씩 출력한다. (줄끝 공백이 없다.)
>
> **Sample Input 1**
>
> ```
> 6
> b e c a d f
> 5 10 12 16 17 25
> 5
> cab
> dec
> fad
> becadf
> fdaceb
> 5
> 110001110
> 011111110
> 100001
> 11101111110000110
> 10010011011111110
> ```
>
> **Sample Output 1**
>
> ```
> +:85 +:33 a:16 d:17 +:52 f:25 +:27 c:12 +:15 b:5 e:10 
> a:16 +:33 d:17 +:85 f:25 +:52 c:12 +:27 b:5 +:15 e:10 
> 110001110
> 011111110
> 100001
> 11101111110000110
> 10010011011111110
> cab
> dec
> fad
> becadf
> fdaceb
> ```

```cpp
//허프만 알고리즘
//길이가 변하는 코드를 효율적으로 encoding하기 위한 알고리즘

#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;

typedef struct node *node_ptr;
typedef struct node{
	char symbol;
	int frequency;
	node_ptr left;
	node_ptr right;
} node_t;

struct compare{
	//frequency 속성을 기준으로 노드들이 정렬됨
	//빈도수가 낮은 노드부터 우선순위 큐에서 추출됨
	bool operator() (node_ptr p, node_ptr q) {
		//작은 빈도수를 가지는 노드가, 우선순위가 더 높아서, 먼저 추출됨
		return p->frequency > q->frequency;
	}
};

//priority_queue<자료형, Compare, 비교함수>
//선언한 자료형 변수들을 비교함수에 따라 정렬하는 priority_queue
typedef priority_queue<node_ptr, vector<node_ptr>, compare> PriorityQueue;

node_ptr create_node(char symbol, int frequency) {
	node_ptr newNode = (node_ptr)malloc(sizeof(node_t));
	newNode->left = NULL;
	newNode->right = NULL;
	newNode->symbol = symbol;
	newNode->frequency = frequency;
	return newNode;
}

void huffman(int n, PriorityQueue& PQ) {
	for(int i = 0; i < n - 1; i++) {
		node_ptr p = PQ.top(); PQ.pop();
		node_ptr q = PQ.top(); PQ.pop();
		//두 노드를 합한 노드 생성
		node_ptr r = create_node('+', p->frequency + q->frequency);
		r->left = p;
		r->right = q;
		PQ.push(r);
	}
}

//허프만 트리를 root부터 순차적으로 돌면서 string을 이진코드로 변환
void make_encoder(node_ptr node, string code, map<char, string> &encoder) {
	if(node->symbol != '+') {
		//두 노드를 합한 노드가 아닌 경우,
		//encoder 맵에, 해당 노드의 symbol을 key값으로 가질때의 code값을 저장해준다.
		encoder[node->symbol] = code;
	} else {
		//두 노드를 합한 노드일때는, 왼쪽 오른쪽으로 가고 이를 code에 저장한다.
		make_encoder(node->left, code + "0", encoder);
		make_encoder(node->right, code + "1", encoder);
	}
}

//이진 코드를 문자열로 변경
//빈도수에 따라 이진코드를 부여했으므로, root노드부터 순회하면 된다.
void decode(node_ptr root, node_ptr node, string s, int i) {
	if(i <= s.length()) {
		if(node->symbol != '+') {
			//두 노드를 합한 노드가 아닐 때는,
			//해당 노드의 symbol을 출력한 후, 다시 root 노드로 돌아가면 된다.
			cout << node->symbol;
			decode(root, root, s, i);
		} else {
			//+ 노드가 아닐 때까지 순회한다.
			if(s[i] == '0') {
				decode(root, node->left, s, i + 1);
			} 
			else {
				decode(root, node->right, s, i + 1);
			}
		}
	}
}

void preorder(node_ptr root) {
	if(root) {
		cout << root->symbol << ":" << root->frequency << " ";
		preorder(root->left);
		preorder(root->right);
	}
}

void inorder(node_ptr root) {
	if(root) {
		inorder(root->left);
		cout << root->symbol << ":" << root->frequency << " ";
		inorder(root->right);
	}
}

int main() {
	int n, t1, t2;
	PriorityQueue PQ;
	node_ptr root;
	string T1[101], T2[101];
	cin >> n;

	vector<char> ch(n + 1, 0);
	vector<int> freq(n + 1, 0);
	for(int i = 0; i < n; i++) {
		cin >> ch[i];
	}
	for(int i = 0; i < n; i++) {
		cin >> freq[i];
	}

	cin >> t1;
	for(int i = 0; i < t1; i++) {
		cin >> T1[i];
	}
	cin >> t2;
	for(int i = 0; i < t2; i++) {
		cin >> T2[i];
	}

	for(int i = 0; i < n; i++) {
		node_ptr newNode = create_node(ch[i], freq[i]);
		PQ.push(newNode);
	}
	huffman(n, PQ);
	root = PQ.top();

	//1. 허프만 트리의 preorder traversal 결과 출력
	preorder(root);
	cout << "\n";

	//2. 허프만 트리의 inorder traversal 결과 출력
	inorder(root);
	cout << "\n";

	//3. T1개의 문자열을 인코딩한 허프만 코드 출력
	string code;
	map<char, string> res_encode;
	make_encoder(root, code, res_encode);
	for(int i = 0; i < t1; i++) {
		for(char &j: T1[i]) {
			auto temp = res_encode.find(j);
			for(int a: temp->second) {
				cout << a - '0';
			}
		}
		cout << "\n";
	}
	
	//4. T2개의 허프만 코드를 디코딩한 텍스트 문자열을 한 줄에 하나씩 출력
	for(int i = 0; i < t2; i++) {
		decode(root, root, T2[i], 0);
		cout << "\n";
	}
}
```

