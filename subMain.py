import json
import os
import re

if __name__ == '__main__':
    print("start")  #

datas = {}
ctl_datas = {}
get_pattern = re.compile(r'get(\w+)', re.IGNORECASE)
get_pattern2 = re.compile(r'.get(\w+)', re.IGNORECASE)


def read_java_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def low_first(str):
    return str[0].lower() + str[1:]


def up_first(str):
    return str[0].upper() + str[1:]


# def parse_java_file(content):
#     tree = parse.parse(content)
test = read_java_file('controller_file/CsmPMController.java')

ARR = ["ports", "current", "Vlans", "{neId}", "{ssp}"]


def get_ctl_data(file_content):
    # pattern = r'Mapping\({(.*?)\)\n.*get.*?\(.*?\)\n.*get.*?\(.*?\)'
    # pattern = r'Mapping\({(.*?)}\)\n.*get.*?\(.*?\)'
    pattern = r'Mapping\({"(.*?)"}\)\n(.*get.*?)\n(.*get.*)'
    # patternR = r'/([^/]+)$'
    patternR = r'[^/]+/([^/]+)$'
    matches = re.finditer(pattern, file_content, re.MULTILINE)
    for match in matches:
        # get_match3 = re.search(pattern3, match.group(1))
        get_match1 = re.search(patternR, match.group(1))
        get_match2 = get_pattern2.search(match.group(3))
        get_match22 = get_pattern.search(match.group(2))
        if get_match1 is not None:
            # tableKey1 = up_first(get_match1.group(0).replace(f'/{get_match1.group(1)}', ""))
            # tableKey2 = up_first(get_match1.group(1))
            ctl_datas[up_first(get_match2.group(1))] = match.group(1).replace("/{neId}", "")
            ctl_datas[up_first(get_match22.group(1))] = match.group(1).replace("/{neId}", "")
            # if tableKey1 in ARR:
            #     if get_match2.group(1) != tableKey2 and get_match22.group(1) != tableKey2:
            #         ctl_datas[up_first(get_match2.group(1))] = tableKey2
            #         ctl_datas[up_first(get_match22.group(1))] = tableKey2
            # elif tableKey2 in ARR:
            #     if get_match2.group(1) != tableKey1 and get_match22.group(1) != tableKey1:
            #         ctl_datas[up_first(get_match2.group(1))] = tableKey1
            #         ctl_datas[up_first(get_match22.group(1))] = tableKey1

            # get_ctl_data(test)


def get_impl_data(file_content):
    # 使用正则表达式匹配包含 dto.set 的内容
    # 定义原始字符串的正则表达式模式
    pattern = r'to\.set(.*)'

    # 编译 set 和 get 的正则表达式模式
    set_pattern = re.compile(r'set(\w+)', re.IGNORECASE)

    matches = re.finditer(pattern, file_content)

    # 输出匹配结果
    for match in matches:
        # print(match.group(0))
        # 匹配 set 后面的单词
        set_match = set_pattern.search(match.group(0))
        get_match = get_pattern.search(match.group(0))
        if set_match:
            # print("Set value:", set_match.group(1))
            if get_match:
                # print("Get value:", get_match.group(1))
                if get_match.group(1) != set_match.group(1):
                    datas[low_first(get_match.group(1))] = low_first(set_match.group(1))


def ttt():
    # directory = "impl_file"
    directory = "controller_file"
    for filename in os.listdir(directory):
        if filename.endswith(".java"):
            with open(os.path.join(directory, filename), "r") as file:
                data = file.read()
                get_ctl_data(data)
                # get_impl_data(data)


table_dict = {}


def tableData():
    with open("data_table.json", "r", encoding='UTF-8') as outfile:
        data = json.load(outfile)
        for d in data:
            for c in ctl_datas:
                print(ctl_datas[c], data[d]["rpc"])
                if ctl_datas[c] == data[d]["rpc"]:
                    key = c.replace("CsmPortInfo", "CsmPortTable").replac("FanTemperature", "IanTemperatureMgmtFanTable")
                    table_dict[key] = d
                    ctl_datas[c] = d

            # table_dict[d] = value["rpc"]


ttt()
tableData()
print(ctl_datas)
print("---------------------------------------------------")
print(table_dict)

with open("ctl_data.json", "w") as outfile:
    # with open("childKeys.json", "w") as outfile:
    json.dump(table_dict, outfile, indent=4)
    # json.dump(datas, outfile, indent=4)
# print(ctl_datas)
# print(datas)
