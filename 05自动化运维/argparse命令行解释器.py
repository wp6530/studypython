# -*- coding=utf-8 -*-
# from __future__ import print_function
import argparse

parser = argparse.ArgumentParser()


def _argparse():
    parser = argparse.ArgumentParser(description="This is a description!!!")
    parser.add_argument('--host', action='store', dest='server', default="localhost", help='connect to host')
    '''
    add_argument
    name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
    action - 当参数在命令行中出现时使用的动作基本类型。
    nargs - 命令行参数应当消耗的数目。
    const - 被一些 action 和 nargs 选择所需求的常数。
    default - 当参数未在命令行中出现时使用的值。
    type - 命令行参数应当被转换成的类型。
    choices - 可用的参数的容器。
    required - 此命令行选项是否可省略 （仅选项可用）。
    help - 一个此选项作用的简单描述。
    metavar - 在使用方法消息中使用的参数值示例。
    dest - 被添加到 parse_args() 所返回对象上的属性名

    '''
    parser.add_argument('-t', action='store_true', default=False, dest='boolean_switch', help='Set a switch to true')
    return parser.parse_args()


def main():
    parser = _argparse()
    # print(parser)
    print('host=', parser.server)
    print('boolean_switch=', parser.boolean_switch)


if __name__ == '__main__':
    main()
