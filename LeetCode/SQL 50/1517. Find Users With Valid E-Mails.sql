-- Runtime 604 ms, beats 98.46% of other submissions
SELECT * FROM USERS
WHERE REGEXP_LIKE(MAIL, "^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com$")
;

-- Explanation of regex
-- ^[A-Za-z] means the first character shouls be a letter.
-- [A-Za-z0-9_.-]* means the next characters can be any valid characters, repeated any number of times, * represents any number of repetitions, even 0
-- @leetcode means domain name should be there
-- [.] means after the domain name should come the dot. If we just write "@leetcode.", this means, the character after leetcode will match with any character, valid or invalid.
-- com$ means this should be the end of the string.