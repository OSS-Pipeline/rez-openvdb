name = "openvdb"

version = "5.2.0"

authors = [
    "Ken Museth",
    "DreamWorks Animation"
]

description = \
    """
    OpenVDB is an Academy Award-winning open-source C++ library comprising a novel hierarchical data structure and a
    suite of tools for the efficient storage and manipulation of sparse volumetric data discretized on
    three-dimensional grids.
    """

requires = [
    "gcc-6+",
    "cmake-3+",
    "python-2.7+<3",
    "blosc-1.5+",
    "boost-1.61",
    "ilmbase-2.2.1+<2.4",
    "openexr-2.2.1+<2.4",
    "tbb-2017.U6+",
    "glew-2+",
    "glfw-3+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "openvdb-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")

    # Helper environment variables.
    env.OPENVDB_INCLUDE_PATH.set("{root}/include")
    env.OPENVDB_LIBRARY_PATH.set("{root}/lib64")
