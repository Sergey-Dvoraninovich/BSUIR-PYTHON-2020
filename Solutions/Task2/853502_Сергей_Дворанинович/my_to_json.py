def ListToJson(a, s):
    local_string = '\n' + s + '['
    old_s = s
    s += '  '
    local_IsFirst = True
    common = ''
    for i in a:
        if local_IsFirst:
            local_IsFirst = False
        else:
            common = ','
        if type(i) == None:
            local_string += common + '\n' + s + 'null' + ''
        if type(i) == bool:
            local_string += common + '\n' + s + str(i) + ''
        elif type(i) == int:
            local_string += common + '\n' + s + str(i) + ''
        elif type(i) == float:
            local_string += common + '\n' + s + str(i) + ''
        elif type(i) == str:
            local_string += common + '\n' + s + str(i) + ''
        else:
            local_string += common + '\n' + s + ToJson(i, s)
    s = old_s
    local_string += '\n' + s + ']'
    return local_string


def DictToJson(a, s):
    local_string = '\n' + s + '{'
    old_s = s
    s += '  '
    local_IsFirst = True
    common = ''
    for i in a.items():
        if local_IsFirst:
            local_IsFirst = False
        else:
            common = ','
        if type(i[1]) == None:
            local_string += common + '\n' + s + '"' + str(i[0]) + '" : ' + 'null'
        elif type(i) == bool:
            local_string += common + '\n' + s + '"' + str(i[0]) + '" : ' + str(i[1])
        elif type(i[1]) == int:
            local_string += common + '\n' + s + '"' + str(i[0]) + '" : ' + str(i[1])
        elif type(i[1]) == float:
            local_string += common + '\n' + s + '"' + str(i[0]) + '" : ' + str(i[1]) + ''
        elif type(i[1]) == str:
            local_string += common + '\n' + s + '"' + str(i[0]) + '" : ' + str(i[1]) + ''
        else:
            local_string += common + '\n' + s + '"' + str(i[0]) + '" :'
            local_string += s + ToJson(i[1], s)
    s = old_s
    local_string += '\n' + s + '}'
    return local_string


def ToJson(a, s):
    json_string = ''
    if type(a) == bool:
        json_string += str(a)
    if type(a) == int:
        json_string += str(a)
    if type(a) == float:
        json_string += str(a)
    if type(a) == str:
        json_string += a

    if type(a) == list:
        json_string += ListToJson(a, s)
    if type(a) == tuple:
        json_string += ListToJson(a, s)
    if type(a) == dict:
        json_string += DictToJson(a, s)

    return json_string


def FullListToJson(parse_list, s):
    json_string = ''
    local_IsFirst = True
    comma = ''
    # print(parse_list)
    for item in parse_list:
        # print(item)
        # print(item)
        if local_IsFirst:
            local_IsFirst = False
        else:
            comma = ','
        if item[0] == 'dict':
            if item[1] != '':
                json_string += comma + '\n'
                json_string += s + '"' + str(item[1]) + '" : '
            json_string += '\n' + s + '{'
            super_local_IsFirst = True
            comma = ''
            for data_list in item[2]:
                if super_local_IsFirst:
                    super_local_IsFirst = False
                else:
                    comma = ','
                # json_string += s + '{'
                json_string += comma + FullListToJson([data_list], s + '  ')
            json_string += '\n' + s + '}'
        #        #json_string = item[2]#FullListToJson(item[2], s)
        #        print(item[2])
        else:
            local_str = item[1]
            json_string += comma + '\n'
            json_string += s + '"' + local_str + '" : '
            if type(item[2]) == list:
                json_string += '\n' + s + '['
                super_local_IsFirst = True
                comma = ''
                for data_list in item[2]:
                    if super_local_IsFirst:
                        super_local_IsFirst = False
                    else:
                        comma = ','
                    # json_string += s + '{'
                    json_string += comma + FullListToJson([data_list], s + '  ')
                json_string += '\n' + s + ']'
            else:
                json_string += ToJson(item[2], s)
    return json_string


def IsPossibleToParse(type):
    if type == bool:
        return True
    elif type == int:
        return True
    elif type == float:
        return True
    elif type == str:
        return True
    elif type == list:
        return True
    elif type == tuple:
        return True
    elif type == dict:
        return True
    else:
        return False


attrib_list = []


class Mypair(object):
    def __init__(self):
        """Constructor"""
        self.pair_x = 1
        self.pair_y = 2


first = Mypair()
second = Mypair()
MainPoint = Mypair()


class Venicle(object):
    def __init__(self, d):
        """Constructor"""
        self.color = 'black'
        self.doors = 4
        self.tires = 'good'
        self.vtype = 'sedan'
        self.dictionary = d
        self.two_points = [first, second]
        self.point = MainPoint
        self.power = 456.3
        self.right_hand = True


def Parse(object_to_parse, MakeClass):
    parse_list = []
    Main_elem = None
    for elem in dir(object_to_parse):
        if elem[0] == '_':
            continue
        else:
            attr_value = getattr(object_to_parse, elem)
            attr_type = type(attr_value)
            if IsPossibleToParse(attr_type):
                if MakeClass == True:
                    Main_elem = elem
                if type(attr_value) == list:
                    if attr_value != []:
                        new_attr_value = []
                        for current_elem in attr_value:
                            if not IsPossibleToParse(type(current_elem)):
                                add = Parse(current_elem, True)
                                new_attr_value.append(add)
                        attr_value = new_attr_value
                parse_list.append([attr_type, elem, attr_value])
            else:
                parsed_elements = Parse(attr_value, False)
                wrong = False
                if type(parsed_elements) == list:
                    if not wrong:
                        parse_list.append(['dict', elem, parsed_elements])

    if Main_elem:
        return ['dict', '', parse_list]
    return parse_list


# for attrib in Parse(test):
#    print(attrib)

def to_json(object_to_parse):
    parse_list = Parse(object_to_parse, False)
    # print(parse_list)
    # for item in parse_list:
    # print('_', item)
    s = '  '
    IsFirst = True
    json_string = '{'
    json_string += FullListToJson(parse_list, s)
    json_string += '\n}'
    return json_string

def to_json_test():
    d = {'Value': 12, 'Problems': 'null', 'Name': 'Alex', 'Cars': ['BMW', 'AUDI', 'Opel', True, False, 12, 12.3]}
    test = Venicle(d)
    ans = ""
    main_string = to_json(test)
    local_items = tuple(locals().items())
    for name, value in local_items:
        if value is test:
            ans += '"' + str(name) + '" : \n'
    ans += main_string
    return ans

#print(to_json_test())
#with open('2_module_right.txt', 'w') as file:
#    file.write(to_json_test())