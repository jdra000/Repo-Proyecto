import random
class Node:
    def __init__(self, data):
        self.data = data 
        # * Directions
        self.next = None 
        self.back = None 
        self.up = None
        self.down = None 
        # * Level in lists. 0 by default
        self.level = 0

class SkipList:
    def __init__(self):
        self.head = Node(float("-inf"))
    
    # * Insert Method
    # * 1. search(x) to find where x fits in the bottom list
    # * 2. Insert x into the bottom list. Invariant: Bottom list contains all the elements
    # * 3. Flip a coin. If heads: promote x to the next level. Flip again.
    def _insert(self, x):
        newNode = Node(x)
        # * 1.
        # * Possible responses: 
        # * (lastStairNode, tempNode) -> insert next to it
        # * (lastStairNode, tempNode, tempNode.next) -> insert in between
        # * node -> node already in list
        searchResponse = self._search(newNode) 
        
        # * 2.
        if isinstance(searchResponse, Node):
            return "Node is already inside the list" # * node already in list
        lastStairNode = searchResponse[0]
        firstNode = searchResponse[1]

        if len(searchResponse) == 2:
            self._linkNodes(firstNode, newNode) # * insert next to it
        else:
            secondNode = searchResponse[2]
            self._linkBetweenNodes(firstNode, newNode, secondNode) # * insert in between

        # * 3.
        randomNum = random.randint(0,1)
        while randomNum == 0:
            self._promoteNode(newNode, lastStairNode)
            # * if it gets promoted again we need to keep track of the last node we used to go down if it exists
            if lastStairNode.up:
                lastStairNode = lastStairNode.up
            #print(f"level up for node{newNode.data}")
            randomNum = random.randint(0,1)

    # * Search method
    # * Looks up for the node inserted. Starting from the level of the head (top left node).
    def _search(self, node: Node):
        tempNode = self.head
        lastNode = self.head
        lastStairNode = self.head
        level = self.head.level
        while True:
            # * Check if we reach the node
            if tempNode.data == node.data:
                return node
            
            if level != 0:
                # * First condition: if the node we are searching has less value than the next one
                # * Second condition: if we reach the end of the level
                # * If any of that happens, go down a level. And keep record of the stair node
                if node.data < tempNode.data or not tempNode.next: 
                    level = lastNode.down.level 
                    tempNode = lastNode.down
                    # * lastStairNode simply keeps track of the last node we used to go down from level 1
                    # * So, we are able to promote the node propertly if it gets promoted
                    lastStairNode = lastNode
            if level == 0:
                # * First condition: if we reach the end of the level -> insert at the end
                # * Second condition: we find the position in between -> insert between
                if not tempNode.next:
                    return (lastStairNode, tempNode) 
                elif node.data > tempNode.data and tempNode.next.data > node.data: 
                    return (lastStairNode, tempNode, tempNode.next) 
                
            # * If none of that happens, keep advancing at the level we are
            lastNode = tempNode
            tempNode = tempNode.next
    
    # * Delete Method
    # * 1. search(x) to find where x is
    # * 2. if x was promoted, delete its nodes all the way up. if not, unlink it from level 0.
    def _delete(self, node: Node):
        searchResponse = self._search(node)
        if isinstance(searchResponse, Node):
            node = searchResponse
            # * Verify if it was promoted 
            if node.level != 0:
                self._unlinkAllTheWay(node)
            else:
                self._unlinkNode(node)
            return "Node removed successfully"
        else:
            return "Node was not found"
        
    def _linkBetweenNodes(self, node1, x, node2):
        node1.next = x
        x.next = node2
        node2.back = x 
        x.back = node1

    def _linkNodes(self, node1, node2):
        node1.next = node2
        node2.back = node1
        #node1.level = node2

    def _unlinkNode(self, node):
        if node.back and node.next:
            leftNode = node.back 
            rightNode = node.next

            node.back = None 
            node.next = None 
            self._linkNodes(leftNode, rightNode)

        elif node.back:
            leftNode = node.back
            node.back = None
            leftNode.next = None

    def _unlinkAllTheWay(self, node):
        while node.level >= 0:
            self._unlinkNode(node)
            node = node.down

    def _promoteNode(self, node, lastStairNode):
        nodePromoted = Node(node.data)
        nodePromoted.level = node.level + 1
        
        node.up = nodePromoted
        nodePromoted.down = node

        # * If it is a new level, head level must be less than the new nodePromoted level.
        if self.head.level < nodePromoted.level: 
            self._createLevel(nodePromoted)
        # * If not, insert at the top level. Between or at the end.
        else:
            if lastStairNode.next:
                self._linkBetweenNodes(lastStairNode, nodePromoted, lastStairNode.next)
            else:
                self._linkNodes(nodePromoted, lastStairNode)
        return
    
    def _createLevel(self, nodePromoted):
        # * Create the new head
        headPromoted = Node(self.head.data)
        headPromoted.level = nodePromoted.level 
        # * Link head and nodePromoted.
        self._linkNodes(headPromoted, nodePromoted)
        # * Link up and down pointers
        headPromoted.down = self.head 
        self.head.up = headPromoted
        # * Update head
        self.head = headPromoted
