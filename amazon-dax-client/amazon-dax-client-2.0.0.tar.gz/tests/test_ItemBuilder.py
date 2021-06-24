from amazondax.ItemBuilder import ItemBuilder

from pprint import pprint


def test_item_builder():
    expected = { 
        'aaa': { 'M': { 
            'bbb': { 'M': { 
                'ccc': { 'S': 'hfuiwefuisdni' },
                'ddd': { 'M': { 
                    'eee': { 'N': '44237' },
                    'fff': { 'L': [ 
                        { 'M': { 'mapkey': { 'N': '123' } } }, 
                        { 'B': '23rh7823' } 
                    ]} 
                }},
                'ggg': { 'L': [ 
                    { 'L': [ { 'N': '3' } ] },
                    { 'M': { 
                        'hhh': { 'N': '1' }, 
                        'jjj': { 'N': '2' } 
                    }}
                ]} 
            }} 
        }} 
    }

    paths = [ 
        ['aaa', 'bbb', 'ccc'], 
        ['aaa', 'bbb', 'ddd', 'eee'], 
        ['aaa', 'bbb', 'ddd', 'fff', 1], 
        ['aaa', 'bbb', 'ddd', 'fff', 0], 
        ['aaa', 'bbb', 'ggg', 1, 'hhh'], 
        ['aaa', 'bbb', 'ggg', 1, 'jjj'], 
        ['aaa', 'bbb', 'ggg', 0, 1] 
    ]
    avs = [
        {'S': 'hfuiwefuisdni'}, 
        {'N': '44237'}, 
        {'B': '23rh7823'}, 
        {'M': {'mapkey': {'N': '123'}}}, 
        {'N': '1'}, 
        {'N': '2'}, 
        {'N': '3'}
    ]
    

    test_data = list(zip(paths, avs))
    
    builder = ItemBuilder()
    for path, av in test_data:
        builder.with_value(path, av)

    actual = builder.build()

    pprint(expected)
    pprint(actual)

    assert actual == expected

