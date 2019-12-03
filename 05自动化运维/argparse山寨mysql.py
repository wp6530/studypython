# -*- coding=utf-8 -*-
import argparse


def _argparser():
    parser = argparse.ArgumentParser(description='How to connect to mysql')
    parser.add_argument('--host', action='store', dest='host', required=True, help='connect to host')
    parser.add_argument('-u', '--user', action='store', dest='user', required=True, help='user for login')
    parser.add_argument('-p', '--password', action='store', dest='password', required=True, help='password')
    parser.add_argument('-P', '--port', action='store', dest='port', required=True, help='configure mysql port',
                        default=3306)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    return parser.parse_args()


def main():
    parser = _argparser()
    conn_args = dict(host=parser.host, user=parser.user, password=parser.password, port=parser.port)
    print(conn_args)


if __name__ == '__main__':
    main()
