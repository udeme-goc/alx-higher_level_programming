#ifndef PYTHON_H
#define PYTHON_H

/* Define PyObject and PyVarObject structures (simplified for illustration) */
typedef struct _object PyObject;
typedef struct {
	PyObject ob_base;
	ssize_t ob_size;
} PyVarObject;

/* Define PyListObject structure (simplified for illustration) */
typedef struct {
	PyVarObject ob_base;
	PyObject *ob_item[];
	ssize_t allocated;
} PyListObject;

/* Define PyBytesObject structure (simplified for illustration) */
typedef struct {
	PyObject ob_base;
	ssize_t ob_size;
	char ob_sval[];
} PyBytesObject;

/* Define PyFloatObject structure (simplified for illustration) */
typedef struct {
	PyObject ob_base;
	double ob_fval;
} PyFloatObject;

/* Define Py_ssize_t type */
typedef ssize_t Py_ssize_t;

/* Define PyOS_double_to_string function */
char *PyOS_double_to_string(double val, char format_code, int precision,
				int flags, int *ptype);

/* Function prototypes for provided functions */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

#endif
