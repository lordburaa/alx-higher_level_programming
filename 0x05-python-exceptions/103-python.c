#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - gives data of the PyFloatObject
 *
 * @p: the Pyobject
 */
void print_python_float(PyObject *p)
{
	double value = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PYFloatObject *)p)->ob_fval;
		
