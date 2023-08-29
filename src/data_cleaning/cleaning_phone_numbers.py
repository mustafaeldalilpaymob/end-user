
import unicodedata
import phonenumbers



def cleaning_special_characters(phone_number):
    """Clean given phone number from any special characters

    Args:
        phone_numbers (str): containing phone numbers that may contain special characters
    Returns: 
        Cleaned version of the given phone numbers
        
    """

    return (phone_number.str.replace("[()\s.+-]", "", regex=True)
                                               .str.replace("[⁰#!'*,/]", "", regex=True)
                                               .str.strip())


def translate_arabic_number(arabic_number):
    """Translate arabic phone numbers to english

    Args:
        arabic_number (string): arabic version of the phone number

    Returns:
        phone_number: english version of the phone number
    """
    return ''.join(
        str(unicodedata.digit(ch))
        for ch in arabic_number
        if unicodedata.category(ch) == 'Nd'
    )

def apply_translate(df, column_name):
    """Apply translate function on a given dataframe

    Args:
        df (DataFrame): Dataframe containing data related to phone numbers
        column_name (str): name of the column containing data about phone numbers

    Returns:
        df: DataFrame with the translated column
    """
    try:
        df[column_name + '_translated'] = df[column_name].apply(translate_arabic_number)
    except :
        df[column_name + '_translated'] =  df[column_name]
    return df

def remove_leading_zeros(s):
    """Remove leading zeros for any phone number

    Args:
        s (str): Phone number that might contain leanding zeros

    Returns:
        phone_number: Phone number after leading zeros removal
    """
    # Count the number of leading zeros
    try:
        leading_zeros = len(s) - len(s.lstrip('0'))
    except:
        return s
    
    # If the number of leading zeros is more than 1, remove them
    if leading_zeros > 1:
        return s.lstrip('0')
    
    # Otherwise, return the original string
    return s


def remove_single_numbers(s):
    """Remove any phone number with only one number in it

    Args:
        s (str): Phone number that might contain just 1 number

    Returns:
        phone_number: Only phone numbers with more than 2 numbers 
    """
    # If the string consists of only one digit, return an empty string
    try:
        s = s.lstrip('0')
    except:
        return s
    if len(set(s)) == 1:
        return ''
       
    return s

def region_codes_json(region_codes):
    """Get the country codes for a given regions

    Args:
        region_codes (list): list of regions to get the country code for
    Returns:
        Dictionay (dict): containig the country code per given region
    """

    country_codes = []
    for region_code in region_codes:
        country_codes.append( str(phonenumbers.country_code_for_region(region_code))) 
    code_dict = dict(zip(region_codes, country_codes))
    return code_dict



def get_region(number, code_dict):
    """Functions that returns the country code of the phone number based on the phone number

    Args:
        number (str): Phone numbers that might include country code

    Returns:
        country_code(str): country code associated with a given phone number
    """
    for region, code in code_dict.items():
        #print(code)
        if str(number).strip().startswith(code):
            if region == 'EG':
                return  number[1:]
            else: 
                return code

def removes_country_code(number, code_dict):
    """Functions that removes the country code of the phone number based on the phone number

    Args:
        number (str): Phone numbers that might include country code

    Returns:
        number(str): phone number without the country code
    """
    for region, code in code_dict.items():
        #print(code)
        if str(number).strip().startswith(code):
            if region == 'EG':
                return  number[1:]
            else: 
                return number[len(code):]
                