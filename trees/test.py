import part1
import part2 as p2
import part3 as p3

################################# Part 1 Test Cases ###############################

def test_part1():
    score = 0
    #insert test
    print("-------------------------------- PART 1 TESTING -----------------------")
    
    test_BST = part1.Tree()
    test_BST.root = part1.Node(6)
    test_BST.root.left = part1.Node(5)
    test_BST.root.right = part1.Node(7)
    test_BST.root.left.left = part1.Node(4)
    test_BST.root.left.right = part1.Node(5.5)
    test_BST.root.right.left = part1.Node(6.5)
    test_BST.root.right.right = part1.Node(8)

    ######## TESTING INSERT ########
    insert_flag_one = False
    insert_flag_two = False

    try:
        test_tree = part1.Tree()        
        test_tree.insert(16)
        insert_flag_one = True
    except:
        insert_flag_one = False

    try:
        test_BST_copy = test_BST
        test_BST_copy.insert(5.7)
        test_BST_copy.insert(6.6)
        test_BST_copy.insert(7.9)
        test_BST_copy.insert(10)

        insert_flag_two = True
    except:
        insert_flag_two = False

    flag_one = False
    flag_two = False

    try:
        if test_tree.in_order() == [16]:
            flag_one = True
    except:
        pass

    try:
        if test_BST_copy.in_order() == [4, 5, 5.5, 5.7, 6, 6.5, 6.6, 7, 7.9, 8, 10]:
            flag_two = True
    except:
        pass

    if (flag_one == True) and (flag_two == True) and (insert_flag_one == True) and (insert_flag_two == True) :
        print("Insert Test Passed")
        score += 2
        print("Score {} / 30".format(score))
        print("")

    else:
        print("Insert Test Failed")
        print("Score {} / 30".format(score) )
        print("")



    ######## TESTING GET NODE ########

    test_BST = part1.Tree()
    test_BST.root = part1.Node(6)
    test_BST.root.left = part1.Node(5)
    test_BST.root.right = part1.Node(7)
    test_BST.root.left.left = part1.Node(4)
    test_BST.root.left.right = part1.Node(5.5)
    test_BST.root.right.left = part1.Node(6.5)
    test_BST.root.right.right = part1.Node(8)

    flag_one = False
    flag_two = False
    flag_three = False

    test_node = test_BST.get_node(50)
    try:
        if test_node == False:
            flag_one = True
        else:
            flag_one = False
    except:
        pass

    test_node = test_BST.get_node(6)
    try:
        if (test_node.value == 6) and (test_node.left.value == 5) and (test_node.right.value == 7):
            flag_two = True
        else:
            flag_two = False
    except:
        pass

    test_node = test_BST.get_node(5)
    try:
        if (test_node.value == 5) and (test_node.left.value == 4) and (test_node.right.value == 5.5):
            flag_three = True

        else:
            flag_three = False
    except:
        pass


    if (flag_one == True) and (flag_two == True) and (flag_three == True):
        print("Get Node Test Passed")
        score += 1
        print("Score {} / 30".format(score))
        print("")

    else:
        print("Get Node Test Failed", flag_one, flag_two, flag_three)
        print(test_tree.get_node(5))
        print("Score {} / 30".format(score))
        print("")



    ######## TESTING FIND NODE ########
    test_BST = part1.Tree()
    test_BST.root = part1.Node(6)
    test_BST.root.left = part1.Node(5)
    test_BST.root.right = part1.Node(7)
    test_BST.root.left.left = part1.Node(4)
    test_BST.root.left.right = part1.Node(5.5)
    test_BST.root.right.left = part1.Node(6.5)
    test_BST.root.right.right = part1.Node(8)

    try:
        if (test_BST.find_node(72) == False) and (test_BST.find_node(-1) == False) and (test_BST.find_node(6.5) == True) and (test_BST.find_node(1.5) == False):
            print("Find Node Test Passed")
            score += 1.5
            print("Score {} / 30".format(score))
        else:
            print("Find Node Test Failed")
            print("Score {} / 30".format(score))
            print("")

    except:
        print("Find Node Test Failed")
        print("Score {} / 30".format(score))
        print("")



    ######## TESTING GET CHILDREN ########
    test_BST = part1.Tree()
    test_BST.root = part1.Node(6)
    test_BST.root.left = part1.Node(5)
    test_BST.root.right = part1.Node(7)
    test_BST.root.left.left = part1.Node(4)
    test_BST.root.left.right = part1.Node(5.5)
    test_BST.root.right.left = part1.Node(6.5)
    test_BST.root.right.right = part1.Node(8)

    try:
        if (test_BST.get_children(6)[0].value == 5 and test_BST.get_children(6)[1].value == 7):
            print("Get Children Test Passed")
            score += 2
            print("Score {} / 30".format(score))
            print("")


        else:
            print("Get Children Test Failed")
            print("Score {} / 30".format(score))
            print("")

    except:
        print("Get Children Test Failed")
        print("Score {} / 30".format(score))
        print("")


    ######## TESTING UPDATE NODE ########
    test_BST = part1.Tree()
    test_BST.root = part1.Node(6)
    test_BST.root.left = part1.Node(5)
    test_BST.root.right = part1.Node(7)
    test_BST.root.left.left = part1.Node(4)
    test_BST.root.left.right = part1.Node(5.5)
    test_BST.root.right.left = part1.Node(6.5)
    test_BST.root.right.right = part1.Node(8)

    flag_one = False
    flag_two = False


    try:

        test_tree_copy = test_BST
        test_tree_copy.update_node(6, 6.1)

        if (test_tree_copy.in_order()== [4, 5, 5.5, 6.1, 6.5, 7, 8]):
            print("Update Node Test Passed")
            score += 3
            print("Score {} / 30".format(score))
            print("")

        else:
            print("Update Node Test Failed", )
            print("Score {} / 30".format(score))
            print("")

    except:
        print("Update Node Test Failed")
        print("Score {} / 30".format(score))
        print("")




    ######## TESTING GET HEIGHT ########

    test_BST = part1.Tree()
    test_BST.root = part1.Node(6)
    test_BST.root.left = part1.Node(5)
    test_BST.root.right = part1.Node(7)
    test_BST.root.left.left = part1.Node(4)
    test_BST.root.left.right = part1.Node(5.5)
    test_BST.root.right.left = part1.Node(6.5)
    test_BST.root.right.right = part1.Node(8)

    flag_one = False
    flag_two = False
    flag_three = False
    flag_four = False
    flag_five = False

    try:

        if (test_BST.get_height() == 3):
            flag_one = True
            print("Get Height Test Passed")
            score += 3
            print("Score {} / 30".format(score))  

        else:
            print("Get Height Test Failed")
            print("Score {} / 30".format(score))
            print("")

    except:
        print("Get Height Test Failed")
        print("Score {} / 30".format(score))
        print("")




    ######## TESTING GET PATH ########
    test_BST = part1.Tree()
    test_BST.root = part1.Node(6)
    test_BST.root.left = part1.Node(5)
    test_BST.root.right = part1.Node(7)
    test_BST.root.left.left = part1.Node(4)
    test_BST.root.left.right = part1.Node(5.5)
    test_BST.root.right.left = part1.Node(6.5)
    test_BST.root.right.right = part1.Node(8)
    flag_one = False
    flag_two = False
    flag_three = False
    flag_four = False
    flag_five = False
    flag_six = False

    try:

        if (test_BST.get_path(7) == [6,7]):
            flag_one = True
        if (test_BST.get_path(6) == [6]):
            flag_two = True
        if (test_BST.get_path(8) == [6,7,8]):
            flag_three = True
        if (test_BST.get_path(6.5) == [6,7,6.5]):
            flag_four = True
        if (test_BST.get_path(4) == [6,5,4]):
            flag_five = True
  

        if (flag_one == True) and (flag_two == True) and (flag_three == True) and (flag_four == True) and (flag_five == True):
            print("Get Path Test Passed" )
            score += 4
            print("Score {} / 30".format(score)) 
            print("")


        else:
            print("Get Path Test Failed")
            print("Score {} / 30".format(score))
            print("")


    except:
        print("Get Path Test Failed")
        print("Score {} / 30".format(score))
        print("")

    ######## TESTING AVG DIFF ########
    test_BST = part1.Tree()
    test_BST.root = part1.Node(6)
    test_BST.root.left = part1.Node(5)
    test_BST.root.right = part1.Node(7)
    test_BST.root.left.left = part1.Node(4)
    test_BST.root.left.right = part1.Node(5.5)
    test_BST.root.right.left = part1.Node(6.5)
    test_BST.root.right.right = part1.Node(8)

    flag_one = False
    flag_two = False
    flag_three = False
    flag_four = False
    flag_five = False

    try:

        if (test_BST.avg_diff() > 2.3) and (test_BST.avg_diff() <2.4):
            print("Avg Diff Test Passed")
            score += 4
            print("Score {} / 30".format(score))  
            print("")


        else:
            print("Avg Diff Test Failed")
            print("Score {} / 30".format(score))   
            print("")


    except:
        print("Avg Diff Test Failed")
        print("Score {} / 30".format(score))
        print("")


    ######## TESTING DELETE ########

    test_BST = part1.Tree()
    test_BST.root = part1.Node(6)
    test_BST.root.left = part1.Node(5)
    test_BST.root.right = part1.Node(7)
    test_BST.root.left.left = part1.Node(4)
    test_BST.root.left.right = part1.Node(5.5)
    test_BST.root.right.left = part1.Node(6.5)
    test_BST.root.right.right = part1.Node(8)

    flag_one = False
    test_tree_copy = test_BST

    try:

        test_tree_copy.delete(4)
        test_tree_copy.delete(5)
        test_tree_copy.delete(5.5)
        test_tree_copy.delete(8)
        test_tree_copy.delete(6.5)

        if (test_tree_copy.in_order() == [6, 7]):
            print("Delete Test Passed")
            score += 3
            print("Score {} / 30".format(score))  
            print("")

        else:
            print("Delete Test Failed")
            print("Score {} / 30".format(score))
            print("")

    except:
        print("Delete Test Failed")
        print("Score {} / 30".format(score))
        print("")

    ######## TESTING DELETE LEAF ########
    test_BST = part1.Tree()
    test_BST.root = part1.Node(6)
    test_BST.root.left = part1.Node(5)
    test_BST.root.right = part1.Node(7)
    test_BST.root.left.left = part1.Node(4)
    test_BST.root.left.right = part1.Node(5.5)
    test_BST.root.right.left = part1.Node(6.5)
    test_BST.root.right.right = part1.Node(8)

    test_tree_copy = test_BST
    flag_one = False
    flag_two = False
    flag_three = False
    flag_four = False
    flag_five = False

    try:
        test_tree_copy.delete_leaf(4)
        test_tree_copy.delete_leaf(6.5)
        test_tree_copy.delete_leaf(5.5)
        test_tree_copy.delete_leaf(8)


        if (test_tree_copy.in_order() == [5, 6, 7]):
            print("Delete Leaf Test Passed")
            score += 2
            print("Score {} / 30".format(score))  
            print("")

        else:
            print("Delete Leaf Test Failed")
            print("Score {} / 30".format(score))
            print("")

    except:
        print("Delete Leaf Test Failed")
        print("Score {} / 30".format(score))
        print("")



    ######## TESTING DELETE LEAVES ########
    test_BST = part1.Tree()
    test_BST.root = part1.Node(6)
    test_BST.root.left = part1.Node(5)
    test_BST.root.right = part1.Node(7)
    test_BST.root.left.left = part1.Node(4)
    test_BST.root.left.right = part1.Node(5.5)
    test_BST.root.right.left = part1.Node(6.5)
    test_BST.root.right.right = part1.Node(8)

    test_tree_copy = test_BST

    try:
        test_tree_copy.delete_leaves()

        if (test_tree_copy.in_order() == [5, 6, 7]):
            flag_one = True
        
            print("Delete Leaves Test Passed")
            score += 3
            print("Score {} / 30".format(score))  
            print("")

        else:
            print("Delete Leaves Test Failed")
            print("Score {} / 30".format(score))
            print("")

    except:
        print("Delete Leaves Test Failed")
        print("Score {} / 30".format(score))
        print("")


    ######## TESTING IN-ORDER ########
    test_BST = part1.Tree()
    test_BST.root = part1.Node(6)
    test_BST.root.left = part1.Node(5)
    test_BST.root.right = part1.Node(7)
    test_BST.root.left.left = part1.Node(4)
    test_BST.root.left.right = part1.Node(5.5)
    test_BST.root.right.left = part1.Node(6.5)
    test_BST.root.right.right = part1.Node(8)

    try:

        if (test_BST.in_order() == [4, 5, 5.5, 6, 6.5, 7, 8]):
            print("In-Order Test Passed")
            score += 0.5
            print("Score {} / 30".format(score))  
            print("")

        else:
            print("In-Order Test Failed")
            print("Score {} / 30".format(score))
            print("")

    except:
        print("In-Order Test Failed")
        print("Score {} / 30".format(score))
        print("")



    ######## TESTING PRE-ORDER ########
    test_BST = part1.Tree()
    test_BST.root = part1.Node(6)
    test_BST.root.left = part1.Node(5)
    test_BST.root.right = part1.Node(7)
    test_BST.root.left.left = part1.Node(4)
    test_BST.root.left.right = part1.Node(5.5)
    test_BST.root.right.left = part1.Node(6.5)
    test_BST.root.right.right = part1.Node(8)

    try:

        if (test_BST.pre_order() == [6, 5, 4, 5.5, 7, 6.5, 8]):
            print("Pre-Order Test Passed")
            score += 0.5
            print("Score {} / 30".format(score))  
            print("")

        else:
            print("Pre-Order Test Failed")
            print("Score {} / 30".format(score))
            print("")

    except:
        print("Pre-Order Test Failed")
        print("Score {} / 30".format(score))
        print("")



    
    ######## TESTING POST-ORDER ########

    try:

        if (test_BST.post_order() == [4, 5.5, 5, 6.5, 8, 7, 6]):
            print("Post-Order Test Passed")
            score += 0.5
            print("Score {} / 30".format(score))  
            print("")

        else:
            print("Post-Order Test Failed")
            print("Score {} / 30".format(score))
            print("")

    except:
        print("Post-Order Test Failed")
        print("Score {} / 30".format(score))
        print("")
    return score

#Making the hard coded tree for the test case with level 4

def preOrder(root,ans):
	if not root:
		return

	ans.append(str(root.value))
	preOrder(root.l,ans)
	preOrder(root.r,ans)
	return ans


def part2():
    ################### TREE 1 ##############################
    # Level 0
    TestTree = p2.AVLTree()
    root = p2.TreeNode(16)
    root.h = 5
    # level 1
    root.l = p2.TreeNode(8)
    root.r = p2.TreeNode(24)
    root.l.h = 4
    root.r.h = 4
    #The left child of the root
    root.l.l = p2.TreeNode(4) # <- level 2
    root.l.r = p2.TreeNode(12) # <- Level 2
    root.l.l.h = 3
    root.l.r.h = 3
    #the right child of the root
    root.r.l = p2.TreeNode(20) # <- level 2
    root.r.r = p2.TreeNode(28) # <- level 2
    root.r.l.h = 3
    root.r.r.h = 3
    #level 3
    root.l.l.l = p2.TreeNode(2) # <- Level 3 child 1
    root.l.l.l.h = 2
    root.l.l.r = p2.TreeNode(6) # <- Level 3 child 2
    root.l.l.r.h = 2
    root.l.r.l = p2.TreeNode(10) # <- Level 3 child 3
    root.l.r.l.h = 2
    root.l.r.r = p2.TreeNode(14)  # <- Level 3 child 4
    root.l.r.r.h = 2
    root.r.l.l = p2.TreeNode(18)  # <- Level 3 child 5
    root.r.l.l.h = 2
    root.r.l.r = p2.TreeNode(22)  # <- Level 3 child 6
    root.r.l.r.h = 2
    root.r.r.l = p2.TreeNode(26)  # <- Level 3 child 7
    root.r.l.r.h = 2
    root.r.r.r = p2.TreeNode(30)  # <- Level 3 child 8
    root.r.r.r.h = 2
    # Level 4 :-
    # Child 1
    root.l.l.l.l = p2.TreeNode(1)
    root.l.l.l.r = p2.TreeNode(3)
    # Child 2
    root.l.l.r.l = p2.TreeNode(5)
    root.l.l.r.r = p2.TreeNode(7)
    # Child 3
    root.l.r.l.l = p2.TreeNode(9)
    root.l.r.l.r = p2.TreeNode(11)
    # Child 4
    root.l.r.r.l = p2.TreeNode(13)
    root.l.r.r.r = p2.TreeNode(15)
    # Child 5
    root.r.l.l.l = p2.TreeNode(17)
    root.r.l.l.r = p2.TreeNode(19)
    # Child 6
    root.r.l.r.l = p2.TreeNode(21)
    root.r.l.r.r = p2.TreeNode(23)
    # Child 7 
    root.r.r.l.l =  p2.TreeNode(25)
    root.r.r.l.r = p2.TreeNode(27)
    # Child 8
    root.r.r.r.l = p2.TreeNode(29)
    root.r.r.r.r = p2.TreeNode(31)

    #Setting the height of the level 4
    root.l.l.l.l.h = 1 
    root.l.l.l.r.h = 1 
    # Child 2
    root.l.l.r.l.h = 1 
    root.l.l.r.r.h = 1 
    # Child 3
    root.l.r.l.l.h = 1 
    root.l.r.l.r.h = 1 
    # Child 4
    root.l.r.r.l.h = 1 
    root.l.r.r.r.h = 1 
    # Child 5
    root.r.l.l.l.h = 1 
    root.r.l.l.r.h = 1 
    # Child 6
    root.r.l.r.l.h = 1 
    root.r.l.r.r.h = 1 
    # Child 7 
    root.r.r.l.l.h = 1 
    root.r.r.l.r.h = 1 
    # Child 8
    root.r.r.r.l.h = 1 
    root.r.r.r.r.h = 1
    ################### TREE 2 ##############################
    # Level 0
    TestTree = p2.AVLTree()
    delete_root = p2.TreeNode(16)
    delete_root.h = 5
    # level 1
    delete_root.l = p2.TreeNode(8)
    delete_root.r = p2.TreeNode(24)
    delete_root.l.h = 4
    delete_root.r.h = 4
    #The left child of the delete_root
    delete_root.l.l = p2.TreeNode(4) # <- level 2
    delete_root.l.r = p2.TreeNode(12) # <- Level 2
    delete_root.l.l.h = 3
    delete_root.l.r.h = 3
    #the right child of the delete_root
    delete_root.r.l = p2.TreeNode(20) # <- level 2
    delete_root.r.r = p2.TreeNode(28) # <- level 2
    delete_root.r.l.h = 3
    delete_root.r.r.h = 3
    #level 3
    delete_root.l.l.l = p2.TreeNode(2) # <- Level 3 child 1
    delete_root.l.l.l.h = 2
    delete_root.l.l.r = p2.TreeNode(6) # <- Level 3 child 2
    delete_root.l.l.r.h = 2
    delete_root.l.r.l = p2.TreeNode(10) # <- Level 3 child 3
    delete_root.l.r.l.h = 2
    delete_root.l.r.r = p2.TreeNode(14)  # <- Level 3 child 4
    delete_root.l.r.r.h = 2
    delete_root.r.l.l = p2.TreeNode(18)  # <- Level 3 child 5
    delete_root.r.l.l.h = 2
    delete_root.r.l.r = p2.TreeNode(22)  # <- Level 3 child 6
    delete_root.r.l.r.h = 2
    delete_root.r.r.l = p2.TreeNode(26)  # <- Level 3 child 7
    delete_root.r.l.r.h = 2
    delete_root.r.r.r = p2.TreeNode(30)  # <- Level 3 child 8
    delete_root.r.r.r.h = 2
    # Level 4 :-
    # Child 1
    delete_root.l.l.l.l = p2.TreeNode(1)
    delete_root.l.l.l.r = p2.TreeNode(3)
    # Child 2
    delete_root.l.l.r.l = p2.TreeNode(5)
    delete_root.l.l.r.r = p2.TreeNode(7)
    # Child 3
    delete_root.l.r.l.l = p2.TreeNode(9)
    delete_root.l.r.l.r = p2.TreeNode(11)
    # Child 4
    delete_root.l.r.r.l = p2.TreeNode(13)
    delete_root.l.r.r.r = p2.TreeNode(15)
    # Child 5
    delete_root.r.l.l.l = p2.TreeNode(17)
    delete_root.r.l.l.r = p2.TreeNode(19)
    # Child 6
    delete_root.r.l.r.l = p2.TreeNode(21)
    delete_root.r.l.r.r = p2.TreeNode(23)
    # Child 7 
    delete_root.r.r.l.l =  p2.TreeNode(25)
    delete_root.r.r.l.r = p2.TreeNode(27)
    # Child 8
    delete_root.r.r.r.l = p2.TreeNode(29)
    delete_root.r.r.r.r = p2.TreeNode(31)

    #Setting the height of the level 4
    delete_root.l.l.l.l.h = 1 
    delete_root.l.l.l.r.h = 1 
    # Child 2
    delete_root.l.l.r.l.h = 1 
    delete_root.l.l.r.r.h = 1 
    # Child 3
    delete_root.l.r.l.l.h = 1 
    delete_root.l.r.l.r.h = 1 
    # Child 4
    delete_root.l.r.r.l.h = 1 
    delete_root.l.r.r.r.h = 1 
    # Child 5
    delete_root.r.l.l.l.h = 1 
    delete_root.r.l.l.r.h = 1 
    # Child 6
    delete_root.r.l.r.l.h = 1 
    delete_root.r.l.r.r.h = 1 
    # Child 7 
    delete_root.r.r.l.l.h = 1 
    delete_root.r.r.l.r.h = 1 
    # Child 8
    delete_root.r.r.r.l.h = 1 
    delete_root.r.r.r.r.h = 1 
    ################################## Starting Testing ######################
    score = 0
    # Testing Get Height
    print("Test Get height function : ")
    print("")
    try:

        if TestTree.get_height(None) == 0:
            print("Get Height Test Case 1 Passed!")
            score += 1
            print("Score = {}/30".format(score))
            print("")            
            if TestTree.get_height(root.r.r.r.l) == 1:
                print("Get Height Test Case 2 Passed!")
                score += 1
                print("Score = {}/30".format(score))
                print("")
            else:
                print("Get Height Test Case 2 Failed :(")
                print("Score = {}/30".format(score))
                print("")
        else:
            print("Get Height Test Case 1 Failed :(")
            print("Score = {}/30".format(score))
            print("")
    except:
        print("Get Height Test Failed due to some error :(")
        print("")
    
    # Test Get balance
    try:
        if TestTree.get_bal(None) == None:
            print("Get Balance Test Case 1 Passed!")
            score += 1
            print("Score = {}/30".format(score))
            print("")
            try:
                if TestTree.get_bal(root) == 0:
                    print("Get Balance Test Case 2 Passed!")
                    score += 0.5
                    print("Score = {}/30".format(score))
                    print("")
                    #Setting up new tree for the Testing
                    balroot = p2.TreeNode(5)
                    balroot.h = 3
                    balroot.l = p2.TreeNode(4)
                    balroot.l.h = 2
                    balroot.l.l = p2.TreeNode(3)
                    balroot.l.l.h = 1
                    balroot.r = p2.TreeNode(6)
                    try:
                        if TestTree.get_bal(balroot) == 1:
                            print("Get Balance Test Case 3 Passed!")
                            score += 0.5
                            print("Score = {}/30".format(score))
                            print("")
                        else:
                            print("Get Balance Test Case 3 Failed :(")
                            print("")
                    except:
                        print("Get Balance Test Failed due to some error :(")
                        print("")
                else:
                    print("Get Balance Test Case 2 Failed :(!")
                    print("")
            except:
                print("Get Balance Test Failed due to some error :(")
                print("")
        else:
            print("Get Balance Test Case 1 Failed :(")
            print("")
    except:
        print("Get Balance Test Failed due to some error :(")
        print("")

    # Test the Right rotate function
    try:
        r2_root = p2.TreeNode(10)
        r_root = p2.TreeNode(5)
        r_root.h = 3
        r_root.l = p2.TreeNode(4)
        r_root.l.h = 2
        r_root.l.l = p2.TreeNode(3)
        r_root.l.l.h = 1
        r_root.r = p2.TreeNode(6)
        ans = TestTree.r_rotate(r_root)
        ans2 = TestTree.r_rotate(r2_root.l)
        if ans2 == None:
            print("Right Rotate Test 1 Passed!")
            score += 1
            print("Score = {}/30".format(score))
            print("")
            if ans.value == 4 and ans.l.value == 3 and ans.r.value == 5 and ans.r.r.value == 6:
                print("Right Rotate Test 2 Passed!")
                score += 1
                print("Score = {}/30".format(score))
                print("")
            else:
                print("Right Rotate Test 2 Failed")
                print("Score = {}/30".format(score))
                print("")
        else:
            print("Right Rotate Test 1 Failed")
            print("Score = {}/30".format(score))
            print("")

    except:
        print("The right rotate test failed due to some error")
        print("Score = {}/30".format(score))
        print("")
    try:
        # Testing the lest rotate function
        if TestTree.l_rotate(None) == None:
            print("Left rotate test 1 passed!")
            score += 1
            print("Score = {}/30".format(score))
            print("")
            l_root = p2.TreeNode(10)
            l_root.h = 3
            l_root.r = p2.TreeNode(11)
            l_root.r.h =2  
            l_root.r.r = p2.TreeNode(12)
            l_root.r.h =2
            l_ans = TestTree.l_rotate(l_root)
            if l_ans.value == 11 and l_ans.l.value == 10 and l_ans.r.value == 12:
                print("Left rotate test 2 passed!")
                score += 1
                print("Score = {}/30".format(score))
                print("")
            else:
                print("Left rotate test 2 Failed !")
                print("Score = {}/30".format(score))
                print("")
        else:
            print("Left rotate test 1 failed")
            print("Score = {}/30".format(score))
            print("")
    except:
        print("The left rotate test failed due to some error")
        print("Score = {}/30".format(score))
        print("")
    # Testing the insert function

    iRoot= None
    iTree = p2.AVLTree()
    try:
        for i in range(1,32):
            iRoot = iTree.insert(iRoot,i)
        if preOrder(iRoot,[]) == preOrder(root,[]):
            print("Insert Test case 1 passed")
            score += 1.5
            print("Score = {}/30".format(score))
            print("")
            i2Tree = p2.AVLTree()
            i2Root = None
            i2Root = i2Tree.insert(None,10)
            if i2Root.value == 10:
                print("Insert Test case 2 Passed")
                score += 1.5
                print("Score = {}/30".format(score))
                print("")
            else:
                print("Insert Test case 2 Failed :(")
                print("Score = {}/30".format(score))
                print("")

        else:
            print("Insert Test case 1 Failed")
            print("Score = {}/30".format(score))
            print("")
    except:
        print("Get insert Test Failed due to some error :(")
        print("Score = {}/30".format(score))
        print("")

    # Testing the Delete function
    # When their is only one done in the tree
    dRoot = p2.TreeNode(10)
    dRootTree = p2.AVLTree()
    dRoot = dRootTree.delete_node(dRoot,10)
    try:
        if dRoot == None:
            print("Delete test 1 passed!")
            score += 1
            print("Score = {}/30".format(score))
            print("")
            #Deleting the Leaf node
            d2Root = p2.TreeNode(10)
            d2Root.h = 2
            d2Root.l = p2.TreeNode(9)
            d2Root.r = p2.TreeNode(11)
            d2Root.h =1 
            d2ans = dRootTree.delete_node(d2Root,9)
            try:
                if d2Root.l == None and d2Root.r.value == 11 and d2Root.value == 10:
                    print("Delete test 2 passed")
                    score += 1
                    print("Score = {}/30".format(score))
                    print("")
                    try:
                        if preOrder(dRootTree.delete_node(delete_root,16),[]) == ['17', '8', '4', '2', '1', '3', '6', '5', '7', '12', '10', '9', '11', '14', '13', '15', '24', '20', '18', '19', '22', '21', '23', '28', '26', '25', '27', '30', '29', '31']:
                            print("Delete test 3 passed")
                            score += 5
                            print("Score = {}/30".format(score))
                            print("")
                        else:
                            print("Delete test 3 failed :(")
                            print("Score = {}/30".format(score))
                            print("")
                    except:
                        print("Get Delete Test Failed due to some error :(")
                else:
                    print("Delete test 2 failed :(")
                    print("Score = {}/30".format(score))
                    print("")
            except:
                    print("Get Delete Test Failed due to some error :(")
                    print("Score = {}/30".format(score))
                    print("")
        else:
            print("Delete Test 1 Failed")
            print("Score = {}/30".format(score))
            print("")
    except:
        print("Get Delete Test Failed due to some error :(")
        print("Score = {}/30".format(score))
        print("")
    #Testing update node
    try:
        updated = TestTree.update_node(root,310,31)
        if root.r.r.r.r.value == 310:
            print("Update Test Case Passed")
            root.r.r.r.r.value = 31
            score += 2
            print("Score = {}/30".format(score))
            print("")
        else:
            print("Update Test Failed :(")
            print("Score = {}/30".format(score))
            print("")
    except:
        print("Update Test Failed due to some error")
    #Delete all nodes at given height 
    dt = p2.AVLTree()
    dt.delete_all_nodes_at_given_height(root,2)
    try:
        if preOrder(root,[]) == ['16', '8', '5', '2', '1', '3', '6', '7', '13', '10', '9', '11', '14', '15', '24', '21', '18', '17', '19', '22', '23', '29', '26', '25', '27', '30', '31']:
            print("Delete all node test 1 is passed!")
            score += 5
            print("Score = {}/30".format(score))
            print("")
            try:
                if dt.delete_all_nodes_at_given_height(None,5) == None:
                    print("Delete all node test 2 is passed!")
                    score += 5
                    print("Score = {}/30".format(score))
                    print("")
                else:
                    print("Delete all node test 2 Failed!")
                    print("Score = {}/30".format(score))
                    print("")
            except:
                print("Delete all node failed due to some error!")
                print("Score = {}/30".format(score))
        else:
            print("Delete all node test 1 Failed!")
            print("Score = {}/30".format(score))
            print("")
    except:
        print("Delete all node failed due to some error!")
        print("Score = {}/30".format(score))
        print("")

    return score
    
def part3():
    score = 0
    root = p3.Node(1)
    root.l = p3.Node(2)
    root.r = p3.Node(3)
    root.l.l = p3.Node(4)
    root.l.r = p3.Node(5)
    root.r.l = p3.Node(6)
    root.r.r = p3.Node(7)
    root.l.l.l = p3.Node(8)
    root.l.l.r = p3.Node(9)
    root.l.r.l = p3.Node(10)
    root.l.r.r = p3.Node(11)
    root.r.l.l = p3.Node(12)
    root.r.l.r = p3.Node(13)
    root.r.r.l = p3.Node(14)
    root.r.r.r = p3.Node(15)
    
    p3.changing_room_numbers(root)
    if root.l.value == 3 and root.r.value == 2 and root.l.l.l.value == 15 and root.l.l.r.value == 14 and root.l.r.l.value == 13 and root.l.r.r.value == 12 and root.r.l.l.value == 11 and root.r.l.r.value == 10 and root.r.r.l.value == 9 and root.r.r.r.value == 8:
        print("Test 1 passed")
        score += 10
        print("Score = {}/40".format(score))
        print("")
        if p3.changing_room_numbers(None) == None:
            print("Test 2 passed")
            score += 10
            print("Score = {}/40".format(score))
            print("")
        else:
            print("Test 2 failed :(")
            print("Score = {}/40".format(score))
            print("")
    else:
        print("Test 1 failed :(")
        print("Score = {}/40".format(score))
        print("")
    if p3.visiting_floors(root) == ['1', '3', '2', '4', '5', '6', '7', '15', '14', '13', '12', '11', '10', '9', '8']:
        print("Test 1 passed")
        score += 20
        print("Score = {}/40".format(score))
        print("")
    else:
        print("Test Failed")
        print("Score = {}/40".format(score))
        print("")

    return score
        
            






        
        

    
        
        

        





            
        






    



    #test the Get balance


if __name__ == "__main__":
    total_score = 0
    print("--------------------------------------- PART 1 Test --------------------------------------- ")
    total_score += test_part1()
    print("Total Score after the part 1 is {}/100".format(total_score))
    print("--------------------------------------- PART 2 Test --------------------------------------- ")
    total_score += part2()
    print("Total Score after the part 2 is {}/100".format(total_score))
    print("--------------------------------------- PART 3 Test --------------------------------------- ")
    total_score += part3()
    print("Total Score after the part 3 is {}/100".format(total_score))




