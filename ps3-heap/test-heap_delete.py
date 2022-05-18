#!/usr/bin/python
import unittest
import time
import heap_delete

class TestHeap(unittest.TestCase):
    def setUp(self):
        pass

    def test0(self):
        "Test original heap functionality"
        h = heap_delete.heap_delete()
        import random
        for i in range(20):
            h.insert(random.randint(0, 10))
        l = []
        while h.heapsize > 0:
            l.append(h.extract_min())

        self.assertEqual(len(l), 20)
        for i in range(len(l)-1):
            self.assertTrue(l[i]<=l[i+1])
            self.assertEqual(h.heapsize, 0)
            self.assertEqual(h.A, [None])


    def test1(self):
        "Insert one element and then delete it"
        h = heap_delete.heap_delete()
        self.assertEqual(h.A, [None])
        self.assertEqual(h.heapsize, 0)
        h.insert(5)
        h.delete(1)
        self.assertEqual(h.A, [None])
        self.assertEqual(h.heapsize, 0)
            
    def test2(self):
        "Insert many elements and then delete one"
        h = heap_delete.heap_delete()
        h.insert(5)
        h.insert(15)
        h.insert(10)
        h.insert(0)
        h.delete(h.A.index(10))
        self.assertEqual(0, h.extract_min())
        self.assertEqual(5, h.extract_min())
        self.assertEqual(15, h.extract_min())
        self.assertEqual(h.A, [None])
        self.assertEqual(h.heapsize, 0)

    def timed_heapsort_test(self, test_name, array):
        "Verifies that the heap can be used to sort array (timed)"
        start_time = time.time()
        self.heapsort_test(array)
        end_time = time.time()
        print ('Time for test', test_name + ':', end_time - start_time, 'seconds')
        
    def heapsort_test(self, array):
        "Verifies that the heap can be used to sort array"
        h = heap_delete.heap_delete()
        for elem in array:
            h.insert(elem)
        sorted_array = sorted(array)
        for elem in sorted_array:
            self.assertEqual(h.extract_min(), elem)
            
    def test3(self):
        "Heapsort on 2 permutations of 1...10"
        self.heapsort_test([9, 1, 6, 3, 7, 8, 2, 5, 4, 10])
        self.heapsort_test([2, 4, 7, 3, 5, 8, 6, 10, 1, 9])
 
    def test4(self):
        "Heapsort on 1k elements"
        self.timed_heapsort_test('1k', [(219 * (i ** 2) + 53 * i + 15) % 10000 for i in range(1000)])

    def test5(self):
        "Heapsort on 10k elements"
        self.timed_heapsort_test('10k', [(257 * (i ** 2) + 19 * i + 66) % 100000 for i in range(10000)])

    def test6(self):
        "Heapsort on 100k elements"
        self.timed_heapsort_test('100k', [(92 * (i ** 3) + 165 * (i ** 2) + 29 * i + 83) % 1000000 for i in range(100000)])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHeap)
    unittest.TextTestRunner(verbosity=2).run(suite)

