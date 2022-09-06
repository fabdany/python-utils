import re

def strip_punc(s):
  """  Removes all punctuation characters from a string.
  """
  return re.sub(r'[^\w\s]', ' ', s)

def remove_prefix(str, prefix):
  """ removes a prefix from the beginning of a string
  """
  if str.startswith(prefix):
    str = str[len(prefix):]
  return str

def remove_suffix(str, suffix):
  """ removes a prefix from the beginning of a string
  """
  if str.endswith(suffix):
    str = str[:-len(suffix)]
  return str
 
def extract_string_path(string,sep):
  """ returns column_name from a string formed under the pattern path/to/column_name (to process Ona-generated data Files, no more than 3 levels)
  separator is given as an input 
  """
  col=string.split(sep)
  if len(col)==1:
    name=col[0]
  elif len(col)==2:
    name=col[1]
  elif len(col)==3:
    name=col[2]
  return name


def split_string(string,sep):
  """splits a string depending on what is the separator between its elements 
  return a list of strings 
  """
    return string.split(sep)
  
def check_validity_email(string):
    """Check if a string is a valid email, returns True or False
    """
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return (bool(re.match(pattern, string)) == True)
    
def check_validity_url(string):
    """Check if a string is a valid url, returns True or False
    check if url starts with https://, or http://, or www.
    or ends with a dot extension
    """
    pattern = '^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'
    return (bool(re.match(pattern, string)) == True)
  
def censor(text,word):
  """Censoring a word in a text. Replaces the word to censor by ****
  """
  replace_string = '*' * len(word)
  textlist = text.split(word)
  return replace_string.join(textlist)

def hasLetter(text):
  """Checks if a text contains letters. Returns a boolean
  """
  if text is None:
    return False
  return re.search("[a-zA-Z]", text) is not None

def hasNonLetter(text):
  """Checks if a text contains non letters. Returns a boolean
  """
  if text is None:
    return False
  return re.search("[^a-zA-Z]", text) is not None

def hasUpperLetter(text):
  """Checks if a text contains capitalized letters. Returns a boolean
  """
  if text is None:  
    return False
  return re.search("[A-Z]", text) is not None

def hasLowerLetter(text):
  """Checks if a text contains non-capitalized letters. Returns a boolean
  """
  if text is None:
    return False
  return re.search("[a-z]", text) is not None


def clean_percentage(str,NA_value):
  """cleaning a percentage written in a text form: e.g. transforming 35% into 0.35
  NA_Value is the value that is to be considered as N/A
  """
 if str==NA_value:
  pass
 else:  
  return float(str.replace('%', '').replace(' ',''))/100
