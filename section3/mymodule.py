import re
import json
fname = 'jawiki-country.json'

def extract_text(title):
    with open(fname) as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == title:
                return data_json['text']
            
def extract_base_info(text):
    pattern = r"^({{基礎情報.*?^}})"
    base_info = re.findall(pattern, text, re.MULTILINE | re.DOTALL)
    return base_info[0]

def remove_accent(text):
    pattern = r"\'{2,5}"
    return re.sub(pattern, "", text) 

def remove_inner_line(text):
    pattern_open_inner_link = r"\[\["
    pattern_close_inner_link = r"\]\]"
    rm_inner_link_text = re.sub(pattern_open_inner_link, "", text)
    return re.sub(pattern_close_inner_link, "", rm_inner_link_text)

def rm_list(text):
    pattern = r"\*{1,2}"
    return re.sub(pattern, "", text)

def rm_lang(text):
    pattern1 = r"\{{2}(.*?)\|(.*?)\|"
    pattern2 = r"(?<!\n)}}"                 # \nの後の}}は対象外
    pre_result = re.sub(pattern1, "", text)
    return re.sub(pattern2, "", pre_result)  

def rm_outer_link(text):
    pattern = r"\[(.*?)\]"
    links = re.findall(pattern, text)
    return re.sub(pattern, "", text)

def rm_html_tag(text):
    pattern = r"<(.*?)>"
    return re.sub(pattern, "", text)