def get_current_date():
    '''
    Get todays date in format YYYYMMDD
    Returns
    -------
    str
        Todays date in format YYYYMMDD.
    '''
    from datetime import datetime
    now = datetime.now()
    return now.strftime("%Y%m%d")