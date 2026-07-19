from datetime import datetime


def transform_asteroid_records(response: dict) -> list[dict]:
    '''Extract and reshape raw NeoWs asteroid records into a format suitable for the Asteroid table.
    
    Args:
        response: A dictionary containing asteroid records for a given date range.

    Returns:
        A list containing the transformed records.
    '''
    records = []

    for daily_records in response['near_earth_objects'].values():
        records.extend(daily_records)
    
    transformed_records = []
    for record in records:
        transformed_records.append({
            'name': record['name'],
            'nasa_id': record['id'],
            'close_approach_date': datetime.strptime(record['close_approach_data'][0]['close_approach_date'], '%Y-%m-%d'),
            'miss_distance_km': float(record['close_approach_data'][0]['miss_distance']['kilometers']),
            'relative_velocity_kmh': float(record['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']),
            'is_potentially_hazardous': record['is_potentially_hazardous_asteroid'],
            'absolute_magnitude': record['absolute_magnitude_h']
        })
        
    return transformed_records
