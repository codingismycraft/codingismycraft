import java.io.*;


class Node {
    public int _value;
    public Node _next;

    public Node(int value){
        this._value = value;
        this._next = null;
    }

    public int getValue() {
        return this._value;
    }

    public Node getNext() {
        return this._next;
    }

    public void setNext(Node node) {
        this._next = node;
    }
}

class LinkedList {
    Node _head;
    Node _tail;

    public LinkedList(){
        this._head = null;
        this._tail = null;
    }

    public void add_to_end(int value) {
        Node new_node = new Node(value);

        if (this._head == null)
        {
            this._head = new_node;
            this._tail = new_node;
        }
        else
        {
            this._tail.setNext(new_node);
            this._tail = new_node;
        }
    }

    public void print_to_console(){
        System.out.println("LinkedList");
        Node node = this._head;
        while (node != null)
        {
            System.out.println(node.getValue());
            node = node.getNext();
        }
    }

    public void reverse(){
        Node previous = null;
        Node n1 = this._head;
        while (n1 != null){
            Node n2 = n1.getNext();
            n1.setNext(previous);
            previous = n1;
            n1 = n2;
        }
        Node old_head = this._head;
        this._head = this._tail;
        this._tail = old_head;
    }
}

class Reverse{
    public static void main(String args[]) throws FileNotFoundException, IOException {
        LinkedList ll = new LinkedList();

        long start1 = System.currentTimeMillis();
        File file = new File("data.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        String str;
        while ((str = br.readLine()) != null){
            ll.add_to_end(Integer.parseInt(str));
        }
        long end1 = System.currentTimeMillis();
        float sec1 = (end1 - start1) / 1000F;
        System.out.println("Reading took : " + sec1 + " seconds");
        long start = System.currentTimeMillis();
        ll.reverse();
        long end = System.currentTimeMillis();
        float sec = (end - start) / 1000F;
        //float sec = end - start;
        System.out.println("Reversing took: " + sec + " seconds");
    }
}
