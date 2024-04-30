import unittest
import valid

def get_bad_strings():
    blns = []
    try:
        with open("blns.txt", encoding='utf8') as f:
            for line in f:
                if not line or line == '' or line[0] == '#':
                    continue
                blns += line
            
            return blns
    except:
        return None

class TestMethods(unittest.TestCase):

    def test_validzipcode_good(self):
        good = ["17701", "12345", "00000", "11111", "87878"]
        
        for zip in good:
            is_valid = valid.zipcode(zip)
            
            self.assertTrue(is_valid)

    def test_validzipcode_bad(self):
        blns = get_bad_strings()
        
        for s in blns:
            is_valid = valid.zipcode(s)
            
            self.assertFalse(is_valid)

    def test_validdict_good(self):
        good = [
        {
            "dt": "123456",
            "main": {
                "temp": "123.45"
            },
            "weather": [
                {
                    "description": "Clear skies"
                }
            ]
        },
        {
            "dt": "11111",
            "main": {
                "temp": "5.36"
            },
            "weather": [
                {
                    "description": "test data"
                }
            ]
        },
        {
            "dt": "000000",
            "main": {
                "temp": "6556.65"
            },
            "weather": [
                {
                    "description": "more tests"
                }
            ]
        },]
        
        for i in good:
            is_valid = valid.weather(i)
            
            self.assertTrue(is_valid)

    def test_validdict_bad(self):
        bad = [
        {
            "dt": "bad data",
            "main": {
                "temp": "123.45"
            },
            "weather": [
                {
                    "description": "Clear skies"
                }
            ]
        },
        {
            "dt": "11111",
            "main": {
                "temp": "bad data"
            },
            "weather": [
                {
                    "description": "test data"
                }
            ]
        },
        {
            "dt": "000000",
            "main": {
                "temp": "6556.65"
            },
            "weather": [
                {
                    "description": "!@#$%^&"
                }
            ]
        },]
        
        for i in bad:
            is_valid = valid.weather(i)
            
            self.assertFalse(is_valid)

    def test_validlog_good(self):
        good = ["valid lowercase log", "VALID UPPERCASE LOG", "another valid ' log", "log()", "log:"]
        
        for s in good:
            is_valid = valid.log(s)
            
            self.assertTrue(is_valid)

    def test_validlog_bad(self):
        blns = get_bad_strings()
        
        for s in blns:
            is_valid = valid.log(s)
            
            self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()