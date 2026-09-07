scores = [85, 72, 91, 64, 78, 88, 95, 70, 83, 76]
def calculate_average(scores):
    total = 0

    for score in scores:
        total = total + score         


    return total/ len(scores)
def count_passing(scores):
    count = 0

    for score in scores:
        if score >= 70:
            count = count + 1

    return count

average = calculate_average(scores)
highest = max(scores)
lowest = min(scores)
passing = count_passing(scores)

print("Student Grade analysis")
print("The result")
print("Average: ",average)
print("highest: ",highest)
print("lowest: ",lowest)
print("students passing: ",passing)
