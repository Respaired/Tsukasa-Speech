formal_to_informal = {
    
    

    'ワタクシ': 'わたし',
     'チカコ':'しゅうこ',
     "タノヒト":"ほかのひと",

    # Add more mappings as needed
}

formal_to_informal2 = {

     "たのひと":"ほかのひと",
     "すうは": "かずは",


    # Add more mappings as needed
}

formal_to_informal3 = {

     "%":"％",
     "@": "あっとさいん",
     "$":"どる",
     "#":"はっしゅたぐ",
     "＄":"どる",
     "＃":"はっしゅたぐ",
     "何が":"なにが",

     "何も":"なにも",
     "何か":"なにか",
    #  "奏":"かなで",
     "何は":"なにが",
     "お父様":"おとうさま",
     "お兄様":"おにいさま",
     "何を":"なにを",
     "良い":"いい",
     "李衣菜":"りいな",
     "志希":"しき",
     "種":"たね",
     "方々":"かたがた",
     "颯":"はやて",
     "茄子さん":"かこさん",
     "茄子ちゃん":"かこちゃん",
     "涼ちゃん":"りょうちゃん",
     "涼さん":"りょうさん",
     "紗枝":"さえ",
     "文香":"ふみか",
     "私":"わたし",
     "周子":"しゅうこ",
     "イェ":"いえ",
     "可憐":"かれん",
     "加蓮":"かれん",
     "･":".",
    #  "方の":"かたの",
    #  "気に":"きに",
     "唯さん":"ゆいさん",
     "唯ちゃん":"ゆいちゃん",
     "聖ちゃん":"ひじりちゃん",
     "他の":"ほかの",
     "他に":"ほかに",
     "一生懸命":"いっしょうけんめい",
     "楓さん":"かえでさん",
     "楓ちゃん":"かえでちゃん",
     "内から":"ないから",
     "の下で":"のしたで",

}


mapper = dict([

    ("仕方","しかた"),
    ("明日","あした"),
    ('私',"わたし"),
    ("従妹","いとこ"),
        
    ("1人","ひとり"),
    ("2人","ふたり"),
    
    ("一期","いちご"),
    ("一会","いちえ"),
    
    ("♪","！"),
    ("?","？"),

    ("どんな方","どんなかた"),
    ("ふたり暮らし","ふたりぐらし"),

    ("新年","しんねん"),
    ("来年","らいねん"),
    ("去年","きょねん"),
    ("壮年","そうねん"),
    ("今年","ことし"),

    ("昨年","さくねん"),
    ("本年","ほんねん"),
    ("平年","へいねん"),
    ("閏年","うるうどし"),
    ("初年","しょねん"),
    ("少年","しょうねん"),
    ("多年","たねん"),
    ("青年","せいねん"),
    ("中年","ちゅうねん"),
    ("老年","ろうねん"),
    ("成年","せいねん"),
    ("幼年","ようねん"),
    ("前年","ぜんねん"),
    ("元年","がんねん"),
    ("経年","けいねん"),
    ("当年","とうねん"),

    ("明年","みょうねん"),
    ("歳年","さいねん"),
    ("数年","すうねん"),
    ("半年","はんとし"),
    ("後年","こうねん"),
    ("実年","じつねん"),
    ("年年","ねんねん"),
    ("連年","れんねん"),
    ("暦年","れきねん"),
    ("各年","かくねん"),
    ("全年","ぜんねん"),

    ("年を","としを"),
    ("年が","としが"),
    ("年も","としも"),
    ("年は","としは"),


    ("奏ちゃん","かなでちゃん"),
    ("負けず嫌い","まけずぎらい"),
    ("貴方","あなた"),
    ("貴女","あなた"),
    ("貴男","あなた"),

    ("その節","そのせつ"),

    ("何し","なにし"),
    ("何する","なにする"),

    ("心さん","しんさん"),
    ("心ちゃん","しんちゃん"),

    ("乃々","のの"),

    ("身体の","からだの"),
    ("身体が","からだが"),
    ("身体を","からだを"),
    ("身体は","からだは"),
    ("身体に","からだに"),
    ("正念場","しょうねんば"),
    ("言う","いう"),
    
    
    ("一回","いっかい"),
    ("一曲","いっきょく"),
    ("一日","いちにち"),
    ("一言","ひとこと"),
    ("一杯","いっぱい"),
    
    
    ("方が","ほうが"),
    ("縦輪城","じゅうりんしろ"),
    ("深息","しんそく"),
    ("家人","かじん"),
    ("お返し","おかえし"),
    ("化物語","ばけものがたり"),
    ("阿良々木暦","あららぎこよみ"),
    ("何より","なにより")


])


# Merge all dictionaries into one
all_transformations = {**formal_to_informal, **formal_to_informal2, **formal_to_informal3, **mapper}

def apply_transformations(text, transformations = all_transformations):
    for key, value in transformations.items():
        text = text.replace(key, value)
    return text

import re

def number_to_japanese(num):
    if not isinstance(num, int) or num < 0 or num > 9999:
        return "Invalid input"

    digits = ["", "いち", "に", "さん", "よん", "ご", "ろく", "なな", "はち", "きゅう"]
    tens = ["", "じゅう", "にじゅう", "さんじゅう", "よんじゅう", "ごじゅう", "ろくじゅう", "ななじゅう", "はちじゅう", "きゅうじゅう"]
    hundreds = ["", "ひゃく", "にひゃく", "さんびゃく", "よんひゃく", "ごひゃく", "ろっぴゃく", "ななひゃく", "はっぴゃく", "きゅうひゃく"]
    thousands = ["", "せん", "にせん", "さんぜん", "よんせん", "ごせん", "ろくせん", "ななせん", "はっせん", "きゅうせん"]

    if num == 0:
        return "ゼロ"

    result = ""
    if num >= 1000:
        result += thousands[num // 1000]
        num %= 1000
    if num >= 100:
        result += hundreds[num // 100]
        num %= 100
    if num >= 10:
        result += tens[num // 10]
        num %= 10
    if num > 0:
        result += digits[num]

    return result

def convert_numbers_in_string(input_string):
    # Regular expression to find numbers in the string
    number_pattern = re.compile(r'\d+')

    # Function to replace numbers with their Japanese pronunciation
    def replace_with_japanese(match):
        num = int(match.group())
        return number_to_japanese(num)

    # Replace all occurrences of numbers in the string
    converted_string = number_pattern.sub(replace_with_japanese, input_string)
    return converted_string


roma_mapper = dict([
    
    ################################

    ("my","mʲ"),
    ("by","bʲ"),
    ("ny","nʲ"),
    ("ry","rʲ"),
    ("si","sʲ"),
    ("ky","kʲ"),
    ("gy","gʲ"),
    ("dy","dʲ"),
    ("di","dʲ"),
    ("fi","fʲ"),
    ("fy","fʲ"),
    ("ch","tɕ"),
    ("sh","ɕ"),
    
 ################################

    ("a","a"),
    ("i","i"),
    ("u","ɯ"),
    ("e","e"),
    ("o","o"),
    ("ka","ka"),
    ("ki","ki"),
    ("ku","kɯ"),
    ("ke","ke"),
    ("ko","ko"),
    ("sa","sa"),
    ("shi","ɕi"),
    ("su","sɯ"),
    ("se","se"),
    ("so","so"),
    ("ta","ta"),
    ("chi","tɕi"),
    ("tsu","tsɯ"),
    ("te","te"),
    ("to","to"),
    ("na","na"),
    ("ni","ni"),
    ("nu","nɯ"),
    ("ne","ne"),
    ("no","no"),
    ("ha","ha"),
    ("hi","çi"),
    ("fu","ɸɯ"),
    ("he","he"),
    ("ho","ho"),
    ("ma","ma"),
    ("mi","mi"),
    ("mu","mɯ"),
    ("me","me"),
    ("mo","mo"),
    ("ra","ɽa"),
    ("ri","ɽi"),
    ("ru","ɽɯ"),
    ("re","ɽe"),
    ("ro","ɽo"),
    ("ga","ga"),
    ("gi","gi"),
    ("gu","gɯ"),
    ("ge","ge"),
    ("go","go"),
    ("za","za"),
    ("ji","dʑi"),
    ("zu","zɯ"),
    ("ze","ze"),
    ("zo","zo"),
    ("da","da"),
    

    ("zu","zɯ"),
    ("de","de"),
    ("do","do"),
    ("ba","ba"),
    ("bi","bi"),
    ("bu","bɯ"),
    ("be","be"),
    ("bo","bo"),
    ("pa","pa"),
    ("pi","pi"),
    ("pu","pɯ"),
    ("pe","pe"),
    ("po","po"),
    ("ya","ja"),
    ("yu","jɯ"),
    ("yo","jo"),
    ("wa","wa"),
    

 

    ("a","a"),
    ("i","i"),
    ("u","ɯ"),
    ("e","e"),
    ("o","o"),
    ("wa","wa"),
    ("o","o"),


    ("wo","o")])

nasal_sound = dict([
    # before m, p, b
    ("ɴm","mm"),
    ("ɴb", "mb"),
    ("ɴp", "mp"),
    
    # before k, g
    ("ɴk","ŋk"),
    ("ɴg", "ŋg"),
    
    # before t, d, n, s, z, ɽ
    ("ɴt","nt"),
    ("ɴd", "nd"),
    ("ɴn","nn"),
    ("ɴs", "ns"),
    ("ɴz","nz"),
    ("ɴɽ", "nɽ"),
    
    ("ɴɲ", "ɲɲ"),
    
])

def Roma2IPA(text):
    orig = text

    for k, v in roma_mapper.items():
        text = text.replace(k, v)
        
    return text

def nasal_mapper(text):
    orig = text


    for k, v in nasal_sound.items():
        text = text.replace(k, v)
        
    return text

def alphabetreading(text):
    alphabet_dict = {"A": "エイ",
                "B": "ビー",
                 "C": "シー",
                 "D": "ディー",
                 "E": "イー",
                 "F": "エフ",
                 "G": "ジー",
                 "H": "エイチ",
                "I":"アイ",
                "J":"ジェイ",
                "K":"ケイ",
                "L":"エル",
                "M":"エム",
                "N":"エヌ",
                "O":"オー",
                "P":"ピー",
                "Q":"キュー",
                "R":"アール",
                "S":"エス",
                "T":"ティー",
                "U":"ユー",
                "V":"ヴィー",
                "W":"ダブリュー",
                "X":"エックス",
                "Y":"ワイ",
                "Z":"ゼッド"}
    text = text.upper()
    text_ret = ""
    for t in text:
        if t in alphabet_dict:
            text_ret += alphabet_dict[t]
        else:
            text_ret += t
    return text_ret

import re
import cutlet

roma_mapper_plus_2 = {
    
"bjo":'bʲo',
"rjo":"rʲo",
"kjo":"kʲo",
"kyu":"kʲu",
    
}

def replace_repeated_chars(input_string):
    result = []
    i = 0
    while i < len(input_string):
        if i + 1 < len(input_string) and input_string[i] == input_string[i + 1] and input_string[i] in 'aiueo':
            result.append(input_string[i] + 'ː')
            i += 2  
        else:
            result.append(input_string[i])
            i += 1
    return ''.join(result)


def replace_chars_2(text, mapping=roma_mapper_plus_2):
    

    sorted_keys = sorted(mapping.keys(), key=len, reverse=True)

    pattern = '|'.join(re.escape(key) for key in sorted_keys)
    

    def replace(match):
        key = match.group(0)
        return mapping.get(key, key)

    return re.sub(pattern, replace, text)


def replace_tashdid_2(s):
    vowels = 'aiueoɯ0123456789.?!_。؟？！．．．＠@＃#＄$％%＾^＆&＊*（)(）_+=[「」]></\\`~～―ー∺"'
    result = []
    
    i = 0
    while i < len(s):
        if i < len(s) - 2 and s[i].lower() == s[i + 2].lower() and s[i].lower() not in vowels and s[i + 1] == ' ':
            result.append('ʔ')
            result.append(s[i + 2])
            i += 3
        elif i < len(s) - 1 and s[i].lower() == s[i + 1].lower() and s[i].lower() not in vowels:
            result.append('ʔ')
            result.append(s[i + 1])
            i += 2
        else:
            result.append(s[i])
            i += 1
            
    return ''.join(result)

def replace_tashdid(input_string):
    result = []
    i = 0
    while i < len(input_string):
        if i + 1 < len(input_string) and input_string[i] == input_string[i + 1] and input_string[i] not in 'aiueo':
            result.append('ʔ')
            result.append(input_string[i])
            i += 2  # Skip the next character as it is already processed
        else:
            result.append(input_string[i])
            i += 1
    return ''.join(result)

def hira2ipa(text, roma_mapper=roma_mapper):
    keys_set = set(roma_mapper.keys())
    special_rule = ("n", "ɴ")
    
    transformed_text = []
    i = 0

    while i < len(text):
        if text[i] == special_rule[0]:  
            if i + 1 == len(text) or text[i + 1] not in keys_set:  
                transformed_text.append(special_rule[1])  
            else:
                transformed_text.append(text[i])  
        else:
            transformed_text.append(text[i])  
        
        i += 1  

    return ''.join(transformed_text)

import re


k_mapper = dict([
    ("ゔぁ","ba"),
    ("ゔぃ","bi"),
    ("ゔぇ","be"),
    ("ゔぉ","bo"),
    ("ゔゃ","bʲa"),
    ("ゔゅ","bʲɯ"),
    ("ゔゃ","bʲa"),
    ("ゔょ","bʲo"),

    ("ゔ","bɯ"),

    ("あぁ"," aː"),
    ("いぃ"," iː"),
    ("いぇ"," je"),
    ("いゃ"," ja"),
    ("うぅ"," ɯː"),
    ("えぇ"," eː"),
    ("おぉ"," oː"),
    ("かぁ"," kaː"),
    ("きぃ"," kiː"),
    ("くぅ","kɯː"),
    ("くゃ","ka"),
    ("くゅ","kʲɯ"),
    ("くょ","kʲo"),
    ("けぇ","keː"),
    ("こぉ","koː"),
    ("がぁ","gaː"),
    ("ぎぃ","giː"),
    ("ぐぅ","gɯː"),
    ("ぐゃ","gʲa"),
    ("ぐゅ","gʲɯ"),
    ("ぐょ","gʲo"),
    ("げぇ","geː"),
    ("ごぉ","goː"),
    ("さぁ","saː"),
    ("しぃ","ɕiː"),
    ("すぅ","sɯː"),
    ("すゃ","sʲa"),
    ("すゅ","sʲɯ"),
    ("すょ","sʲo"),
    ("せぇ","seː"),
    ("そぉ","soː"),
    ("ざぁ","zaː"),
    ("じぃ","dʑiː"),
    ("ずぅ","zɯː"),
    ("ずゃ","zʲa"),
    ("ずゅ","zʲɯ"),
    ("ずょ","zʲo"),
    ("ぜぇ","zeː"),
    ("ぞぉ","zeː"),
    ("たぁ","taː"),
    ("ちぃ","tɕiː"),
    ("つぁ","tsa"),
    ("つぃ","tsi"),
    ("つぅ","tsɯː"),
    ("つゃ","tɕa"),
    ("つゅ","tɕɯ"),
    ("つょ","tɕo"),
    ("つぇ","tse"),
    ("つぉ","tso"),
    ("てぇ","teː"),
    ("とぉ","toː"),
    ("だぁ","daː"),
    ("ぢぃ","dʑiː"),
    ("づぅ","dɯː"),
    ("づゃ","zʲa"),
    ("づゅ","zʲɯ"),
    ("づょ","zʲo"),
    ("でぇ","deː"),
    ("どぉ","doː"),
    ("なぁ","naː"),
    ("にぃ","niː"),
    ("ぬぅ","nɯː"),
    ("ぬゃ","nʲa"),
    ("ぬゅ","nʲɯ"),
    ("ぬょ","nʲo"),
    ("ねぇ","neː"),
    ("のぉ","noː"),
    ("はぁ","haː"),
    ("ひぃ","çiː"),
    ("ふぅ","ɸɯː"),
    ("ふゃ","ɸʲa"),
    ("ふゅ","ɸʲɯ"),
    ("ふょ","ɸʲo"),
    ("へぇ","heː"),
    ("ほぉ","hoː"),
    ("ばぁ","baː"),
    ("びぃ","biː"),
    ("ぶぅ","bɯː"),
    ("ふゃ","ɸʲa"),
    ("ぶゅ","bʲɯ"),
    ("ふょ","ɸʲo"),
    ("べぇ","beː"),
    ("ぼぉ","boː"),
    ("ぱぁ","paː"),
    ("ぴぃ","piː"),
    ("ぷぅ","pɯː"),
    ("ぷゃ","pʲa"),
    ("ぷゅ","pʲɯ"),
    ("ぷょ","pʲo"),
    ("ぺぇ","peː"),
    ("ぽぉ","poː"),
    ("まぁ","maː"),
    ("みぃ","miː"),
    ("むぅ","mɯː"),
    ("むゃ","mʲa"),
    ("むゅ","mʲɯ"),
    ("むょ","mʲo"),
    ("めぇ","meː"),
    ("もぉ","moː"),
    ("やぁ","jaː"),
    ("ゆぅ","jɯː"),
    ("ゆゃ","jaː"),
    ("ゆゅ","jɯː"),
    ("ゆょ","joː"),
    ("よぉ","joː"),
    ("らぁ","ɽaː"),
    ("りぃ","ɽiː"),
    ("るぅ","ɽɯː"),
    ("るゃ","ɽʲa"),
    ("るゅ","ɽʲɯ"),
    ("るょ","ɽʲo"),
    ("れぇ","ɽeː"),
    ("ろぉ","ɽoː"),
    ("わぁ","ɯaː"),
    ("をぉ","oː"),

    ("う゛","bɯ"),
    ("でぃ","di"),
    ("でぇ","deː"),
    ("でゃ","dʲa"),
    ("でゅ","dʲɯ"),
    ("でょ","dʲo"),
    ("てぃ","ti"),
    ("てぇ","teː"),
    ("てゃ","tʲa"),
    ("てゅ","tʲɯ"),
    ("てょ","tʲo"),
    ("すぃ","si"),
    ("ずぁ","zɯa"),
    ("ずぃ","zi"),
    ("ずぅ","zɯ"),
    ("ずゃ","zʲa"),
    ("ずゅ","zʲɯ"),
    ("ずょ","zʲo"),
    ("ずぇ","ze"),
    ("ずぉ","zo"),
    ("きゃ","kʲa"),
    ("きゅ","kʲɯ"),
    ("きょ","kʲo"),
    ("しゃ","ɕʲa"),
    ("しゅ","ɕʲɯ"),
    ("しぇ","ɕʲe"),
    ("しょ","ɕʲo"),
    ("ちゃ","tɕa"),
    ("ちゅ","tɕɯ"),
    ("ちぇ","tɕe"),
    ("ちょ","tɕo"),
    ("とぅ","tɯ"),
    ("とゃ","tʲa"),
    ("とゅ","tʲɯ"),
    ("とょ","tʲo"),
    ("どぁ","doa"),
    ("どぅ","dɯ"),
    ("どゃ","dʲa"),
    ("どゅ","dʲɯ"),
    ("どょ","dʲo"),
    ("どぉ","doː"),
    ("にゃ","nʲa"),
    ("にゅ","nʲɯ"),
    ("にょ","nʲo"),
    ("ひゃ","çʲa"),
    ("ひゅ","çʲɯ"),
    ("ひょ","çʲo"),
    ("みゃ","mʲa"),
    ("みゅ","mʲɯ"),
    ("みょ","mʲo"),
    ("りゃ","ɽʲa"),
    ("りぇ","ɽʲe"),
    ("りゅ","ɽʲɯ"),
    ("りょ","ɽʲo"),
    ("ぎゃ","gʲa"),
    ("ぎゅ","gʲɯ"),
    ("ぎょ","gʲo"),
    ("ぢぇ","dʑe"),
    ("ぢゃ","dʑa"),
    ("ぢゅ","dʑɯ"),
    ("ぢょ","dʑo"),
    ("じぇ","dʑe"),
    ("じゃ","dʑa"),
    ("じゅ","dʑɯ"),
    ("じょ","dʑo"),
    ("びゃ","bʲa"),
    ("びゅ","bʲɯ"),
    ("びょ","bʲo"),
    ("ぴゃ","pʲa"),
    ("ぴゅ","pʲɯ"),
    ("ぴょ","pʲo"),
    ("うぁ","ɯa"),
    ("うぃ","ɯi"),
    ("うぇ","ɯe"),
    ("うぉ","ɯo"),
    ("うゃ","ɯʲa"),
    ("うゅ","ɯʲɯ"),
    ("うょ","ɯʲo"),
    ("ふぁ","ɸa"),
    ("ふぃ","ɸi"),
    ("ふぅ","ɸɯ"),
    ("ふゃ","ɸʲa"),
    ("ふゅ","ɸʲɯ"),
    ("ふょ","ɸʲo"),
    ("ふぇ","ɸe"),
    ("ふぉ","ɸo"),

    ("あ"," a"),
    ("い"," i"),
    ("う","ɯ"),
    ("え"," e"),
    ("お"," o"),
    ("か"," ka"),
    ("き"," ki"),
    ("く"," kɯ"),
    ("け"," ke"),
    ("こ"," ko"),
    ("さ"," sa"),
    ("し"," ɕi"),
    ("す"," sɯ"),
    ("せ"," se"),
    ("そ"," so"),
    ("た"," ta"),
    ("ち"," tɕi"),
    ("つ"," tsɯ"),
    ("て"," te"),
    ("と"," to"),
    ("な"," na"),
    ("に"," ni"),
    ("ぬ"," nɯ"),
    ("ね"," ne"),
    ("の"," no"),
    ("は"," ha"),
    ("ひ"," çi"),
    ("ふ"," ɸɯ"),
    ("へ"," he"),
    ("ほ"," ho"),
    ("ま"," ma"),
    ("み"," mi"),
    ("む"," mɯ"),
    ("め"," me"),
    ("も"," mo"),
    ("ら"," ɽa"),
    ("り"," ɽi"),
    ("る"," ɽɯ"),
    ("れ"," ɽe"),
    ("ろ"," ɽo"),
    ("が"," ga"),
    ("ぎ"," gi"),
    ("ぐ"," gɯ"),
    ("げ"," ge"),
    ("ご"," go"),
    ("ざ"," za"),
    ("じ"," dʑi"),
    ("ず"," zɯ"),
    ("ぜ"," ze"),
    ("ぞ"," zo"),
    ("だ"," da"),
    ("ぢ"," dʑi"),
    ("づ"," zɯ"),
    ("で"," de"),
    ("ど"," do"),
    ("ば"," ba"),
    ("び"," bi"),
    ("ぶ"," bɯ"),
    ("べ"," be"),
    ("ぼ"," bo"),
    ("ぱ"," pa"),
    ("ぴ"," pi"),
    ("ぷ"," pɯ"),
    ("ぺ"," pe"),
    ("ぽ"," po"),
    ("や"," ja"),
    ("ゆ"," jɯ"),
    ("よ"," jo"),
    ("わ"," wa"),
    ("ゐ"," i"),
    ("ゑ"," e"),
    ("ん"," ɴ"),
    ("っ"," ʔ"),
    ("ー"," ː"),

    ("ぁ"," a"),
    ("ぃ"," i"),
    ("ぅ"," ɯ"),
    ("ぇ"," e"),
    ("ぉ"," o"),
    ("ゎ"," ɯa"),
    ("ぉ"," o"),
    ("っ","?"),

    ("を","o")

])


def post_fix(text):
    orig = text

    for k, v in k_mapper.items():
        text = text.replace(k, v)

    return text




sym_ws = dict([
    
    ("$ ","dorɯ"),
    ("＄ ","dorɯ"),
    
    ("〇 ","marɯ"),
    ("¥ ","eɴ"),

    ("# ","haʔɕɯ tagɯ"),
    ("＃ ","haʔɕɯ tagɯ"),
    
    ("& ","ando"),
    ("＆ ","ando"),
    
    ("% ","paːsento"),
    ("％ ","paːsento"),
    
    ("@ ","aʔto saiɴ"),
    ("＠ ","aʔto saiɴ")
    

    
])

def random_sym_fix(text): # with space
    orig = text

    for k, v in sym_ws.items():
        text = text.replace(k, f" {v} ")
        
    return text


sym_ns = dict([
    
    ("$","dorɯ"),
    ("＄","dorɯ"),
    
    ("〇","marɯ"),
    ("¥","eɴ"),

    ("#","haʔɕɯ tagɯ"),
    ("＃","haʔɕɯ tagɯ"),
    
    ("&","ando"),
    ("＆","ando"),
    
    ("%","paːsento"),
    ("％","paːsento"),
    
    ("@","aʔto saiɴ"),
    ("＠","aʔto saiɴ"),
    
    ("～","—"),
    ("kʲɯɯdʑɯɯkʲɯɯ.kʲɯɯdʑɯɯ","kʲɯɯdʑɯɯ kʲɯɯ teɴ kʲɯɯdʑɯɯ")
    

    

    
])

def random_sym_fix_no_space(text):
    orig = text

    for k, v in sym_ns.items():
        text = text.replace(k, f" {v} ")
        
    return text


spaces = dict([
    
    ("ɯ ɴ","ɯɴ"),
    ("na ɴ ","naɴ "),
    (" mina ", " miɴna "),
    ("ko ɴ ni tɕi ha","konnitɕiwa"),
    ("ha i","hai"),
    ("boɯtɕama","boʔtɕama"),
    ("i eːi","ieːi"),
    ("taiɕɯtsɯdʑoɯ","taiɕitsɯdʑoɯ"),
    ("soɴna ka ze ni","soɴna fɯɯ ni"),
    (" i e ","ke "),
    ("�",""),
    ("×"," batsɯ "),
    ("se ka ɯndo","sekaɯndo"),
    ("i i","iː"),
    ("i tɕi","itɕi"),
    ("ka i","kai"),
    ("naɴ ga","nani ga"),
    ("i eː i","ieːi"),
    
    ("naɴ koɽe","nani koɽe"),
    ("naɴ soɽe","nani soɽe"),
    (" ɕeɴ "," seɴ "),
    
    # ("konna","koɴna"),
    # ("sonna"," soɴna "),
    # ("anna","aɴna"),
    # ("nn","ɴn"),
    
    ("en ","eɴ "),
    ("in ","iɴ "),
    ("an ","aɴ "),
    ("on ","oɴ "),
    ("ɯn ","ɯɴ "),
    # ("nd","ɴd"),
    
    ("koɴd o","kondo"),
    ("ko ɴ d o","kondo"),
    ("ko ɴ do","kondo"),
    
    ("oanitɕaɴ","oniːtɕaɴ"),
    ("oanisaɴ","oniːsaɴ"),
    ("oanisama","oniːsama"),
    ("hoːmɯrɯɴɯ","hoːmɯrɯːmɯ"),
    ("so ɴ na ","sonna"),
    ("  sonna  "," sonna "),
    ("  konna  "," konna "),
    ("ko ɴ na ","konna"),
    (" ko to  "," koto "),
    ("edʑdʑi","eʔtɕi"),
    (" edʑdʑ "," eʔtɕi "),
    (" dʑdʑ "," dʑiːdʑiː "),
    ("secɯnd","sekaɯndo"),
    
    ("ɴɯ","nɯ"),
    ("ɴe","ne"),
    ("ɴo","no"),
    ("ɴa","na"),
    ("ɴi","ni"),
    ("ɴʲ","nʲ"),
    
    ("hotond o","hotondo"),
    ("hakoɴd e","hakoɴde"),
    ("gakɯtɕi ɽi","gaʔtɕiɽi "),
    
    (" ʔ","ʔ"),
    ("ʔ ","ʔ"),
    
    ("-","ː"),
    ("- ","ː"),
    ("--","~ː"),
    ("~","—"),
    ("、",","),

    
    (" ː","ː"),
    ('ka nade',"kanade"),

    ("ohahasaɴ","okaːsaɴ"),
    ("　"," "),
    ("viː","bɯiː"),
    ("ːː","ː—"),
    
    ("d ʑ","dʑ"),
    ("d a","da"),
    ("d e","de"),
    ("d o","do"),
    ("d ɯ","dɯ"),
    
    ("niːɕiki","ni iɕiki"),
    ("anitɕaɴ","niːtɕaɴ"),
    ("daiːtɕi","dai itɕi"),
    ("niːta","ni ita"),
    ("niːrɯ","ni irɯ"),
    ("a—","aː"),
    ("waːis","wa ais"),
    ("waːiɕ","wa aiɕ"),
    ("aːt","a at"),
    ("waːʔ", "wa aʔ"),
    
    ("naɴ sono","nani sono"),
    ("naɴ kono","nani kono"),
    ("naɴ ano","nani ano"), # Cutlet please fix your shit
    (" niːtaɽa"," ni itaɽa"),
    ("doɽamaɕiːd","doɽama ɕiːdʲi"),
    ("aɴ ta","anta"),
    ("aɴta","anta"),
    ("naniːʔteɴ","nani iʔteɴ"),
    ("niːkite","ni ikite"),
    ("niːʔ","ni iʔ"),
    ("niːɯ","ni iɯ"),
    ("niːw","ni iw"),
    ("niːkɯ","ni ikɯ"),
    ("de—","de e"),
    ("aːj","aː aj"),
    ("aːɽ","a aɽ"),
    ("aːr","a ar"),
    ("ɕiːk ","ɕi ik"),
    ("ɕijoː neɴ","ɕoɯneɴ")
    

])



def random_space_fix(text):
    orig = text

    for k, v in spaces.items():
        text = text.replace(k, v)
        
    return text
