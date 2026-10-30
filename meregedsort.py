class TreeNode:
    def __init__(self,val=0, next=0):
        self.val = val
        self.next = next
    def insert_into_bts(root, val):
        if not root :
            return TreeNode(val)
        if val < root.val:
            root.left = insert_into_bts(root.left, val)
        else:
            root.right = insert_into_bts(root.right, val)
        return root
    def inorder(root,result):
        if  root:
            inorder(root.left, result)
            result.append(root.val)
            inorder(root.right, result)
    def merged(list1,list2):
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged.append(list1[i])
            else:
                merged.append(list2[j])

        merged.extend(list1[i:])
        merged.extend(list2[j:])
        return merged
arr1 = list(map(int(input().split(","))))
arr2 = list(map(int(input().split(","))))

root1 = None
root2 = None

for num in arr1 :
    root1 = insert_into_bst(root1, num)
for num in arr2:
    root2 = insert_intobst(root2, num)

list1 = []
list2 = []

inorder(root1, list1)
inorder(root2, list2)

result = merged(list1,list2)
print(result)