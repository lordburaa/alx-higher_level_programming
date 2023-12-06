#include <stdio.h>

struct timespec;

#include <time.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - prit list info abot python
 * @p: py object
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	struct timespec;
	Py_ssize_t i, py_list_size;
	PyObject *item;
	const char *item_t;
	PyListObject *list_object_cast;

	list_object_cast = (PyListObject *)p;
	py_list_size = PyList_Size(p);

	printf("[*] Size of the python List = %d\n", (int) py_list_size);
	printf("[*] Allocated = %d\n", (int)list_object_cast->allocated);
	for (i = 0; i < py_list_size; i++)
	{
		item = PyList_GetItem(p, i);
		item_t = Py_TYPE(item)->tp_name;
		printf("Element %d: %s\n", (int) i, item_t);

	}
}
