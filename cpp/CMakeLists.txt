cmake_minimum_required(VERSION 3.14)
project(leetcode)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g")
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
        UPDATE_COMMAND ${GIT_EXECUTABLE} pull
        CONFIGURE_COMMAND ${CMAKE_COMMAND} -DCMAKE_BUILD_TYPE=Debug ${CMAKE_BINARY_DIR}/precompiled/src/precompiled/cpp
        BUILD_COMMAND ${CMAKE_COMMAND} --build .
        INSTALL_COMMAND ""
        LOG_DOWNLOAD ON
)

# Get precompiled source directory
ExternalProject_Get_Property(precompiled source_dir binary_dir)
set(PRECOMPILED_INCLUDE_DIR ${source_dir}/cpp CACHE INTERNAL "Path to include folder for precompiled")
set(PRECOMPILED_BINARY_DIR ${binary_dir} CACHE INTERNAL "Path to binary folder for precompiled")
set(PRECOMPILED_LIB_DIR ${binary_dir}/lib CACHE INTERNAL "Path to library for precompiled")


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


# Glob test source files
file(GLOB_RECURSE TEST_SOURCE_FILES "cn/*.cpp")
string(REPLACE ";" "\\n" TEST_SOURCE_FILES_STRING "${TEST_SOURCE_FILES}")
# Generate CMake file for test sources
configure_file(
        ${CMAKE_CURRENT_SOURCE_DIR}/test_sources.cmake.in
        ${CMAKE_CURRENT_BINARY_DIR}/test_sources.cmake
        @ONLY
)
# Include generated file
include(${CMAKE_CURRENT_BINARY_DIR}/test_sources.cmake)

# Custom command to update test sources
add_custom_command(
        OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/test_sources.cmake
        COMMAND ${CMAKE_COMMAND} -E echo "Updating test sources..."
        COMMAND ${CMAKE_COMMAND} -E touch ${CMAKE_CURRENT_BINARY_DIR}/test_sources.cmake
        DEPENDS ${TEST_SOURCE_FILES}
        COMMENT "Checking for updated source files..."
)

# Custom target to ensure test sources are up-to-date
add_custom_target(UpdateSources ALL DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/test_sources.cmake)

# Create test executable
add_executable(tests ${TEST_SOURCE_FILES})

add_dependencies(tests doctest)
add_dependencies(tests precompiled)

# Include directories for tests
include_directories(${DOCTEST_INCLUDE_DIR})
include_directories(${PRECOMPILED_INCLUDE_DIR})
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/common)


# Link libraries
add_library(common STATIC common/common.cpp)
target_link_libraries(tests PRIVATE ${PRECOMPILED_LIB_DIR}/libprecompiled.a common)

# Configure testing
enable_testing()
add_test(NAME RunTests COMMAND tests)

# Debug information
message(STATUS "Test source files: ${TEST_SOURCE_FILES}")