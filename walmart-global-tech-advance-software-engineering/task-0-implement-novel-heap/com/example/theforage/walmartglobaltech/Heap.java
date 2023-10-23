
import java.util.List;

public final class Heap {
    final int powerOf2MaxHeap;

    Heap() {
        this.powerOf2MaxHeap = 1;
    }

    Heap(final int powerOf2MaxHeap) {
        this.powerOf2MaxHeap = powerOf2MaxHeap;
    }

    // https://en.wikipedia.org/wiki/Heapsort
    // std impl
    public void heapify(final List<Integer> list) {
        int endIdx = list.size();
        int startIdx = Math.floorDiv(endIdx, (int) Math.pow(2, this.powerOf2MaxHeap));

        while (endIdx > 1) {
            if (startIdx > 0) {
                startIdx -= 1;
            } else {
                endIdx -= 1;
                this.swap(list, endIdx, startIdx);
            }

            this.siftDown(list, startIdx, endIdx);
        }
    }

    int parentIdx(final int idx) {
        return Math.floorDiv(idx - 1, (int) Math.pow(2, this.powerOf2MaxHeap));
    }

    int leftChildIdx(final int idx) {
        return idx * (int) Math.pow(2, this.powerOf2MaxHeap) + 1;
    }

    int rightChildIdx(final int idx) {
        return idx * (int) Math.pow(2, this.powerOf2MaxHeap) + 2;
    }

    void swap(final List<Integer> list, final int fromIdx, final int toIdx) {
        final int from = list.get(fromIdx);
        final int to = list.get(toIdx);

        list.set(fromIdx, to);
        list.set(toIdx, from);
    }

    void siftDown(final List<Integer> list, int startIdx, int endIdx) {
        int rootIdx = startIdx;

        while (this.leftChildIdx(rootIdx) < endIdx) {
            int childIdx = this.leftChildIdx(rootIdx);

            if (childIdx + 1 < endIdx && list.get(childIdx) < list.get(childIdx + 1)) {
                childIdx += 1;
            }

            if (list.get(rootIdx) < list.get(childIdx)) {
                this.swap(list, rootIdx, childIdx);
                rootIdx = childIdx;
                continue;
            }

            break;
        }
    }

    void siftUp(final List<Integer> list, int endIdx) {
        while (endIdx > 0) {
            final int parentIdx = this.parentIdx(endIdx);

            if (list.get(parentIdx) < list.get(endIdx)) {
                this.swap(list, parentIdx, endIdx);
                endIdx = parentIdx;
                continue;
            }

            break;
        }
    }

    public void insert(final List<Integer> list, final int elem) {
        list.add(elem);

        // below are
        // heapify from williams
        int endIdx = 1;

        final int totalSize = list.size();

        while (endIdx < totalSize) {
            this.siftUp(list, endIdx);
            endIdx += 1;
        }
    }

    public void pop(final List<Integer> list) {
        final int lastElem = list.get(list.size() - 1);

        list.set(0, lastElem);

        list.remove(list.size() - 1);

        this.heapify(list);
    }
}
