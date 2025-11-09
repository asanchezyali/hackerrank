# Top Competitors
# url: https://www.hackerrank.com/challenges/full-score/problem

SELECT 
    Hackers.hacker_id, 
    Hackers.name
FROM Submissions 
INNER JOIN Challenges 
    ON Submissions.challenge_id = Challenges.challenge_id
INNER JOIN Difficulty 
    ON Challenges.difficulty_level = Difficulty.difficulty_level
INNER JOIN Hackers
    ON Submissions.hacker_id = Hackers.hacker_id
WHERE Submissions.score = Difficulty.score
GROUP BY Hackers.hacker_id, Hackers.name
HAVING COUNT(*) > 1 
ORDER BY COUNT(*) DESC, Hackers.hacker_id ASC;