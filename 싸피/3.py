#SWEA 1983

def count_score(mid, final, assignment):
    return 0.35 * mid + 0.45 * final + 0.2 * assignment
    
T = int(input())
grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for _ in range(1, T + 1):
    scores = []
    n, idx = map(int, input().split())
    
    for i in range(n):
        mid, final, assignment = map(int, input().split())
        scores.append(count_score(mid, final, assignment))
        
    find_score = scores[idx - 1]
    scores.sort(reverse=True)
    num_of_people = n // 10
    final_idx = scores.index(find_score) // num_of_people
    print(f"#{_} {grades[final_idx]}")