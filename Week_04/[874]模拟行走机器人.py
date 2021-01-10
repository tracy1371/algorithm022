# 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令： 
# 
#  
#  -2：向左转 90 度 
#  -1：向右转 90 度 
#  1 <= x <= 9：向前移动 x 个单位长度 
#  
# 
#  在网格上有一些格子被视为障碍物。 
# 
#  第 i 个障碍物位于网格点 (obstacles[i][0], obstacles[i][1]) 
# 
#  机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。 
# 
#  返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。 
# 
#  
# 
#  示例 1： 
# 
#  输入: commands = [4,-1,3], obstacles = []
# 输出: 25
# 解释: 机器人将会到达 (3, 4)
#  
# 
#  示例 2： 
# 
#  输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# 输出: 65
# 解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
#  
#
#  
# 
#  提示： 
# 
#  
#  0 <= commands.length <= 10000 
#  0 <= obstacles.length <= 10000 
#  -30000 <= obstacle[i][0] <= 30000 
#  -30000 <= obstacle[i][1] <= 30000 
#  答案保证小于 2 ^ 31 
#  
#  Related Topics 贪心算法 
#  👍 120 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 障碍点转成set提高速度
        obstacles = set(map(tuple,obstacles))
        x, y = 0, 0
        res = 0
        # 方向列表，或者循环链表
        faceto = ['N','E','S','W']
        faceindex = 0
        for i in commands:
            # command 为 -1，顺时针转向，超限重新从index 0 开始
            if i == -1:
                if faceindex + 1 == 4:
                    faceindex = 0
                else:faceindex += 1
            # command 为 -2，逆时针转向，超限重新从index -1 开始
            elif i == -2:
                if faceindex - 1 == -5:
                    faceindex = -1
                else:faceindex -= 1
            # command 大于0，一步一步走，判断每一步是否走到障碍点，如果走到则break，停在前一步
            else:
                for step in range(i):
                    if faceto[faceindex] == 'N' and (x,y + 1) not in obstacles:
                        y += 1
                    elif faceto[faceindex] == 'S' and (x,y - 1) not in obstacles:
                        y -= 1
                    elif faceto[faceindex] == 'E' and (x + 1,y) not in obstacles:
                        x += 1
                    elif faceto[faceindex] == 'W' and (x - 1,y) not in obstacles:
                        x -= 1
                    else:break
            # 要求返回最大距离
            res = max(res, x*x + y*y)
        return res








        
# leetcode submit region end(Prohibit modification and deletion)
