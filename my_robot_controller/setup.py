from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rosario',
    maintainer_email='rosario@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "nao_controller = my_robot_controller.nao_controller:main",
            "patient_data_controller = my_robot_controller.patient_data_controller:main",
            "sensor = my_robot_controller.sensor:main",
            "new = my_robot_controller.new:main",
            "speech = my_robot_controller.speech:main",
            "patient_data_controller2 = my_robot_controller.patient_data_controller2:main"
        ],
    },
)
