#! /usr/bin/env python

"""This is the nosetest module for coordinates2region.py"""
from coordinates2region import coordinates2region

def test_coordinates2region():
	"""This function tests the functionality for the coordinates2region 
	function"""
	#Check all the single region results first, starting with 1
	#Region 1 only
	assert coordinates2region({'x':0,'y':0})== [1], 'something failed'
	assert coordinates2region({'x':149,'y':0})== [1], 'something failed'
	assert coordinates2region({'x':0,'y':149})== [1], 'something failed'
	assert coordinates2region({'x':149,'y':149})== [1], 'something failed'
	#Region 2 only
	assert coordinates2region({'x':201,'y':0})== [2], 'something failed'
	assert coordinates2region({'x':350,'y':0})== [2], 'something failed'
	assert coordinates2region({'x':201,'y':149})== [2], 'something failed'
	assert coordinates2region({'x':350,'y':149})== [2], 'something failed'
	#Region 3 only
	assert coordinates2region({'x':201,'y':201})== [3], 'something failed'
	assert coordinates2region({'x':350,'y':201})== [3], 'something failed'
	assert coordinates2region({'x':201,'y':250})== [3], 'something failed'
	assert coordinates2region({'x':350,'y':350})== [3], 'something failed'
	#Region 4 only
	assert coordinates2region({'x':0,'y':201})== [4], 'something failed'
	assert coordinates2region({'x':149,'y':201})== [4], 'something failed'
	assert coordinates2region({'x':0,'y':350})== [4], 'something failed'
	assert coordinates2region({'x':149,'y':350})== [4], 'something failed'

	#Check two-way overlaps, starting with 1 and 2
	#Regions 1 and 2
	assert coordinates2region({'x':151,'y':0})== [1,2], 'something failed'
	assert coordinates2region({'x':199,'y':0})== [1,2], 'something failed'
	assert coordinates2region({'x':151,'y':151})== [1,2], 'something failed'
	assert coordinates2region({'x':199,'y':151})== [1.2], 'something failed'
	#Region 1 and 4
	assert coordinates2region({'x':0,'y':201})== [4], 'something failed'
	assert coordinates2region({'x':149,'y':201})== [4], 'something failed'
	assert coordinates2region({'x':0,'y':350})== [4], 'something failed'
	assert coordinates2region({'x':149,'y':350})== [4], 'something failed'
	#Region 3 only
	assert coordinates2region({'x':201,'y':201})== [3], 'something failed'
	assert coordinates2region({'x':350,'y':201})== [3], 'something failed'
	assert coordinates2region({'x':201,'y':250})== [3], 'something failed'
	assert coordinates2region({'x':350,'y':350})== [3], 'something failed'
	#Region 4 only
	
	#Should test points outside the box too
	#Define testing behavior for when input is not valid (not two numbers/integers)

def test_coordinates2region_badinput():
	"""This function will test if the inputs are in the correct format"""
	pass

	#assert condition, err message