cmake_minimum_required(VERSION 3.10)

project(gl-scrapbook)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

file(GLOB_RECURSE SOURCES "src/main.cc" "src/glad.c" "src/*.h" "src/*.cc" "src/*.hh" "src/OpenGL/*.cc" "src/OpenGL/*.hh")

add_executable(gl-scrapbook ${SOURCES})

target_include_directories(gl-scrapbook PUBLIC "${PROJECT_SOURCE_DIR}/include")

target_link_libraries(gl-scrapbook glfw)

add_custom_target(copy_resources ALL
    COMMAND ${CMAKE_COMMAND} -E copy_directory
    ${PROJECT_SOURCE_DIR}/src/Resources
    ${PROJECT_BINARY_DIR}/Resources
    COMMENT "Copiando recursos...")

add_dependencies(gl-scrapbook copy_resources) 