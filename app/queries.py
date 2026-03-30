GET_ADS = """
SELECT *
FROM ad
WHERE deleted_at IS NULL
"""