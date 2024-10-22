// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from naoqi_bridge_msgs:msg/WordRecognized.idl
// generated code does not contain a copyright notice
#include "naoqi_bridge_msgs/msg/detail/word_recognized__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `words`
#include "rosidl_runtime_c/string_functions.h"
// Member `confidence_values`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
naoqi_bridge_msgs__msg__WordRecognized__init(naoqi_bridge_msgs__msg__WordRecognized * msg)
{
  if (!msg) {
    return false;
  }
  // words
  if (!rosidl_runtime_c__String__Sequence__init(&msg->words, 0)) {
    naoqi_bridge_msgs__msg__WordRecognized__fini(msg);
    return false;
  }
  // confidence_values
  if (!rosidl_runtime_c__float__Sequence__init(&msg->confidence_values, 0)) {
    naoqi_bridge_msgs__msg__WordRecognized__fini(msg);
    return false;
  }
  return true;
}

void
naoqi_bridge_msgs__msg__WordRecognized__fini(naoqi_bridge_msgs__msg__WordRecognized * msg)
{
  if (!msg) {
    return;
  }
  // words
  rosidl_runtime_c__String__Sequence__fini(&msg->words);
  // confidence_values
  rosidl_runtime_c__float__Sequence__fini(&msg->confidence_values);
}

bool
naoqi_bridge_msgs__msg__WordRecognized__are_equal(const naoqi_bridge_msgs__msg__WordRecognized * lhs, const naoqi_bridge_msgs__msg__WordRecognized * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // words
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->words), &(rhs->words)))
  {
    return false;
  }
  // confidence_values
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->confidence_values), &(rhs->confidence_values)))
  {
    return false;
  }
  return true;
}

bool
naoqi_bridge_msgs__msg__WordRecognized__copy(
  const naoqi_bridge_msgs__msg__WordRecognized * input,
  naoqi_bridge_msgs__msg__WordRecognized * output)
{
  if (!input || !output) {
    return false;
  }
  // words
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->words), &(output->words)))
  {
    return false;
  }
  // confidence_values
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->confidence_values), &(output->confidence_values)))
  {
    return false;
  }
  return true;
}

naoqi_bridge_msgs__msg__WordRecognized *
naoqi_bridge_msgs__msg__WordRecognized__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  naoqi_bridge_msgs__msg__WordRecognized * msg = (naoqi_bridge_msgs__msg__WordRecognized *)allocator.allocate(sizeof(naoqi_bridge_msgs__msg__WordRecognized), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(naoqi_bridge_msgs__msg__WordRecognized));
  bool success = naoqi_bridge_msgs__msg__WordRecognized__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
naoqi_bridge_msgs__msg__WordRecognized__destroy(naoqi_bridge_msgs__msg__WordRecognized * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    naoqi_bridge_msgs__msg__WordRecognized__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
naoqi_bridge_msgs__msg__WordRecognized__Sequence__init(naoqi_bridge_msgs__msg__WordRecognized__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  naoqi_bridge_msgs__msg__WordRecognized * data = NULL;

  if (size) {
    data = (naoqi_bridge_msgs__msg__WordRecognized *)allocator.zero_allocate(size, sizeof(naoqi_bridge_msgs__msg__WordRecognized), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = naoqi_bridge_msgs__msg__WordRecognized__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        naoqi_bridge_msgs__msg__WordRecognized__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
naoqi_bridge_msgs__msg__WordRecognized__Sequence__fini(naoqi_bridge_msgs__msg__WordRecognized__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      naoqi_bridge_msgs__msg__WordRecognized__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

naoqi_bridge_msgs__msg__WordRecognized__Sequence *
naoqi_bridge_msgs__msg__WordRecognized__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  naoqi_bridge_msgs__msg__WordRecognized__Sequence * array = (naoqi_bridge_msgs__msg__WordRecognized__Sequence *)allocator.allocate(sizeof(naoqi_bridge_msgs__msg__WordRecognized__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = naoqi_bridge_msgs__msg__WordRecognized__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
naoqi_bridge_msgs__msg__WordRecognized__Sequence__destroy(naoqi_bridge_msgs__msg__WordRecognized__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    naoqi_bridge_msgs__msg__WordRecognized__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
naoqi_bridge_msgs__msg__WordRecognized__Sequence__are_equal(const naoqi_bridge_msgs__msg__WordRecognized__Sequence * lhs, const naoqi_bridge_msgs__msg__WordRecognized__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!naoqi_bridge_msgs__msg__WordRecognized__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
naoqi_bridge_msgs__msg__WordRecognized__Sequence__copy(
  const naoqi_bridge_msgs__msg__WordRecognized__Sequence * input,
  naoqi_bridge_msgs__msg__WordRecognized__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(naoqi_bridge_msgs__msg__WordRecognized);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    naoqi_bridge_msgs__msg__WordRecognized * data =
      (naoqi_bridge_msgs__msg__WordRecognized *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!naoqi_bridge_msgs__msg__WordRecognized__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          naoqi_bridge_msgs__msg__WordRecognized__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!naoqi_bridge_msgs__msg__WordRecognized__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
