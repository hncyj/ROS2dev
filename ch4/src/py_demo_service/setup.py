from setuptools import find_packages, setup

package_name = 'py_demo_service'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/resource', ['resource/faces.jpg', 'resource/test1.jpeg'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='chenyinjie',
    maintainer_email='chenyinjie666@foxmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'learn_face_detect=py_demo_service.learn_face_detect:main',
            'face_detect_node=py_demo_service.face_detect_node:main',
            'face_detect_client_node=py_demo_service.face_detect_client_node:main'
        ],
    },
)
