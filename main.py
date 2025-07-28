import os


def list_directory(path, indent=0):
    """
    递归列出指定目录下的所有文件和文件夹

    参数:
        path (str): 要列出的目录路径
        indent (int): 用于格式化输出的缩进量
    """
    try:
        # 获取目录中的所有项目
        items = os.listdir(path)

        for item in items:
            # 构建项目的完整路径
            item_path = os.path.join(path, item)

            # 确定项目类型（文件夹或文件）
            if os.path.isdir(item_path):
                # 文件夹，使用不同的符号标识
                print("  " * indent + "├── 📁 " + item)
                # 递归列出子目录
                list_directory(item_path, indent + 1)
            else:
                # 文件
                print("  " * indent + "├── 📄 " + item)

    except PermissionError:
        print("  " * indent + "❌ 权限不足，无法访问该目录")
    except FileNotFoundError:
        print("❌ 目录不存在: " + path)
    except Exception as e:
        print(f"  " * indent + f"❌ 发生错误: {str(e)}")


if __name__ == "__main__":
    # 可以修改为你想要查看的目录路径
    target_directory = "ACwing蓝桥杯每日一题"  # 当前目录

    print(f"📂 目录内容: {os.path.abspath(target_directory)}\n")
    list_directory(target_directory)
