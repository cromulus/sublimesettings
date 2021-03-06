#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Format CSS properties: add space after property name:
padding:0; -> padding: 0;
@author Sergey Chikuyonok (serge.che@gmail.com)
@link http://chikuyonok.ru
'''
import re
import zencoding

re_css_prop = re.compile(r'([\w\-]+\s*:)(?!:)\s*')

@zencoding.filter('fc')
def process(tree, profile):
    for item in tree.children:
        # CSS properties are always snippets 
        if item.type == 'snippet':
            item.start = re_css_prop.sub(r'\1 ', item.start)
        
        process(item, profile)
        
    return tree