# Contest Leaderboard
# URL: https://www.hackerrank.com/challenges/contest-leaderboard/problem

SELECT 
    H.HACKER_ID, 
    H.NAME,
    SUM(M.max_score) AS TOTAL_SCORE
FROM HACKERS H
INNER JOIN (
    SELECT 
        HACKER_ID,
        CHALLENGE_ID,
        MAX(SCORE) AS max_score
    FROM SUBMISSIONS
    GROUP BY HACKER_ID, CHALLENGE_ID
) AS M
    ON H.HACKER_ID = M.HACKER_ID
GROUP BY H.HACKER_ID, H.NAME
HAVING TOTAL_SCORE > 0
ORDER BY TOTAL_SCORE DESC, H.HACKER_ID ASC;