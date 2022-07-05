text = 'vujgvmCfb tj ufscfu ouib z/vhm ' \
       'jdjuFyqm jt fscfuu uibo jdju/jnqm ' \
       'fTjnqm tj scfuuf ibou fy/dpnqm ' \
       'yDpnqmf jt cfuufs boui dbufe/dpnqmj ' \
       'uGmb tj fuufsc ouib oftufe/ ' \
       'bstfTq jt uufscf uibo otf/ef ' \
       'uzSfbebcjmj vout/dp ' \
       'djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ' \
       'ipvhiBmu zqsbdujdbmju fbutc uz/qvsj ' \
       'Fsspst tipvme wfsof qbtt foumz/tjm ' \
       'omfttV mjdjumzfyq odfe/tjmf ' \
       'Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv ' \
       'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
       'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud ' \
       'xOp tj scfuuf ibou /ofwfs ' \
       'uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op ' \
       'gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb ' \
       'Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
       'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'


def encrypt_caesar(string):
    key = 1
    translate = ''
    for symbol in string:
        if symbol.isalpha():
            num = alphabet.index(symbol)
            translate = translate + alphabet[num - key]
        else:
            translate = translate + symbol
    return translate


def string_shift(string, shift):
    shift_element = ''
    for i in range(len(string)):
        shift_element += (string[i - shift % len(string)])
    return shift_element


alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
shift = 3
enc_text = ''
for element in text.split():
    element = encrypt_caesar(element)
    element = string_shift(element, shift)
    if element.endswith('/'):
        element = element + '\n'
        shift += 1
    enc_text += element + ' '

enc_text = enc_text.replace('/', '.')
enc_text = enc_text.replace('(', "'")
enc_text = enc_text.replace('"', '!')
enc_text = enc_text.replace('-', ',')
enc_text = enc_text.replace('..', ' - ')
enc_text = enc_text.replace('+', '')
print(' ' + enc_text)
