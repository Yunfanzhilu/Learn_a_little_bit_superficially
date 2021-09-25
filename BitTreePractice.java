import java.sql.SQLOutput;
import java.util.*;

import static java.lang.System.out;
//二叉树节点定义
public class BitTreePractice {
    public static class BitTreeNode {
        public int value;
        public BitTreeNode left;
        public BitTreeNode right;

        public BitTreeNode(int v) {
            value = v;
        }

    }


    //二叉树前序遍历
    public static void pre1(BitTreeNode head) {
        if (head == null) {
            return;
        }
        System.out.print(head.value + " ");
        pre1(head.left);
        pre1(head.right);

    }

    //二叉树前序遍历（非递归）
//    public static void pre_NonRecursive(BitTreeNode head)
//    {
//         if(head==null)
//         {
//             return;
//         }
//         Stack<BitTreeNode>stack=new Stack<BitTreeNode>();
//         stack.push(head);
//         while(!stack.isEmpty())
//         {
//             BitTreeNode cur=stack.pop();
//             System.out.print(cur.value);
//             if(cur.right!=null)
//             {
//                 stack.push(cur.right);
//             }
//             if(cur.left!=null)
//             {
//                 stack.push(cur.left);
//             }
//         }
//         return ;
//    }
    public static void pre_NonRecursive(BitTreeNode head) {
        if (head == null) {
            return;
        }
        Stack<BitTreeNode> s1 = new Stack<>();
        s1.push(head);
        while (!s1.isEmpty()) {
            BitTreeNode cur = s1.pop();
            System.out.print(cur.value + " ");
            if (cur.right != null) {
                s1.push(cur.right);
            }
            if (cur.left != null) {
                s1.push(cur.left);
            }


        }
        return;
    }


    //二叉树中序遍历
    public static void mid1(BitTreeNode head) {
        if (head == null) {
            return;
        }

        mid1(head.left);
        System.out.print(head.value + " ");
        mid1(head.right);

    }

    //二叉树中序遍历（非递归）
    public static void mid_NonRecursive(BitTreeNode head) {
        int a;
        Stack<BitTreeNode> stack = new Stack<BitTreeNode>();
        BitTreeNode cur;
        while (!stack.isEmpty() || head != null) {
            if (head != null) {
                stack.push(head);
                head = head.left;

            } else {
                head = stack.pop();
                System.out.print(head.value + " ");
                head = head.right;
            }
        }


    }

    //二叉树后序遍历
    public static void pos1(BitTreeNode head) {
        if (head == null) {
            return;
        }

        pos1(head.left);
        pos1(head.right);
        System.out.print(head.value + " ");

    }

    //二叉树后序遍历（非递归）
    public static void pos_NonRecursive(BitTreeNode head) {
        if (head == null) {
            return;
        }
        Stack<BitTreeNode> stack = new Stack<BitTreeNode>();
        Stack<BitTreeNode> stack1 = new Stack<BitTreeNode>();
        stack.push(head);
        while (!stack.isEmpty()) {
            BitTreeNode cur = stack.pop();

            //System.out.print(cur.value);
            stack1.push(cur);
            if (cur.left != null) {
                stack.push(cur.left);

            }
            if (cur.right != null) {
                stack.push(cur.right);

            }
        }
        while (!stack1.isEmpty()) {
            BitTreeNode cur1;
            cur1 = stack1.pop();
            System.out.print(cur1.value + " ");
        }
        return;
    }


    //二叉树的序列化
//    public static Queue<String>preSerial(BitTreeNode head)
//    {
//        Queue<String>ans=new LinkedList<>() ;
//        pres(head,ans);
//   System.out.print(ans);
//        return ans;
//
//    }
//    public static void pres(BitTreeNode head,Queue<String>ans)
//    {
//        if(head==null)
//        {
//            ans.add(null);
//        }
//        else {
//            ans.add(String.valueOf(head.value));
//            pres(head.left, ans);
//            pres(head.right, ans);
//        }
//    }
    public static Queue<String> preSerial(BitTreeNode head) {
        Queue<String> res = new LinkedList<>();
        pres(head, res);
        System.out.print(res);
        return res;


    }

    public static void pres(BitTreeNode head, Queue<String> res) {


        BitTreeNode tmp;
        if (head == null) {
            res.add(null);
        } else {
            res.add(String.valueOf(head.value));
            pres(head.left, res);
            pres(head.right, res);
        }


    }
//二叉树的反序列化
//    public  static BitTreeNode bulidByPreQueue(Queue<String>prelist){
//        if(prelist==null||prelist.size()==0)
//        {
//            return null;
//        }
//        return preb(prelist);
//    }
//    public static BitTreeNode preb(Queue<String>prelist)
//    {
//        String value=prelist.poll();
//        if(value==null)
//        {
//            return null;
//        }
//        BitTreeNode head =new BitTreeNode(Integer.valueOf(value));
//        head.left=preb(prelist);
//        head.right=preb(prelist);
//        return head;
//    }


    public static BitTreeNode bulidByPreQueue(Queue<String> prelist) {
        if (prelist == null || prelist.size() == 0) {
            return null;
        }
        return preb(prelist);
    }

    public static BitTreeNode preb(Queue<String> prelist) {
        String value = prelist.poll();
        if (value == null) {
            return null;
        }
        BitTreeNode head = new BitTreeNode(Integer.valueOf(value));
        head.left = preb(prelist);
        head.right = preb(prelist);
        return head;
    }
    //Morris遍历（线索二叉树）：一种遍历二叉树的方式，并且时间复杂度O(N),额外空间复杂度O(1)
    //通过利用原树叶节点中大量空闲指针的方式，达到节省空间的目的
    // 叶节点访问一次，其余访问2次

    //    Morris遍历细节
//    假如来到当前节点cur，开始时cur来到头节点位置
//    1）如果cur没有左子树，cur向右移动(cur=cur.right)
//    2）如果cur有左子树，找到左子树上最右的节点mostRight:
//    a.如果MostRight的右指针指向空，让其指向cur，然后cur向左移动(cur=cur.left)
//    b.如果mostRight的右指针指向cur，让其指向null,然后cur向右移动(cur=cur.right)
//    3)cur为空时遍历停止
//    前序中序后序遍历在此基础上更改
    public static void morris(BitTreeNode head) {
        if (head == null) {
            return;
        }
        BitTreeNode cur = head;
        BitTreeNode mostRight = null;
        while (cur != null) {
            mostRight = cur.left;
            if (mostRight != null)//有左子树
            {
                while (mostRight.right != null && mostRight.right != cur) {
                    mostRight = mostRight.right;
                }
                //此时mostRight变成了cur左子树上，最右的节点
                if (mostRight.right == null)//这是第一次来到cur
                {
                    mostRight.right = cur;
                    cur = cur.left;
                    continue;
                } else//mostRight.right==cur
                {
                    mostRight.right = null;
                }
            }
            cur = cur.right;
        }
    }

    //基于Morris的先序遍历：
    //先序遍历：只访问1次的节点，直接打印，访问2次的节点，第一次访问打印
    public static void MorrisPre(BitTreeNode head) {
        if (head == null) {
            return;
        }
        BitTreeNode cur = head;
        BitTreeNode mostRight = null;
        while (cur != null) {
            mostRight = cur.left;
            if (mostRight != null)//有左子树
            {
                while (mostRight.right != null && mostRight.right != cur) {
                    mostRight = mostRight.right;
                }
                //此时mostRight变成了cur左子树上，最右的节点
                if (mostRight.right == null)//这是第一次来到cur
                {
                    System.out.print(cur.value + " ");
                    mostRight.right = cur;
                    cur = cur.left;
                    continue;
                } else//mostRight.right==cur
                {
                    mostRight.right = null;
                }
            } else//没有左子树的情况
            {
                System.out.print(cur.value + " ");
            }
            cur = cur.right;
        }
    }

    //基于Morris的中序遍历：
    //先序遍历：只访问1次的节点，直接打印，访问2次的节点，第二次访问打印
    public static void MorrisMid(BitTreeNode head) {
        if (head == null) {
            return;
        }
        BitTreeNode cur = head;
        BitTreeNode mostRight = null;
        while (cur != null) {
            mostRight = cur.left;
            if (mostRight != null)//有左子树
            {
                while (mostRight.right != null && mostRight.right != cur) {
                    mostRight = mostRight.right;
                }
                //此时mostRight变成了cur左子树上，最右的节点
                if (mostRight.right == null)//这是第一次来到cur
                {

                    mostRight.right = cur;
                    cur = cur.left;
                    continue;
                } else//mostRight.right==cur
                {
                    System.out.print(cur.value + " ");
                    mostRight.right = null;
                }
            } else//没有左子树的情况
            {
                System.out.print(cur.value + " ");
            }
            cur = cur.right;
        }
    }

    //如何判断一颗树是搜索二叉树（中序遍历，是否一直升序）
    public static class ReturnData {
        public boolean isBST;
        public int min;
        public int max;

        public ReturnData(boolean is, int mi, int ma) {
            isBST = is;
            min = mi;
            max = ma;
        }
    }

    public static ReturnData process2(BitTreeNode x)
    {
        if(x==null)
        {
            return null;
        }
        ReturnData leftData=process2(x.left);
        ReturnData rightData=process2(x.right);

        int min=x.value;
        int max=x.value;
        if(leftData!=null)
    {
        min=Math.min(min,leftData.min);
        max=Math.max(min,rightData.max);
    }
        if(rightData!=null)
        {
            min=Math.min(min,rightData.min);
            max=Math.max(max,rightData.max);
        }

        boolean leftIsBST=false;
        boolean rightIsBST=false;
        boolean isBST=false;
        if(leftData!=null) {
            if (leftData.isBST = true && leftData.max < x.value)
            {
                leftIsBST=true;
            }

        }
        if(rightData!=null)
        {
            if (rightData.isBST = true && rightData.min>x.value)
            {
                rightIsBST=true;
            }
        }
        if(leftIsBST&&rightIsBST)
        {
            isBST=true;
        }
        return new ReturnData(isBST,min,max);
    }









    //如何判断一颗树是平衡二叉树(左子树是平衡二叉树，右子树是平衡二叉树，左右子树高度差小于等于1)
    public static boolean isBalanced(BitTreeNode head)
    {
        return process(head).isBalanced;
    }
    public static class ReturnType
    {
        public boolean isBalanced;
        public int height;
        public ReturnType(boolean isB,int hei)
        {
            isBalanced=isB;
            height=hei;
        }

    }
    public static ReturnType process(BitTreeNode x)
    {
        if(x==null)
        {
            return new ReturnType(true,0);

        }
        ReturnType DataLeft=process(x.left);
        ReturnType DataRight=process(x.right);
        ReturnType selftNode=new ReturnType(false,-2);
        selftNode.height=Math.max(DataLeft.height,DataRight.height)+1;

        if(DataLeft.isBalanced&&DataRight.isBalanced&&Math.abs((DataLeft.height)-(DataRight.height))<=1)
        {
            selftNode.isBalanced=true;
        }
     return selftNode;

    }



public static BitTreeNode lca(BitTreeNode head,BitTreeNode o1,BitTreeNode o2)
{
    int i,j;
    HashMap<BitTreeNode,BitTreeNode>map=new HashMap<>();
    map.put(head,head);
    processlca(head,o1,o2,map);
    BitTreeNode res=head;
    BitTreeNode cur;
    HashSet<BitTreeNode>set=new HashSet<>();
    set.add(head);
    while(o1!=head)
    {
        set.add(o1);
        o1=map.get(o1);
    }
    while(o2!=head)
    {
        if(set.contains(o2))
        {
            res=o2;
            return o2;
        }
        o2=map.get(o2);
    }
    return res;
}


public static void processlca(BitTreeNode head,BitTreeNode o1tmp,BitTreeNode o2tmp,HashMap<BitTreeNode,BitTreeNode>map)
{
    if(head==null)
    {
        return ;
    }
    map.put(head.left,head);
    map.put(head.right,head);
    processlca(head.left,o1tmp,o2tmp,map);
    processlca(head.right,o1tmp,o2tmp,map);

}

public static void main(String[] args){

        BitTreeNode a=new BitTreeNode(1);
        BitTreeNode b=new BitTreeNode(2);
        BitTreeNode c=new BitTreeNode(18);
        BitTreeNode d=new BitTreeNode(4);
        BitTreeNode e=new BitTreeNode(5);
        BitTreeNode f=new BitTreeNode(7);
        BitTreeNode g=new BitTreeNode(7);
    BitTreeNode h=new BitTreeNode(8);
    BitTreeNode i=new BitTreeNode(9);
    BitTreeNode j=new BitTreeNode(10);
    BitTreeNode k=new BitTreeNode(12);

        a.left=b;
        a.right=c;
        b.left=d;
        b.right=e;
        c.left=f;
        c.right=g;




    System.out.print("二叉树前序遍历：");
    pre1(a);
    System.out.println("");


    System.out.print("二叉树前序遍历（非递归）：");
    pre_NonRecursive(a);
    System.out.println("");

    System.out.print("二叉树前序遍历（Morris）：");
    MorrisPre(a);
    System.out.println("");


    System.out.print("二叉树中序遍历：");
    mid1(a);
    System.out.println("");


    System.out.print("二叉树中序遍历（非递归）：");
    mid_NonRecursive(a);
   System.out.println("");

    System.out.print("二叉树中序遍历（Morris）：");
    MorrisMid(a);
    System.out.println("");


    System.out.print("二叉树后序遍历：");
    pos1(a);
    System.out.println("");


    System.out.print("二叉树后序遍历（非递归）：");
    pos_NonRecursive(a);
    System.out.println("");


    System.out.print("二叉树的序列化：");
    preSerial(a);
    System.out.println("");


    System.out.print("二叉树的反序列化：");
    bulidByPreQueue(preSerial(a));
    System.out.println("");

    System.out.print("判断是否是平衡二叉树：");
    boolean temp=isBalanced(a);
    System.out.println(temp);
    System.out.println("");

}

}


