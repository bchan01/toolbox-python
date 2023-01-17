from datetime import datetime

def is_within_range(date_range_str : str, today : datetime.date):
    result = {
        'start': None,
        'end': None,
        'start_inclusive': False,
        'end_inclusive': False,
        'has_range': False
    }

    is_valid = lambda d : True

    # [|(start,end)]
    date_range_str = date_range_str.strip()

    if date_range_str == 'empty':
        return True

    result['start_inclusive'] = True if date_range_str.startswith('[') else False
    result['end_inclusive'] = True if date_range_str.endswith(']') else False

    # Remove 
    date_range_raw = date_range_str.replace("[", '').replace('(', '').replace(']', '').replace(')', '').strip()

    # Permutations: 
    # empty, (None, None)
    # [d1, d2], [d1,], [,d2]
    #print(f"raw: {date_range_raw}")
   
    if date_range_raw.startswith(','):
        # end only
        d = date_range_raw.replace(',', '').strip()
        result['end'] = datetime.strptime(d, '%Y-%m-%d').date()
        result['has_range'] = True
        is_valid  = (lambda d : d <= result['end']) if result['end_inclusive'] else (lambda d : d < result['end'])
    elif date_range_raw.endswith(','):
        # start only
        d = date_range_raw.replace(',', '').strip()
        result['start'] = datetime.strptime(d, '%Y-%m-%d').date()
        result['has_range'] = True
        is_valid = (lambda d : d >= result['start']) if result['start_inclusive'] else (lambda d : d > result['start'])
    else:
        # start and end
        parts = date_range_raw.split(',')
        if parts[0].strip() != 'None':
            result['start'] = datetime.strptime(parts[0].strip(), '%Y-%m-%d').date()
            result['has_range'] = True
        if parts[1].strip() != 'None':
            result['end'] = datetime.strptime(parts[1].strip(), '%Y-%m-%d').date()
            result['has_range'] = True

        # Permutations: start <= d <= end, start <= d < end, start < d <= end, start < d < end
        if  result['has_range']:
            if result['start_inclusive'] and result['end_inclusive']:
                is_valid  = (lambda d :  result['start'] <= d <= result['end'])
            elif result['start_inclusive'] and not result['end_inclusive']:
                is_valid = (lambda d :  result['start'] <= d < result['end']) 
            elif not result['start_inclusive'] and result['end_inclusive']:
                is_valid = (lambda d :  result['start'] < d <= result['end']) 
            else:
                is_valid  = (lambda d :  result['start'] < d < result['end']) 
    
    return is_valid(today)

