def bubble_sort(scores):
    n = len(scores)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if scores[j] > scores[j + 1]:

                scores[j], scores[j + 1] = scores[j + 1], scores[j]
    return scores
n = 5
scores = [55, 90, 70, 60, 80]
sorted_scores = bubble_sort(scores)
print("Sorted Scores:", sorted_scores)