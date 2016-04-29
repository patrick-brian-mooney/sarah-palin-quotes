#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv, os

stats_file_path = 'stats/stats.csv'

def get_speech_info(quoteloc):
    """Get basic info for a specified speech, based on its filename"""
    desc = 'in a speech'    # Set some defaults in case something goes wrong
    location =''
    with open('speeches/sources.csv') as f:
        header = f.readline()               # Yeah, ignore that line.
        reader=csv.reader(f)
        the_table = [][:]
        for row in reader:
            if os.path.basename(quoteloc) == row[0]:
                desc = row[1]
                location = row[2]
                break
    return desc, location 

def create_stats_file():
    """Let's hope this only ever gets called the very first time stats get counted. Otherwise, it means we've lost count and are starting over.
    
    For the sake of being explicit:
          sarah_right means USER CORRECTLY IDENTIFIED A QUOTE AS COMING FROM SARAH PALIN
          sarah_wrong means USER SAID IT WAS FROM SARAH PALIN, BUT THAT WAS WRONG (e.g., wasn't able to identify a quote from the algorithm)
    
    Same deal for algorithm_right and algorithm_wrong.
    """
    empty_counts = {
        'sarah_right': 0,
        'sarah_wrong': 0,
        'algorithm_right': 0,
        'algorithm_wrong': 0}
    try:
        stats_file = open(stats_file_path, 'w')
    except FileNotFoundError:   # The directory doesn't exist, either
        os.mkdir(stats_file_path[ : len(stats_file_path) - len(os.path.basename(stats_file_path))])
        stats_file = open(stats_file_path, 'w')
    writer = csv.writer(stats_file)
    for which_key in empty_counts:
        writer.writerow([which_key, empty_counts[which_key]])
    stats_file.close()

def get_stats_dictionary():
    with open(stats_file_path) as stats_file:
        reader = csv.reader(stats_file)
        the_stats = {rows[0]:int(rows[1]) for rows in reader}
    return the_stats

def get_basic_stats():
    """Returns a tuple: ([int] total questions answered, [float] ratio of correct answers)"""
    try:
        with open(stats_file_path) as stats_file:
            reader = csv.reader(stats_file)
            the_stats = {rows[0]:int(rows[1]) for rows in reader}
        total = sum(the_stats.values())
        try:
            return total, (the_stats['sarah_right'] + the_stats['algorithm_right']) / total
        except ZeroDivisionError:
            return 0, 0
    except FileNotFoundError:   # create the file
        create_stats_file()
        return 0, 0

def bump_count(which_key):
    try:
        fd_file = os.open(stats_file_path, (os.O_RDWR | os.O_EXCL))
    except FileNotFoundError:
        create_stats_file()
        fd_file = os.open(stats_file_path, (os.O_RDWR | os.O_EXCL))
    stats_file = os.fdopen(fd_file, 'r+')
    reader = csv.reader(stats_file)
    the_stats = {rows[0]:int(rows[1]) for rows in reader}
    the_stats[which_key] += 1
    stats_file.seek(0)
    stats_file.truncate()
    writer = csv.writer(stats_file)
    for which_key in the_stats:
        writer.writerow([which_key, the_stats[which_key]])
    stats_file.close()          # I take it we don't need to separately close the file descriptor.
    