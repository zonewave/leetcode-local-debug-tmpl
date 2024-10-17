cmake_minimum_required(VERSION 3.14)
project(leetcode)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS_DEBUG "-g")
set(CMAKE_MESSAGE_LOG_LEVEL DEBUG)

# Download precompiled packages
include(ExternalProject)
find_package(Git REQUIRED)

# Precompiled external project
ExternalProject_Add(
        precompiled
        PREFIX ${CMAKE_BINARY_DIR}/precompiled
        GIT_REPOSITORY https://github.com/zonewave/leetcode-precompiled
        GIT_TAG master
        TIMEOUT 10
#        UPDATE_COMMAND ${GIT_EXECUTABLE} pull
        CONFIGURE_COMMAND ${CMAKE_COMMAND} -DCMAKE_BUILD_TYPE=Debug ${CMAKE_BINARY_DIR}/precompiled/src/precompiled/cpp
        BUILD_COMMAND ${CMAKE_COMMAND} --build . -- -j26
        INSTALL_COMMAND ""
        LOG_DOWNLOAD ON
)

# Get precompiled source directory
ExternalProject_Get_Property(precompiled source_dir binary_dir)
set(PRECOMPILED_INCLUDE_DIR ${source_dir}/cpp CACHE INTERNAL "Path to include folder for precompiled")
set(PRECOMPILED_BINARY_DIR ${binary_dir} CACHE INTERNAL "Path to binary folder for precompiled")
set(PRECOMPILED_LIB_DIR ${binary_dir}/lib CACHE INTERNAL "Path to library for precompiled")

# Download doctest
ExternalProject_Add(
        doctest
        PREFIX ${CMAKE_BINARY_DIR}/doctest
        GIT_REPOSITORY https://github.com/doctest/doctest.git
        GIT_TAG v2.4.11
        TIMEOUT 10
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
add_dependencies(common precompiled)

# Include directories for tests
include_directories(
        ${DOCTEST_INCLUDE_DIR} 
        ${PRECOMPILED_INCLUDE_DIR} 
        ${CMAKE_CURRENT_SOURCE_DIR}/common
)

set(TEST_SOURCE_FILES
    cn/test_1_two_sum.cpp
    cn/test_2_add_two_numbers.cpp
    # add want test cpp
)
# Create test executable
add_executable(tests ${TEST_SOURCE_FILES})
add_dependencies(tests doctest common)

# Link libraries
target_link_libraries(tests PRIVATE ${PRECOMPILED_LIB_DIR}/libprecompiled.a common)

# Configure testing
enable_testing()
add_test(NAME RunTests COMMAND tests)

# Debug information
message(STATUS "Test source files: ${TEST_SOURCE_FILES}")