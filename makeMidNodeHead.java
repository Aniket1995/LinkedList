public class Node
{
    int data;
    Node next;
    public Node(int data){
        this.data = data;
        this.next = null;
    }

    static Node head;
    public static void printLL(Node head){
        Node p = head;
        while(p != null){
            System.out.print(p.data + "->");
            p = p.next;
        }

        System.out.print(p);
        System.out.println();
    }

    public static void main (String[] args) {

        //  1 -> 2 -> 3 -> 4 -> 5 -> 6
        //  3 -> 2 -> 4 -> 5 -> 6
        head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next =new Node(4);
        head.next.next.next.next = new Node(5);
        head.next.next.next.next.next = new Node(6);
        printLL(head);
        head = makeMidHead(head);
        printLL(head);
    }

    public static Node makeMidHead(Node head){
        Node p1 = head;
        Node p2 = head;
        Node pre = null;

        while(p2 != null && p2.next != null){
            pre = p1;
            p2 = p2.next.next;
            p1 = p1.next;
        }

        pre.next = pre.next.next;
        p1.next = head;
        head = p1;
        return head;
    }

}