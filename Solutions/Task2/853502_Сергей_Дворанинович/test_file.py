import unittest
import sys

import vector as v
import my_from_json as f
import my_to_json as t
import my_decorator as dec
import extern_merge as sort
import singleton as s

sort_nums = "23 34 12 11 32 12 56 90 74 65 23 34 12 11 32 12 56 90 74 65 23 34 12 11 32 12 56 90 74 65"
sample_sotred_nums = "11 11 11 12 12 12 12 12 12 23 23 23 32 32 32 34 34 34 56 56 56 65 65 65 74 74 74 90 90 90"


class TestLab(unittest.TestCase):

  def test_external_sort(self):
      with open('temp1.txt', 'w') as file:
          file.write(sort_nums)
      sort.ExternSort()
      with open('temp1.txt', 'r') as file:
          sorted_nums = file.read()
      self.assertEqual(sorted_nums, sample_sotred_nums)

  def test_to_json(self):
      with open('my_cash_2.txt', 'w') as file:
          file.write(t.to_json_test())
      with open('my_cash_2.txt', 'r') as file:
          processed_string = file.read()
      with open('2_module_right.txt', 'r') as file:
          sample_string = file.read()
      self.assertEqual(processed_string, sample_string)

  def test_from_json_1(self):
      dict_info = f.from_json(' "abc" : { "d" : null, "ans" : [ "s1" : 1, "s2" : 2] }, "b" : true ')
      a = f.make_class('MyClass', dict_info)
      self.assertTrue(a.b)

  def test_from_json_2(self):
      dict_info = f.from_json(' "abc" : { "d" : null, "ans" : [ "s1" : 1, "ss2" : 2] }, "b" : true, , "v" : false ')
      a = f.make_class('MyClass', dict_info)
      self.assertIsNone(a.abc.d)

  def test_from_json_3(self):
      dict_info = f.from_json(' "abc" : 12.1 ')
      a = f.make_class('MyClass', dict_info)
      self.assertEqual(a.abc, 12.1)

  def test_from_json_4(self):
      dict_info = f.from_json(' "abc" : "aaa" ')
      a = f.make_class('MyClass', dict_info)
      self.assertEqual(a.abc, "aaa")

  def test_from_json_5(self):
      dict_info = f.from_json(' "abc" : [ "a" : 12, "list" : ["b" : 4], "c" : { "num" : 12}] ')
      a = f.make_class('MyClass', dict_info)
      d = a.abc[1]
      d = d["list"]
      d = d[0]
      d = d["b"]
      self.assertEqual(d, 4.0)

  def test_vector_1(self):
      with open('my_cash_3.txt', 'w') as file:
          file.write(v.ShowWork(v.TestVector(3, [5, 6, 7]), v.TestVector(3, [12, 0, 4]), v.TestVector(2, [4, 5])))
      with open('my_cash_3.txt', 'r') as file:
          processed_string = file.read()
      with open('3_module_right.txt', 'r') as file:
          sample_string = file.read()
      self.assertEqual(processed_string, sample_string)

  def test_vector_2(self):
      processed_string = str(v.TestVector("s", []))
      self.assertEqual(processed_string, "[  0 ]")

  def test_decorator(self):
      with open('my_cash_4.txt', 'w') as file:
          file.write(dec.ShowWork())
      with open('my_cash_4.txt', 'r') as file:
          processed_string = file.read()
      with open('4_module_right.txt', 'r') as file:
          sample_string = file.read()
      self.assertEqual(processed_string, sample_string)

  def test_singleton(self):
      a = s.TestClass('second', 24)
      b = s.TestClass()
      self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()