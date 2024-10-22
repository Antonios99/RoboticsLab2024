// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from naoqi_bridge_msgs:msg/RobotInfo.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "naoqi_bridge_msgs/msg/detail/robot_info__struct.h"
#include "naoqi_bridge_msgs/msg/detail/robot_info__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool naoqi_bridge_msgs__msg__robot_info__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[44];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("naoqi_bridge_msgs.msg._robot_info.RobotInfo", full_classname_dest, 43) == 0);
  }
  naoqi_bridge_msgs__msg__RobotInfo * ros_message = _ros_message;
  {  // type
    PyObject * field = PyObject_GetAttrString(_pymsg, "type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->type = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // model
    PyObject * field = PyObject_GetAttrString(_pymsg, "model");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->model, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // head_version
    PyObject * field = PyObject_GetAttrString(_pymsg, "head_version");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->head_version, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // body_version
    PyObject * field = PyObject_GetAttrString(_pymsg, "body_version");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->body_version, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // arm_version
    PyObject * field = PyObject_GetAttrString(_pymsg, "arm_version");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->arm_version, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // has_laser
    PyObject * field = PyObject_GetAttrString(_pymsg, "has_laser");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->has_laser = (Py_True == field);
    Py_DECREF(field);
  }
  {  // has_extended_arms
    PyObject * field = PyObject_GetAttrString(_pymsg, "has_extended_arms");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->has_extended_arms = (Py_True == field);
    Py_DECREF(field);
  }
  {  // number_of_legs
    PyObject * field = PyObject_GetAttrString(_pymsg, "number_of_legs");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->number_of_legs = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // number_of_arms
    PyObject * field = PyObject_GetAttrString(_pymsg, "number_of_arms");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->number_of_arms = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // number_of_hands
    PyObject * field = PyObject_GetAttrString(_pymsg, "number_of_hands");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->number_of_hands = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * naoqi_bridge_msgs__msg__robot_info__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of RobotInfo */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("naoqi_bridge_msgs.msg._robot_info");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "RobotInfo");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  naoqi_bridge_msgs__msg__RobotInfo * ros_message = (naoqi_bridge_msgs__msg__RobotInfo *)raw_ros_message;
  {  // type
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->type);
    {
      int rc = PyObject_SetAttrString(_pymessage, "type", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // model
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->model.data,
      strlen(ros_message->model.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "model", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // head_version
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->head_version.data,
      strlen(ros_message->head_version.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "head_version", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // body_version
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->body_version.data,
      strlen(ros_message->body_version.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "body_version", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // arm_version
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->arm_version.data,
      strlen(ros_message->arm_version.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "arm_version", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // has_laser
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->has_laser ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "has_laser", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // has_extended_arms
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->has_extended_arms ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "has_extended_arms", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // number_of_legs
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->number_of_legs);
    {
      int rc = PyObject_SetAttrString(_pymessage, "number_of_legs", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // number_of_arms
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->number_of_arms);
    {
      int rc = PyObject_SetAttrString(_pymessage, "number_of_arms", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // number_of_hands
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->number_of_hands);
    {
      int rc = PyObject_SetAttrString(_pymessage, "number_of_hands", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
