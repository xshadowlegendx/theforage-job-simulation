
import java.util.List;
import java.util.ArrayList;

final class Main {
    public static void main(final String[] _args) {
        final List<Integer> arr = new ArrayList<Integer>() {{
            // add(1);
            // add(2);
            // add(3);
            // add(4);
            // add(5);
            // add(6);

            add(9);
            add(3);
            add(7);
            add(1);
            add(5);

            // add(12);
            // add(4);
            // add(8);
            // add(2);
            // add(11);
            // add(6);
        }};

        System.out.println("before heapify");

        for (int idx = 0; idx < arr.size(); idx++) {
            System.out.print(arr.get(idx));
            System.out.print(",");
        }

        System.out.println("");

        final Heap heap = new Heap();

        heap.heapify(arr);

        System.out.println("after heapify");

        for (int idx = 0; idx < arr.size(); idx++) {
            System.out.print(arr.get(idx));
            System.out.print(",");
        }

        heap.insert(arr, 25);
        heap.insert(arr, 22);

        heap.pop(arr);

        System.out.println("after insert and pop");

        for (int idx = 0; idx < arr.size(); idx++) {
            System.out.print(arr.get(idx));
            System.out.print(",");
        }
    }
}
