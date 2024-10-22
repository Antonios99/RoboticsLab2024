# generated from rosidl_generator_py/resource/_idl.py.em
# with input from naoqi_bridge_msgs:action/JointAnglesWithSpeed.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_JointAnglesWithSpeed_Goal(type):
    """Metaclass of message 'JointAnglesWithSpeed_Goal'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('naoqi_bridge_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'naoqi_bridge_msgs.action.JointAnglesWithSpeed_Goal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__joint_angles_with_speed__goal
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__joint_angles_with_speed__goal
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__joint_angles_with_speed__goal
            cls._TYPE_SUPPORT = module.type_support_msg__action__joint_angles_with_speed__goal
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__joint_angles_with_speed__goal

            from naoqi_bridge_msgs.msg import JointAnglesWithSpeed
            if JointAnglesWithSpeed.__class__._TYPE_SUPPORT is None:
                JointAnglesWithSpeed.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class JointAnglesWithSpeed_Goal(metaclass=Metaclass_JointAnglesWithSpeed_Goal):
    """Message class 'JointAnglesWithSpeed_Goal'."""

    __slots__ = [
        '_joint_angles',
    ]

    _fields_and_field_types = {
        'joint_angles': 'naoqi_bridge_msgs/JointAnglesWithSpeed',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['naoqi_bridge_msgs', 'msg'], 'JointAnglesWithSpeed'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from naoqi_bridge_msgs.msg import JointAnglesWithSpeed
        self.joint_angles = kwargs.get('joint_angles', JointAnglesWithSpeed())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.joint_angles != other.joint_angles:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def joint_angles(self):
        """Message field 'joint_angles'."""
        return self._joint_angles

    @joint_angles.setter
    def joint_angles(self, value):
        if __debug__:
            from naoqi_bridge_msgs.msg import JointAnglesWithSpeed
            assert \
                isinstance(value, JointAnglesWithSpeed), \
                "The 'joint_angles' field must be a sub message of type 'JointAnglesWithSpeed'"
        self._joint_angles = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_JointAnglesWithSpeed_Result(type):
    """Metaclass of message 'JointAnglesWithSpeed_Result'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('naoqi_bridge_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'naoqi_bridge_msgs.action.JointAnglesWithSpeed_Result')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__joint_angles_with_speed__result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__joint_angles_with_speed__result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__joint_angles_with_speed__result
            cls._TYPE_SUPPORT = module.type_support_msg__action__joint_angles_with_speed__result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__joint_angles_with_speed__result

            from sensor_msgs.msg import JointState
            if JointState.__class__._TYPE_SUPPORT is None:
                JointState.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class JointAnglesWithSpeed_Result(metaclass=Metaclass_JointAnglesWithSpeed_Result):
    """Message class 'JointAnglesWithSpeed_Result'."""

    __slots__ = [
        '_goal_position',
    ]

    _fields_and_field_types = {
        'goal_position': 'sensor_msgs/JointState',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['sensor_msgs', 'msg'], 'JointState'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from sensor_msgs.msg import JointState
        self.goal_position = kwargs.get('goal_position', JointState())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.goal_position != other.goal_position:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_position(self):
        """Message field 'goal_position'."""
        return self._goal_position

    @goal_position.setter
    def goal_position(self, value):
        if __debug__:
            from sensor_msgs.msg import JointState
            assert \
                isinstance(value, JointState), \
                "The 'goal_position' field must be a sub message of type 'JointState'"
        self._goal_position = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_JointAnglesWithSpeed_Feedback(type):
    """Metaclass of message 'JointAnglesWithSpeed_Feedback'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('naoqi_bridge_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'naoqi_bridge_msgs.action.JointAnglesWithSpeed_Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__joint_angles_with_speed__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__joint_angles_with_speed__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__joint_angles_with_speed__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__action__joint_angles_with_speed__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__joint_angles_with_speed__feedback

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class JointAnglesWithSpeed_Feedback(metaclass=Metaclass_JointAnglesWithSpeed_Feedback):
    """Message class 'JointAnglesWithSpeed_Feedback'."""

    __slots__ = [
    ]

    _fields_and_field_types = {
    }

    SLOT_TYPES = (
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_JointAnglesWithSpeed_SendGoal_Request(type):
    """Metaclass of message 'JointAnglesWithSpeed_SendGoal_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('naoqi_bridge_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'naoqi_bridge_msgs.action.JointAnglesWithSpeed_SendGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__joint_angles_with_speed__send_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__joint_angles_with_speed__send_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__joint_angles_with_speed__send_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__joint_angles_with_speed__send_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__joint_angles_with_speed__send_goal__request

            from naoqi_bridge_msgs.action import JointAnglesWithSpeed
            if JointAnglesWithSpeed.Goal.__class__._TYPE_SUPPORT is None:
                JointAnglesWithSpeed.Goal.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class JointAnglesWithSpeed_SendGoal_Request(metaclass=Metaclass_JointAnglesWithSpeed_SendGoal_Request):
    """Message class 'JointAnglesWithSpeed_SendGoal_Request'."""

    __slots__ = [
        '_goal_id',
        '_goal',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'goal': 'naoqi_bridge_msgs/JointAnglesWithSpeed_Goal',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['naoqi_bridge_msgs', 'action'], 'JointAnglesWithSpeed_Goal'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_Goal
        self.goal = kwargs.get('goal', JointAnglesWithSpeed_Goal())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.goal != other.goal:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def goal(self):
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value):
        if __debug__:
            from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_Goal
            assert \
                isinstance(value, JointAnglesWithSpeed_Goal), \
                "The 'goal' field must be a sub message of type 'JointAnglesWithSpeed_Goal'"
        self._goal = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_JointAnglesWithSpeed_SendGoal_Response(type):
    """Metaclass of message 'JointAnglesWithSpeed_SendGoal_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('naoqi_bridge_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'naoqi_bridge_msgs.action.JointAnglesWithSpeed_SendGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__joint_angles_with_speed__send_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__joint_angles_with_speed__send_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__joint_angles_with_speed__send_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__joint_angles_with_speed__send_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__joint_angles_with_speed__send_goal__response

            from builtin_interfaces.msg import Time
            if Time.__class__._TYPE_SUPPORT is None:
                Time.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class JointAnglesWithSpeed_SendGoal_Response(metaclass=Metaclass_JointAnglesWithSpeed_SendGoal_Response):
    """Message class 'JointAnglesWithSpeed_SendGoal_Response'."""

    __slots__ = [
        '_accepted',
        '_stamp',
    ]

    _fields_and_field_types = {
        'accepted': 'boolean',
        'stamp': 'builtin_interfaces/Time',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.accepted = kwargs.get('accepted', bool())
        from builtin_interfaces.msg import Time
        self.stamp = kwargs.get('stamp', Time())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.accepted != other.accepted:
            return False
        if self.stamp != other.stamp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def accepted(self):
        """Message field 'accepted'."""
        return self._accepted

    @accepted.setter
    def accepted(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'accepted' field must be of type 'bool'"
        self._accepted = value

    @builtins.property
    def stamp(self):
        """Message field 'stamp'."""
        return self._stamp

    @stamp.setter
    def stamp(self, value):
        if __debug__:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'stamp' field must be a sub message of type 'Time'"
        self._stamp = value


class Metaclass_JointAnglesWithSpeed_SendGoal(type):
    """Metaclass of service 'JointAnglesWithSpeed_SendGoal'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('naoqi_bridge_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'naoqi_bridge_msgs.action.JointAnglesWithSpeed_SendGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__joint_angles_with_speed__send_goal

            from naoqi_bridge_msgs.action import _joint_angles_with_speed
            if _joint_angles_with_speed.Metaclass_JointAnglesWithSpeed_SendGoal_Request._TYPE_SUPPORT is None:
                _joint_angles_with_speed.Metaclass_JointAnglesWithSpeed_SendGoal_Request.__import_type_support__()
            if _joint_angles_with_speed.Metaclass_JointAnglesWithSpeed_SendGoal_Response._TYPE_SUPPORT is None:
                _joint_angles_with_speed.Metaclass_JointAnglesWithSpeed_SendGoal_Response.__import_type_support__()


class JointAnglesWithSpeed_SendGoal(metaclass=Metaclass_JointAnglesWithSpeed_SendGoal):
    from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_SendGoal_Request as Request
    from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_SendGoal_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_JointAnglesWithSpeed_GetResult_Request(type):
    """Metaclass of message 'JointAnglesWithSpeed_GetResult_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('naoqi_bridge_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'naoqi_bridge_msgs.action.JointAnglesWithSpeed_GetResult_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__joint_angles_with_speed__get_result__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__joint_angles_with_speed__get_result__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__joint_angles_with_speed__get_result__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__joint_angles_with_speed__get_result__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__joint_angles_with_speed__get_result__request

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class JointAnglesWithSpeed_GetResult_Request(metaclass=Metaclass_JointAnglesWithSpeed_GetResult_Request):
    """Message class 'JointAnglesWithSpeed_GetResult_Request'."""

    __slots__ = [
        '_goal_id',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.goal_id != other.goal_id:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_JointAnglesWithSpeed_GetResult_Response(type):
    """Metaclass of message 'JointAnglesWithSpeed_GetResult_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('naoqi_bridge_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'naoqi_bridge_msgs.action.JointAnglesWithSpeed_GetResult_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__joint_angles_with_speed__get_result__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__joint_angles_with_speed__get_result__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__joint_angles_with_speed__get_result__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__joint_angles_with_speed__get_result__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__joint_angles_with_speed__get_result__response

            from naoqi_bridge_msgs.action import JointAnglesWithSpeed
            if JointAnglesWithSpeed.Result.__class__._TYPE_SUPPORT is None:
                JointAnglesWithSpeed.Result.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class JointAnglesWithSpeed_GetResult_Response(metaclass=Metaclass_JointAnglesWithSpeed_GetResult_Response):
    """Message class 'JointAnglesWithSpeed_GetResult_Response'."""

    __slots__ = [
        '_status',
        '_result',
    ]

    _fields_and_field_types = {
        'status': 'int8',
        'result': 'naoqi_bridge_msgs/JointAnglesWithSpeed_Result',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['naoqi_bridge_msgs', 'action'], 'JointAnglesWithSpeed_Result'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.status = kwargs.get('status', int())
        from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_Result
        self.result = kwargs.get('result', JointAnglesWithSpeed_Result())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.status != other.status:
            return False
        if self.result != other.result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def status(self):
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'status' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'status' field must be an integer in [-128, 127]"
        self._status = value

    @builtins.property
    def result(self):
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value):
        if __debug__:
            from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_Result
            assert \
                isinstance(value, JointAnglesWithSpeed_Result), \
                "The 'result' field must be a sub message of type 'JointAnglesWithSpeed_Result'"
        self._result = value


class Metaclass_JointAnglesWithSpeed_GetResult(type):
    """Metaclass of service 'JointAnglesWithSpeed_GetResult'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('naoqi_bridge_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'naoqi_bridge_msgs.action.JointAnglesWithSpeed_GetResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__joint_angles_with_speed__get_result

            from naoqi_bridge_msgs.action import _joint_angles_with_speed
            if _joint_angles_with_speed.Metaclass_JointAnglesWithSpeed_GetResult_Request._TYPE_SUPPORT is None:
                _joint_angles_with_speed.Metaclass_JointAnglesWithSpeed_GetResult_Request.__import_type_support__()
            if _joint_angles_with_speed.Metaclass_JointAnglesWithSpeed_GetResult_Response._TYPE_SUPPORT is None:
                _joint_angles_with_speed.Metaclass_JointAnglesWithSpeed_GetResult_Response.__import_type_support__()


class JointAnglesWithSpeed_GetResult(metaclass=Metaclass_JointAnglesWithSpeed_GetResult):
    from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_GetResult_Request as Request
    from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_GetResult_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_JointAnglesWithSpeed_FeedbackMessage(type):
    """Metaclass of message 'JointAnglesWithSpeed_FeedbackMessage'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('naoqi_bridge_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'naoqi_bridge_msgs.action.JointAnglesWithSpeed_FeedbackMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__joint_angles_with_speed__feedback_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__joint_angles_with_speed__feedback_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__joint_angles_with_speed__feedback_message
            cls._TYPE_SUPPORT = module.type_support_msg__action__joint_angles_with_speed__feedback_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__joint_angles_with_speed__feedback_message

            from naoqi_bridge_msgs.action import JointAnglesWithSpeed
            if JointAnglesWithSpeed.Feedback.__class__._TYPE_SUPPORT is None:
                JointAnglesWithSpeed.Feedback.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class JointAnglesWithSpeed_FeedbackMessage(metaclass=Metaclass_JointAnglesWithSpeed_FeedbackMessage):
    """Message class 'JointAnglesWithSpeed_FeedbackMessage'."""

    __slots__ = [
        '_goal_id',
        '_feedback',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'feedback': 'naoqi_bridge_msgs/JointAnglesWithSpeed_Feedback',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['naoqi_bridge_msgs', 'action'], 'JointAnglesWithSpeed_Feedback'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_Feedback
        self.feedback = kwargs.get('feedback', JointAnglesWithSpeed_Feedback())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.feedback != other.feedback:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def feedback(self):
        """Message field 'feedback'."""
        return self._feedback

    @feedback.setter
    def feedback(self, value):
        if __debug__:
            from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_Feedback
            assert \
                isinstance(value, JointAnglesWithSpeed_Feedback), \
                "The 'feedback' field must be a sub message of type 'JointAnglesWithSpeed_Feedback'"
        self._feedback = value


class Metaclass_JointAnglesWithSpeed(type):
    """Metaclass of action 'JointAnglesWithSpeed'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('naoqi_bridge_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'naoqi_bridge_msgs.action.JointAnglesWithSpeed')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__action__joint_angles_with_speed

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass_GoalStatusArray._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass_GoalStatusArray.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass_CancelGoal._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass_CancelGoal.__import_type_support__()

            from naoqi_bridge_msgs.action import _joint_angles_with_speed
            if _joint_angles_with_speed.Metaclass_JointAnglesWithSpeed_SendGoal._TYPE_SUPPORT is None:
                _joint_angles_with_speed.Metaclass_JointAnglesWithSpeed_SendGoal.__import_type_support__()
            if _joint_angles_with_speed.Metaclass_JointAnglesWithSpeed_GetResult._TYPE_SUPPORT is None:
                _joint_angles_with_speed.Metaclass_JointAnglesWithSpeed_GetResult.__import_type_support__()
            if _joint_angles_with_speed.Metaclass_JointAnglesWithSpeed_FeedbackMessage._TYPE_SUPPORT is None:
                _joint_angles_with_speed.Metaclass_JointAnglesWithSpeed_FeedbackMessage.__import_type_support__()


class JointAnglesWithSpeed(metaclass=Metaclass_JointAnglesWithSpeed):

    # The goal message defined in the action definition.
    from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_Goal as Goal
    # The result message defined in the action definition.
    from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_Result as Result
    # The feedback message defined in the action definition.
    from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_Feedback as Feedback

    class Impl:

        # The send_goal service using a wrapped version of the goal message as a request.
        from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_SendGoal as SendGoalService
        # The get_result service using a wrapped version of the result message as a response.
        from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_GetResult as GetResultService
        # The feedback message with generic fields which wraps the feedback message.
        from naoqi_bridge_msgs.action._joint_angles_with_speed import JointAnglesWithSpeed_FeedbackMessage as FeedbackMessage

        # The generic service to cancel a goal.
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
        # The generic message for get the status of a goal.
        from action_msgs.msg._goal_status_array import GoalStatusArray as GoalStatusMessage

    def __init__(self):
        raise NotImplementedError('Action classes can not be instantiated')
