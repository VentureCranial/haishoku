#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-15 15:10
# @Author  : Gin (gin.lance.inside@hotmail.com)
# @Link    :
# @Disc    : alg about palette

import math

# def partition(num):
#     size = 256/num
#     return [[math.floor(size*i), math.floor(size*(i+1))] for i in range(num)]

# def in_partition(value, segment, partition):
#     return partition[segment][0] <= value and partition[segment][1] > value

def sort_by_rgb(colors_tuple):
    """ colors_tuple contains color count and color RGB
        we want to sort the tuple by RGB
        tuple[1]
    """
    sorted_tuple = sorted(colors_tuple, key=lambda x:x[1])
    return sorted_tuple

def group_by_accuracy(sorted_tuple, accuracy=3):
    """ group the colors by the accuaracy was given
        the R G B colors will be depart to accuracy parts
        default accuracy = 3

        [0, 85), [85, 170), [170, 256)

        Increasing accuracy will result in more granularity of the
        colorspace.
    """

    # 3D colorspace of accuracy
    rgb = [[[[] for i in range(accuracy)]
           for j in range(accuracy)]
           for k in range(accuracy)]

    size = math.floor(256.0 / accuracy)

    for color_tuple in sorted_tuple:
        r_tmp_i = color_tuple[1][0]
        r_part = min(math.floor(r_tmp_i/size), accuracy-1)

        g_tmp_i = color_tuple[1][1]
        g_part = min(math.floor(g_tmp_i/size), accuracy-1)

        b_tmp_i = color_tuple[1][2]
        b_part = min(math.floor(b_tmp_i/size), accuracy-1)

        rgb[r_part][g_part][b_part].append(color_tuple)

    return rgb

def get_weighted_mean(grouped_image_color):
    """ calculate every group's weighted mean

        r_weighted_mean = sigma(r * count) / sigma(count)
        g_weighted_mean = sigma(g * count) / sigma(count)
        b_weighted_mean = sigma(b * count) / sigma(count)
    """
    sigma_count = 0
    sigma_r = 0
    sigma_g = 0
    sigma_b = 0

    for item in grouped_image_color:
        sigma_count += item[0]
        sigma_r += item[1][0] * item[0]
        sigma_g += item[1][1] * item[0]
        sigma_b += item[1][2] * item[0]

    r_weighted_mean = int(sigma_r / sigma_count)
    g_weighted_mean = int(sigma_g / sigma_count)
    b_weighted_mean = int(sigma_b / sigma_count)

    weighted_mean = (sigma_count, (r_weighted_mean, g_weighted_mean, b_weighted_mean))
    return weighted_mean
