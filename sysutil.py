# -*- coding: utf-8 -*-
"""
@author: minghao.ma
@description: 
"""

import os
import shutil
import time


def clean_dir(target_dir):
    """
    清空目录中的所有文件和子目录
    :param target_dir: 目标目录
    """
    if not os.path.isdir(target_dir):
        raise Exception("Invalid directory!")
    paths = [os.path.join(target_dir, item) for item in os.listdir(target_dir)]
    for item in paths:
        if os.path.isfile(item):
            os.remove(item)
        elif os.path.isdir(item):
            shutil.rmtree(item)


def get_dir_files(target_dir):
    """
    递归的获取指定目录下的所有文件
    :param target_dir: 目标目录
    :return: 文件路径列表
    """
    if not os.path.isdir(target_dir):
        return []
    results = []
    obj_names = os.listdir(target_dir)
    for name in obj_names:
        obj_path = os.path.join(target_dir, name)
        if os.path.isdir(obj_path):
            results.extend(get_dir_files(obj_path))
        else:
            results.append(obj_path)
    return results


def get_dir_files_by_postfix(target_dir, postfix):
    """
    根据后缀获取某个目录下的文件列表
    :param target_dir: 目录
    :param postfix: 后缀，如：.py .txt等
    :return: 文件路径列表
    """
    all_files = get_dir_files(target_dir)
    target_files = [py_file for py_file in all_files if py_file.endswith(postfix)]
    return target_files


def get_parent_dir(target_dir):
    """
    获取上一级目录
    :param target_dir: 目录字符串
    :return: 上一级目录
    """
    if "/" in target_dir:
        filter_dir = target_dir.rstrip("/")
        return filter_dir[:filter_dir.rfind("/")]
    elif "\\" in target_dir:
        filter_dir = target_dir.rstrip("\\")
        return filter_dir[:filter_dir.rfind("\\")]
    raise ValueError("invalid input")


def judge_util_ok(judge_func, timeout=20, sleep_interval=0.3, *args):
    """
    循环调用判断方法，直到判断为True或者超时
    :param judge_func: 判断方法，判断成功返回True
    :param timeout: 超时时间
    :param args: 判断方法的输入参数
    :return: True-满足判断条件；False-超时
    """
    is_ok = False
    start_time = time.time()
    while (time.time() - start_time) < timeout:
        is_ok = judge_func(*args)
        if is_ok:
            break
        time.sleep(sleep_interval)
    return is_ok