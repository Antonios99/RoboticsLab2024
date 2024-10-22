// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from naoqi_bridge_msgs:msg/MemoryPairInt.idl
// generated code does not contain a copyright notice

#ifndef NAOQI_BRIDGE_MSGS__MSG__DETAIL__MEMORY_PAIR_INT__STRUCT_HPP_
#define NAOQI_BRIDGE_MSGS__MSG__DETAIL__MEMORY_PAIR_INT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__naoqi_bridge_msgs__msg__MemoryPairInt __attribute__((deprecated))
#else
# define DEPRECATED__naoqi_bridge_msgs__msg__MemoryPairInt __declspec(deprecated)
#endif

namespace naoqi_bridge_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MemoryPairInt_
{
  using Type = MemoryPairInt_<ContainerAllocator>;

  explicit MemoryPairInt_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->memory_key = "";
      this->data = 0l;
    }
  }

  explicit MemoryPairInt_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : memory_key(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->memory_key = "";
      this->data = 0l;
    }
  }

  // field types and members
  using _memory_key_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _memory_key_type memory_key;
  using _data_type =
    int32_t;
  _data_type data;

  // setters for named parameter idiom
  Type & set__memory_key(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->memory_key = _arg;
    return *this;
  }
  Type & set__data(
    const int32_t & _arg)
  {
    this->data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    naoqi_bridge_msgs::msg::MemoryPairInt_<ContainerAllocator> *;
  using ConstRawPtr =
    const naoqi_bridge_msgs::msg::MemoryPairInt_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<naoqi_bridge_msgs::msg::MemoryPairInt_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<naoqi_bridge_msgs::msg::MemoryPairInt_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      naoqi_bridge_msgs::msg::MemoryPairInt_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<naoqi_bridge_msgs::msg::MemoryPairInt_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      naoqi_bridge_msgs::msg::MemoryPairInt_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<naoqi_bridge_msgs::msg::MemoryPairInt_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<naoqi_bridge_msgs::msg::MemoryPairInt_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<naoqi_bridge_msgs::msg::MemoryPairInt_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__naoqi_bridge_msgs__msg__MemoryPairInt
    std::shared_ptr<naoqi_bridge_msgs::msg::MemoryPairInt_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__naoqi_bridge_msgs__msg__MemoryPairInt
    std::shared_ptr<naoqi_bridge_msgs::msg::MemoryPairInt_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MemoryPairInt_ & other) const
  {
    if (this->memory_key != other.memory_key) {
      return false;
    }
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const MemoryPairInt_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MemoryPairInt_

// alias to use template instance with default allocator
using MemoryPairInt =
  naoqi_bridge_msgs::msg::MemoryPairInt_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace naoqi_bridge_msgs

#endif  // NAOQI_BRIDGE_MSGS__MSG__DETAIL__MEMORY_PAIR_INT__STRUCT_HPP_
