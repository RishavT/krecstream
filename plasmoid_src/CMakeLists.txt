project( kde4project )
find_package( KDE4 REQUIRED )
include(KDE4Defaults)
 
include_directories( ${KDE4_INCLUDES} )
 
set( KDE4ProjectSources kde4mainapp.cpp someclass.cpp someotherclass.cpp )
 
kde4_add_executable( kde4project ${KDE4ProjectSources} )
 
target_link_libraries( kde4project ${KDE4_KDEUI_LIBS} ${KDE4_KPARTS_LIBS} )
 
install( TARGETS kde4project  ${INSTALL_TARGETS_DEFAULT_ARGS} )
plasma_install_package(tutorial org.kde.tutorial plasma/plasmoids applet) 
