# -*- coding: utf-8 -*-

# Copyright (c) 2017 Feras A. Saad <fsaad@mit.edu>
# Released under the MIT License; refer to LICENSE.txt.

import functools

import sublime
import sublime_plugin

from sublime import Region

LINESEP = '\n'

def region_reducer(state, region):
    """Helper method for line_to_paragraph_regions."""
    latest = state[-1]
    start, end  = region.begin(), region.end()
    pair = (start, end)
    if start == end:
        state.append(pair)
    elif latest[0] == latest[1]:
        state.append((start, end))
    else:
        state[-1] = (latest[0], end)
    return state

def line_to_paragraph_regions(splits):
    """Convert list of line regions into list of paragraph regions.

    >> splits = [(300, 364), (365, 441), (442, 498), (499, 499), (500, 500),
        (501, 576), (577, 649)]
    >> line_to_paragraph_regions(splits)
    [(300, 498), (499, 499), (500, 500), (501, 649)]
    """
    initial = (splits[0].begin(), splits[0].end())
    return functools.reduce(region_reducer, splits[1:], [initial])

class remove_paragraph_line_breaks(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        window = self.view.window()
        regions = list(view.sel())
        # Only handle one region for now. To handle multiple regions, it should
        # be easy to specify the remainder of this method as a function of
        # with a region parameter and provide each selected region as an
        # argument.
        if len(regions) > 1:
            window.status_message('Cannot remove lines in multiple regions.')
            return
        region = regions[0]
        region_selection = view.full_line(region)
        line_regions = view.split_by_newlines(region_selection)
        if len(line_regions) == 1:
            # This condition address a bug. When the last (blank) line in the
            # document is highlighted, an additional new line is added, because
            # the last line in the file is the only line that is not terminated
            # by \n.
            return
        paragraph_regions = line_to_paragraph_regions(line_regions)
        lines = [view.substr(Region(p[0], p[1])) for p in paragraph_regions]
        output = ''.join(
            '{contents}{linesep}'.format(
                contents=line.replace(LINESEP, ' '),
                linesep=LINESEP
                ) if line else LINESEP
            for line in lines
        )
        view.replace(edit, region_selection, output)
