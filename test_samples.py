import re
import pdb

import pytest

class TestClass:

  def test_hello(self):
    fd = open("temp", "a+")
    fd.write("hello function\n")
    fd.close()
  
  def test_world(self):
    fd = open("temp", "a+")
    fd.write("world function\n")
    fd.close()
