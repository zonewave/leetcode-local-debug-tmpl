cmake_minimum_required(VERSION 3.14)
project(leetcode)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g")
set(CMAKE_MESSAGE_LOG_LEVEL DEBUG)

# Download precompiled packages
include(ExternalProject)
find_package(Git REQUIRED)

# 添加 precompiled 子模块
add_subdirectory(precompiled/cpp)

# 设置 PRECOMPILED_INCLUDE_DIR 和 PRECOMPILED_LIB_DIR
set(PRECOMPILED_INCLUDE_DIR ${precompiled_SOURCE_DIR})
set(PRECOMPILED_LIB_DIR ${precompiled_BINARY_DIR}/lib)
message(STATUS "this is ${PRECOMPILED_LIB_DIR}")
# Common library


# Download doctest
ExternalProject_Add(
        doctest
        PREFIX ${CMAKE_BINARY_DIR}/doctest
        GIT_REPOSITORY https://github.com/doctest/doctest.git
        TIMEOUT 10
        UPDATE_COMMAND ${GIT_EXECUTABLE} pull
        CONFIGURE_COMMAND ""
        BUILD_COMMAND ""
        INSTALL_COMMAND ""
        LOG_DOWNLOAD ON
)

# Get doctest source directory
ExternalProject_Get_Property(doctest source_dir)
set(DOCTEST_INCLUDE_DIR ${source_dir}/doctest CACHE INTERNAL "Path to include folder for doctest")
# set common
add_library(common STATIC common/common.cpp)
add_dependencies(common doctest)

# Include directories for tests
include_directories(${DOCTEST_INCLUDE_DIR})
include_directories(${PRECOMPILED_INCLUDE_DIR})
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/common)

set(TEST_SOURCE_FILES
    cn/test_1_two_sum.cpp
    cn/test_2_add_two_numbers.cpp
    # add want test cpp
)
# Create test executable
add_executable(tests ${TEST_SOURCE_FILES})
add_dependencies(tests doctest)
add_dependencies(tests precompiled)
# Link libraries
target_link_libraries(tests PRIVATE precompiled common)
# Configure testing
enable_testing()
add_test(NAME RunTests COMMAND tests)

# Debug information
message(STATUS "Test source files: ${TEST_SOURCE_FILES}")