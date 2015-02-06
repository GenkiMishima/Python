#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
	for_sample = []
	for_sample.append("python")
	for_sample.append(".")
	for_sample.append("izm")
	for_sample.append(".")
	for_sample.append("com")
	for value in for_sample:
		print value,
	for value in for_sample:
		print value
	counter = 0
	while counter < 10:
		counter += 1
		print counter
	for num in range(-5,50):
		if num % 3:
			continue
		print num
		if num == 30:
			break
