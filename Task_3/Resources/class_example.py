#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Тези две химии горе се пишат за да може скрипта да се изпълнява в конзолата под линукс (първия ред) ... горе долу нещо такова, малко по криво е за обяснение
## втория ред е за да можеш да използваш кирилица общо взето без да ти гърми


class ExampleClass(object):
	'''
	Всичко в основата си започва от object като наследен обект.
	Ще се опитам да ти го обясня максимално човешки с риск да не е съвсем точно, но в последствие ще си го доразбереш сам.
	'''
	variable_for_name = "Pesho Diviq"
	# Това не е глобална променлива, a локална за самия клас и е достъпна само със self.variable_for_name

	def print_name(self):
		# self се използва за да можеш да кажеш, че 
		print (self.variable_for_name)


class extendedClass(ExampleClass):
	'''
	Наследявания на класове ... на кратко
	Всичко, което е в ExampleClass ... в момента като го сложиш в горните скоби вече е достъпно в този клас.

	Това се прави за да имаш модулност и да работиш малко абстрактно, т.е. защо като си разцъкал нещо и то ти работи да рискуваш да го счупиш :) 
	... работиш си в новия клас и само преизползваш компоненти от предния
	'''
	def change_name(self):
		self.variable_for_name = 'Drugiq lud pesho'

if __name__ == "__main__":
	exampleObject = ExampleClass()
	print ('ExampleClass print: '), # тази запетайка накрая е за долепи долния ред до горния
	exampleObject.print_name()

	newExtendedObject = extendedClass()
	print ('extendedClass print: '), # тази запетайка накрая е за долепи долната разпечатка до тази
	newExtendedObject.print_name()
	newExtendedObject.change_name() # сменяме стойността на променливата в този обект
	print ('extendedClass after change print: '), # тази запетайка накрая е за долепи долната разпечатка до тази
	newExtendedObject.print_name()
