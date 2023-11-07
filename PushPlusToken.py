import os
import re
import subprocess

while True:
    push_plus_token = input("请输入您的 PushPlusToken: ")
    if push_plus_token:
        save_choice = input("要保存修改吗？(y/n): ")
        if save_choice == "y":
            config_file = "/sms/forward/DbusSmsForward.dll.config"
            if os.path.isfile(config_file):
                with open(config_file, "r") as file:
                    config_data = file.read()
                    # 使用re.sub进行正则表达式替换
                    updated_data = re.sub(
                        r"<add key=\"pushPlusToken\" value=\"[^\"]*\" />",
                        f"<add key=\"pushPlusToken\" value=\"{push_plus_token}\" />",
                        config_data
                    )
                with open(config_file, "w") as file:
                    file.write(updated_data)
                print(f"PushPlusToken 已成功设置为: {push_plus_token}")

                # 执行systemctl restart sms
                try:
                    subprocess.run(["systemctl", "restart", "sms"], check=False)
                    print("已执行 systemctl restart sms")
                except Exception as e:
                    print(f"执行 systemctl restart sms 时出现错误: {str(e)}")

                break
            else:
                print(f"配置文件 {config_file} 不存在，请确保文件存在。")
        elif save_choice == "n":
            print("未保存修改，重新输入 PushPlusToken。")
        else:
            print("无效的选择，请输入 'y' 或 'n'。")
    else:
        print("未提供有效的 PushPlusToken，请重新输入。")
