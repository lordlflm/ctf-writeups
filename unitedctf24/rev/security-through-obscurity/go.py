import subprocess
import string

#IMPORTANT NOTE: Upon restarting the program there is a bug where you need to go reset the algo.k file and leave a trailing line

enc_flag = [51, 207, 228, 236, 120, 202, 45, 76, 165, 140, 155, 172, 232, 68, 4, 177, 19, 204, 196, 50, 27, 52, 209, 10, 143, 15, 133, 206, 224, 23,]
flag = 'flag-'
all_characters = (
    string.ascii_letters  # a-zA-Z
    + string.digits       # 0-9
    + string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    + string.whitespace   # space, tab, newline, etc.
)
char = list(all_characters)

def run():
    r = subprocess.run(['rlfe', '-h', '~/.k_history', './k/k', './algo.k'], capture_output=True)
    return r.stdout.decode('utf-8').rstrip()


for i in range(5, len(enc_flag)):
    for c in range(len(char)):
        with open('algo.k', 'r+') as f:
            f.seek(210)
            s = flag + char[c] + '"\n\n' # adding trailing line otherwise getting parse/eoleof errors from k
            f.write(s)

        # fix because getting inconsistency
        out = ''
        while(out.rstrip() == ''):
            out = run()
        out_list = list(map(int, out.split()))
        print(out_list)
        if (out_list[i] == enc_flag[i]):
            flag += char[c]
            print(flag)
            break




