# encoding = utf-8

# 批量升级maven的版本
import os


def search(file, dir):
    file = str(file)
    dir = str(dir)

    if not os.path.isdir(dir):
        if dir.endswith(file):
            print(dir)
            return [dir]
        else:
            return []
    if not dir.endswith("/"):
        dir += "/"
    all_files = []
    for new_dir in os.listdir(dir):
        if new_dir.startswith("."):
            continue
        all_files += search(file, dir + new_dir)
    return all_files


def get_label_content(label, string):
    label = str(label)
    string = str(string).strip()

    if string.count(label) >= 2:
        length = len(label) + 2

        return string[length:-(length + 1)]

    return None


def replace_label_content(label, string, new_content):
    content = get_label_content(label, string)
    if content:
        new_string = ""
        for i in range(0, line.index("<")):
            new_string += " "
        new_string += "<" + label + ">" + new_content + "</" + label + ">\n"
        string = new_string

    return string


if __name__ == "__main__":
    root_path = input("输入路径：")
    artifactId = input("请输入artifactId：")
    version = input("请输入version：")

    list = search("pom.xml", root_path)



    for path in list:
        pom_file = open(path, encoding="utf-8")
        new_pom_file = open(path + ".new", "w", encoding="utf-8")
        is_fund = False
        version_placeholder = None
        for line in pom_file:
            new_line = line
            if is_fund:
                # 如果标记位为true，则表示改行为版本号所在行
                content = get_label_content("version", line)
                if content and content.startswith("${"):
                    # 如果以${其实，表示使用了占位符
                    version_placeholder = content[2:-1]
                else:
                    # 否则，此处content就是版本号
                    new_line = replace_label_content("version", line, version)

                is_fund = False
            else:

                if version_placeholder != None:
                    # 如果占位符已经找到，则尝试替换
                    new_line = replace_label_content(version_placeholder, line, version)

                # 尝试查询artifactId
                content = get_label_content("artifactId", new_line)
                if content and content == artifactId:
                    # 如果找到，则修改标记，将在下一行获取占位符
                    is_fund = True

            new_pom_file.write(new_line)

        pom_file.close()
        new_pom_file.close()

        os.remove(path)
        os.rename(path + ".new", path)

    print("完成")
    print("共搜索到" + str(len(list)) + "个pom.xml")
