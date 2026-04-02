GET_ADS = """
SELECT title
FROM ads
WHERE deleted_at IS NULL
AND title REGEXP '[^a-z]';
"""

GET_ALIVE_ADS = """
SELECT title  
FROM ads  
WHERE status = 'accepted' 
AND deleted_at IS NULL
AND title REGEXP '[^a-z]';
"""