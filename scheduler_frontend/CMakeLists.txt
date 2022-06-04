cmake_minimum_required(VERSION 3.16)

project(scheduler_frontend VERSION 0.1 LANGUAGES CXX)

set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 6.2 COMPONENTS Quick REQUIRED)

qt_add_executable(appscheduler_frontend
    main.cpp
    controllers/mastercontroller.h
    controllers/mastercontroller.cpp
)

qt_add_qml_module(appscheduler_frontend
    URI scheduler_frontend
    VERSION 1.0
    QML_FILES main.qml 
)

set_target_properties(appscheduler_frontend PROPERTIES
    MACOSX_BUNDLE_GUI_IDENTIFIER my.example.com
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

target_compile_definitions(appscheduler_frontend
    PRIVATE $<$<OR:$<CONFIG:Debug>,$<CONFIG:RelWithDebInfo>>:QT_QML_DEBUG>)
target_link_libraries(appscheduler_frontend
    PRIVATE Qt6::Quick)

add_custom_command(TARGET appscheduler_frontend POST_BUILD
    COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/../copy_wasm.sh
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/..
    COMMENT "Copying wasm output into scheduler_backend"
)
