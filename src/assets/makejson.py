import json
a = [
    {
        "name": "pynodeA",
        "value": "null",
        "children": [
            {
                "name": "nodeAa",
                "value": 40
            },
            {
                "name": "nodeAb",
                "value": "null",
                "children": [
                    {
                        "name": "a",
                        "value": 20
                    },
                    {
                        "name": "b",
                        "value": "null",
                        "children": [
                            {
                                "name": "aa",
                                "value": 10
                            },
                            {
                                "name": "bbb",
                                "value": 30
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "name": "nodeB",
        "value": "null",
        "children": [
            {
                "name": "nodeBa",
                "value": "null",
                "children": [
                    {
                        "name": "nodeBa1",
                        "value": 10
                    },
                    {
                        "name": "nodeBa2",
                        "value": 10
                    }
                ]
            },
            {
                "name": "nodeBb",
                "value": 10
            }
        ]
    },
    {
        "name": "111",
        "value": 5
    },
    {
        "name": "222",
        "value": 20
    }
]

filename="test3.json"
f_obj=open(filename,'w')
json.dump(a,f_obj)
f_obj.close()
