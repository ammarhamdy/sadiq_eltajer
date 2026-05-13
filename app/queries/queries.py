GET_ADS = """
SELECT 
    title
FROM ads
WHERE deleted_at IS NULL
AND title REGEXP '[^a-z]';
"""

GET_ALIVE_ADS = """
SELECT 
    title, 
    classification_id,
    type_id,
    price, 
    price_type, 
    area_id, 
    city_id, 
    neighborhood_id,
    number_of_rooms, 
    number_of_bathrooms, 
    area_by_meter, 
    street_frontage
FROM ads  
WHERE status = 'accepted' 
AND deleted_at IS NULL
AND title REGEXP '[^a-z]';
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
