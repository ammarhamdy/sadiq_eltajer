GET_ADS = """
SELECT title
FROM ads
WHERE deleted_at IS NULL
AND title REGEXP '[^a-z]';
"""