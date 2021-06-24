import re

from amazondax.DynamoDbV1Converter import convert_request, _convert_conditions_to_expr
from amazondax.Constants import DaxDataRequestParam, DaxMethodIds

import pytest

attributesToGet = ['attr0', 'attr1']
expectedOrFilter = {
        'attr0': {
            'ComparisonOperator': 'LE',
            'AttributeValueList': [ {'N':'0.00'} ]
            },
        'attr1': {
            'ComparisonOperator': 'GT',
            'AttributeValueList': [ {'N':'1.00'} ]
            },
        'attr2': {
            'ComparisonOperator': 'GE',
            'AttributeValueList': [ {'N':'2.00'} ]
            }
        }

TEST_V1V2 = [
    pytest.param(
        {
            'ReturnConsumedCapacity': 'NONE',
            'ProjectionExpression': '#key0,#key1',
            'ExpressionAttributeNames': {
                '#key0': 'attr0',
                '#key1': 'attr1'
            }
        },
        DaxMethodIds.getItem_263244906_1_Id, 
        {
            'ReturnConsumedCapacity': 'NONE',
            'ProjectionExpression': '#key0,#key1',
            'ExpressionAttributeNames': {
                '#key0': 'attr0',
                '#key1': 'attr1'
            }
        },
        id='getItem non-V1 request'
    ),
    pytest.param(
        {'AttributesToGet': attributesToGet},
        DaxMethodIds.getItem_263244906_1_Id, 
        {
            'ReturnConsumedCapacity': 'NONE',
            'ProjectionExpression': '#key0,#key1',
            'ExpressionAttributeNames': {
                '#key0': 'attr0',
                '#key1': 'attr1'
            }
        },
        id='getItem with AttributesToGet'
    ), 
    pytest.param(
        {'RequestItems': {
            'Table0': {
                'AttributesToGet': attributesToGet
                }
            }},
        DaxMethodIds.batchGetItem_N697851100_1_Id, 
        {
            'ReturnConsumedCapacity': 'NONE',
            'RequestItems': {
                'Table0': {
                    'ProjectionExpression': '#key0,#key1',
                    'ExpressionAttributeNames': {
                        '#key0': 'attr0',
                        '#key1': 'attr1'
                        },
                    }
                }
            },
        id='batchGetItem with AttributesToGet'
        ), 
    pytest.param(
        {'Expected': expectedOrFilter},
        DaxMethodIds.deleteItem_1013539361_1_Id, 
        {
            'ReturnConsumedCapacity': 'NONE',
            'ConditionExpression': '#key0 <= :val0 AND #key1 > :val1 AND #key2 >= :val2',
            'ExpressionAttributeNames': {
                '#key0': 'attr0',
                '#key1': 'attr1',
                '#key2': 'attr2'
                },
            'ExpressionAttributeValues': {
                ':val0': {'N':'0.00'},
                ':val1': {'N':'1.00'},
                ':val2': {'N':'2.00'}
                }
            },
        id='deleteItem with Expected'
        ), 
    pytest.param(
        {'Expected': expectedOrFilter},
        DaxMethodIds.updateItem_1425579023_1_Id, 
        {
            'ReturnConsumedCapacity': 'NONE',
            'ConditionExpression': '#key0 <= :val0 AND #key1 > :val1 AND #key2 >= :val2',
            'ExpressionAttributeNames': {
                '#key0': 'attr0',
                '#key1': 'attr1',
                '#key2': 'attr2'
                },
            'ExpressionAttributeValues': {
                ':val0': {'N':'0.00'},
                ':val1': {'N':'1.00'},
                ':val2': {'N':'2.00'}
                }

        },
        id='updateItem with Expected'
    ), 
    pytest.param(
        {'AttributeUpdates':{
            'attr0': {
                'Action': 'PUT',
                'Value': {'S': 'ss3'}
            },
            'attr1': {
                'Action': 'ADD',
                'Value': {'SS': ['ss51', 'ss52']}
                },
            'attr2': {
                'Action': 'DELETE',
                'Value': {'SS': ['ss71', 'ss72']}
                },
            'attr3': {
                'Action': 'DELETE',
                }
            }
            },
        DaxMethodIds.updateItem_1425579023_1_Id, 
        {
            'ReturnConsumedCapacity': 'NONE',
            'ExpressionAttributeNames': {
                '#key0': 'attr0',
                '#key1': 'attr1',
                '#key2': 'attr2',
                '#key3': 'attr3'
            },
            'ExpressionAttributeValues': {
                ':val0': {'S': 'ss3'},
                ':val1': {'SS': ['ss51', 'ss52']},
                ':val2': {'SS': ['ss71', 'ss72']}
            },
            'UpdateExpression': 'SET #key0 = :val0 ADD #key1 :val1 DELETE #key2 :val2 REMOVE #key3'        
        },
        id='updateItem with AttributeUpdates where actions appear once'
    ), 
    pytest.param({'AttributeUpdates':
            {
                'attr3': {
                    'Action': 'PUT',
                    'Value': {'S': 'ss3'}
                    },
                'attr4': {
                    'Action': 'PUT',
                    'Value': {'S': 'ss4'}
                    },
                'attr5': {
                    'Action': 'ADD',
                    'Value': {'SS': ['ss51', 'ss52']}
                    },
                'attr6': {
                    'Action': 'ADD',
                    'Value': {'N': '6'}
                    },
                'attr7': {
                    'Action': 'DELETE',
                    'Value': {'SS': ['ss71', 'ss72']}
                    },
                'attr8': {
                    'Action': 'DELETE',
                    'Value': {'N': '8'}
                    },
                'attr9': {
                    'Action': 'DELETE',
                    },
                'attr10': {
                    'Action': 'DELETE',
                    }
                }},
            DaxMethodIds.updateItem_1425579023_1_Id, 
            {
                'ReturnConsumedCapacity': 'NONE',
                'ExpressionAttributeNames': {
                    '#key0': 'attr10',
                    '#key1': 'attr3',
                    '#key2': 'attr4',
                    '#key3': 'attr5',
                    '#key4': 'attr6',
                    '#key5': 'attr7',
                    '#key6': 'attr8',
                    '#key7': 'attr9',
                    },
                'ExpressionAttributeValues': {
                    ':val0': {'S': 'ss3'},
                    ':val1': {'S': 'ss4'},
                    ':val2': {'SS': ['ss51', 'ss52']},
                    ':val3': {'N': '6'},
                    ':val4': {'SS': ['ss71', 'ss72']},
                    ':val5': {'N': '8'}
                    },
                'UpdateExpression': 'SET #key1 = :val0, #key2 = :val1 ADD #key3 :val2, #key4 :val3 DELETE #key5 :val4, #key6 :val5 REMOVE #key0, #key7'
                },
            id='updateItem with AttributeUpdates where Actions appear multiple times'
    ), 
    pytest.param(
            {
                'Expected': expectedOrFilter,
                'AttributeUpdates': {
                    'attr3': {
                        'Action': 'PUT',
                        'Value': {'S': 'ss3'}
                        },
                    'attr4': {
                        'Action': 'PUT',
                        'Value': {'S': 'ss4'}
                        },
                    'attr5': {
                        'Action': 'ADD',
                        'Value': {'SS': ['ss51', 'ss52']}
                        },
                    'attr6': {
                        'Action': 'ADD',
                        'Value': {'N': '6'}
                        },
                    'attr7': {
                        'Action': 'DELETE',
                        'Value': {'SS': ['ss71', 'ss72']}
                        },
                    'attr8': {
                        'Action': 'DELETE',
                        'Value': {'N': '8'}
                        },
                    'attr9': {
                        'Action': 'DELETE',
                        },
                    'attr10': {
                        'Action': 'DELETE',
                        }
                    }

                },
            DaxMethodIds.updateItem_1425579023_1_Id, 
            {
                'ReturnConsumedCapacity': 'NONE',
                'ConditionExpression': '#key0 <= :val0 AND #key1 > :val1 AND #key2 >= :val2',
                'ExpressionAttributeNames': {
                    '#key0': 'attr0',
                    '#key1': 'attr1',
                    '#key2': 'attr2',
                    '#key3': 'attr10',
                    '#key4': 'attr3',
                    '#key5': 'attr4',
                    '#key6': 'attr5',
                    '#key7': 'attr6',
                    '#key8': 'attr7',
                    '#key9': 'attr8',
                    '#key10': 'attr9'
                    },
                'ExpressionAttributeValues': {
                    ':val0': {'N':'0.00'},
                    ':val1': {'N':'1.00'},
                    ':val2': {'N':'2.00'},
                    ':val3': {'S': 'ss3'},
                    ':val4': {'S': 'ss4'},
                    ':val5': {'SS': ['ss51', 'ss52']},
                    ':val6': {'N': '6'},
                    ':val7': {'SS': ['ss71', 'ss72']},
                    ':val8': {'N': '8'}

                    },
                'UpdateExpression': 
                    'SET #key4 = :val3, #key5 = :val4 ADD #key6 :val5, #key7 :val6 DELETE #key8 :val7, #key9 :val8 REMOVE #key3, #key10'
                },
            id='updateItem fully loaded'
    ), 
    pytest.param(
        {'Expected': expectedOrFilter,},
        DaxMethodIds.putItem_N2106490455_1_Id, 
        {
            'ReturnConsumedCapacity': 'NONE',
            'ConditionExpression': '#key0 <= :val0 AND #key1 > :val1 AND #key2 >= :val2',
            'ExpressionAttributeNames': {
                '#key0': 'attr0',
                '#key1': 'attr1',
                '#key2': 'attr2'
                },
            'ExpressionAttributeValues': {
                ':val0': {'N':'0.00'},
                ':val1': {'N':'1.00'},
                ':val2': {'N':'2.00'}
                }
        },
        id='putItemWithExpected'
    ), 
    # TODO vvv Copy the query/scan test from JS vvv
    pytest.param(
        {'AttributesToGet': attributesToGet},
        DaxMethodIds.query_N931250863_1_Id, 
        {
            'ReturnConsumedCapacity': 'NONE',
            'ProjectionExpression': '#key0,#key1',
            'ExpressionAttributeNames': {
                '#key0': 'attr0',
                '#key1': 'attr1'
            }
        },
        id='Query with AttributesToGet'
    ), 
    pytest.param(
        {'QueryFilter': expectedOrFilter},
        DaxMethodIds.query_N931250863_1_Id, 
        {
            'ReturnConsumedCapacity': 'NONE',
            'FilterExpression': '#key0 <= :val0 AND #key1 > :val1 AND #key2 >= :val2',
            'ExpressionAttributeNames': {
                '#key0': 'attr0',
                '#key1': 'attr1',
                '#key2': 'attr2'
            },
            'ExpressionAttributeValues': {
                ':val0': {'N':'0.00'},
                ':val1': {'N':'1.00'},
                ':val2': {'N':'2.00'}
            }
        },
        id='Query with QueryFilter'
    ), 
    pytest.param(
        {'KeyConditions': expectedOrFilter},
        DaxMethodIds.query_N931250863_1_Id, 
        {
            'ReturnConsumedCapacity': 'NONE',
            'KeyConditionExpression': '#key0 <= :val0 AND #key1 > :val1 AND #key2 >= :val2',
            'ExpressionAttributeNames': {
                '#key0': 'attr0',
                '#key1': 'attr1',
                '#key2': 'attr2'
            },
            'ExpressionAttributeValues': {
                ':val0': {'N':'0.00'},
                ':val1': {'N':'1.00'},
                ':val2': {'N':'2.00'}
            }
        },
        id='Query with KeyConditions'
    ), 
    pytest.param(
        {
            'AttributesToGet': attributesToGet,
            'QueryFilter': expectedOrFilter,
            'KeyConditions': expectedOrFilter,
        },
        DaxMethodIds.query_N931250863_1_Id, 
        {
            'ReturnConsumedCapacity': 'NONE',
            'ExpressionAttributeNames': {
                '#key0': 'attr0',
                '#key1': 'attr1',
                '#key2': 'attr0',
                '#key3': 'attr1',
                '#key4': 'attr2',
                '#key5': 'attr0',
                '#key6': 'attr1',
                '#key7': 'attr2'
            },
            'ExpressionAttributeValues': {
                ':val0': {'N':'0.00'},
                ':val1': {'N':'1.00'},
                ':val2': {'N':'2.00'},
                ':val3': {'N':'0.00'},
                ':val4': {'N':'1.00'},
                ':val5': {'N':'2.00'}
            },
            'FilterExpression': '#key5 <= :val3 AND #key6 > :val4 AND #key7 >= :val5',
            'KeyConditionExpression': '#key2 <= :val0 AND #key3 > :val1 AND #key4 >= :val2',
            'ProjectionExpression': '#key0,#key1',
        },
        id='Query fully loadded'
    ), 
    pytest.param(
        {'AttributesToGet': attributesToGet},
        DaxMethodIds.scan_N1875390620_1_Id, 
        {
            'ReturnConsumedCapacity': 'NONE',
            'ProjectionExpression': '#key0,#key1',
            'ExpressionAttributeNames': {
                '#key0': 'attr0',
                '#key1': 'attr1'
            }
        },
        id='scan with AttributesToGet'
    ), 
    pytest.param(
        {'ScanFilter': expectedOrFilter},
        DaxMethodIds.scan_N1875390620_1_Id, 
        {
            'ReturnConsumedCapacity': 'NONE',
            'FilterExpression': '#key0 <= :val0 AND #key1 > :val1 AND #key2 >= :val2',
            'ExpressionAttributeNames': {
                '#key0': 'attr0',
                '#key1': 'attr1',
                '#key2': 'attr2'
            },
            'ExpressionAttributeValues': {
                ':val0': {'N':'0.00'},
                ':val1': {'N':'1.00'},
                ':val2': {'N':'2.00'}
            }
        },
        id='scan with ScanFilter'
    ), 
    pytest.param(
        {
            'AttributesToGet': attributesToGet,
            'ScanFilter': expectedOrFilter
        },
        DaxMethodIds.scan_N1875390620_1_Id, 
        {
            'ReturnConsumedCapacity': 'NONE',
            'ExpressionAttributeNames': {
                '#key0': 'attr0',
                '#key1': 'attr1',
                '#key2': 'attr0',
                '#key3': 'attr1',
                '#key4': 'attr2'
            },
            'ExpressionAttributeValues': {
                ':val0': {'N':'0.00'},
                ':val1': {'N':'1.00'},
                ':val2': {'N':'2.00'}
            },
            'FilterExpression': '#key2 <= :val0 AND #key3 > :val1 AND #key4 >= :val2',
            'ProjectionExpression': '#key0,#key1'
        },
        id='scan fullyLoaded'
    ), 
]
@pytest.mark.parametrize("ddb_request, method_id, expected", TEST_V1V2)
def test_v1_to_v2_conversion(ddb_request, method_id, expected):
    orig_request = ddb_request.copy()

    result = convert_request(ddb_request, method_id)

    # Ensure the orignal is not changed
    assert ddb_request == orig_request

    assert result == expected

def test_convert_conditions_to_filter_expr():
    arg = [{'N': '12'},
        {'N': '15'},
        {'S': 'value2'},
        {'S': 'value3'},
        {'S': 'SS2'},
        {'N': '17'},
        {'N': '20'},
        {'N': '21'},
        {'N': '22'},
        {'N': '23'},
        {'N': '24'},
        {'N': '25'},
        {'N': '26'},
        {'S': 'ABC'},
        {'S': 'DEF'}
    ]

    input_filter = {
      'Attribute1': {
        'AttributeValueList':[arg[0], arg[1]],
        'ComparisonOperator': 'BETWEEN'
      },
      'Attribute2': {
        'AttributeValueList':[arg[2]],
        'ComparisonOperator': 'BEGINS_WITH'
      },
      'Attribute3': {
        'AttributeValueList':[arg[3]],
        'ComparisonOperator': 'NOT_CONTAINS'
      },
      'Attribute4': {
        'AttributeValueList':[arg[4]],
        'ComparisonOperator': 'CONTAINS'
      },
      'Attribute5': {
        'ComparisonOperator': 'NOT_NULL'
      },
      'Attribute6': {
        'ComparisonOperator': 'NULL'
      },
      'Attribute7': {
        'AttributeValueList':[arg[5], arg[6]],
        'ComparisonOperator': 'IN'
      },
      'Attribute8': {
        'AttributeValueList':[arg[7]],
        'ComparisonOperator': 'EQ'
      },
      'Attribute9': {
        'AttributeValueList':[arg[8]],
        'ComparisonOperator': 'LE'
      },
      'Attribute10': {
        'AttributeValueList':[arg[9]],
        'ComparisonOperator': 'LT'
      },
      'Attribute11': {
        'AttributeValueList':[arg[10]],
        'ComparisonOperator': 'GE'
      },
      'Attribute12': {
        'AttributeValueList':[arg[11]],
        'ComparisonOperator': 'GT'
      },
      'Attribute13': {
        'AttributeValueList':[arg[12]],
        'ComparisonOperator': 'NE'
      },
      'Attribute14': {
        'AttributeValueList':[arg[13], arg[14]],
        'ComparisonOperator': 'BETWEEN'
      }
    }

    expr_attr_names = {}
    expr_attr_values = {}
    actual = _convert_conditions_to_expr(input_filter,
      'AND', expr_attr_names, expr_attr_values, DaxDataRequestParam.FilterExpression)
    expected = '''#key0 between :val0 AND :val1  
        AND #key1 < :val2 
        AND #key2 >= :val3 
        AND #key3 > :val4 
        AND #key4 <> :val5 
        AND #key5 between :val6 AND :val7
        AND begins_with(#key6, :val8)
        AND attribute_exists(#key7) AND NOT contains(#key7, :val9) 
        AND contains(#key8, :val10)
        AND attribute_exists(#key9) 
        AND attribute_not_exists(#key10) 
        AND #key11 IN (:val11,:val12) 
        AND #key12 = :val13
        AND #key13 <= :val14'''
    expected = re.sub(r'\s+', ' ', expected)

    assert actual == expected

    assert len(expr_attr_names) == 14
    for i, k in enumerate(sorted(input_filter)):
        assert expr_attr_names['#key%s' % i] == k

    assert len(expr_attr_values) == 15
    for i, arg in enumerate(arg for k, v in sorted(input_filter.items()) for arg in v.get('AttributeValueList', [])):
        assert expr_attr_values[':val%s' % i] == arg

def test_convert_conditions_to_condition_expr():
    input_expr = {
        'attr0': {
            'ComparisonOperator': 'LE',
            'AttributeValueList': [ {'N':'0.00'} ]
            },
        'attr1': {
            'Exists': 'true',
            'Value': {'N':'1.00'}
            },
        'attr2': {
            'ComparisonOperator': 'GT',
            'Value': {'N':'2.00'}
            }
        }

    expected = {
        'ConditionExpression': '#key0 <= :val0 AND #key1 = :val1 AND #key2 > :val2',
        'ExpressionAttributeNames': {
            '#key0': 'attr0',
            '#key1': 'attr1',
            '#key2': 'attr2'
            },
        'ExpressionAttributeValues': {
            ':val0': {'N':'0.00'},
            ':val1': {'N':'1.00'},
            ':val2': {'N':'2.00'}
            }
        }

    expr_attr_names = {}
    expr_attr_values = {}
    
    cond_expr = _convert_conditions_to_expr(input_expr,
      'AND', expr_attr_names, expr_attr_values, DaxDataRequestParam.ConditionExpression)

    actual = {
        'ConditionExpression': cond_expr,
        'ExpressionAttributeNames': expr_attr_names,
        'ExpressionAttributeValues': expr_attr_values,
    }

    assert actual == expected


