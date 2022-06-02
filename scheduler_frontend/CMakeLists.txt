cmake_minimum_required(VERSION 3.16)

project(scheduler_frontend VERSION 0.1 LANGUAGES CXX)

set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 6.2 COMPONENTS Quick REQUIRED)

qt_add_executable(appscheduler_frontend
    main.cpp
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

#set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -sERROR_ON_UNDEFINED_SYMBOLS=0")
set_target_properties(Qt6::Platform PROPERTIES
  INTERFACE_LINK_OPTIONS "SHELL:-s EXIT_RUNTIME=1;SHELL:-s ERROR_ON_UNDEFINED_SYMBOLS=0;SHELL:-s EXTRA_EXPORTED_RUNTIME_METHODS=[UTF16ToString,stringToUTF16];SHELL:-s USE_WEBGL2=1;--bind;SHELL:-s FETCH=1;SHELL:-s INITIAL_MEMORY=20MB;SHELL:-s FULL_ES2=1;SHELL:-s DISABLE_EXCEPTION_CATCHING=1;SHELL:-s ALLOW_MEMORY_GROWTH=1;\$<\$<CONFIG:Debug>:;SHELL:-s DEMANGLE_SUPPORT=1;SHELL:-s GL_DEBUG=1;SHELL:-s ASSERTIONS=2;--profiling-funcs>"
)
