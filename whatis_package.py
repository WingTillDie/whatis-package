#!/usr/bin/python3
import re
import subprocess
import sys

def usage():
    print('Usage: whatis_package.py <package-name>\n'
          'e.g. whatis_package.py gzip', file=sys.stderr)

def whatis_package(package_name: str = None):
    if package_name is None:
        package_name = sys.argv[1]
    try:
        bytes_ = subprocess.check_output(f'dpkg -L {package_name} ', shell=True)
    except subprocess.CalledProcessError as e:
        print(e, file=sys.stderr)
        exit(1)

    str_ = bytes_.decode()

    def whatis_package_0():
        list_ = []
        for _ in str_.splitlines():
            m = re.fullmatch(r'/usr/share/man/man\d/(?P<TEST>\w+).\d[A-Za-z]*.gz', _)
            if m is not None:
                list_.append(m.group("TEST"))
        return subprocess.check_output('whatis ' + ' '.join(list_) , shell=True)
    def whatis_package_1():
        return subprocess.check_output('whatis ' + ' '.join(_.group("TEST") for _ in (re.fullmatch(r'/usr/share/man/man\d/(?P<TEST>\w+).\d[A-Za-z]*.gz', _) for _ in str_.splitlines() ) if _ is not None ) , shell = True)
    
    match command:='whatis_package_1':
        case 'ASSERT':
            assert(whatis_package_0() == whatis_package_1())
            command = 'whatis_package_1'
            ret = eval(f'{command}()')
        case 'whatis_package_0':
            ret = eval(f'{command}()')
        case 'whatis_package_1':
            ret = eval(f'{command}()')
        case _:
            raise Exception("Unknown command")
    return ret

def test():
    str_test = '''gzexe (1)            - compress executable files in place
    gzip (1)             - compress or expand files
    zdiff (1)            - compare compressed files
    zforce (1)           - force a '.gz' extension on all gzip files
    zgrep (1)            - search possibly compressed files for a regular expression
    zless (1)            - file perusal filter for crt viewing of compressed text
    zmore (1)            - file perusal filter for crt viewing of compressed text
    znew (1)             - recompress .Z files to .gz files
    gunzip (1)           - compress or expand files
    uncompress (1)       - compress or expand files
    zcat (1)             - compress or expand files
    zcmp (1)             - compare compressed files
    zegrep (1)           - search possibly compressed files for a regular expression
    zfgrep (1)           - search possibly compressed files for a regular expression
    '''
    str_test = re.sub('^[\t ]+', '', str_test, flags=re.MULTILINE)
    result = whatis_package('gzip').decode()
    print(result)
    if str_test == result:
        print("Test of the program is success")
    else:
        print("Test of the program is failed, expected output should be: ")
        print(str_test, end='')

if len(sys.argv) != 2:
    print('Wrong number of command line arguments', file=sys.stderr)
    usage()
    exit(1)
if sys.argv[1] == '--test':
    test()
    exit()
if sys.argv[1] == '--help' or sys.argv[1] == '-h':
    usage()
    exit(1)
else:
    print(whatis_package().decode(), end='')

