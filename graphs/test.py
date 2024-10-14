import Graph as g

score = 0
score1 = 0
score2 = 0
score3 = 0
score4 = 0

def test_part1():
    global score 
    global score1
    print("----- Test 1 -----")
    g1 = g.Graph("graph1.txt", False)
    g2 = g.Graph("graph2.txt", False)
    g4 = g.Graph("graph4.txt", False)

    display_check1 = "(A,B,6) (A,C,7) (B,A,6) (B,C,3) (C,A,7) (C,B,3) (C,E,8) (D,E,2) (E,C,8) (E,D,2)"
    if g1.display() == display_check1:
        print("Display Test 1 --- Passed :)")
        score1 = score1 + 5
        print("Score:", score1)
    else:
        print("Display Test 1 --- Failed :(")
        print("Score:", score1)
    
    display_check2 = "(A,B,3) (A,C,2) (A,G,6) (B,A,3) (B,C,2) (B,D,1) (B,E,6) (C,A,2) (C,B,2) (C,D,3) (D,B,1) (D,C,3) (D,F,4) (E,B,6) (E,F,1) (F,D,4) (F,E,1) (F,G,2) (G,A,6) (G,F,2)"
    if g2.display() == display_check2:
        print("Display Test 2 --- Passed :)")
        score1 = score1 + 5
        print("Score:", score1)
    else:
        print("Display Test 2 --- Failed :(")
        print("Score:", score1)
    
    display_check4 = "(A,B,2) (A,C,7) (A,E,2) (B,A,2) (B,C,3) (C,A,7) (C,B,3) (C,E,1) (D,F,2) (E,A,2) (E,C,1) (F,D,2)"
    if g4.display() == display_check4:
        print("Display Test 3 --- Passed :)")
        score1 = score1 + 5
        print("Score:", score1)     
    else:
        print("Display Test 3 --- Failed :(")
        print("Score:", score1)
    
    score = score1
    print("Total score of Part 1:", str(score1) + "/15")

    print()

def test_part2():
    global score 
    global score2
    print("----- Test 2 -----")

    g1 = g.Graph("graph1.txt", False)
    g2 = g.Graph("graph2.txt", False)
    g4 = g.Graph("graph4.txt", False)


    if(g1.reachable('A', 'D') == True):
        print("Reachable Test 1 --- Passed :)")
        score2 = score2 + 10
        print("Score:", score2)  
    else:
        print("Reachable Test 1 --- Failed :(")
        print("Score:", score2)
        
    
    if((g2.reachable('A', 'F') == True) and (g2.reachable('D', 'A') == True) and (g2.reachable('E', 'A') == True)):
        print("Reachable Test 2 --- Passed :)")
        score2 = score2 + 10
        print("Score:", score2)   
    else:
        print("Reachable Test 2 --- Failed :(")
        print("Score:", score2)
        

    if((g4.reachable('E', 'B') == True) and (g4.reachable('A', 'F') == False) and (g4.reachable('D', 'F') == True) and (g4.reachable('B', 'D') == False)):
        print("Reachable Test 3 --- Passed :)")
        score2 = score2 + 10
        print("Score:", score2)
    else:
        print("Reachable Test 3 --- Failed :(")
        print("Score:", score2)
        
    
    score = score + score2
    print("Total score of Part 2:", str(score2) + "/30")
    print()

def test_part3():
    global score 
    global score3
    print("----- Test 3 -----")

    g1 = g.Graph("graph1.txt", False)
    g2 = g.Graph("graph2.txt", False)
    g3 = g.Graph("graph3.txt", False)
    g4 = g.Graph("graph4.txt", False)

    if(g2.dijkstra('A' , 'F') != 8):
        print("Dijkstra Test 1 --- Failed :(")
        print("Score:", score3)
    else:
        print("Dijkstra Test 1 --- Passed :)")
        score3 = score3 + 3
        print("Score:", score3)

    if(g2.dijkstra('B', 'G') != 7):
        print("Dijkstra Test 1 --- Failed :(")
        print("Score:", score3)
    else:
        print("Dijkstra Test 2 --- Passed :)")
        score3 = score3 + 3
        print("Score:", score3)
    

    if(g3.dijkstra('A', 'H') != 9):
        print("Dijkstra Test 3 --- Failed :(")
        print("Score:", score3)
    else:
        print("Dijkstra Test 3 --- Passed :)")
        score3 = score3 + 3
        print("Score:", score3)

    if(g3.dijkstra('E', 'B') != 8):
        print("Dijkstra Test 4 --- Failed :(")
        print("Score:", score3)
    else:
        print("Dijkstra Test 4 --- Passed :)")
        score3 = score3 + 3
        print("Score:", score3)

    if(g3.dijkstra('E', 'D') != 7):
        print("Dijkstra Test 5 --- Failed :(")
        print("Score:", score3)
    else:
        print("Dijkstra Test 5 --- Passed :)")
        score3 = score3 + 3
        print("Score:", score3)

    # adjacent but shorter is two step away
    if(g4.dijkstra('A', 'C') != 3):
        print("Dijkstra Test 6 --- Failed :(")
        print("Score:", score3)
    else:
        print("Dijkstra Test 6 --- Passed :)")
        score3 = score3 + 5
        print("Score:", score3)

    # not reachable
    if(g4.dijkstra('E', 'D') != -1):
        print("Dijkstra Test 7 --- Failed :(")
        print("Score:", score3)
    else:
        print("Dijkstra Test 7 --- Passed :)")
        score3 = score3 + 5
        print("Score:", score3)

    if(g4.dijkstra('F', 'D') != 2):
        print("Dijkstra Test 8 --- Failed :(")
        print("Score:", score3)
    else:
        print("Dijkstra Test 8 --- Passed :)")
        score3 = score3 + 5
        print("Score:", score3)

    print("Total score of Part 3:", str(score3) + "/30")
    score = score + score3
    print()

def test_part4():
    global score 
    global score4
    print("----- Test 4 -----")
    g1 = g.Graph("graph1.txt", True)
    g2 = g.Graph("graph2.txt", True)
    g5 = g.Graph("graph5.txt", True)

    if(g1.topo_sort() != "ABDEC" and g1.topo_sort() != "ADBEC" and g1.topo_sort() != "ADEBC" and g1.topo_sort() != "DABEC" and g1.topo_sort() != "DEABC" and g1.topo_sort() != "DAEBC"):
        print("TopoSort Test 1 --- Failed :(")
        print("Score:", score4)
    else:
        print("TopoSort Test 1 --- Passed :)")
        score4 = score4 + 5
        print("Score:", score4)

    if (g2.topo_sort() != "ACBDEGF" and g2.topo_sort() != "ACBDGEF" and g2.topo_sort() != "ACBEDGF" and g2.topo_sort() !="ACBEGDF" and g2.topo_sort() !=  "ACBGDEF" and g2.topo_sort() !=  "ACBGEDF" and g2.topo_sort() !=  "ACGBDEF" and g2.topo_sort() != "ACGBEDF" and g2.topo_sort() !=  "AGCBDEF" and g2.topo_sort() !=  "AGCBEDF"):
        print("TopoSort Test 2 --- Failed :(")
        print("Score:", score4)
    else:
        print("TopoSort Test 2 --- Passed :)")
        score4 = score4 + 5
        print("Score:", score4)

    if (g5.topo_sort() != "ABCDEF" and g5.topo_sort() != "ABCEDF" and g5.topo_sort() != "ABCEFD" and g5.topo_sort() != "ABECDF" and g5.topo_sort() != "ABECFD" and g5.topo_sort() != "ABEFCD"):
        print("TopoSort Test 3 --- Failed :(")
        print("Score:", score4)
    else:
        print("TopoSort Test 3 --- Passed :)")
        score4 = score4 + 5
        print("Score:", score4)
    
    print("Total score of Part 4:", str(score4) + "/15")
    print()
    
    
def main():
    test_part1()
    test_part2()
    test_part3()
    test_part4()
    print("---Total Score", str(score) + "/75---")
    print("---Optional Score", str(score4) + "/15---")


    
main()


