import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

import static java.lang.System.out;




public class LinkListPractice {
    public static class Node{
        public int value;
        public Node next;
        public Node(int v){
            value=v;
        }

    }
    public static Node midOrUpMidNode(Node head)
    {
        if(head==null||head.next==null||head.next.next==null)
        {
            return head;
        }
        Node slow=head.next;
        Node fast=head.next.next;
        while(fast.next!=null&&fast.next.next!=null)
        {
            slow=slow.next;
            fast=fast.next.next;
        }
        return slow;
    }

    public static void main(String[] args)
    {
        Node a=new Node(1);
        Node b=new Node(2);
        Node c=new Node(3);
        Node d=new Node(4);
        Node e=new Node(5);
        a.next=b;
        b.next=c;
        c.next=d;
        d.next=e;
        e.next=null;
        Node res=midOrUpMidNode(a);
        System.out.print(res.value);

    }




}
