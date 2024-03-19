#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info -  function print some basic
 *							info about Python lists
 * @p: the python list
 */
void print_python_list_info(PyObject *p)
{
	int rep;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (rep = 0; rep < Py_SIZE(p); rep++)
		printf("Element %d: %s\n", rep, Py_TYPE(PyList_GetItem(p, rep))->tp_name);
}
