# Problem: Fraudulent Activity Notifications
# Link: https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
import time
from functools import cmp_to_key


def activityNotifications(expenditure, d):
    max_expenditure = max(expenditure[:d])
    count = [0] * (max_expenditure + 1)

    for i in range(d):
        count[expenditure[i]] += 1

    def find_median():
        if d % 2 == 0:
            first = d // 2
            second = first + 1
            count_sum = 0
            first_val = second_val = 0

            for i in range(len(count)):
                count_sum += count[i]
                if not first_val and count_sum >= first:
                    first_val = i
                if count_sum >= second:
                    second_val = i
                    break
            return (first_val + second_val) / 2
        else:
            target = (d + 1) // 2
            count_sum = 0
            for i in range(len(count)):
                count_sum += count[i]
                if count_sum >= target:
                    return i

    notifications = 0
    for i in range(d, len(expenditure)):
        median = find_median()

        if expenditure[i] >= 2 * median:
            notifications += 1

        count[expenditure[i - d]] -= 1

        if expenditure[i] >= len(count):
            count.extend([0] * (expenditure[i] - len(count) + 1))

        count[expenditure[i]] += 1
    return notifications


if __name__ == "__main__":
    start_time = time.time()
    n = 9
    d = 5
    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    result = activityNotifications(expenditure, d)
    print(result)
    elapsed_time = time.time() - start_time
    print(f"--- {elapsed_time:.4f} seconds ---")
