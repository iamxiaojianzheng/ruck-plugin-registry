import os
import json
import re


def to_camel_case(snake_str):
    """
    将包含横杠的文件名转换为驼峰格式
    """
    components = snake_str.split("-")
    # 首字母小写，后面的首字母大写，其他字母小写
    return components[0] + "".join(x.title() for x in components[1:])


def merge_json_files():
    # 获取当前目录下所有的json文件
    json_files = [f for f in os.listdir(".") if f.endswith(".json")]

    merged_data = {}

    for json_file in json_files:
        # 去掉文件扩展名，获取文件名
        file_name = os.path.splitext(json_file)[0]
        # 如果文件名包含横杠，则转换为驼峰格式
        camel_case_name = to_camel_case(file_name)

        # 打开并读取json文件内容
        with open(json_file, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                merged_data[camel_case_name] = data
            except json.JSONDecodeError:
                print(f"Warning: {json_file} is not a valid JSON file, skipping.")

    # 输出合并后的 JSON 对象到一个新的文件
    with open("all.json", "w", encoding="utf-8") as output_file:
        json.dump(merged_data, output_file, ensure_ascii=False, indent=4)

    print("All JSON files have been merged into 'merged_output.json'.")


if __name__ == "__main__":
    merge_json_files()
