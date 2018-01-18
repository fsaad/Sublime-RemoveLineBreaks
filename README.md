# RemoveLineBreaks

Sublime text plugin for removing all line breaks within paragraphs of text.
This plugin can be thought of as the inverse of hard wrapping lines, in the
sense that it removes all hard line breaks within a contiguous paragraph of
text.

Note that the plugin is not intended to merge separate paragraphs, as line
breaks between independent paragraphs are maintained. This plugin is appropriate
for editing text documents, not source code.

### Usage

First highlight the region of text in which to remove within-paragraph line
breaks (the highlight can span multiple paragraphs). Then open the command
palette using `ctrl+shift+p` and select "Remove Paragraph Line Breaks".

### Default Shortcuts

- __Remove Paragraph Line Breaks__: `alt+shift+q`

### Installation

Using [Package Control](https://packagecontrol.io/packages/RemoveLineBreaks),
type `ctrl+shift+p` > "Package Control: Install Package" > "RemoveLineBreaks".

Alternatively, clone this repository directly into
`~/.config/sublime-text-3/Packages/`.
