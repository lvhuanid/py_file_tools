# This is a sample Python script.
import os
import re
import json

if __name__ == '__main__':
    print("start")


def low_first(str):
    return str[0].lower() + str[1:]



def childData():
    # 创建一个空字典，用于存储合并后的数据
    merged_data = {}
    # 遍历指定目录下的所有JSON文件
    directory = "new_json"
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    newKey = key.replace("Table", "")
                    if "nodetype" in value and value["nodetype"] == "table":
                        table_data = {k: v for k, v in value.items() if not isinstance(v, dict)}
                        table_child = {}
                        for k, v in value.items():
                            if isinstance(v, dict):
                                # oid_value = v.pop("oid", None)
                                oid_value = v["oid"]
                                # if "ProfileName" in v["name"] or "profileName" in v["name"]:
                                #     v["name"] = "name"
                                # if "ProfileIndex" in v["name"] or "profileIndex" in v["name"]:
                                #     v["name"] = "index"

                                # v["name"] = v["name"].replace(newKey, "")
                                # if v["name"]:
                                #     v["name"] = low_first(v["name"])

                                v.pop("nodetype", None)
                                v.pop("oid", None)
                                if oid_value is not None:
                                    j = oid_value.rsplit(".", 1)[-1]
                                    table_child[j] = v
                        table_data["child"] = table_child
                        table_data.pop("name", None)
                        merged_data[key] = table_data
    # 将合并后的数据写入一个新的JSON文件
    output_file = "merged_data5.json"
    with open(output_file, "w") as outfile:
        json.dump(merged_data, outfile, indent=4)

    print("JSON files merged and saved to", output_file)

def mergeData():
    # 存储所有JSON数据的列表
    all_data = []

    # 遍历指定目录下的所有JSON文件
    directory = "new_json"
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), "r") as file:
                data = json.load(file)
                all_data.append(data)

    # 将所有数据合并为一个列表
    merged_data = []
    for data in all_data:
        merged_data.extend(data)

    # 写入合并后的数据到新的JSON文件
    output_file = "merged_data.json"
    with open(output_file, "w") as outfile:
        json.dump(merged_data, outfile, indent=4)

    print("All JSON files merged and saved to", output_file)


def update_json_file(file_path, file_name):
    with open(file_path, 'r') as file:
        data = json.load(file)

    tables = {key: value for key, value in data.items() if
              isinstance(value, dict) and "Table" in key and "oid" in value}
    objects = [value for value in data.values() if isinstance(value, dict) and "oid" in value]
    updated_tables = {}  # 创建一个新字典来存储更新后的表格数据
    # table_objects = [{**obj, "oid": obj["oid"][obj["oid"].rfind(".") + 1:]} for obj in objects if table_value["oid"] in obj["oid"] and obj["oid"].count(".") - table_value["oid"].count(".") == 2]
    for table_key, table_value in tables.items():
        table_objects = []
        for obj in objects:
            if (len(table_value["oid"]) + 1 < len(obj["oid"])):
                if (table_value["oid"] == obj["oid"][:len(table_value["oid"])] and
                    obj["oid"].count(".") - table_value["oid"].count(".") == 2) and obj["oid"][
                    len(table_value["oid"])] == ".":
                    table_objects.append(obj)

        updated_table = {obj["name"]: obj for obj in table_objects}
        updated_tables[table_key] = {**table_value, **updated_table}  # 更新表格数据
    with open(f'new_json/{file_name}', 'w') as j_file:
        json.dump(updated_tables, j_file, indent=4)


def getData():
    # 指定包含JSON文件的文件夹路径
    folder_path = 'json'

    # 获取文件夹中所有文件的文件名列表
    file_names = os.listdir(folder_path)

    # 遍历文件夹中的每个文件
    for file_name in file_names:
        # 拼接文件的完整路径
        file_path = os.path.join(folder_path, file_name)
        print(file_name)

        # 检查文件是否为JSON文件
        if file_name.endswith('.json'):
            # 打开JSON文件并加载数据
            with open(file_path, 'r') as file:
                # json_data = json.load(file)
                file_path = os.path.join(folder_path, file_name)
                update_json_file(file_path, file_name)
                # 处理加载的JSON数据，这里只是简单打印
                # print(json_data)


# childData()
# with open('json/GENEW-FM-MIB.json', 'r') as file:
#     data = json.load(file)
#
# tables = {key: value for key, value in data.items() if isinstance(value, dict) and "Table" in key and "oid" in value}
# objects = [value for value in data.values() if isinstance(value, dict) and "oid" in value]
#
# updated_tables = {}  # 创建一个新字典来存储更新后的表格数据
#
# for table_key, table_value in tables.items():
#     table_objects = [obj for obj in objects if table_value["oid"] in obj["oid"]]
#     updated_table = {obj["name"]: obj for obj in table_objects}
#     updated_tables[table_key] = {**table_value, **updated_table}  # 更新表格数据
#
#
# # pprintpp.pprint(updated_tables)
#
# # # 将更新后的表格数据写入新的 JSON 文件
# with open('new_json/updated_tables.json', 'w') as j_file:
#     json.dump(updated_tables, j_file)


# with open("OnuRateControlSchedulerProfTable.java_file", 'r') as file:
#     data = file.read()
#     print(data)

def getJavaData():
    # 初始化一个列表来存储截取的内容
    datas = {}
    # 指定包含JSON文件的文件夹路径
    folder_path = 'java_file'

    # 获取文件夹中所有文件的文件名列表
    file_names = os.listdir(folder_path)

    # 遍历文件夹中的每个文件
    for file_name in file_names:
        # 拼接文件的完整路径
        file_path = os.path.join(folder_path, file_name)
        print(file_name)

        # 检查文件是否为JSON文件
        if file_name.endswith('.java'):
            # 打开JSON文件并加载数据
            with open(file_path, 'r') as file:
                # json_data = json.load(file)
                file_path = os.path.join(folder_path, file_name)
                test(file_path, datas)
                # 处理加载的JSON数据，这里只是简单打印
                # print(json_data)
    with open(f'new_java/1g.json', 'w') as j_file:
        json.dump(datas, j_file, indent=4)


t1 = open("childKeys.json", 'r')
childKeys: dict[str,str] = json.load(t1)
t2 = open("ctl_data.json", 'r')
ctlKeys: dict[str,str] = json.load(t2)
def test(file_path, datas):
    java_file_path = file_path
    # 初始化一个列表来存储截取的内容
    contents = []
    tableoid = ""
    # 定义正则表达式模式
    # pattern_braces = r'\{([^{}]+)\}'

    # 定义正则表达式模式
    pattern_init_table = r'/\*+\s*\*/\s*public class (\w+)'
    pattern_init_braces = r'init\(\) \{([^{}]+)\}'
    pattern_retrieve_braces = r'retrieve\(\) throws Exception \{([^{}]+)\}'

    pattern_snmp = r'initProperty\("(.*?)",\s*new SnmpMibBeanProperty\(".*?",\s*"(.*?)",\s*(\d+)\)'
    pattern_retrieve = r'getProperty\("(.*?)"\)'
    # 打开Java文件并读取内容
    with open(java_file_path, 'r') as file:
        java_code = file.read()

    # 使用正则表达式截取特定字符串开头的花括号内的内容
    matches_init = re.finditer(pattern_init_table, java_code)
    for match in matches_init:
        contents.append(match.group(1))
    newKey = low_first(contents[0].replace("Table", ""))
    replace_uts ="uts" + contents[0].replace("Table", "")
    matches_init = re.finditer(pattern_init_braces, java_code)
    for match in matches_init:
        fields = {}
        for match1 in re.finditer(pattern_snmp, match.group(1)):
            field_name, field_oid, field_type = match1.groups()
            j = field_oid.rsplit(".")
            if tableoid == "": tableoid = ".".join(j[:-2])
            # if "ProfileName" in field_name or "profileName" in field_name:
            #     field_name = "name"
            # if "ProfileIndex" in field_name or "profileIndex" in field_name:
            #     field_name = "index"

            # field_name = field_name.replace(newKey, "").replace(replace_uts, "")
            # if field_name:
            #     field_name = low_first(field_name)
            if field_name in childKeys:
                field_name = childKeys[field_name]
            type = 4 if int(field_type) == 100 else int(field_type)
            fields[j[-1]] = {"name": field_name, "type": type}
        contents.append(fields)

    matches_retrieve = re.finditer(pattern_retrieve_braces, java_code)
    for match in matches_retrieve:
        fields = []
        for match1 in re.finditer(pattern_retrieve, match.group(1)):
            value = match1.group(1)
            # if "ProfileName" in value or "profileName" in value:
            #     value = "name"
            # if "ProfileIndex" in value or "profileIndex" in value:
            #     value = "index"
            fields.append(value.replace(newKey, ""))
        contents.append(fields)
    print(contents)
    # if contents[0] == "OnuVPortSvcProfTable":
    #     contents[0] = "VirtualPortServiceProfile"
    # elif contents[0] == "OnuRateControlSchedulerProfTable":
    #     contents[0] = "RateControlProfile"
    # elif contents[0] == "IanModuleEntityTable":
    #     contents[0] = "BoardInformation"
    if contents[0] in ctlKeys:
        if len(contents) == 3:
            datas[ctlKeys[contents[0]]] = {"oid": tableoid[1:], "child": contents[1], "retrieve": contents[2]}
        else:
            datas[ctlKeys[contents[0]]] = {"oid": tableoid[1:], "child": contents[1]}
    else:
        if len(contents) == 3:
            datas[contents[0]] = {"oid": tableoid[1:], "child": contents[1], "retrieve": contents[2]}
        else:
            datas[contents[0]] = {"oid": tableoid[1:], "child": contents[1]}

    # # 输出截取的内容
    # for content in contents:
    #     # 使用正则表达式提取字段信息
    #     print(content)
    # print(fields)


# childData()
# getJavaData()
getJavaData()

def translate_file():
    # t1 = open("new_java/1.json", 'r')
    # javaData = json.load(t1)
    #
    # t1 = open("merged_data4.json", 'r')
    # all_data = json.load(t1)
    #
    # for data in all_data:
    #     value = all_data[data]
    #     for d in javaData:
    #         v = javaData[d]
    #         if value["oid"] == v["oid"]:
    #             print(v)

    contents = []
    t1 = open("60.async.js", 'r')
    text = t1.read()
    # 定义正则表达式模式
    pattern = r' = \{\s*tableId:.*?\};'
    # 使用正则表达式查找匹配项
    for match in re.finditer(pattern, text, re.DOTALL):
        t = match.group(0)
        m = t.replace("var r=", "").replace(";", "")
        contents.append(t)

    with open(f'new_java/2.json', 'w') as j_file:
        json.dump(contents, j_file, indent=4)

    x = open("new_java/3.js", 'w')
    tt = open("new_java/2.json", 'r')
    tm = json.load(tt)
    for t in tm:
        m = t.replace("var r =", "").replace(";", "")
        # print(m)
        x.write(f"\n{m},")

def tabel_column():
    new_data = {}
    new_data2 = {}
    file = open("new_java/d4.json", 'r', encoding='UTF-8')
    data = json.load(file)
    for d in data:
        column = []
        column2 = []
        for c in d["fields"]:
            line = c
            line["dataIndex"] = c["id"]
            line["title"] = c["display"][0]
            column.append(line)
            column2.append(c["id"])
        new_data[d["tableId"]] = {"columns": column}
        new_data2[d["tableId"]] = column2
    print(new_data)
    # # # 将更新后的表格数据写入新的 JSON 文件
    with open('new_java/column_dataz.json', 'w', encoding='utf-8') as j_file:
        json.dump(new_data, j_file, ensure_ascii=False, indent=4)
    with open('new_java/column_dataz2.json', 'w', encoding='utf-8') as j_file:
        json.dump(new_data2, j_file, ensure_ascii=False, indent=4)