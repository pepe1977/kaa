from kaa.theme import Theme, Style

DefaultThemes = {
    'default':
        Theme([
            Style('default', 'default', 'default', False, False),
            Style('lineno', 'White', 'Blue', False, False),
            Style('parenthesis_cur', 'White', 'Blue', False, False),
            Style('parenthesis_match', 'Red', 'Yellow', False, False),

            Style('keyword', 'red', 'default'),
            Style('comment', 'cyan', 'default'),
            Style('string', 'green', 'default'),
        ])
}
