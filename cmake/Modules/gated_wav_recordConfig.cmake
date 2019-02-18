INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_GATED_WAV_RECORD gated_wav_record)

FIND_PATH(
    GATED_WAV_RECORD_INCLUDE_DIRS
    NAMES gated_wav_record/api.h
    HINTS $ENV{GATED_WAV_RECORD_DIR}/include
        ${PC_GATED_WAV_RECORD_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GATED_WAV_RECORD_LIBRARIES
    NAMES gnuradio-gated_wav_record
    HINTS $ENV{GATED_WAV_RECORD_DIR}/lib
        ${PC_GATED_WAV_RECORD_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GATED_WAV_RECORD DEFAULT_MSG GATED_WAV_RECORD_LIBRARIES GATED_WAV_RECORD_INCLUDE_DIRS)
MARK_AS_ADVANCED(GATED_WAV_RECORD_LIBRARIES GATED_WAV_RECORD_INCLUDE_DIRS)

