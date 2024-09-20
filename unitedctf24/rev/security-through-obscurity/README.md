# Security through obscurity
For safety reasons, we need to audit our rides. For safety reasons, the logs are encrypted. For "safety" reasons... we use [a weird obscure language](https://razetime.github.io/ngn-k-tutorial/) I don't know. We lost the decryption algorithm. Oops.

[Online interpreter](https://ngn.codeberg.page/k/#eJwljctugzAQRfd8RRwWzCSuDFZIYUaR+AV2lgBFcUOzYcGjCyPL+fZa7fbonHstValmQ/C+oeKRrHrflO0zySt511RiP4sq8ERedryn+bDfXUg20uXFw8wLkmMwALbXn3g6zTzz1M1cDMhdS4s34CJwvA8YVHHQhwsbaDn6ddRbjLiPdzotkv+5s1VZtvFGALmcUdS19FaZBmRMapSxdLgqEmXIFmyELq9J7rdm/DsJ/fF7erw+1vH5+PoZn8fkF+P6P3w=)
## Solution
Sorry, I'm not learning the k language today. As a matter of fact, I should probably go for a walk or something. Attempting to brute force...

It'll take 5 min...

The online interpreter link above reveals the algorithm. I copied it to a file named `algo.k`
```k
b:8#2;X:(~=)/;e:b/~=/b\',;r:{x@8!y+!8};l:{,[;y#0]y_x}
s:254{(p;q):x;(X((b\27)**p;p;l[p;1]);[Q:q{X(x;l[x;y])}/1 2 4;X(Q;(b\9)**Q)])}\b\'2#1
(p;q):+b/''s;s:((0,p)!99,{b/X@(,b\99),(b\x)r/:!5}'q)@!256
0{s@e[x;y]}\"flag-redacted"
```

Using [this ngn/k open-source kernel](https://codeberg.org/ngn/k)
```bash
# compile
make

# run
rlfe -h ~/.k_history ./k ../algo.k
```

## Script
```python
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


```

## Flag
flag-h0peUd1dntR34Dev3erything (I didn't)
