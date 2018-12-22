#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time


class Swipeclass(object):
	def __init__ (self, driver):
		self.driver = driver

	# 向上滑动
	def swipeUp(self,d, t=0.5):

		width = self.driver.info['displayWidth']
		height = self.driver.info['displayHeight']

		x1 = width * 0.5
		y1 = height * 0.85
		y2 = height * 0.25

		d.swipe(x1,y1,x1,y2,t)

	# 从左边向上滑动
	def swipeUp_from_left(self,d, t=0.5):

		width = self.driver.info['displayWidth']
		height = self.driver.info['displayHeight']

		x1 = width * 0.1
		y1 = height * 0.85
		y2 = height * 0.25

		d.swipe(x1,y1,x1,y2,t)

	# 从右边向上滑动
	def swipeUp_from_right(self,d, t=0.5):

		width = self.driver.info['displayWidth']
		height = self.driver.info['displayHeight']

		x1 = width * 0.9
		y1 = height * 0.85
		y2 = height * 0.25

		d.swipe(x1,y1,x1,y2,t)	

	#  '''向下滑动屏幕'''
	def swipeDown(self,d, t=0.5):

		width = self.driver.info['displayWidth']
		height = self.driver.info['displayHeight']

		x1 = width * 0.5
		y1 = height * 0.25
		y2 = height * 0.85

		d.swipe(x1, y1, x1, y2, t)

	# 从左边向下滑动
	def swipeDown_from_left(self,d, t=0.5):

		width = self.driver.info['displayWidth']
		height = self.driver.info['displayHeight']

		x1 = width * 0.1
		y1 = height * 0.25
		y2 = height * 0.85

		d.swipe(x1, y1, x1, y2, t)

	# 从右边向下滑动
	def swipeDown_from_right(self,d, t=0.5):

		width = self.driver.info['displayWidth']
		height = self.driver.info['displayHeight']

		x1 = width * 0.9
		y1 = height * 0.25
		y2 = height * 0.85

		d.swipe(x1, y1, x1, y2, t)

	# 从左往右滑动
	def swipeRight(self,d, t=0.5):
		width = self.driver.info['displayWidth']
		height = self.driver.info['displayHeight']

		y1 = width * 0.5
		x1 = height * 0.25
		x2 = height * 0.85

		d.swipe(x1, y1, x2, y1, t)

	# 从上面左往右滑动
	def swipeRight_from_up(self,d, t=0.5):
		width = self.driver.info['displayWidth']
		height = self.driver.info['displayHeight']

		y1 = width * 0.1
		x1 = height * 0.25
		x2 = height * 0.85

		d.swipe(x1, y1, x2, y1, t)

	# 从下面左往右滑动
	def swipeRight_from_down(self,d, t=0.5):
		width = self.driver.info['displayWidth']
		height = self.driver.info['displayHeight']

		y1 = width * 0.9
		x1 = height * 0.25
		x2 = height * 0.85

		d.swipe(x1, y1, x2, y1, t)

	# 从右往左滑动
	def swipeLeft(self,d, t=0.5):
		width = self.driver.info['displayWidth']
		height = self.driver.info['displayHeight']

		y1 = width * 0.5
		x2 = height * 0.25
		x1 = height * 0.85

		d.swipe(x1, y1, x2, y1, t)

	# 从上面右往左滑动
	def swipeLeft_from_up(self,d, t=0.5):
		width = self.driver.info['displayWidth']
		height = self.driver.info['displayHeight']

		y1 = width * 0.1
		x2 = height * 0.25
		x1 = height * 0.85

		d.swipe(x1, y1, x2, y1, t)

	# 从下面右往左滑动
	def swipeLeft_from_down(self,d, t=0.5):
		width = self.driver.info['displayWidth']
		height = self.driver.info['displayHeight']

		y1 = width * 0.9
		x2 = height * 0.25
		x1 = height * 0.85

		d.swipe(x1, y1, x2, y1, t)









