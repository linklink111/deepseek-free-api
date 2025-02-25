import os

def print_directory_tree(root_dir, ignore_dirs=["node_modules"], prefix=""):
    # 获取目录下的所有项
    items = os.listdir(root_dir)
    directories = []
    files = []

    # 分离文件夹和文件
    for item in items:
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            if item not in ignore_dirs:  # 忽略指定文件夹
                directories.append(item)
        else:
            files.append(item)

    # 排序以保持一致性
    directories.sort()
    files.sort()

    # 打印目录结构
    items = directories + files
    for index, item in enumerate(items):
        is_last = index == len(items) - 1  # 判断是否是最后一个项
        item_path = os.path.join(root_dir, item)

        # 根据是否是最后一个项选择连接符
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{item}")

        # 如果是目录，递归打印子目录
        if item in directories:
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_directory_tree(item_path, ignore_dirs, new_prefix)

# 使用当前目录作为根目录
current_dir = os.getcwd()
print(f"Directory tree for: {current_dir}")
print_directory_tree(current_dir)