import sys
import urllib.parse
import urllib.request
import os.path
def main(arg1):
    if os.path.isdir(arg1) == False:
            if os.path.isfile(arg1):
                code = open(arg1, 'r').read()
            else:
                code = arg1
            p_devkey = # dev key
            p_private = 1
            p_name = arg1
            p_expire_in = "10M"
            p_user = ''
            p_code = code

            p_url = 'http://pastebin.com/api/api_post.php'

            params = urllib.parse.urlencode({'api_option':'paste',
                'api_user_key': p_user,
                'api_paste_private': p_private,
                'api_paste_name': p_name,
                'api_paste_expire_date': p_expire_in,
                'api_dev_key': p_devkey,
                'api_paste_code': p_code
                })

            url = urllib.request.urlopen(p_url, params.encode('utf8'))
            te = url.read()
            with open('lastest_link.txt', 'w') as f:
                f.write(str(te))
            return te
    else:
            return "no directories!"

if __name__ == '__main__':
    status = main()
    with open('lastest_link.txt', 'w') as f:
        f.write(str(status))
    sys.exit(status)