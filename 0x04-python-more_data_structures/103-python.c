nclude <Python.h>

/**
 * print_python_list - Prints information about Python lists
 * @p: Pointer to PyObject representing the list
 */
void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = list->allocated;
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);
    for (i = 0; i < size; i++)
    {
        PyObject *element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
    }
}

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: Pointer to PyObject representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size = PyBytes_GET_SIZE(p);
    Py_ssize_t i;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AS_STRING(p));
    printf("  first 10 bytes:");
    for (i = 0; i < size && i < 10; i++)
    {
        printf(" %02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
    }
    printf("\n");
}

