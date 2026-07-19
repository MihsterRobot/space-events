def validate_asteroid_record(record: dict) -> bool:
    '''Validate a single asteroid record.

    Args:
        record: A dictionary representing an asteroid record.

    Returns:
        True if the record is valid, False otherwise.
    '''
    required_keys = {'id', 'name', 'absolute_magnitude_h', 'is_potentially_hazardous_asteroid', 'close_approach_data'}

    if not required_keys.issubset(record.keys()) or any(record[key] is None for key in required_keys):
        return False

    close_approach_data = record['close_approach_data']

    if not isinstance(close_approach_data, list) or not close_approach_data:
        return False

    close_approach = close_approach_data[0]
    miss_distance = close_approach.get('miss_distance', {})
    relative_velocity = close_approach.get('relative_velocity', {})

    required_close_approach_keys = {'close_approach_date', 'miss_distance', 'relative_velocity'}

    if not required_close_approach_keys.issubset(close_approach.keys()) or any(close_approach[key] is None for key in required_close_approach_keys):
        return False

    if miss_distance.get('kilometers') is None or relative_velocity.get('kilometers_per_hour') is None:
        return False

    return True
