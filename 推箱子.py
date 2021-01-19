def Init():
    Interface = [
        [2, 0, 0, 0, 0, 2],
        [0, 0, 2, 2, 0, 2],
        [0, 5, 1, 2, 0, 2],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 2, 1, 2, 0],
        [0, 4, 1, 2, 2, 0],
        [0, 4, 4, 3, 4, 0],
        [0, 0, 0, 0, 0, 0]
    ]  # 初始化界面
    return Interface


Interface = Init()

target = []  # 当人在目的地行走时，不会用空白将目的地覆盖
target_flag = 1


# 显示界面
def show(Interface):
    global target_flag
    for i in range(len(Interface)):
        for j in range(len(Interface[i])):
            if ((j + 1) % len(Interface[i]) != 0):  # 没有一行不换行
                end = ''
            else:
                end = '\n'
            if Interface[i][j] == 0:
                print('■', end=end)
            if Interface[i][j] == 1:
                print('☆', end=end)
            if Interface[i][j] == 2:
                print('  ', end=end)
            if Interface[i][j] == 3:
                print('●', end=end)
                if target_flag == 1:
                    target.append([i, j])
            if Interface[i][j] == 4:
                print('★', end=end)
                if target_flag == 1:
                    target.append([i, j])
            if Interface[i][j] == 5:
                print('♀', end=end)
    print('Show complete!')
    target_flag += 1  # 只添加第一次到target


def get_input(Interface):
    while True:
        break_flag = False  # 若指定运行完，则break
        input_key = input('请输入asdw(不区分大小写,分别对应左下右上):')
        for i in range(len(Interface)):
            for j in range(len(Interface[i])):
                if input_key == 'a' or input_key == 'A':  # 向左移动
                    # 如果数组为人且左边不为墙 那么俩种情况
                    if Interface[i][j] == 5 and Interface[i][j - 1] != 0:
                        if Interface[i][j - 1] != 1 and Interface[i][j - 1] != 3:  # 左边不为箱子，到达目的地
                            Interface[i][j - 1] = 5
                            Interface[i][j] = 2
                            break
                        else:  # 左边为箱子或目的地到达
                            if Interface[i][j - 2] != 0:  # 箱子左边不是墙
                                if Interface[i][j - 2] != 4:  # 箱子左边不是目的地
                                    Interface[i][j] = 2
                                    Interface[i][j - 1] = 5
                                    Interface[i][j - 2] = 1
                                else:  # 箱子到达目的地
                                    Interface[i][j] = 2
                                    Interface[i][j - 1] = 5
                                    Interface[i][j - 2] = 3

                            else:
                                pass
                elif input_key == 'd' or input_key == 'D':  # 向右移动
                    # 如果数组为人且右边不为墙 那么俩种情况
                    if Interface[i][j] == 5 and Interface[i][j + 1] != 0:
                        if Interface[i][j + 1] != 1 and Interface[i][j + 1] != 3:  # 右边不为箱子，到达目的地
                            Interface[i][j + 1] = 5
                            Interface[i][j] = 2
                            break  # 如果不break且右边没有障碍物 它会一直右走 for自左向右 向左无影响
                        else:  # 右边为箱子或目的地到达
                            if Interface[i][j + 2] != 0:  # 箱子右边不是墙
                                if Interface[i][j + 2] != 4:  # 箱子右边不是目的地
                                    Interface[i][j] = 2
                                    Interface[i][j + 1] = 5
                                    Interface[i][j + 2] = 1
                                    break
                                else:  # 箱子到达目的地
                                    Interface[i][j] = 2
                                    Interface[i][j + 1] = 5
                                    Interface[i][j + 2] = 3
                                    break
                            else:
                                pass
                elif input_key == 'w' or input_key == 'W':  # 向上移动
                    # 如果数组为人且上边不为墙 那么俩种情况
                    if Interface[i][j] == 5 and Interface[i - 1][j] != 0:
                        if Interface[i - 1][j] != 1 and Interface[i - 1][j] != 3:  # 上边不为箱子，到达目的地
                            Interface[i - 1][j] = 5
                            Interface[i][j] = 2
                            break
                        else:  # 上边为箱子或目的地到达
                            if Interface[i - 2][j] != 0:  # 箱子上边不是墙
                                if Interface[i - 2][j] != 4:  # 箱子上边不是目的地
                                    Interface[i][j] = 2
                                    Interface[i - 1][j] = 5
                                    Interface[i - 2][j] = 1
                                else:  # 箱子到达目的地
                                    Interface[i][j] = 2
                                    Interface[i - 1][j] = 5
                                    Interface[i - 2][j] = 3
                            else:
                                pass

                elif input_key == 's' or input_key == 'S':  # 向下移动
                    # 如果数组为人且下边不为墙 那么俩种情况
                    if Interface[i][j] == 5 and Interface[i + 1][j] != 0:
                        if Interface[i + 1][j] != 1 and Interface[i + 1][j] != 3:  # 下边不为 箱子，到达目的地
                            Interface[i + 1][j] = 5
                            Interface[i][j] = 2
                            break_flag = True

                        else:  # 下边为箱子或目的地到达
                            if Interface[i + 2][j] != 0:  # 箱子下边不是墙
                                if Interface[i + 2][j] != 4:  # 箱子下边不是目的地
                                    Interface[i][j] = 2
                                    Interface[i + 1][j] = 5
                                    Interface[i + 2][j] = 1
                                    break_flag = True
                                else:  # 箱子到达目的地
                                    Interface[i][j] = 2
                                    Interface[i + 1][j] = 5
                                    Interface[i + 2][j] = 3
                                    break_flag = True

                            else:
                                pass
                    if break_flag == True:  # 跳出第二层循环，否则会一直向下走 向上不会出现这种情况，因为for自上而下
                        break
                else:
                    print('您的输入有误，请重新输入')
                    break_flag = True
                    break
            if break_flag == True:  # 跳出第二层循环，否则会一直向下走 向上不会出现这种情况，因为for自上而下
                break

        for i in range(len(target)):
            for j in range(1):
                # 如果不是到达目的地的情况和人在目的地的情况   目的地还是为'★'
                if Interface[target[i][j]][target[i][j + 1]] != 3 and Interface[target[i][j]][target[i][j + 1]] != 5:
                    Interface[target[i][j]][target[i][j + 1]] = 4

        show(Interface)
        count = judge(Interface)

        if count == len(target):
            print('恭喜您，通关了')
            break


# 判断是否通关
def judge(Interface):
    count = 0  # 计数 如果都到达目的地 退出循环
    for i in range(len(Interface)):
        for j in range(len(Interface[i])):
            if Interface[i][j] == 3:
                count += 1
    return count


def main():
    show(Interface)
    get_input(Interface)


if __name__ == '__main__':
    main()
