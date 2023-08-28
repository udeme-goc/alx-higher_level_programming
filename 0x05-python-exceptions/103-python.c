#include <Python.h>

/* Function prototypes */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	/* Retrieve list size and allocated memory */
	size = var->ob_size;
	alloc = list->allocated;

	/* Flush stdout buffer */
	fflush(stdout);

	/* Print list info */
	printf("[*] Python list info\n");

	/* Check if the object is a valid list */
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	/* Print size and allocated memory */
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	/* Iterate over list elements */
	for (i = 0; i < size; i++)
	{
		/* Get the type name of the current element */
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);

		/* Print additional information based on the type */
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes = (PyBytesObject *)p;

	/* Flush stdout buffer */
	fflush(stdout);

	/* Print bytes object info */
	printf("[.] bytes object info\n");

	/* Check if the object is a valid bytes object */
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/* Print size and trying string */
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	/* Calculate number of bytes to print */
	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	/* Print first bytes in hexadecimal format */
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	/* Cast PyObject to PyFloatObject */
	PyFloatObject *float_obj = (PyFloatObject *)p;

	/* Flush stdout buffer */
	fflush(stdout);

	/* Print float object info */
	printf("[.] float object info\n");

	/* Check if the object is a valid float object */
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	/* Convert float value to string */
	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
				    Py_DTSF_ADD_DOT_0, NULL);

	/* Print float value */
	printf("  value: %s\n", buffer);

	/* Free allocated memory */
	PyMem_Free(buffer);
}

