# coding: utf8
"""Complete collection of Urdu alphabet."""

# Official Urdu Unicode Character
URDU_CHARACTERS = frozenset("""

  آ ا ب پ ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ
 س ش ص ض ط ظ ع غ ف ق ک گ ل م ن ں و ہ ۃ ھ ء ی ے ‬
 
  ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹
 
 \u0600 \u0601 \u0602 \u0603 \u060c \u060d \u060e \u060f 
 
 \u0610 \u0611 \u0612 \u0613 \u0614 \u0615  ؟ ؛
 
 \u064b \u064c \u064d \u064e \u064f
 
 \u0650 \u0651 \u0652 \u0653 \u0654 \u0656 \u0657 \u0658 
 
 ٪ ٫ ٬

 \u0670

۔ 
 
""".split())

URDU_CHARACTERS_UNICODE = {'\u0600': '0600',
                           '\u0601': '0601',
                           '\u0602': '0602',
                           '\u0603': '0603',
                           '،': '060c',
                           '؍': '060d',
                           '؎': '060e',
                           '؏': '060f',
                           'ؐ': '0610',
                           'ؑ': '0611',
                           'ؒ': '0612',
                           'ؓ': '0613',
                           'ؔ': '0614',
                           'ؕ': '0615',
                           '؛': '061b',
                           '؟': '061f',
                           'ء': '0621',
                           'ً': '064b',
                           'ٌ': '064c',
                           'ٍ': '064d',
                           'َ': '064e',
                           'ُ': '064f',
                           'ِ': '0650',
                           'ّ': '0651',
                           'ْ': '0652',
                           'ٓ': '0653',
                           'ٔ': '0654',
                           'ٖ': '0656',
                           'ٗ': '0657',
                           '٘': '0658',
                           '٪': '066a',
                           '٫': '066b',
                           '٬': '066c',
                           'ٰ': '0670',
                           '۔': '06d4',
                           'آ': '0622',
                           'ا': '0627',
                           'ب': '0628',
                           'ت': '062a',
                           'ث': '062b',
                           'ج': '062c',
                           'ح': '062d',
                           'خ': '062e',
                           'د': '062f',
                           'ذ': '0630',
                           'ر': '0631',
                           'ز': '0632',
                           'س': '0633',
                           'ش': '0634',
                           'ص': '0635',
                           'ض': '0636',
                           'ط': '0637',
                           'ظ': '0638',
                           'ع': '0639',
                           'غ': '063a',
                           'ف': '0641',
                           'ق': '0642',
                           'ل': '0644',
                           'م': '0645',
                           'ن': '0646',
                           'و': '0648',
                           'ٹ': '0679',
                           'پ': '067e',
                           'چ': '0686',
                           'ڈ': '0688',
                           'ڑ': '0691',
                           'ژ': '0698',
                           'ک': '06a9',
                           'گ': '06af',
                           'ں': '06ba',
                           'ھ': '06be',
                           'ہ': '06c1',
                           'ۃ': '06c3',
                           'ی': '06cc',
                           'ے': '06d2',
                           '۰': '06f0',
                           '۱': '06f1',
                           '۲': '06f2',
                           '۳': '06f3',
                           '۴': '06f4',
                           '۵': '06f5',
                           '۶': '06f6',
                           '۷': '06f7',
                           '۸': '06f8',
                           '۹': '06f9',
                           }

# Complete set of Urdu alphabet.
URDU_ALPHABET = frozenset("""

 آ ا ب پ ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ
 س ش ص ض ط ظ ع غ ف ق ک گ ل م ن ں و ہ ه ۃ ھ ء ی ے ‬
 
""".split())

# Urdu Digits from 0 to 9
URDU_DIGITS = frozenset(""" ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹  """.split())

# Urdu punctuation
URDU_PUNCTUATION = frozenset("""

 ؛ ، ٫  ؟ ۔ ٪

""".split())

# Urdu Aerabs
DIACRITICS = frozenset("""
 
 \u064B \u0670 \u0650 \u064F 

""".split())
