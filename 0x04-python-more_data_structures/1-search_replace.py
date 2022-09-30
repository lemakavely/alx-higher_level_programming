#!/usr/bin/python3
def search_replace(list_to_search, find, replace):
    def search_element(element):
        return (element if element != find else replace)
    return list(map(search_element, list_to_search))
