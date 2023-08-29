import phonenumbers
from utils.constants import region_codes, phone_number_cleaned, is_phone_valid, country
import pandas as pd

def phone_number_validation(phone_number, region_codes):
    """Checks if a given phone number is valid in accordance to given region_codes using google phonenumbers library

    Args:
        phone_number (str): cleaned phone number string to be checked
        region_codes (list): list of supported region codes

    Returns:
        flag (bool): indicating whether the given phone number is valid
        region(str): region is returned for valid phone numbers
    """
    flag = False
    region = None
    for region in (region_codes):
        try:
            parsed_number = phonenumbers.parse(phone_number, region)
        except:
            continue
        flag = phonenumbers.is_valid_number(parsed_number)
        if flag == True:
            break
    return flag, region

def apply_phone_number_validation(phone_numbers):
    """Apply phone validation using phone_number_validation func

    Args:
        phone_numbers (list): list of phone numbers to be validated
    Returns:
        df (DataFrame): containing all phone numbers and a flag indicating whether this phone number is valid.
    """
    is_valid_phone_number = {}
    for ind, ph in enumerate(phone_numbers):
        # if ind % 2 == 0:
        #     print(ind)
        flag,region = phone_number_validation(ph)
        is_valid_phone_number[ph] = [flag, region]  
    df = pd.DataFrame(is_valid_phone_number.items())
    df.columns = [phone_number_cleaned, 'agg']
    df[is_phone_valid] = phone_number_validity.iloc[:, 1].apply(lambda x:x[0])
    df[country] = phone_number_validity.iloc[:, 1].apply(lambda x:x[1])

    df = df[[phone_number_cleaned, is_phone_valid, country]]
    return df

def merge_validation_results(non_checked_phone_numbers, checked_phone_numbers):
    """Merge the transactional data with the phone numbers after checks to check transactions with valid phone numbers

    Args:
        non_checked_phone_numbers (DataFrame): Transactional data that contains cleaned_version of the phone number
        checked_phone_numbers (DataFrame): checked data containing cleaned_version of the phone number and flag indicating its validity

    Returns:
        df: containing transactions flagged with the validity of the phone number associated with each transaction.
    """
    return pd.merge(non_checked_phone_numbers, checked_phone_numbers, on = phone_number_cleaned, how = 'left')
