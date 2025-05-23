cmake_minimum_required(VERSION 3.8)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(cpp_demo_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

find_package(rclcpp REQUIRED)

include_directories(include)

add_executable(cpp_node src/cpp_node.cpp)
add_executable(thread_node src/learn_thread.cpp)
add_executable(func_node src/learn_func.cpp)
add_executable(person_node src/person_node.cpp)

ament_target_dependencies(cpp_node rclcpp)
ament_target_dependencies(thread_node rclcpp)
ament_target_dependencies(func_node rclcpp)
ament_target_dependencies(person_node rclcpp)

install(
    TARGETS cpp_node thread_node func_node person_node
    DESTINATION lib/${PROJECT_NAME}
)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

if(BUILD_TESTING)
    find_package(ament_lint_auto REQUIRED)
    # the following line skips the linter which checks for copyrights
    # comment the line when a copyright and license is added to all source files
    set(ament_cmake_copyright_FOUND TRUE)
    # the following line skips cpplint (only works in a git repo)
    # comment the line when this package is in a git repo and when
    # a copyright and license is added to all source files
    set(ament_cmake_cpplint_FOUND TRUE)
    ament_lint_auto_find_test_dependencies()
endif()

ament_package()