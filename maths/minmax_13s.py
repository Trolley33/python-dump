from sys import maxsize


# TREE BUILDER
class Node(object):
    def __init__(self, i_depth, i_playerNum, i_sticksRemaining, i_value=0):
        self.i_depth = i_depth
        self.i_playerNum = i_playerNum
        self.i_sticksRemaining = i_sticksRemaining
        self.i_value = i_value
        self.children = []
        self.create_children()

    def create_children(self):
        if self.i_depth >= 0:
            for i in range(1, 4):
                v = self.i_sticksRemaining - i
                self.children.append(
                    Node(
                        self.i_depth - 1,
                        -self.i_playerNum,
                        v,
                        self.real_val(v))
                )

    def real_val(self, value):
        if value == 0:
            return maxsize * self.i_playerNum
        elif value > 0:
            return maxsize * -self.i_playerNum
        return 0

    def print_tree(self):
        print("Branch: " + str(self.i_depth), str(self.i_value), str(13-self.i_sticksRemaining))
        for t in self.children:
            t.print_tree()



# ALGORITHM
def min_max(node, i_depth, i_playerNum):
    if (i_depth == 0) or (abs(node.i_value) == maxsize):
        return node.i_value

    i_bestValue = maxsize * -i_playerNum

    for i in range(len(node.children)):
        child = node.children[i]
        i_val = min_max(child, i_depth - 1, -i_playerNum)
        if abs(maxsize * i_playerNum - i_val) < abs(maxsize * i_playerNum - i_bestValue):
            i_bestValue = i_val

    return i_bestValue


def win_check(i_sticks, i_playerNum):
    if i_sticks <= 0:
        print("*"*30)
        if i_playerNum > 0:
            if i_sticks == 0:
                print("No sticks on user turn.")
            else:
                print("Less than 0 sticks on user turn.")
        else:
            if i_sticks == 0:
                print("No sticks on comp turn.")
            else:
                print("Less than 0 sticks on comp turn.")
        print("*"*30)
        return 0
    return 1

if __name__ == '__main__':
    i_stickTotal = 12
    i_depth = 4
    i_curPlayer = 1
    print("Instructions: It's just 13s pal.")
    while i_stickTotal > 0:
        print("Current number is {}, how many steps would you like to advance?".format(13-i_stickTotal))
        i_choice = input("\n1-3: ")
        i_stickTotal -= int(float(i_choice))
        if win_check(i_stickTotal, i_curPlayer):
            i_curPlayer *= -1
            node = Node(i_depth, i_curPlayer, i_stickTotal)
            node.print_tree()
            bestChoice = -100
            i_bestValue = -i_curPlayer * maxsize
            for i in range(len(node.children)):
                n_child = node.children[i]
                i_val = min_max(n_child, i_depth, -i_curPlayer)
                if abs(i_curPlayer * maxsize - i_val) <= abs(i_curPlayer * maxsize - i_bestValue):
                    i_bestValue = i_val
                    bestChoice = i

            bestChoice += 1
            print(i_stickTotal)
            print("Computer chooses: {} Based on value: {}".format(bestChoice, i_bestValue))
            i_stickTotal -= bestChoice
            win_check(i_stickTotal, i_curPlayer)
            i_curPlayer *= -1

input()