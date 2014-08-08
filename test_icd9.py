from icd9 import is_valid, short_description, canonical_form
from nose.tools import assert_equal, assert_raises

def test_is_valid():
    assert is_valid('0029')
    assert is_valid('00322')
    assert not is_valid('00029')
    assert not is_valid(29)
    assert not is_valid('hello')
    assert is_valid('V909')
    assert is_valid('V9100')
    
def test_short_description():
    assert_equal(short_description('0029'), 'Paratyphoid fever NOS')
    assert_equal(short_description('V909'), 'Retain FB, mat NOS')
    assert_raises(lambda: short_description('not a code'), KeyError)
    
def test_canonical_form():
    assert_equal(canonical_form('0029'), '0029')
    assert_equal(canonical_form('029'), '029')
    assert_equal(canonical_form('29'), '029')
    assert_equal(canonical_form('029.'), '029')
    assert_equal(canonical_form('29.'), '029')
    assert_equal(canonical_form('002.9'), '0029')
    assert_equal(canonical_form('02.9'), '0029')
    assert_equal(canonical_form('2.9'), '0029')
    assert_equal(canonical_form('52342'), '52342')
    assert_equal(canonical_form('523.42'), '52342')
    assert_equal(canonical_form('733.7'), '7337')
    assert_equal(canonical_form('73340'), '73340')
    assert_equal(canonical_form('733.40'), '73340')
    assert_equal(canonical_form('733.7 '), '7337')
    assert_equal(canonical_form('  73340'), '73340')
    assert_equal(canonical_form(' 733.40  '), '73340')
    assert_equal(canonical_form('E984'), 'E984')
    assert_equal(canonical_form('E984.'), 'E984')
    assert_equal(canonical_form('E9872'), 'E9872')
    assert_equal(canonical_form('E987.2'), 'E9872')
    assert_equal(canonical_form(' E984'), 'E984')
    assert_equal(canonical_form('E984. '), 'E984')
    assert_equal(canonical_form('  E9872\t'), 'E9872')
    assert_equal(canonical_form('\tE987.2 \n'), 'E9872')
    assert_equal(canonical_form('V131'), 'V131')
    assert_equal(canonical_form('V13.1'), 'V131')
    assert_equal(canonical_form('V13'), 'V13')
    assert_equal(canonical_form('V1367'), 'V1367')
    assert_equal(canonical_form('V13.67'), 'V1367')
    assert_equal(canonical_form('V1367 '), 'V1367')
    assert_equal(canonical_form('  V13.67\t'), 'V1367')
    assert_equal(canonical_form('V140'), 'V140')
    assert_equal(canonical_form('V14.0'), 'V140')
    assert_raises(canonical_form('V120.0'), ValueError) # Too many digits before decimal
    assert_raises(canonical_form('V1.200'), ValueError) # Too few digits before decimal
    assert_raises(canonical_form('V1'), ValueError) # Too few digits
    assert_raises(canonical_form('E9873.2'), ValueError) # Too many digits before decimal
    assert_raises(canonical_form('E0873.2'), ValueError) # Too many digits before decimal
    assert_raises(canonical_form('E93.2'), ValueError) # Too few digits before decimal
    assert_raises(canonical_form('E93'), ValueError) # Too few digits
    assert_raises(canonical_form('9873.2'), ValueError) # Too many digits before decimal
    assert_raises(canonical_form('0873.2'), ValueError) # Too many digits before decimal
    
    
    