GET_ADS = """
SELECT 
    title
FROM ads
WHERE deleted_at IS NULL
AND title REGEXP '[^a-z]';
"""

GET_ALIVE_ADS = """
SELECT
    ads.title,
    classifications.name AS classification,
    types.name AS type,
    ads.price,

    CASE ads.price_type
        WHEN 'negotiable' THEN 'سوم'
        WHEN 'fixed' THEN 'حد'
        WHEN 'ignore_negotiable' THEN 'علي السوم'
    END AS price_type,

    areas.name AS area,
    cities.name AS city,
    neighborhoods.name AS neighborhood,
    ads.number_of_rooms,
    ads.number_of_bathrooms,
    ads.area_by_meter,
    ads.street_frontage

FROM ads

INNER JOIN (
    SELECT MAX(id) AS id
    FROM ads
    WHERE status = 'accepted'
      AND deleted_at IS NULL
      AND title REGEXP '[^a-z]'
    GROUP BY title
) unique_ads
    ON unique_ads.id = ads.id

LEFT JOIN classifications
    ON classifications.id = ads.classification_id

LEFT JOIN types
    ON types.id = ads.type_id

LEFT JOIN areas
    ON areas.id = ads.area_id

LEFT JOIN cities
    ON cities.id = ads.city_id

LEFT JOIN neighborhoods
    ON neighborhoods.id = ads.neighborhood_id;
"""

GET_ALIVE_AREAS = """
SELECT id, name FROM areas WHERE deleted_at IS NULL AND is_active = 1
"""

GET_ALIVE_CITIES = """
SELECT id, name FROM cities WHERE deleted_at IS NULL AND is_active = 1
"""

GET_ALIVE_NEIGHBORHOODS = """
SELECT id, name FROM neighborhoods WHERE deleted_at IS NULL AND is_active = 1
"""

GET_ALIVE_TYPES = """
SELECT id, name FROM types WHERE deleted_at IS NULL AND is_active = 1
"""

GET_ALIVE_CLASSIFICATIONS = """
SELECT id, name FROM classifications WHERE deleted_at IS NULL AND is_active = 1
"""
