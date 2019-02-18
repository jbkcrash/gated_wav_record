# Copyright 2011,2012,2016 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})

list(APPEND gated_wav_record_sources
)

set(gated_wav_record_sources "${gated_wav_record_sources}" PARENT_SCOPE)
if(NOT gated_wav_record_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT gated_wav_record_sources)

add_library(gnuradio-gated_wav_record SHARED ${gated_wav_record_sources})
target_link_libraries(gnuradio-gated_wav_record ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-gated_wav_record PROPERTIES DEFINE_SYMBOL "gnuradio_gated_wav_record_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-gated_wav_record PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
include(GrMiscUtils)
GR_LIBRARY_FOO(gnuradio-gated_wav_record RUNTIME_COMPONENT "gated_wav_record_runtime" DEVEL_COMPONENT "gated_wav_record_devel")

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_gated_wav_record_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_gated_wav_record.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_gated_wav_record.cc
)

add_executable(test-gated_wav_record ${test_gated_wav_record_sources})

target_link_libraries(
  test-gated_wav_record
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-gated_wav_record
)

GR_ADD_TEST(test_gated_wav_record test-gated_wav_record)

########################################################################
# Print summary
########################################################################
message(STATUS "Using install prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "Building for version: ${VERSION} / ${LIBVER}")

