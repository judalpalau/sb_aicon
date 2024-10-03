import re
class UtilRegex:
    @staticmethod
    def all_matches(regex,text):
        r = re.compile(regex)
        res = r.findall(text)
        if res :
            return res
        return []
    @staticmethod
    def all_groups(regex,text):
        r = re.match(regex,text)
        if r:
            return r.groups()
        return []
        
