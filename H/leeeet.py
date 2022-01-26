class Solution(object):
    def deepestLeavesSum(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """
        frontier      = [root]
        layer_null = False
        steps = 0

        while (not layer_null):
            new_frontier  = []
            layer_null = True
            
            for node in frontier:
                if (node!= None):
                    new_frontier.append(node.left)
                    new_frontier.append(node.right)
                    layer_null = (layer_null and (node.left == None) and (node.right == None))

            if (layer_null):
                output = 0
                for node in frontier:
                    if node!= None:
                        output+=node.val
                return output

            frontier = new_frontier


"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_node(input_list):
    layer_vals = 1
    prev_layer_pos = 0

    while(layer_vals!=0):
        list_end   = prev_layer_pos+layer_vals
        prev_vals = layer_vals
        layer_vals = 0

        for check_pos, val in enumerate(input_list[prev_layer_pos:list_end]):
            if (val != None):
                layer_vals+=1
            
        
        prev_layer_pos += layer_vals
        layer_vals     *= 2
"""